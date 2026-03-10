#!/usr/bin/env python3
"""Inspect SchedulerService status without starting the real scheduler."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from typing import Any, Dict

from flask import current_app

from switchbot_dashboard import create_app

ISO_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


def _format_timestamp(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime(ISO_FORMAT)
    return None


def capture_scheduler_snapshot() -> Dict[str, Any]:
    os.environ.setdefault("SCHEDULER_ENABLED", "false")
    app = create_app()
    with app.app_context():
        scheduler = current_app.extensions["scheduler_service"]
        settings_store = current_app.extensions["settings_store"]
        state_store = current_app.extensions["state_store"]

        settings = settings_store.read()
        state = state_store.read()
        poll_interval = settings.get("poll_interval_seconds", "n/a")

        snapshot: Dict[str, Any] = {
            "scheduler_running": scheduler.is_running(),
            "poll_interval_seconds": poll_interval,
            "last_tick_at": state.get("last_tick_at"),
            "last_tick_status": state.get("last_tick_status"),
            "pending_off_repeat": state.get("pending_off_repeat"),
        }
    return snapshot


def main() -> None:
    try:
        snapshot = capture_scheduler_snapshot()
    except Exception as exc:  # pragma: no cover
        print(f"[scheduler-ops] Snapshot failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
