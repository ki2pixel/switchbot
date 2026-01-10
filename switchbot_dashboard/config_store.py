from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any, Protocol

from redis import Redis
from redis.exceptions import RedisError


class StoreError(RuntimeError):
    """Raised when a storage backend cannot satisfy a read/write operation."""


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
