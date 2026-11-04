"""Tests pour SchedulerService avec focus sur l'exécution du premier tick."""
from __future__ import annotations

import datetime as dt
import logging
import threading
import time
from typing import Any

from switchbot_dashboard.scheduler import SchedulerService
from switchbot_dashboard.config_store import StoreError


class MemoryStore:
    def __init__(self, initial: dict[str, Any] | None = None) -> None:
        self._data = initial or {}
        self._lock = threading.Lock()

    def read(self) -> dict[str, Any]:
        with self._lock:
            return dict(self._data)

    def write(self, new_data: dict[str, Any]) -> None:
        with self._lock:
            self._data = dict(new_data)


def test_scheduler_triggers_immediate_first_tick() -> None:
    """Vérifie que le scheduler déclenche un tick immédiatement au démarrage."""
    settings_store = MemoryStore({"poll_interval_seconds": 30})
    call_count = {"count": 0}

    def tick_callable() -> None:
        call_count["count"] += 1

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )

    # Démarre le scheduler
    scheduler.start()

    # Le premier tick doit être exécuté immédiatement (synchrone)
    assert call_count["count"] == 1, "Premier tick doit être exécuté immédiatement"

    # Arrêt du scheduler
    scheduler.stop()


def test_scheduler_logs_startup_information(caplog: Any) -> None:
    """Vérifie que le scheduler loggue correctement son démarrage."""
    settings_store = MemoryStore({"poll_interval_seconds": 15})

    def tick_callable() -> None:
        pass

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )

    caplog.set_level(logging.INFO)

    scheduler.start()

    # Vérifie que les logs sont présents
    messages = [record.message for record in caplog.records]
    assert any("[scheduler] BackgroundScheduler started successfully" in message for message in messages)
    assert any("[scheduler] Job scheduled with interval=15 seconds" in message for message in messages)
    assert any("[scheduler] Triggering immediate first tick" in message for message in messages)

    scheduler.stop()


def test_scheduler_interval_job_executes_periodically(monkeypatch: Any) -> None:
    """
    Le scheduler doit réellement déclencher des ticks périodiques.

    ``poll_interval_seconds`` est clampé à 15 s par la configuration métier.
    On patche donc l'intervalle effectif à 1 s pour rendre le test rapide et
    déterministe, sans modifier le comportement de production.
    """
    settings_store = MemoryStore({"poll_interval_seconds": 1})
    call_timestamps = []

    def tick_callable() -> None:
        call_timestamps.append(time.time())

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )
    monkeypatch.setattr(
        scheduler,
        "_get_effective_interval_seconds",
        lambda **kwargs: (1, "test"),
    )

    scheduler.start()

    # Given: le premier tick synchrone a déjà eu lieu au démarrage
    assert len(call_timestamps) == 1, "Premier tick immédiat doit fonctionner"

    # When: on laisse tourner le scheduler plus de deux intervalles
    time.sleep(2.5)

    scheduler.stop()

    # Then: au moins deux ticks périodiques supplémentaires ont été exécutés
    assert len(call_timestamps) >= 2, (
        f"APScheduler devait exécuter au moins 2 ticks, obtenu {len(call_timestamps)}"
    )


def test_scheduler_clamps_poll_interval_to_15_seconds() -> None:
    """Le minimum de 15 s est une règle métier, pas un bug scheduler."""
    settings_store = MemoryStore({"poll_interval_seconds": 1})
    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=lambda: None,
    )

    interval, mode = scheduler._get_effective_interval_seconds(
        now_utc=dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
    )

    assert interval == 15
    assert mode == "automation_disabled"



def test_scheduler_is_running_reports_correct_state() -> None:
    """Vérifie que is_running() retourne l'état correct."""
    settings_store = MemoryStore({"poll_interval_seconds": 30})

    def tick_callable() -> None:
        pass

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )

    # Avant démarrage
    assert not scheduler.is_running()

    # Après démarrage
    scheduler.start()
    assert scheduler.is_running()

    # Après arrêt
    scheduler.stop()
    assert not scheduler.is_running()


