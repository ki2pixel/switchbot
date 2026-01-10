from __future__ import annotations

import datetime as dt
import logging
from typing import Any

from .config_store import BaseStore

logger = logging.getLogger(__name__)


class ApiQuotaTracker:
    """Persist and expose a daily SwitchBot API quota estimate."""

    def __init__(self, state_store: BaseStore, default_daily_limit: int = 10_000) -> None:
        self._state_store = state_store
        self._default_daily_limit = max(int(default_daily_limit), 1)

    def record_call(self, *, increment: int = 1) -> None:
        """Fallback path used when the API does not expose quota headers."""
        if increment <= 0:
            return

        state = self._normalize_state()
        limit = self._extract_limit(state)
        used = self._safe_int(state.get("api_requests_total"), fallback=0)
        used = max(used, 0) + increment
        remaining = max(limit - used, 0)

        state["api_requests_total"] = used
        state["api_requests_remaining"] = remaining
        self._state_store.write(state)
        logger.debug("[quota] fallback increment recorded: used=%s remaining=%s limit=%s", used, remaining, limit)

    def record_from_headers(self, *, limit: int | None, remaining: int | None) -> bool:
        """
        Persist authoritative data when SwitchBot exposes X-RateLimit headers.

        Returns True when the state was updated, False otherwise (e.g. headers missing).
        """
        if remaining is None:
            return False

        state = self._normalize_state()

        limit_value: int
        if limit is not None:
            limit_value = max(int(limit), 1)
            state["api_requests_limit"] = limit_value
        else:
            limit_value = self._extract_limit(state)

        remaining_value = max(min(int(remaining), limit_value), 0)
        used = max(limit_value - remaining_value, 0)

        state["api_requests_total"] = used
        state["api_requests_remaining"] = remaining_value
        self._state_store.write(state)

        logger.debug(
            "[quota] headers snapshot recorded: used=%s remaining=%s limit=%s",
            used,
            remaining_value,
            limit_value,
        )
        return True

    def refresh_snapshot(self) -> dict[str, Any]:
        """
        Force a normalization of the quota snapshot even if no API call occurred recently.

        Returns the refreshed state for callers that want to reuse the values.
        """
        state = self._normalize_state()
        self._state_store.write(state)
        logger.debug("[quota] snapshot refreshed: day=%s remaining=%s", state.get("api_quota_day"), state.get("api_requests_remaining"))
        return state

    def _normalize_state(self) -> dict[str, Any]:
        state = self._state_store.read()
        now = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
        today = now.date().isoformat()
        if state.get("api_quota_day") != today:
            state["api_quota_day"] = today
            state["api_requests_total"] = 0
            state["api_requests_limit"] = self._default_daily_limit
            state["api_requests_remaining"] = self._default_daily_limit
            state["api_quota_reset_at"] = now.isoformat()
        else:
            # Ensure limit field is always present for downstream consumers.
            state["api_requests_limit"] = self._extract_limit(state)
            state.setdefault("api_quota_reset_at", now.isoformat())
        return state

    def _extract_limit(self, state: dict[str, Any]) -> int:
        limit = self._safe_int(state.get("api_requests_limit"), fallback=self._default_daily_limit)
        return max(limit, 1)

    @staticmethod
    def _safe_int(value: Any, *, fallback: int) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return fallback
