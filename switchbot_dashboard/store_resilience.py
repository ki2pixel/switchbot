"""Runtime resilience wrapper for the primary data store.

The application already falls back to JSON at boot when PostgreSQL is
unavailable. This module adds the runtime counterpart:

* count consecutive ``StoreError`` failures on the primary backend;
* log a ``CRITICAL`` alert at the configured threshold;
* optionally switch to a JSON fallback when running outside production (or
  when ``STORE_RUNTIME_FALLBACK=true`` is explicitly set).

Production deliberately does not switch to an ephemeral JSON file: with
Gunicorn multi-workers and Render's ephemeral disk it would create a
split-brain and silently lose data. In production the wrapper only alerts and
lets the existing ``StoreError`` handler return HTTP 503.
"""

from __future__ import annotations

import copy
import logging
import threading
from typing import Any

from .config_store import BaseStore, StoreError


class _TransactionProxy:
    """Track transaction depth and defer failover until the transaction ends."""

    def __init__(self, manager: "ResilientStore") -> None:
        self._manager = manager
        self._ctx: Any = None

    def __enter__(self) -> Any:
        self._manager._enter_transaction()
        try:
            self._ctx = self._manager._primary.transaction()
            return self._ctx.__enter__()
        except Exception as exc:
            self._manager._exit_transaction()
            if isinstance(exc, StoreError):
                self._manager._record_failure("transaction", exc)
                if self._manager._should_use_fallback():
                    self._ctx = self._manager._fallback.transaction()
                    self._manager._enter_transaction()
                    try:
                        return self._ctx.__enter__()
                    except Exception:
                        self._manager._exit_transaction()
                        raise
            raise

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        try:
            result = self._ctx.__exit__(exc_type, exc_val, exc_tb)
        except Exception as exc:
            if isinstance(exc, StoreError):
                self._manager._record_failure("transaction", exc)
            raise
        finally:
            self._manager._exit_transaction()
        return result


