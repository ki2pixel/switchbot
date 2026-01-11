from __future__ import annotations

import copy
import logging
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
        self.send_command_calls: list[dict[str, Any]] = []
        self.last_quota_snapshot: dict[str, int] | None = None
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

    def send_command(
        self,
        device_id: str,
        *,
        command: str,
        parameter: str = "default",
        command_type: str = "command",
    ) -> None:
        self._record_quota()
        self.send_command_calls.append(
            {
                "device_id": device_id,
                "command": command,
                "parameter": parameter,
                "command_type": command_type,
            }
        )

    def get_last_quota_snapshot(self) -> dict[str, int] | None:
        return self.last_quota_snapshot


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
        "command_cooldown_seconds": 0,
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
        "summer": {
            "min_temp": 22.0,
            "max_temp": 26.0,
            "target_temp": 24.0,
            "ac_mode": 2,
            "fan_speed": 2,
        },
        "aircon_scenes": {
            "winter": "scene-w",
            "summer": "scene-s",
            "fan": "scene-f",
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


def test_run_once_prefers_winter_scene_and_records_quota() -> None:
    settings = _default_settings()
    service, client, _settings_store, state_store = _build_service(
        settings=settings, temperature=17.0
    )

    service.run_once()

    assert client.run_scene_calls == ["scene-w"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "on"
    assert str(state["last_action"]).startswith("scene(")
    assert int(state["api_requests_total"]) >= 1


def test_run_once_falls_back_to_setall_when_scene_missing() -> None:
    settings = _default_settings()
    settings["aircon_scenes"]["winter"] = ""
    service, client, _settings_store, state_store = _build_service(
        settings=settings, temperature=17.0
    )

    service.run_once()

    assert client.run_scene_calls == []
    assert len(client.send_command_calls) == 1
    command = client.send_command_calls[0]
    assert command["command"] == "setAll"
    state = state_store.read()
    assert state["assumed_aircon_power"] == "on"
    assert str(state["last_action"]).startswith("setAll(")


def test_turn_off_outside_window_prefers_off_scene() -> None:
    settings = _default_settings()
    settings["time_windows"] = []
    settings["turn_off_outside_windows"] = True
    service, client, _settings_store, state_store = _build_service(
        settings=settings, temperature=23.0
    )

    service.run_once()

    assert client.run_scene_calls == ["scene-off"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "off"
    assert "automation_off_outside_window" in state["last_action"]


def test_turn_off_falls_back_to_turnoff_command_when_scene_missing() -> None:
    settings = _default_settings()
    settings["time_windows"] = []
    settings["turn_off_outside_windows"] = True
    settings["aircon_scenes"]["off"] = ""
    service, client, _settings_store, state_store = _build_service(
        settings=settings, temperature=23.0
    )

    service.run_once()

    assert client.run_scene_calls == []
    assert len(client.send_command_calls) == 1
    command = client.send_command_calls[0]
    assert command["command"] == "turnOff"
    state = state_store.read()
    assert state["assumed_aircon_power"] == "off"
    assert state["last_action"] == "turnOff"


def test_run_once_emits_detailed_logs(caplog: Any) -> None:
    settings = _default_settings()
    # Force thresholds that will trigger a winter ON action.
    settings["winter"]["min_temp"] = 24.0
    settings["winter"]["max_temp"] = 27.0
    settings["winter"]["target_temp"] = 26.0

    service, client, _settings_store, _state_store = _build_service(
        settings=settings,
        temperature=23.0,
    )

    caplog.set_level(logging.DEBUG, logger="switchbot_dashboard.automation")

    service.run_once()

    # Ensure the automation took the expected action.
    assert client.run_scene_calls == ["scene-w"]

    messages = [record.message for record in caplog.records if record.name == "switchbot_dashboard.automation"]
    assert any("Automation tick started" in message for message in messages)
    assert any("Time window evaluation" in message for message in messages)
    assert any("Temperature evaluation" in message for message in messages)
    assert any("Winter mode: below min threshold" in message for message in messages)
    assert any("Automation tick finished" in message and "outcome='winter_on'" in message for message in messages)


def test_winter_mode_above_max_temp_triggers_off_action() -> None:
    """Test que le mode hiver déclenche l'action OFF quand température > max_temp + hysteresis."""
    settings = _default_settings()
    settings["winter"]["min_temp"] = 24.0
    settings["winter"]["max_temp"] = 27.0
    settings["hysteresis_celsius"] = 0.3
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=28.1,  # Dépasse max_temp (27.0) + hysteresis (0.3) = 27.3
    )

    service.run_once()

    # Vérifie que la scène OFF a été appelée
    assert client.run_scene_calls == ["scene-off"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "off"
    assert "automation_winter_off" in state["last_action"]


def test_winter_mode_above_max_within_hysteresis_no_action() -> None:
    """Test qu'aucune action n'est prise si température entre max_temp et max_temp + hysteresis."""
    settings = _default_settings()
    settings["winter"]["min_temp"] = 24.0
    settings["winter"]["max_temp"] = 27.0
    settings["hysteresis_celsius"] = 0.5
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=27.2,  # Entre max_temp (27.0) et max_temp + hysteresis (27.5)
    )

    service.run_once()

    # Aucune action ne doit être déclenchée (hystérésis)
    assert client.run_scene_calls == []
    assert client.send_command_calls == []
    state = state_store.read()
    # last_action ne devrait pas contenir winter_off ou winter_on
    last_action = state.get("last_action", "")
    assert "winter_off" not in str(last_action)
    assert "winter_on" not in str(last_action)
