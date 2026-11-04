from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any, Protocol, runtime_checkable


class StoreError(RuntimeError):
    """Raised when a storage backend cannot satisfy a read/write operation."""


@runtime_checkable
class BaseStore(Protocol):
    def read(self) -> dict[str, Any]:
        ...

    def write(self, data: dict[str, Any]) -> None:
        ...

    def transaction(self) -> Any:
        ...


class JsonStoreTransactionContext:
    """Re-entrant, thread-local transaction context for :class:`JsonStore`.

    Nested ``with store.transaction():`` blocks join the transaction already
    active on the current thread instead of trying to re-acquire the
    non-reentrant ``threading.Lock`` (which used to deadlock the worker).
    """

    def __init__(self, store: JsonStore):
        self._store = store
        self._cached_data: dict[str, Any] | None = None
        self._dirty = False
        self._is_nested = False

    def __enter__(self) -> "JsonStoreTransactionContext":
        active_tx = getattr(self._store._local, "active_transaction", None)
        if active_tx is not None:
            self._is_nested = True
            return active_tx

        # Acquire lock for the duration of the root transaction.
        self._store._lock.acquire()
        try:
            self._cached_data = self._store._read_without_lock()
            self._store._local.active_transaction = self
            return self
        except BaseException:
            self._store._lock.release()
            raise

    def read(self) -> dict[str, Any]:
        if self._is_nested:
            return self._store._local.active_transaction.read()
        import copy
        return copy.deepcopy(self._cached_data or {})

    def write(self, data: dict[str, Any]) -> None:
        if self._is_nested:
            self._store._local.active_transaction.write(data)
            return
        import copy
        self._cached_data = copy.deepcopy(data)
        self._dirty = True

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._is_nested:
            return

        self._store._local.active_transaction = None
        try:
            if exc_type is None and self._dirty:
                self._store._write_without_lock(self._cached_data or {})
        finally:
            self._store._lock.release()


class JsonStore:
    def __init__(self, path: str) -> None:
        self._path = Path(path)
        self._lock = threading.Lock()
        self._local = threading.local()

    @property
    def path(self) -> Path:
        return self._path

    def transaction(self) -> Any:
        return JsonStoreTransactionContext(self)

    def read(self) -> dict[str, Any]:
        tx = getattr(self._local, "active_transaction", None)
        if tx is not None:
            return tx.read()

        with self._lock:
            return self._read_without_lock()

    def _read_without_lock(self) -> dict[str, Any]:
        if not self._path.exists():
            return {}

        with self._path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def write(self, data: dict[str, Any]) -> None:
        tx = getattr(self._local, "active_transaction", None)
        if tx is not None:
            tx.write(data)
            return

        self._path.parent.mkdir(parents=True, exist_ok=True)

        with self._lock:
            self._write_without_lock(data)

    def _write_without_lock(self, data: dict[str, Any]) -> None:
        tmp_path = self._path.with_suffix(self._path.suffix + ".tmp")
        with tmp_path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")

        tmp_path.replace(self._path)



