import threading
from typing import Callable

from apscheduler.schedulers.background import BackgroundScheduler

from .config_store import BaseStore


class SchedulerService:
    def __init__(self, settings_store: BaseStore, tick_callable: Callable[[], None]) -> None:
        self._settings_store = settings_store
        self._tick_callable = tick_callable
        self._scheduler: BackgroundScheduler | None = None
        self._job_id = "automation_tick"
        self._lock = threading.Lock()

    def _get_interval_seconds(self) -> int:
        settings = self._settings_store.read()
        raw = settings.get("poll_interval_seconds", 120)

        try:
            interval = int(raw)
        except (TypeError, ValueError):
            interval = 120

        if interval < 15:
            interval = 15

        return interval

    def start(self) -> None:
        with self._lock:
            if self._scheduler is not None:
                return

            self._scheduler = BackgroundScheduler(daemon=True)
            self._scheduler.start()
            self._schedule_or_reschedule_locked()

    def _schedule_or_reschedule_locked(self) -> None:
        if self._scheduler is None:
            return

        interval = self._get_interval_seconds()

        existing_job = self._scheduler.get_job(self._job_id)
        if existing_job is not None:
            existing_job.remove()

        self._scheduler.add_job(
            func=self._tick_callable,
            trigger="interval",
            seconds=interval,
            id=self._job_id,
            replace_existing=True,
            max_instances=1,
            coalesce=True,
        )

    def reschedule(self) -> None:
        with self._lock:
            self._schedule_or_reschedule_locked()

    def stop(self) -> None:
        with self._lock:
            if self._scheduler is None:
                return

            self._scheduler.shutdown(wait=False)
            self._scheduler = None

    def is_running(self) -> bool:
        with self._lock:
            if self._scheduler is None:
                return False

            return getattr(self._scheduler, "running", False)
