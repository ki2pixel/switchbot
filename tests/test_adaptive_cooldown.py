"""Tests pour le cooldown adaptatif (ON vs OFF actions)."""
from __future__ import annotations

import copy
import datetime as dt
from typing import Any

from switchbot_dashboard.automation import AutomationService
from switchbot_dashboard.quota import ApiQuotaTracker


class MemoryStore:
    def __init__(self, initial: dict[str, Any] | None = None) -> None:
        self._data = copy.deepcopy(initial or {})

    def read(self) -> dict[str, Any]:
        return copy.deepcopy(self._data)

    def write(self, new_data: dict[str, Any]) -> None:
        self._data = copy.deepcopy(new_data)


class DummyClient:
    def __init__(self, temperature: float, quota_tracker: ApiQuotaTracker | None = None) -> None:
        self.temperature = temperature
        self.run_scene_calls: list[str] = []
        self._quota_tracker = quota_tracker

    def _record_quota(self) -> None:
        if self._quota_tracker:
            self._quota_tracker.record_call()

    def get_device_status(self, device_id: str) -> dict[str, Any]:
        self._record_quota()
        return {"body": {"temperature": self.temperature, "humidity": 50}}

    def run_scene(self, scene_id: str) -> None:
        self._record_quota()
        self.run_scene_calls.append(scene_id)


class DummyIFTTTClient:
    def __init__(self) -> None:
        self.webhook_calls: list[str] = []

    def trigger_webhook(self, webhook_url: str, *, event_data: dict | None = None) -> None:
        self.webhook_calls.append(webhook_url)


def _default_settings() -> dict[str, Any]:
    return {
        "automation_enabled": True,
        "mode": "winter",
        "meter_device_id": "meter-1",
        "aircon_device_id": "aircon-1",
        "hysteresis_celsius": 0.5,
        "command_cooldown_seconds": 60,
        "action_on_cooldown_seconds": 300,
        "action_off_cooldown_seconds": 60,
        "time_windows": [
            {"days": [0, 1, 2, 3, 4, 5, 6], "start": "00:00", "end": "23:59"}
        ],
        "winter": {
            "min_temp": 18.0,
            "max_temp": 24.0,
            "target_temp": 21.0,
            "ac_mode": 5,
            "fan_speed": 3,
        },
        "aircon_scenes": {
            "winter": "scene-w",
            "off": "scene-off",
        },
    }


def _build_service(
    *,
    settings: dict[str, Any],
    temperature: float,
    initial_state: dict[str, Any] | None = None,
) -> tuple[AutomationService, DummyClient, MemoryStore, MemoryStore]:
    settings_store = MemoryStore(settings)
    state_store = MemoryStore(initial_state or {})
    quota_tracker = ApiQuotaTracker(state_store)
    client = DummyClient(temperature=temperature, quota_tracker=quota_tracker)
    ifttt_client = DummyIFTTTClient()
    service = AutomationService(settings_store, state_store, client, ifttt_client)
    return service, client, settings_store, state_store


def test_adaptive_cooldown_blocks_on_action_for_5_minutes() -> None:
    """
    Vérifie que après un démarrage (ON), le cooldown est de 5 minutes (action_on_cooldown_seconds).
    """
    settings = _default_settings()
    now_utc = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    last_action_at = (now_utc - dt.timedelta(minutes=4, seconds=30)).isoformat()
    
    initial_state = {
        "assumed_aircon_power": "on",
        "last_action": "ifttt_webhook(winter)",
        "last_action_at": last_action_at,
    }
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=17.0,  # Inférieur à min_temp - hysteresis
        initial_state=initial_state,
    )

    service.run_once()

    # Cooldown encore actif (4m30s < 5min) → Aucune nouvelle action
    assert client.run_scene_calls == []
    state = state_store.read()
    assert state["assumed_aircon_power"] == "on"
    assert state["last_action"] == "ifttt_webhook(winter)"


