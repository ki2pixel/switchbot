#!/usr/bin/env python3
"""Refresh and print the current quota snapshot."""
from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict

from flask import current_app

from switchbot_dashboard import create_app


def main() -> None:
    os.environ.setdefault("SCHEDULER_ENABLED", "false")
    app = create_app()
    with app.app_context():
        quota_tracker = current_app.extensions["quota_tracker"]
        snapshot: Dict[str, Any] = quota_tracker.refresh_snapshot()

    print(json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover
        print(f"[quota-alerting] Snapshot failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