def test_scheduler_duplicate_start_is_safe() -> None:
    """Vérifie que start() peut être appelé plusieurs fois sans erreur."""
    settings_store = MemoryStore({"poll_interval_seconds": 30})
    call_count = {"count": 0}

    def tick_callable() -> None:
        call_count["count"] += 1

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )

    scheduler.start()
    initial_count = call_count["count"]

    # Appel start() une seconde fois
    scheduler.start()

    # Le compteur ne devrait pas avoir augmenté (pas de second tick immédiat)
    assert call_count["count"] == initial_count

    scheduler.stop()


def test_run_tick_safe_logs_exceptions(caplog: Any) -> None:
    """Vérifie que les exceptions des ticks sont capturées et logguées."""
    settings_store = MemoryStore({"poll_interval_seconds": 30})

    def tick_callable() -> None:
        raise RuntimeError("tick boom")

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )

    caplog.set_level(logging.ERROR)

    # Appel direct pour isoler le wrapper
    scheduler._run_tick_safe()

    assert any(
        "Automation tick raised exception" in record.message for record in caplog.records
    )


class FailingStore(MemoryStore):
    def read(self) -> dict[str, Any]:
        raise StoreError("database is down")


def test_run_tick_safe_survives_reschedule_store_failure(caplog: Any) -> None:
    """Une panne store dans le finally ne doit pas tuer le job APScheduler."""
    scheduler = SchedulerService(
        settings_store=FailingStore(),
        tick_callable=lambda: None,
    )
    # Simule un scheduler démarré sans lancer de thread réel.
    scheduler._scheduler = object()
    scheduler._current_interval_seconds = 30

    caplog.set_level(logging.ERROR)

    # Given/When: le store tombe pendant _maybe_reschedule_after_tick
    scheduler._run_tick_safe()

    # Then: l'exception est capturée et loguée, pas propagée
    assert any(
        "Post-tick reschedule failed" in record.message for record in caplog.records
    )


def test_reschedule_failure_keeps_existing_job() -> None:
    """Un échec de reschedule ne doit pas supprimer le job existant."""
    scheduler = SchedulerService(
        settings_store=MemoryStore({"poll_interval_seconds": 15}),
        tick_callable=lambda: None,
    )
    scheduler.start()
    try:
        internal = scheduler.get_scheduler()
        assert internal is not None
        assert internal.get_job(scheduler._job_id) is not None

        # Given: le store devient indisponible
        scheduler._settings_store = FailingStore()

        # When: reschedule est appelé
        scheduler.reschedule()

        # Then: le job précédent est toujours planifié
        assert internal.get_job(scheduler._job_id) is not None
    finally:
        scheduler.stop()



def test_effective_interval_outside_window_uses_idle_interval() -> None:
    settings_store = MemoryStore(
        {
            "automation_enabled": True,
            "poll_interval_seconds": 15,
            "idle_poll_interval_seconds": 600,
            "poll_warmup_minutes": 15,
            "timezone": "UTC",
            "time_windows": [{"days": [0], "start": "10:00", "end": "00:00"}],
        }
    )

    scheduler = SchedulerService(settings_store=settings_store, tick_callable=lambda: None)

    now_utc = dt.datetime(2026, 1, 26, 5, 0, tzinfo=dt.timezone.utc)  # Monday
    interval, mode = scheduler._get_effective_interval_seconds(now_utc=now_utc)
    assert interval == 600
    assert mode == "idle"


def test_effective_interval_disables_adaptive_mode_when_flag_off() -> None:
    settings_store = MemoryStore(
        {
            "automation_enabled": True,
            "adaptive_polling_enabled": False,
            "poll_interval_seconds": 120,
            "idle_poll_interval_seconds": 900,
            "poll_warmup_minutes": 30,
            "timezone": "UTC",
            "time_windows": [{"days": [0], "start": "10:00", "end": "00:00"}],
        }
    )

    scheduler = SchedulerService(settings_store=settings_store, tick_callable=lambda: None)

    now_utc = dt.datetime(2026, 1, 26, 5, 0, tzinfo=dt.timezone.utc)
    interval, mode = scheduler._get_effective_interval_seconds(now_utc=now_utc)
    assert interval == 120
    assert mode == "fixed"


