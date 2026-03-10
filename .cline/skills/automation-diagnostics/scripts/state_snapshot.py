#!/usr/bin/env python3
"""Dump settings/state stores for offline diagnostics."""
from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict

from flask import current_app

from switchbot_dashboard import create_app


def _serialize(data: Any) -> Any:
    if isinstance(data, dict):
        return {k: _serialize(v) for k, v in data.items()}
    if isinstance(data, list):
        return [_serialize(v) for v in data]
    return data


def capture_snapshot() -> Dict[str, Any]:
    os.environ.setdefault("SCHEDULER_ENABLED", "false")
    app = create_app()
    with app.app_context():
        settings_store = current_app.extensions["settings_store"]
        state_store = current_app.extensions["state_store"]
        snapshot: Dict[str, Any] = {
            "settings": _serialize(settings_store.read()),
            "state": _serialize(state_store.read()),
        }
    return snapshot


def main() -> None:
    try:
        snapshot = capture_snapshot()
    except Exception as exc:  # pragma: no cover - CLI surface
        print(f"[automation-diagnostics] Snapshot failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print(json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