def test_adaptive_cooldown_allows_on_action_after_5_minutes() -> None:
    """
    Vérifie qu'après 5 minutes (action_on_cooldown_seconds), une nouvelle action ON est autorisée.
    """
    settings = _default_settings()
    now_utc = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    last_action_at = (now_utc - dt.timedelta(minutes=5, seconds=1)).isoformat()
    
    initial_state = {
        "assumed_aircon_power": "on",
        "last_action": "ifttt_webhook(winter)",
        "last_action_at": last_action_at,
    }
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=17.0,
        initial_state=initial_state,
    )

    service.run_once()

    # Cooldown expiré (5m01s > 5min) → Nouvelle action autorisée
    assert client.run_scene_calls == ["scene-w"]


def test_adaptive_cooldown_blocks_off_action_for_1_minute() -> None:
    """
    Vérifie que après un arrêt (OFF), le cooldown est de 1 minute (action_off_cooldown_seconds).
    """
    settings = _default_settings()
    now_utc = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    last_action_at = (now_utc - dt.timedelta(seconds=45)).isoformat()
    
    initial_state = {
        "assumed_aircon_power": "off",
        "last_action": "ifttt_webhook(off)",
        "last_action_at": last_action_at,
    }
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=17.0,  # Doit redémarrer
        initial_state=initial_state,
    )

    service.run_once()

    # Cooldown encore actif (45s < 1min) → Aucune nouvelle action
    assert client.run_scene_calls == []
    state = state_store.read()
    assert state["assumed_aircon_power"] == "off"


def test_adaptive_cooldown_allows_off_action_after_1_minute() -> None:
    """
    Vérifie qu'après 1 minute (action_off_cooldown_seconds), une nouvelle action est autorisée.
    """
    settings = _default_settings()
    now_utc = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    last_action_at = (now_utc - dt.timedelta(minutes=1, seconds=1)).isoformat()
    
    initial_state = {
        "assumed_aircon_power": "off",
        "last_action": "ifttt_webhook(off)",
        "last_action_at": last_action_at,
    }
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=17.0,  # Doit redémarrer
        initial_state=initial_state,
    )

    service.run_once()

    # Cooldown expiré (1m01s > 1min) → Nouvelle action autorisée
    assert client.run_scene_calls == ["scene-w"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "on"


def test_adaptive_cooldown_falls_back_to_default() -> None:
    """
    Vérifie que si action_on/off_cooldown_seconds ne sont pas configurés,
    on utilise command_cooldown_seconds (rétro-compatibilité).
    """
    settings = _default_settings()
    del settings["action_on_cooldown_seconds"]
    del settings["action_off_cooldown_seconds"]
    settings["command_cooldown_seconds"] = 120
    
    now_utc = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    last_action_at = (now_utc - dt.timedelta(seconds=90)).isoformat()
    
    initial_state = {
        "assumed_aircon_power": "on",
        "last_action": "ifttt_webhook(winter)",
        "last_action_at": last_action_at,
    }
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=17.0,
        initial_state=initial_state,
    )

    service.run_once()

    # Cooldown default actif (90s < 120s) → Aucune nouvelle action
    assert client.run_scene_calls == []


def test_adaptive_cooldown_logs_remaining_time(caplog: Any) -> None:
    """
    Vérifie que le cooldown loggue le temps restant et le type d'action.
    """
    import logging
    settings = _default_settings()
    now_utc = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    last_action_at = (now_utc - dt.timedelta(minutes=2, seconds=30)).isoformat()
    
    initial_state = {
        "assumed_aircon_power": "on",
        "last_action": "ifttt_webhook(winter)",
        "last_action_at": last_action_at,
    }
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=17.0,
        initial_state=initial_state,
    )

    caplog.set_level(logging.DEBUG, logger="switchbot_dashboard.automation")
    service.run_once()

    messages = [record.message for record in caplog.records if record.name == "switchbot_dashboard.automation"]
    
    # Vérifie que le log contient le type de cooldown et le temps restant
    assert any("Cooldown active (ON action)" in message for message in messages)
    assert any("remaining_time='2m30s'" in message or "remaining_time='2m29s'" in message for message in messages)