class ResilientStore:
    """Primary/fallback store with consecutive-failure accounting."""

    def __init__(
        self,
        primary: BaseStore,
        fallback: BaseStore | None,
        *,
        logger: logging.Logger,
        name: str,
        failure_threshold: int = 3,
        allow_fallback: bool = False,
    ) -> None:
        self._primary = primary
        self._fallback = fallback
        self._logger = logger
        self._name = name
        self._failure_threshold = max(1, int(failure_threshold))
        self._allow_fallback = bool(allow_fallback and fallback is not None)
        self._lock = threading.Lock()
        self._consecutive_failures = 0
        self._degraded = False
        self._pending_switch = False
        self._active_transactions = 0
        self._last_good: dict[str, Any] | None = None
        self._tx_local = threading.local()

    # ------------------------------------------------------------------
    # Public store interface
    # ------------------------------------------------------------------
    @property
    def primary(self) -> BaseStore:
        return self._primary

    @property
    def degraded(self) -> bool:
        with self._lock:
            return self._degraded

    @property
    def active_backend(self) -> str:
        with self._lock:
            if self._degraded and self._fallback is not None:
                return "filesystem"
            return "postgres"

    @property
    def consecutive_failures(self) -> int:
        with self._lock:
            return self._consecutive_failures

    def read(self) -> dict[str, Any]:
        if self._is_degraded():
            return self._fallback.read()

        try:
            data = self._primary.read()
        except StoreError as exc:
            if self._record_failure("read", exc) and self._should_use_fallback():
                return self._fallback.read()
            raise

        self._remember_good(data)
        return data

    def write(self, data: dict[str, Any]) -> None:
        if self._is_degraded():
            self._fallback.write(data)
            return

        try:
            self._primary.write(data)
        except StoreError as exc:
            if self._record_failure("write", exc) and self._should_use_fallback():
                self._fallback.write(data)
                return
            raise

        self._remember_good(data)

    def transaction(self) -> Any:
        if self._is_degraded():
            return self._fallback.transaction()
        return _TransactionProxy(self)

    def health_check(self) -> bool:
        try:
            healthy = bool(self._primary.health_check())
        except Exception as exc:
            self._logger.warning(
                "[store] Primary health check failed for %s store (%s)",
                self._name,
                exc,
            )
            healthy = False
        return healthy and not self.degraded

    def close(self) -> None:
        for label, store in (("primary", self._primary), ("fallback", self._fallback)):
            if store is None:
                continue
            close = getattr(store, "close", None)
            if close is None:
                continue
            try:
                close()
            except Exception as exc:
                self._logger.warning(
                    "[store] Failed to close %s backend for %s store (%s)",
                    label,
                    self._name,
                    exc,
                )

    # ------------------------------------------------------------------
    # Failure accounting / failover
    # ------------------------------------------------------------------
    def _is_degraded(self) -> bool:
        with self._lock:
            return self._degraded

    def _should_use_fallback(self) -> bool:
        with self._lock:
            return self._degraded and self._fallback is not None

    def _record_failure(self, operation: str, exc: Exception) -> bool:
        """Record a failure and return True when the caller may use fallback."""
        apply_switch = False
        with self._lock:
            self._consecutive_failures += 1
            count = self._consecutive_failures
            threshold = self._failure_threshold
            if (
                not self._degraded
                and count >= threshold
                and self._allow_fallback
            ):
                self._pending_switch = True
            apply_switch = (
                self._pending_switch and self._active_transactions == 0
            )

        if count < threshold:
            self._logger.warning(
                "[store] %s store %s failure %d/%d: %s",
                self._name,
                operation,
                count,
                threshold,
                exc,
            )
        elif count == threshold:
            self._logger.critical(
                "[store] CRITICAL: %s store has failed %d consecutive times (last %s failure: %s)",
                self._name,
                count,
                operation,
                exc,
            )
        else:
            self._logger.warning(
                "[store] %s store still failing (%d consecutive failures, last %s: %s)",
                self._name,
                count,
                operation,
                exc,
            )

        if apply_switch:
            self._apply_switch()
        return self._should_use_fallback()

    def _apply_switch(self) -> None:
        with self._lock:
            if self._degraded or not self._allow_fallback:
                self._pending_switch = False
                return
            self._degraded = True
            self._pending_switch = False
            snapshot = copy.deepcopy(self._last_good)

        self._logger.critical(
            "[store] Switching %s store to filesystem fallback after %d consecutive failures",
            self._name,
            self._failure_threshold,
        )

        if snapshot is not None and self._fallback is not None:
            try:
                self._fallback.write(snapshot)
            except Exception as exc:
                self._logger.error(
                    "[store] Failed to seed filesystem fallback for %s store (%s)",
                    self._name,
                    exc,
                )

    def _remember_good(self, data: dict[str, Any]) -> None:
        in_transaction = self._transaction_depth() != 0
        with self._lock:
            if self._degraded:
                return
            self._consecutive_failures = 0
            # A failure observed inside a transaction may have scheduled a
            # switch; a subsequent successful operation proves the backend
            # recovered, so cancel it before it fires on transaction exit.
            self._pending_switch = False
            if not in_transaction:
                # Never seed the fallback snapshot with uncommitted data.
                self._last_good = copy.deepcopy(data)

    # ------------------------------------------------------------------
    # Thread-local transaction depth
    # ------------------------------------------------------------------
    def _transaction_depth(self) -> int:
        return int(getattr(self._tx_local, "depth", 0))

    def _enter_transaction(self) -> None:
        self._tx_local.depth = self._transaction_depth() + 1
        with self._lock:
            self._active_transactions += 1

    def _exit_transaction(self) -> None:
        depth = max(0, self._transaction_depth() - 1)
        self._tx_local.depth = depth
        apply_switch = False
        with self._lock:
            self._active_transactions = max(0, self._active_transactions - 1)
            if self._active_transactions == 0 and self._pending_switch:
                apply_switch = True
        if apply_switch:
            self._apply_switch()
