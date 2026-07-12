from __future__ import annotations

import datetime as dt
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

DEFAULT_TIMEZONE = "Europe/Paris"

def _safe_int(value: Any, *, default: int, minimum: int | None = None, maximum: int | None = None) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        parsed = default

    if minimum is not None and parsed < minimum:
        parsed = minimum
    if maximum is not None and parsed > maximum:
        parsed = maximum
    return parsed

def _safe_float(value: Any, *, default: float, minimum: float | None = None, maximum: float | None = None) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        parsed = default

    if minimum is not None and parsed < minimum:
        parsed = minimum
    if maximum is not None and parsed > maximum:
        parsed = maximum
    return parsed

def _safe_bool(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    val_str = str(value).strip().lower()
    return val_str in ("true", "1", "yes", "on")

def _utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()

def _resolve_timezone(settings: dict[str, Any]) -> dt.tzinfo:
    timezone_name = str(settings.get("timezone") or "").strip() or DEFAULT_TIMEZONE
    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError:
        return dt.timezone.utc

def _parse_iso_datetime(value: str) -> dt.datetime | None:
    if not value:
        return None
    try:
        clean_value = value.strip()
        if clean_value.endswith("Z"):
            clean_value = clean_value[:-1] + "+00:00"
        parsed = dt.datetime.fromisoformat(clean_value)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=dt.timezone.utc)
        return parsed
    except ValueError:
        return None
