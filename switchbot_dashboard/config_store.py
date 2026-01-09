import json
import threading
from pathlib import Path
from typing import Any


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
