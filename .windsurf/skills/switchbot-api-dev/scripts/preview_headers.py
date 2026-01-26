#!/usr/bin/env python3
"""Generate and print SwitchBot HMAC headers for diagnostics."""
from __future__ import annotations

import json
import os
import sys
from typing import Dict

from switchbot_dashboard.switchbot_api import SwitchBotClient, SwitchBotApiError


def build_headers() -> Dict[str, str]:
    token = os.environ.get("SWITCHBOT_TOKEN", "").strip()
    secret = os.environ.get("SWITCHBOT_SECRET", "").strip()
    if not token or not secret:
        raise SwitchBotApiError("SWITCHBOT_TOKEN/SECRET not configured in environment")

    client = SwitchBotClient(token=token, secret=secret)
    return client._build_headers()  # type: ignore[attr-defined]


def main() -> None:
    try:
        headers = build_headers()
    except Exception as exc:  # pragma: no cover
        print(f"[switchbot-api-dev] Failed to build headers: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    safe_headers = {k: v for k, v in headers.items() if k.lower() != "authorization"}
    print(json.dumps(safe_headers, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
