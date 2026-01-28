from __future__ import annotations

import datetime as dt
import logging
import threading
from typing import Any, Callable
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from apscheduler.schedulers.background import BackgroundScheduler

from .config_store import BaseStore
from .automation import DEFAULT_TIMEZONE, OFF_REPEAT_STATE_KEY, _is_now_in_windows, _parse_hhmm


class SchedulerService:
    def __init__(
        self,
        settings_store: BaseStore,
        tick_callable: Callable[[], None],
        *,
        state_store: BaseStore | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._settings_store = settings_store
        self._state_store = state_store
        self._tick_callable = tick_callable
        self._scheduler: BackgroundScheduler | None = None
        self._job_id = "automation_tick"
        self._lock = threading.Lock()
        self._logger = logger or logging.getLogger(__name__)
        self._current_interval_seconds: int | None = None

    def _run_tick_safe(self) -> None:
        """Execute tick callable while guarding against uncaught exceptions."""
        try:
            self._tick_callable()
        except Exception as exc:  # pragma: no cover - exercised via tests
            self._logger.error(
                "[scheduler] Automation tick raised exception: %s",
                exc,
                exc_info=True,
            )
        finally:
            self._maybe_reschedule_after_tick()

    @staticmethod
    def _as_int(value: Any, *, default: int, minimum: int | None = None, maximum: int | None = None) -> int:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            parsed = default

        if minimum is not None and parsed < minimum:
            parsed = minimum
        if maximum is not None and parsed > maximum:
            parsed = maximum
        return parsed

    def _has_pending_off_repeat(self) -> bool:
        if self._state_store is None:
            return False

        state = self._state_store.read()
        task = state.get(OFF_REPEAT_STATE_KEY)
        if not isinstance(task, dict):
            return False
        remaining = self._as_int(task.get("remaining"), default=0, minimum=0)
        return remaining > 0

    def _resolve_timezone(self, settings: dict[str, Any]) -> dt.tzinfo:
        timezone_name = str(settings.get("timezone") or "").strip() or DEFAULT_TIMEZONE
        try:
            return ZoneInfo(timezone_name)
        except ZoneInfoNotFoundError:
            return dt.timezone.utc

    def _next_window_start(self, time_windows: list[dict[str, Any]], now: dt.datetime) -> dt.datetime | None:
        if not time_windows:
            return None

        candidates: list[dt.datetime] = []
        tzinfo = now.tzinfo or dt.timezone.utc
        base_date = now.date()
        base_weekday = now.weekday()

        for window in time_windows:
            days = window.get("days")
            if not isinstance(days, list):
                continue
            start_raw = window.get("start")
            end_raw = window.get("end")
            if not isinstance(start_raw, str) or not isinstance(end_raw, str):
                continue

            try:
                start_time = _parse_hhmm(start_raw)
            except ValueError:
                continue

            for day_offset in range(0, 8):
                candidate_weekday = (base_weekday + day_offset) % 7
                if candidate_weekday not in days:
                    continue
                candidate_date = base_date + dt.timedelta(days=day_offset)
                candidate_start = dt.datetime.combine(candidate_date, start_time, tzinfo=tzinfo)
                if candidate_start > now:
                    candidates.append(candidate_start)

        if not candidates:
            return None
        return min(candidates)

    def _get_effective_interval_seconds(self, *, now_utc: dt.datetime | None = None) -> tuple[int, str]:
        settings = self._settings_store.read()

        base_interval = self._as_int(
            settings.get("poll_interval_seconds", 120),
            default=120,
            minimum=15,
            maximum=3600,
        )

        adaptive_enabled = bool(settings.get("adaptive_polling_enabled", True))
        if not adaptive_enabled:
            return base_interval, "fixed"

        automation_enabled = bool(settings.get("automation_enabled", False))
        if not automation_enabled:
            return base_interval, "automation_disabled"

        time_windows = settings.get("time_windows", [])
        if not isinstance(time_windows, list) or not time_windows:
            return base_interval, "no_windows"

        if self._has_pending_off_repeat():
            return base_interval, "pending_off_repeat"

        tzinfo = self._resolve_timezone(settings)
        now = (now_utc or dt.datetime.now(dt.timezone.utc)).astimezone(tzinfo)
        in_window = _is_now_in_windows(time_windows, now)
        if in_window:
            return base_interval, "in_window"

        idle_interval = self._as_int(
            settings.get("idle_poll_interval_seconds", 600),
            default=600,
            minimum=15,
            maximum=86_400,
        )
        warmup_minutes = self._as_int(
            settings.get("poll_warmup_minutes", 15),
            default=15,
            minimum=0,
            maximum=24 * 60,
        )
        if warmup_minutes <= 0:
            return idle_interval, "idle"

        next_start = self._next_window_start(time_windows, now)
        if next_start is None:
            return idle_interval, "idle"

        warmup_delta = dt.timedelta(minutes=warmup_minutes)
        if next_start - now <= warmup_delta:
            return base_interval, "warmup"

        seconds_until_warmup_start = int((next_start - warmup_delta - now).total_seconds())
        if seconds_until_warmup_start <= 0:
            return base_interval, "warmup"

        clamped_idle = min(idle_interval, max(15, seconds_until_warmup_start))
        return clamped_idle, "idle"

    def _get_interval_seconds(self) -> int:
        interval, _ = self._get_effective_interval_seconds()
        return interval

    def _maybe_reschedule_after_tick(self) -> None:
        with self._lock:
            if self._scheduler is None:
                return

            desired_interval, mode = self._get_effective_interval_seconds()
            if self._current_interval_seconds == desired_interval:
                return

            previous = self._current_interval_seconds
            self._logger.info(
                "[scheduler] Adaptive polling reschedule: %s -> %s seconds (mode=%s)",
                previous,
                desired_interval,
                mode,
            )
            self._schedule_or_reschedule_locked()

    def start(self) -> None:
        with self._lock:
            if self._scheduler is not None:
                self._logger.warning("[scheduler] Scheduler already started, ignoring duplicate start() call")
                return

            self._scheduler = BackgroundScheduler(daemon=True)
            self._scheduler.start()
            self._logger.info("[scheduler] BackgroundScheduler started successfully")
            self._schedule_or_reschedule_locked()

        self._logger.info("[scheduler] Triggering immediate first tick")
        self._run_tick_safe()

    def _schedule_or_reschedule_locked(self) -> None:
        if self._scheduler is None:
            self._logger.warning("[scheduler] Cannot schedule job: scheduler is None")
            return

        interval = self._get_interval_seconds()

        existing_job = self._scheduler.get_job(self._job_id)
        if existing_job is not None:
            self._logger.debug("[scheduler] Removing existing job before rescheduling")
            existing_job.remove()

        self._scheduler.add_job(
            func=self._run_tick_safe,
            trigger="interval",
            seconds=interval,
            id=self._job_id,
            replace_existing=True,
            max_instances=1,
            coalesce=True,
        )
        self._current_interval_seconds = interval
        self._logger.info("[scheduler] Job scheduled with interval=%d seconds", interval)

    def reschedule(self) -> None:
        with self._lock:
            if self._scheduler is None:
                self._logger.debug("[scheduler] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)")
                return
            
            self._logger.info("[scheduler] Rescheduling automation job")
            self._schedule_or_reschedule_locked()

    def stop(self) -> None:
        with self._lock:
            if self._scheduler is None:
                self._logger.debug("[scheduler] Stop called but scheduler already stopped")
                return

            self._logger.info("[scheduler] Shutting down scheduler")
            self._scheduler.shutdown(wait=False)
            self._scheduler = None

    def is_running(self) -> bool:
        with self._lock:
            if self._scheduler is None:
                return False

            return getattr(self._scheduler, "running", False)
