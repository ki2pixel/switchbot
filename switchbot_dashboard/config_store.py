from __future__ import annotations

import json
import logging
import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, Protocol, TypeVar, runtime_checkable

from redis import Redis
from redis.exceptions import RedisError


class StoreError(RuntimeError):
    """Raised when a storage backend cannot satisfy a read/write operation."""


@runtime_checkable
class BaseStore(Protocol):
    def read(self) -> dict[str, Any]:
        ...

    def write(self, data: dict[str, Any]) -> None:
        ...


class JsonStore:
    def __init__(self, path: str) -> None:
        self._path = Path(path)
        self._lock = threading.Lock()

    @property
    def path(self) -> Path:
        return self._path

    def read(self) -> dict[str, Any]:
        with self._lock:
            if not self._path.exists():
                return {}

            with self._path.open("r", encoding="utf-8") as handle:
                return json.load(handle)

    def write(self, data: dict[str, Any]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)

        with self._lock:
            tmp_path = self._path.with_suffix(self._path.suffix + ".tmp")
            with tmp_path.open("w", encoding="utf-8") as handle:
                json.dump(data, handle, indent=2, ensure_ascii=False)
                handle.write("\n")

            tmp_path.replace(self._path)


class RedisJsonStore:
    def __init__(
        self,
        client: Redis,
        key: str,
        ttl_seconds: int | None = None,
    ) -> None:
        self._client = client
        self._key = key
        self._ttl_seconds = ttl_seconds

    def read(self) -> dict[str, Any]:
        try:
            raw_value = self._client.get(self._key)
        except RedisError as exc:
            raise StoreError(f"Redis read failed for key '{self._key}'") from exc

        if raw_value is None:
            return {}

        try:
            raw_text = raw_value.decode("utf-8") if isinstance(raw_value, bytes) else str(raw_value)
            return json.loads(raw_text)
        except json.JSONDecodeError as exc:
            raise StoreError(f"Redis payload for '{self._key}' is not valid JSON") from exc

    def write(self, data: dict[str, Any]) -> None:
        payload = json.dumps(data, ensure_ascii=False)
        try:
            self._client.set(name=self._key, value=payload, ex=self._ttl_seconds)
        except RedisError as exc:
            raise StoreError(f"Redis write failed for key '{self._key}'") from exc


_T = TypeVar("_T")


class FailoverStore:
    def __init__(
        self,
        *,
        kind: str,
        primary: BaseStore,
        secondary: BaseStore | None,
        logger: logging.Logger,
        unhealthy_cooldown_seconds: int = 60,
    ) -> None:
        self._kind = kind
        self._primary = primary
        self._secondary = secondary
        self._logger = logger
        self._unhealthy_cooldown_seconds = max(unhealthy_cooldown_seconds, 1)

        self._lock = threading.Lock()
        self._primary_unhealthy_until = 0.0
        self._secondary_unhealthy_until = 0.0

    def mark_unhealthy(self, backend_name: str) -> None:
        if backend_name not in ("primary", "secondary"):
            raise ValueError(f"Unknown backend: {backend_name}")
        if backend_name == "secondary" and self._secondary is None:
            return
        self._mark_unhealthy(backend_name)

    def read(self) -> dict[str, Any]:
        return self._execute("read", lambda store: store.read())

    def write(self, data: dict[str, Any]) -> None:
        self._execute("write", lambda store: store.write(data))
        return None

    def _execute(self, operation: str, func: Callable[[BaseStore], _T]) -> _T:
        if self._secondary is None:
            return func(self._primary)

        backends = self._get_backend_order()
        last_exc: StoreError | None = None

        for backend_name, store in backends:
            try:
                result = func(store)
            except StoreError as exc:
                last_exc = exc
                self._mark_unhealthy(backend_name)
                self._logger.error(
                    "[store] %s store: %s backend failed during %s (%s)",
                    self._kind,
                    backend_name,
                    operation,
                    exc,
                )
                continue

            with self._lock:
                if backend_name == "primary":
                    self._primary_unhealthy_until = 0.0
                elif backend_name == "secondary":
                    self._secondary_unhealthy_until = 0.0
            return result

        raise StoreError(
            f"All backends failed for {self._kind} store (operation={operation})"
        ) from last_exc

    def _get_backend_order(self) -> list[tuple[str, BaseStore]]:
        now = time.monotonic()
        with self._lock:
            primary_healthy = now >= self._primary_unhealthy_until
            secondary_healthy = now >= self._secondary_unhealthy_until

        order: list[tuple[str, BaseStore]] = []
        if primary_healthy:
            order.append(("primary", self._primary))
        if secondary_healthy:
            order.append(("secondary", self._secondary))
        if not order:
            order = [("primary", self._primary), ("secondary", self._secondary)]

        return order

    def _mark_unhealthy(self, backend_name: str) -> None:
        until = time.monotonic() + self._unhealthy_cooldown_seconds
        with self._lock:
            if backend_name == "primary":
                self._primary_unhealthy_until = until
            elif backend_name == "secondary":
                self._secondary_unhealthy_until = until
