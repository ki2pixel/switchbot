#!/usr/bin/env python3
"""Inspect PostgresStore health and fallback status."""
from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict

from flask import current_app

from switchbot_dashboard import create_app
from switchbot_dashboard.postgres_store import PostgresStore


def _store_info(store: Any, *, name: str) -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "name": name,
        "class": store.__class__.__name__,
    }
    if isinstance(store, PostgresStore):
        info["backend"] = "postgres"
        info["health_check"] = store.health_check()
    else:
        info["backend"] = "filesystem"
    return info


def capture() -> Dict[str, Any]:
    os.environ.setdefault("STORE_BACKEND", "postgres")
    os.environ.setdefault("SCHEDULER_ENABLED", "false")

    app = create_app()
    with app.app_context():
        settings_store = current_app.extensions["settings_store"]
        state_store = current_app.extensions["state_store"]

        snapshot = {
            "settings_store": _store_info(settings_store, name="settings_store"),
            "state_store": _store_info(state_store, name="state_store"),
        }

    return snapshot


def main() -> None:
    try:
        snapshot = capture()
    except Exception as exc:  # pragma: no cover
        print(f"[postgres-store-maintenance] Snapshot failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