def test_effective_interval_idle_is_clamped_to_warmup_boundary() -> None:
    settings_store = MemoryStore(
        {
            "automation_enabled": True,
            "poll_interval_seconds": 15,
            "idle_poll_interval_seconds": 7200,
            "poll_warmup_minutes": 30,
            "timezone": "UTC",
            "time_windows": [{"days": [0], "start": "10:00", "end": "00:00"}],
        }
    )

    scheduler = SchedulerService(settings_store=settings_store, tick_callable=lambda: None)

    now_utc = dt.datetime(2026, 1, 26, 8, 0, tzinfo=dt.timezone.utc)
    interval, mode = scheduler._get_effective_interval_seconds(now_utc=now_utc)
    assert interval == 5400
    assert mode == "idle"


def test_effective_interval_warmup_before_window_uses_base_interval() -> None:
    settings_store = MemoryStore(
        {
            "automation_enabled": True,
            "poll_interval_seconds": 15,
            "idle_poll_interval_seconds": 600,
            "poll_warmup_minutes": 30,
            "timezone": "UTC",
            "time_windows": [{"days": [0], "start": "10:00", "end": "00:00"}],
        }
    )

    scheduler = SchedulerService(settings_store=settings_store, tick_callable=lambda: None)

    now_utc = dt.datetime(2026, 1, 26, 9, 45, tzinfo=dt.timezone.utc)  # 15 minutes before start
    interval, mode = scheduler._get_effective_interval_seconds(now_utc=now_utc)
    assert interval == 15
    assert mode == "warmup"


def test_effective_interval_in_window_uses_base_interval() -> None:
    settings_store = MemoryStore(
        {
            "automation_enabled": True,
            "poll_interval_seconds": 15,
            "idle_poll_interval_seconds": 600,
            "poll_warmup_minutes": 15,
            "timezone": "UTC",
            "time_windows": [{"days": [0], "start": "10:00", "end": "00:00"}],
        }
    )

    scheduler = SchedulerService(settings_store=settings_store, tick_callable=lambda: None)

    now_utc = dt.datetime(2026, 1, 26, 12, 0, tzinfo=dt.timezone.utc)
    interval, mode = scheduler._get_effective_interval_seconds(now_utc=now_utc)
    assert interval == 15
    assert mode == "in_window"


def test_effective_interval_pending_off_repeat_forces_base_interval() -> None:
    settings_store = MemoryStore(
        {
            "automation_enabled": True,
            "poll_interval_seconds": 15,
            "idle_poll_interval_seconds": 600,
            "poll_warmup_minutes": 15,
            "timezone": "UTC",
            "time_windows": [{"days": [0], "start": "10:00", "end": "00:00"}],
        }
    )
    state_store = MemoryStore({"pending_off_repeat": {"remaining": 2, "interval_seconds": 10, "next_run_at": "2026-01-26T05:00:00+00:00"}})
    scheduler = SchedulerService(settings_store=settings_store, state_store=state_store, tick_callable=lambda: None)

    now_utc = dt.datetime(2026, 1, 26, 5, 0, tzinfo=dt.timezone.utc)
    interval, mode = scheduler._get_effective_interval_seconds(now_utc=now_utc)
    assert interval == 15
    assert mode == "pending_off_repeat"


def test_scheduler_start_handles_tick_exception(caplog: Any) -> None:
    """Vérifie que le premier tick n'explose pas le scheduler même en cas d'erreur."""
    settings_store = MemoryStore({"poll_interval_seconds": 30})
    call_count = {"attempts": 0}

    def tick_callable() -> None:
        call_count["attempts"] += 1
        raise RuntimeError("boom at start")

    scheduler = SchedulerService(
        settings_store=settings_store,
        tick_callable=tick_callable,
    )

    caplog.set_level(logging.ERROR)

    # Ne doit pas lever malgré l'exception
    scheduler.start()
    scheduler.stop()

    assert call_count["attempts"] == 1
    assert any(
        "Automation tick raised exception" in record.message for record in caplog.records
    )
