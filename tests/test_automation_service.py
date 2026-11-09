from __future__ import annotations

import copy
import logging
import threading
from typing import Any

import pytest

import datetime as dt
from unittest.mock import MagicMock, patch
from zoneinfo import ZoneInfo

from switchbot_dashboard.automation import (
    AutomationService,
    CachedStoreWrapper,
    LockLostError,
    _build_aircon_status_updates,
    _is_now_in_windows,
)
from switchbot_dashboard.quota import ApiQuotaTracker


class MemoryStore:
    def __init__(self, initial: dict[str, Any] | None = None) -> None:
        self._data = copy.deepcopy(initial or {})

    def read(self) -> dict[str, Any]:
        return copy.deepcopy(self._data)

    def write(self, new_data: dict[str, Any]) -> None:
        self._data = copy.deepcopy(new_data)


class DummyClient:
    def __init__(
        self,
        temperature: float,
        quota_tracker: ApiQuotaTracker | None = None,
        aircon_power: str = "off",
        aircon_mode: int = 4,
        aircon_temp: float = 22.0,
        aircon_fan_speed: int = 3,
    ) -> None:
        self.temperature = temperature
        self.run_scene_calls: list[str] = []
        self.send_command_calls: list[dict[str, Any]] = []
        self.last_quota_snapshot: dict[str, int] | None = None
        self._quota_tracker = quota_tracker
        self.aircon_power = aircon_power
        self.aircon_mode = aircon_mode
        self.aircon_temp = aircon_temp
        self.aircon_fan_speed = aircon_fan_speed

    def _record_quota(self) -> None:
        if self._quota_tracker:
            self._quota_tracker.record_call()

    def get_device_status(self, device_id: str) -> dict[str, Any]:
        self._record_quota()
        if "meter" in device_id:
            return {"body": {"temperature": self.temperature, "humidity": 50}}
        else:
            return {
                "body": {
                    "deviceId": device_id,
                    "deviceType": "Air Conditioner",
                    "power": self.aircon_power,
                    "mode": self.aircon_mode,
                    "temperature": self.aircon_temp,
                    "fanSpeed": self.aircon_fan_speed,
                }
            }

    def run_scene(self, scene_id: str) -> None:
        self._record_quota()
        self.run_scene_calls.append(scene_id)
        if "off" in scene_id:
            self.aircon_power = "off"
        elif "-f" in scene_id or "fan" in scene_id:
            self.aircon_power = "on"
            self.aircon_mode = 4
        elif "-w" in scene_id:
            self.aircon_power = "on"
            self.aircon_mode = 5
        elif "-s" in scene_id:
            self.aircon_power = "on"
            self.aircon_mode = 2

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
        if command == "turnOff":
            self.aircon_power = "off"
        elif command == "setAll":
            parts = parameter.split(",")
            if len(parts) == 4:
                try:
                    self.aircon_temp = float(parts[0])
                    self.aircon_mode = int(parts[1])
                    self.aircon_fan_speed = int(parts[2])
                    self.aircon_power = parts[3]
                except ValueError:
                    pass

    def get_last_quota_snapshot(self) -> dict[str, int] | None:
        return self.last_quota_snapshot




def _default_settings() -> dict[str, Any]:
    return {
        "automation_enabled": True,
        "mode": "winter",
        "trigger_mode": "direct",
        "meter_device_id": "meter-1",
        "aircon_device_id": "aircon-1",
        "hysteresis_celsius": 0.5,
        "command_cooldown_seconds": 0,
        "off_repeat_count": 1,
        "off_repeat_interval_seconds": 10,
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
    
    # Propagate initial assumed state to dummy client status to maintain consistency in tests
    kwargs = {}
    if initial_state and "assumed_aircon_power" in initial_state:
        kwargs["aircon_power"] = initial_state["assumed_aircon_power"]
    if initial_state and "assumed_aircon_mode" in initial_state:
        kwargs["aircon_mode"] = initial_state["assumed_aircon_mode"]

    client = DummyClient(temperature=temperature, quota_tracker=quota_tracker, **kwargs)
    service = AutomationService(settings_store, state_store, client)
    return service, client, settings_store, state_store


@patch("switchbot_dashboard.automation.ZoneInfo")
def test_get_timezone_caches_valid_zone(mock_zoneinfo: MagicMock) -> None:
    """Vérifie que les résolutions de timezone sont mises en cache."""
    mock_zone_instance = MagicMock()
    mock_zoneinfo.return_value = mock_zone_instance

    settings = _default_settings()
    settings["timezone"] = "Europe/Paris"

    service, _, _, _ = _build_service(settings=settings, temperature=20.0)

    tz1 = service._get_timezone(settings, trigger="test")
    tz2 = service._get_timezone(settings, trigger="test")

    assert tz1 == (mock_zone_instance, "Europe/Paris")
    assert tz2 == (mock_zone_instance, "Europe/Paris")
    mock_zoneinfo.assert_called_once_with("Europe/Paris")


def test_get_timezone_fallback_cached(caplog: Any) -> None:
    """Vérifie que les timezones invalides se replient vers UTC et sont mises en cache."""
    settings = _default_settings()
    settings["timezone"] = "Invalid/Timezone"

    service, _, _, _ = _build_service(settings=settings, temperature=20.0)

    caplog.set_level(logging.WARNING)

    tz1 = service._get_timezone(settings, trigger="test")
    tz2 = service._get_timezone(settings, trigger="test")

    assert tz1[1] == "UTC"
    assert tz1[0] is dt.timezone.utc
    assert tz2 == tz1
    warnings = [record for record in caplog.records if "Invalid timezone" in record.message]
    assert len(warnings) == 1  # logged once thanks au cache


@patch("switchbot_dashboard.automation.ZoneInfo")
def test_get_timezone_cache_invalidated_on_change(mock_zoneinfo: MagicMock) -> None:
    """Vérifie que changer de timezone invalide le cache."""
    paris_zone = MagicMock(name="paris")
    ny_zone = MagicMock(name="ny")
    mock_zoneinfo.side_effect = [paris_zone, ny_zone]

    settings = _default_settings()
    settings["timezone"] = "Europe/Paris"

    service, _, _, _ = _build_service(settings=settings, temperature=20.0)

    tz1 = service._get_timezone(settings, trigger="test")
    assert tz1 == (paris_zone, "Europe/Paris")

    settings["timezone"] = "America/New_York"
    tz2 = service._get_timezone(settings, trigger="test")
    assert tz2 == (ny_zone, "America/New_York")

    assert mock_zoneinfo.call_count == 2


def test_run_once_records_history_when_automation_disabled() -> None:
    # Given: automation is disabled but the meter is still polled
    settings = _default_settings()
    settings["automation_enabled"] = False
    settings_store = MemoryStore(settings)
    state_store = MemoryStore({"last_temperature": 19.0, "last_humidity": 55})
    client = DummyClient(temperature=19.0)
    history = MagicMock()
    service = AutomationService(
        settings_store, state_store, client, history_service=history
    )

    # When: a tick runs
    service.run_once()

    # Then: the reading is persisted to history exactly once
    history.record_state.assert_called_once()
    recorded_state, timezone_name = history.record_state.call_args.args
    assert recorded_state["last_temperature"] == 19.0
    assert timezone_name == "Europe/Paris"


def test_run_once_records_history_outside_time_window() -> None:
    # Given: automation is enabled but the current time matches no window
    settings = _default_settings()
    settings["time_windows"] = [
        {"days": [], "start": "00:00", "end": "23:59"}
    ]
    settings_store = MemoryStore(settings)
    state_store = MemoryStore({"last_temperature": 23.0, "last_humidity": 48})
    client = DummyClient(temperature=23.0)
    history = MagicMock()
    service = AutomationService(
        settings_store, state_store, client, history_service=history
    )

    # When: a tick runs outside the configured window
    service.run_once()

    # Then: the meter reading is still recorded (no chart gap)
    history.record_state.assert_called_once()
    recorded_state, _timezone_name = history.record_state.call_args.args
    assert recorded_state["last_temperature"] == 23.0


def test_run_once_records_history_once_on_normal_tick() -> None:
    # Given: a standard tick inside the automation window
    settings = _default_settings()
    settings_store = MemoryStore(settings)
    state_store = MemoryStore({})
    client = DummyClient(temperature=17.0)
    history = MagicMock()
    service = AutomationService(
        settings_store, state_store, client, history_service=history
    )

    # When: the tick executes the normal automation path
    service.run_once()

    # Then: exactly one snapshot is recorded (no duplicate)
    history.record_state.assert_called_once()


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
        settings=settings, temperature=23.0, initial_state={"assumed_aircon_power": "on"}
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
        settings=settings, temperature=23.0, initial_state={"assumed_aircon_power": "on"}
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
        initial_state={"assumed_aircon_power": "on"},
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


def test_winter_off_skipped_when_repeat_pending() -> None:
    """Test que winter_off ne se déclenche pas si une répétition OFF est déjà en attente."""
    settings = _default_settings()
    settings["winter"]["min_temp"] = 24.0
    settings["winter"]["max_temp"] = 27.0
    settings["hysteresis_celsius"] = 0.3
    settings["off_repeat_count"] = 2
    settings["off_repeat_interval_seconds"] = 10
    
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=27.5,  # > max_temp + hysteresis (27.3)
        initial_state={"assumed_aircon_power": "on"},
    )

    # Premier tick : déclenche winter_off et planifie une répétition
    service.run_once()
    assert client.run_scene_calls == ["scene-off"]
    state = state_store.read()
    assert state.get("pending_off_repeat") is not None
    assert state["pending_off_repeat"]["remaining"] == 1

    # Réinitialiser les compteurs du mock client
    client.run_scene_calls.clear()

    # Deuxième tick immédiat : température toujours > 27.3, mais répétition en attente
    service.run_once()
    
    # Aucune nouvelle action OFF ne doit être déclenchée
    assert client.run_scene_calls == []
    assert client.send_command_calls == []
    state = state_store.read()
    # La répétition doit toujours être en attente
    assert state.get("pending_off_repeat") is not None
    assert state["pending_off_repeat"]["remaining"] == 1


def test_winter_off_skipped_when_already_assumed_off() -> None:
    """Test que winter_off ne se déclenche pas si la clim est déjà supposée OFF.

    Cela évite une rafale de OFF toutes les ~N secondes (cooldown) tant que la
    température reste au-dessus de max_temp + hysteresis.
    """
    settings = _default_settings()
    settings["winter"]["min_temp"] = 24.0
    settings["winter"]["max_temp"] = 27.0
    settings["hysteresis_celsius"] = 0.3
    settings["off_repeat_count"] = 2
    settings["off_repeat_interval_seconds"] = 10

    initial_state = {
        "assumed_aircon_power": "off",
        "last_action": "manual_off",
        "last_action_at": "2000-01-01T00:00:00Z",
    }

    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=27.7,
        initial_state=initial_state,
    )

    service.run_once()

    assert client.run_scene_calls == []
    assert client.send_command_calls == []

    state = state_store.read()
    assert state.get("pending_off_repeat") is None


def test_time_window_evaluation_respects_timezone() -> None:
    time_windows = [{"days": [0, 1, 2, 3, 4, 5, 6], "start": "10:00", "end": "01:00"}]

    now_utc = dt.datetime(2026, 1, 12, 0, 30, tzinfo=dt.timezone.utc)
    now_paris = now_utc.astimezone(ZoneInfo("Europe/Paris"))

    assert now_paris.hour == 1
    assert now_paris.minute == 30

    assert _is_now_in_windows(time_windows, now_utc) is True
    assert _is_now_in_windows(time_windows, now_paris) is False


def test_time_window_crossing_midnight_includes_next_morning() -> None:
    """Une fenêtre 22:00-06:00 déclarée lundi reste active mardi matin."""
    # Given: a Monday-only window that crosses midnight
    time_windows = [{"days": [0], "start": "22:00", "end": "06:00"}]
    monday_late = dt.datetime(2026, 11, 2, 23, 0, tzinfo=dt.timezone.utc)
    tuesday_early = dt.datetime(2026, 11, 3, 5, 0, tzinfo=dt.timezone.utc)

    # When: the window is evaluated on the start day and the next morning
    start_day_result = _is_now_in_windows(time_windows, monday_late)
    next_day_result = _is_now_in_windows(time_windows, tuesday_early)

    # Then: both timestamps are inside the window
    assert start_day_result is True
    assert next_day_result is True


def test_time_window_crossing_midnight_excludes_outside_bounds() -> None:
    """Avant 22:00 et après 06:00, la fenêtre traversant minuit est fermée."""
    # Given: the same Monday-only 22:00-06:00 window
    time_windows = [{"days": [0], "start": "22:00", "end": "06:00"}]
    monday_evening = dt.datetime(2026, 11, 2, 21, 0, tzinfo=dt.timezone.utc)
    tuesday_morning = dt.datetime(2026, 11, 3, 7, 0, tzinfo=dt.timezone.utc)

    # When: timestamps fall one hour before the start and one hour after the end
    before_result = _is_now_in_windows(time_windows, monday_evening)
    after_result = _is_now_in_windows(time_windows, tuesday_morning)

    # Then: both timestamps are outside the window
    assert before_result is False
    assert after_result is False


def test_time_window_crossing_midnight_requires_start_day() -> None:
    """Le report au lendemain ne s'applique pas si seul mardi est déclaré."""
    # Given: a Tuesday-only window evaluated on Tuesday morning
    time_windows = [{"days": [1], "start": "22:00", "end": "06:00"}]
    tuesday_early = dt.datetime(2026, 11, 3, 5, 0, tzinfo=dt.timezone.utc)

    # When: the window is evaluated before Tuesday's 22:00 start
    result = _is_now_in_windows(time_windows, tuesday_early)

    # Then: the window is closed because Monday is not declared
    assert result is False


def test_time_window_without_midnight_crossing_does_not_spill() -> None:
    """Une fenêtre 08:00-18:00 ne déborde pas sur le lendemain."""
    # Given: a Monday-only daytime window
    time_windows = [{"days": [0], "start": "08:00", "end": "18:00"}]
    tuesday_noon = dt.datetime(2026, 11, 3, 12, 0, tzinfo=dt.timezone.utc)

    # When: the window is evaluated on Tuesday at noon
    result = _is_now_in_windows(time_windows, tuesday_noon)

    # Then: Tuesday is outside the declared day
    assert result is False


def test_fan_mode_neutral_zone_auto_start() -> None:
    """Test qu'en entrant dans la fenêtre horaire avec fan_mode_during_window=True, le climatiseur s'allume en mode ventilation si la température est neutre."""
    settings = _default_settings()
    settings["fan_mode_during_window"] = True
    settings["winter"]["min_temp"] = 18.0
    settings["winter"]["max_temp"] = 24.0
    
    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=21.0,  # Neutral zone
        initial_state={"assumed_aircon_power": "off"}
    )

    service.run_once()

    assert client.run_scene_calls == ["scene-f"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "on"
    assert "scene" in state["last_action"]


def test_fan_mode_over_max_temp_switches_to_fan() -> None:
    """Test qu'au sein de la fenêtre horaire, un dépassement de seuil thermique provoquant d'ordinaire un arrêt bascule bien en ventilation."""
    settings = _default_settings()
    settings["fan_mode_during_window"] = True
    settings["winter"]["min_temp"] = 18.0
    settings["winter"]["max_temp"] = 24.0
    settings["hysteresis_celsius"] = 0.5
    
    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=25.0,  # > max_temp + hysteresis -> trigger winter_off -> substituted by fan
        initial_state={"assumed_aircon_power": "on", "assumed_aircon_mode": 5}
    )

    service.run_once()

    assert client.run_scene_calls == ["scene-f"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "on"
    assert "scene" in state.get("last_action", "")


def test_fan_mode_off_repeat_repeats_fan() -> None:
    """Test que le cycle répétitif d'arrêt répète bien la commande de ventilation."""
    settings = _default_settings()
    settings["fan_mode_during_window"] = True
    settings["off_repeat_count"] = 2
    settings["off_repeat_interval_seconds"] = 10
    settings["winter"]["max_temp"] = 24.0
    
    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=25.0,
        initial_state={"assumed_aircon_power": "on", "assumed_aircon_mode": 5, "last_action": "manual_on"}
    )
    
    service.run_once()
    assert client.run_scene_calls == ["scene-f"]
    
    state = state_store.read()
    assert "pending_off_repeat" in state
    
    # Make the next run in the past to trigger immediately
    state["pending_off_repeat"]["next_run_at"] = "2000-01-01T00:00:00+00:00"
    state["last_action_at"] = "2000-01-01T00:00:00+00:00"
    state_store.write(state)
    client.run_scene_calls.clear()
    
    service.run_once()

    assert client.run_scene_calls == ["scene-f"]


def test_fan_mode_turn_off_outside_window() -> None:
    """Test qu'en sortant de la fenêtre horaire, le climatiseur s'éteint complètement."""
    settings = _default_settings()
    settings["fan_mode_during_window"] = True
    settings["turn_off_outside_windows"] = True
    settings["time_windows"] = []
    
    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=21.0,
        initial_state={"assumed_aircon_power": "on", "last_action": "manual_on"}
    )

    service.run_once()

    assert client.run_scene_calls == ["scene-off"]
    state = state_store.read()
    assert state["assumed_aircon_power"] == "off"


def test_trigger_scene_no_scene_with_device_id_no_error(caplog: Any) -> None:
    """Test qu'en mode direct, si la scène est manquante mais l'ID de l'appareil est présent, aucune erreur n'est remontée car le repli direct prendra le relais."""
    settings = _default_settings()
    settings["aircon_scenes"]["winter"] = ""
    settings["aircon_device_id"] = "device-123"
    
    service, _, _, state_store = _build_service(
        settings=settings, temperature=17.0
    )
    
    caplog.set_level(logging.DEBUG, logger="switchbot_dashboard.automation")
    
    result = service._trigger_scene(
        action_key="winter",
        scene_id="",
        state_reason="test",
        assumed_power="on",
        trigger="test",
        aircon_device_id="device-123"
    )
    
    assert result is False
    state = state_store.read()
    assert state.get("last_error") is None
    
    messages = [record.message for record in caplog.records if record.name == "switchbot_dashboard.automation"]
    assert any("will use direct API commands" in message for message in messages)


def test_automation_syncs_divergent_aircon_state() -> None:
    """Test that the automation service queries real-time status of AC,
    corrects the stored assumed state, and re-emits commands bypassing
    idempotency checks when they are divergent.
    """
    settings = _default_settings()
    settings["mode"] = "summer"
    settings["fan_mode_during_window"] = True
    settings["aircon_scenes"]["summer"] = ""  # No scene, force direct commands
    
    # Configure summer profile
    settings["summer"] = {
        "min_temp": 22.0,
        "max_temp": 25.0,
        "target_temp": 22.5,
        "ac_mode": 2,  # COOL
        "fan_speed": 4,
    }
    settings["hysteresis_celsius"] = 0.5

    # 1. State store initially assumes the AC is already set to COOL
    # (mode=2, legacy temp=22.5, speed=4, power=on). If the service didn't
    # poll, it would skip sending commands due to idempotency.
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": 2,
        "assumed_aircon_parameter": "22.5,2,4,on",
    }

    # 2. Build the service with a temperature that triggers summer cooling (26.3 > 25.5)
    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=26.3,
        initial_state=initial_state,
    )

    # 3. Simulate divergent AC physical status returned by the API:
    # The physical unit is actually in FAN mode (mode=4, temp=22.0, speed=3, power=on).
    client.aircon_power = "on"
    client.aircon_mode = 4
    client.aircon_temp = 22.0
    client.aircon_fan_speed = 3

    # 4. Execute the automation tick
    service.run_once()

    # 5. Assertions:
    # The service must have queried the real AC status and updated the state store to the physical values.
    # Then, it detected divergence (mode 4 physical vs mode 2 desired) and bypassed the idempotency skip.
    assert len(client.send_command_calls) == 1
    call = client.send_command_calls[0]
    assert call["device_id"] == "aircon-1"
    assert call["command"] == "setAll"
    # round(22.5) == 22 with Python's banker's rounding: the target is
    # normalized to an integer before building the setAll parameter.
    assert call["parameter"] == "22,2,4,on"

    # Finally, the state store must be updated to the new targeted state
    final_state = state_store.read()
    assert final_state["assumed_aircon_power"] == "on"
    assert final_state["assumed_aircon_mode"] == 2
    assert final_state["assumed_aircon_parameter"] == "22,2,4,on"


def test_poll_aircon_status_cooldown() -> None:
    """Test that when poll cooldown is active, poll_aircon_status does not query the API and returns cached status."""
    settings = _default_settings()
    settings["aircon_poll_cooldown_minutes"] = 15

    # Set up active cache state with a recent poll timestamp
    now = dt.datetime.now(dt.timezone.utc)
    recent_timestamp = now.isoformat()
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": 2,
        "assumed_aircon_parameter": "24.0,2,2,on",
        "last_aircon_poll_at": recent_timestamp,
    }

    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=20.0,
        initial_state=initial_state,
    )

    # If the API were queried, it would return physical power as "off",
    # but the cache says "on".
    client.aircon_power = "off"
    
    # Run poll without force
    with patch.object(client, "get_device_status", wraps=client.get_device_status) as mock_get_status:
        status = service.poll_aircon_status("aircon-1")
        assert mock_get_status.call_count == 0
        assert status == {
            "power": "on",
            "mode": 2,
            "temperature": 24,
            "fanSpeed": 2,
        }


def test_poll_aircon_status_force() -> None:
    """Test that passing force=True bypasses the cooldown and queries the physical API."""
    settings = _default_settings()
    settings["aircon_poll_cooldown_minutes"] = 15

    # Set up active cache state with a recent poll timestamp
    now = dt.datetime.now(dt.timezone.utc)
    recent_timestamp = now.isoformat()
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": 2,
        "assumed_aircon_parameter": "24.0,2,2,on",
        "last_aircon_poll_at": recent_timestamp,
    }

    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=20.0,
        initial_state=initial_state,
    )

    # Physical status differs
    client.aircon_power = "off"
    client.aircon_mode = 1
    client.aircon_temp = 20.0
    client.aircon_fan_speed = 3

    # Run poll with force=True
    with patch.object(client, "get_device_status", wraps=client.get_device_status) as mock_get_status:
        status = service.poll_aircon_status("aircon-1", force=True)
        assert mock_get_status.call_count == 1
        assert status == {
            "power": "off",
            "mode": 1,
            "temperature": 20.0,
            "fanSpeed": 3,
        }
        
        # Verify state store got updated
        updated_state = state_store.read()
        assert updated_state["assumed_aircon_power"] == "off"
        assert updated_state["last_aircon_poll_at"] != recent_timestamp


def test_poll_aircon_status_expiry() -> None:
    """Test that after the cooldown duration expires, a regular poll queries the physical API."""
    settings = _default_settings()
    settings["aircon_poll_cooldown_minutes"] = 15

    # Set up expired cache timestamp (e.g. 20 minutes ago)
    now = dt.datetime.now(dt.timezone.utc)
    expired_timestamp = (now - dt.timedelta(minutes=20)).isoformat()
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": 2,
        "assumed_aircon_parameter": "24.0,2,2,on",
        "last_aircon_poll_at": expired_timestamp,
    }

    service, client, _, state_store = _build_service(
        settings=settings,
        temperature=20.0,
        initial_state=initial_state,
    )

    # Physical status differs
    client.aircon_power = "off"
    client.aircon_mode = 1
    client.aircon_temp = 20.0
    client.aircon_fan_speed = 3

    # Run regular poll (force=False)
    with patch.object(client, "get_device_status", wraps=client.get_device_status) as mock_get_status:
        status = service.poll_aircon_status("aircon-1")
        assert mock_get_status.call_count == 1
        assert status == {
            "power": "off",
            "mode": 1,
            "temperature": 20.0,
            "fanSpeed": 3,
        }

        # Verify state store got updated
        updated_state = state_store.read()
        assert updated_state["assumed_aircon_power"] == "off"
        assert updated_state["last_aircon_poll_at"] != expired_timestamp


def test_poll_aircon_status_virtual_bypass() -> None:
    """Test that virtual infrared device IDs bypass API status queries entirely."""
    settings = _default_settings()
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": 2,
        "assumed_aircon_parameter": "24.0,2,2,on",
    }
    service, client, _, _ = _build_service(
        settings=settings,
        temperature=20.0,
        initial_state=initial_state,
    )
    
    # Run poll with virtual device ID (length > 12 and >= 2 hyphens)
    with patch.object(client, "get_device_status", wraps=client.get_device_status) as mock_get_status:
        status = service.poll_aircon_status("01-202401301615-24010246", force=True)
        # Should not call the API at all
        assert mock_get_status.call_count == 0
        assert status == {
            "power": "on",
            "mode": 2,
            "temperature": 24,
            "fanSpeed": 2,
        }


def test_automation_lock_lost_fencing_token_raised_and_handled() -> None:
    """Test that if the lock token is stolen during run_once, LockLostError is raised and caught."""
    settings = _default_settings()
    settings["automation_enabled"] = True
    settings["time_windows"] = [
        {"days": [0, 1, 2, 3, 4, 5, 6], "start": "00:00", "end": "23:59"}
    ]
    service, client, settings_store, state_store = _build_service(
        settings=settings,
        temperature=16.0,
    )
    
    # We monkeypatch self._run_once_impl to simulate lock theft mid-execution.
    # In _run_once_impl, we change the token in the state store directly behind the service's back.
    original_run_once_impl = service._run_once_impl
    
    def mock_run_once_impl():
        # Someone steals the lock! They increment the token.
        state = state_store.read()
        state["automation_lock_token"] = int(state.get("automation_lock_token", 0)) + 1
        state_store.write(state)
        # Call the original method which will try to write state (e.g. updating last_tick or recording outcomes)
        original_run_once_impl()
        
    service._run_once_impl = mock_run_once_impl
    
    # Execute run_once. It should not raise an unhandled exception, but it should log a warning
    # and abort safely without throwing an error to the scheduler.
    with patch.object(service, "_warning") as mock_warning:
        service.run_once()
        assert mock_warning.call_count >= 1
        warning_msg = mock_warning.call_args_list[0][0][0]
        assert "lock was lost or stolen" in warning_msg


def test_cached_store_wrapper_isolates_cache_per_thread() -> None:
    """Le cache du wrapper ne doit jamais être partagé entre threads."""
    backing_store = MemoryStore({"value": 1})
    wrapper = CachedStoreWrapper(backing_store)

    # Given: le thread principal a rempli son cache
    assert wrapper.read() == {"value": 1}
    backing_store.write({"value": 2})
    assert wrapper.read() == {"value": 1}

    # When: un autre thread lit le store
    result: dict[str, Any] = {}

    def worker() -> None:
        result["value"] = wrapper.read()

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()

    # Then: il voit la valeur réelle, pas le cache du thread principal
    assert result["value"] == {"value": 2}

    # Et le clear_cache du worker ne vide pas celui du main thread
    wrapper.clear_cache()
    assert wrapper.read() == {"value": 2}


def test_apply_state_updates_rejects_stolen_lock() -> None:
    """Le fencing token doit bloquer une écriture après vol du verrou."""
    service, _client, _settings_store, state_store = _build_service(
        settings=_default_settings(),
        temperature=20.0,
    )
    service._local.current_lock_token = 5
    state = state_store.read()
    state["automation_lock_token"] = 6
    state_store.write(state)

    with pytest.raises(LockLostError):
        service.apply_state_updates(last_error="stolen lock")


@pytest.mark.parametrize(
    ("action_key", "expected_mode"),
    [("winter", 5), ("summer", 2), ("fan", 4)],
)
def test_trigger_scene_preserves_aircon_mode(
    action_key: str, expected_mode: int
) -> None:
    """Une scène ne doit pas remettre assumed_aircon_mode à None."""
    service, client, _settings_store, state_store = _build_service(
        settings=_default_settings(),
        temperature=20.0,
    )

    # Given/When: la scène correspondant au mode est exécutée
    result = service._trigger_scene(
        action_key,
        f"scene-{action_key}",
        "manual",
        "on",
        "test",
        "",
    )

    # Then: le mode métier est conservé pour is_in_fan_mode et l'UI
    assert result is True
    assert client.run_scene_calls == [f"scene-{action_key}"]
    assert state_store.read()["assumed_aircon_mode"] == expected_mode


def test_missing_meter_still_records_history_snapshot(monkeypatch) -> None:
    """Une panne capteur ne doit pas créer un trou dans l'historique."""
    service, _client, _settings_store, _state_store = _build_service(
        settings=_default_settings(),
        temperature=20.0,
    )
    monkeypatch.setattr(service, "poll_meter", lambda: None)

    with patch.object(service, "_record_history_snapshot") as mock_record:
        # Given/When: le tick ne peut pas lire la température
        service.run_once()

    # Then: l'état stale est tout de même historisé
    mock_record.assert_called_once()


def test_invalid_temperature_still_records_history_snapshot(monkeypatch) -> None:
    """Une température invalide ne doit pas non plus trouer l'historique."""
    service, _client, _settings_store, _state_store = _build_service(
        settings=_default_settings(),
        temperature=20.0,
    )
    monkeypatch.setattr(service, "poll_meter", lambda: {"temperature": "n/a"})

    with patch.object(service, "_record_history_snapshot") as mock_record:
        # Given/When: la lecture capteur est corrompue
        service.run_once()

    # Then: l'état est historisé malgré l'abandon de l'automatisation
    mock_record.assert_called_once()


def test_invalid_profile_configuration_returns_invalid_profile() -> None:
    # Given: a profile with a non-numeric minimum temperature
    settings = _default_settings()
    settings["winter"]["min_temp"] = "n/a"
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=20.0,
    )

    # When: the automation tick evaluates the temperature
    service.run_once()

    # Then: the tick aborts with an explicit configuration error
    state = state_store.read()
    assert state["last_error"] == "Invalid profile configuration for mode: winter"
    assert client.run_scene_calls == []
    assert client.send_command_calls == []


def test_invalid_temperature_thresholds_returns_invalid_thresholds() -> None:
    # Given: a profile where min_temp is greater than max_temp
    settings = _default_settings()
    settings["winter"]["min_temp"] = 26.0
    settings["winter"]["max_temp"] = 20.0
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=20.0,
    )

    # When: the automation tick evaluates the temperature
    service.run_once()

    # Then: the invalid thresholds are reported and no action is sent
    state = state_store.read()
    assert state["last_error"] == "Invalid thresholds: min_temp > max_temp (winter)"
    assert client.run_scene_calls == []
    assert client.send_command_calls == []


def test_unknown_mode_with_valid_profile_returns_invalid_mode() -> None:
    # Given: an unknown mode backed by a valid profile
    settings = _default_settings()
    settings["mode"] = "spring"
    settings["spring"] = {
        "min_temp": 18.0,
        "max_temp": 24.0,
        "target_temp": 21.0,
        "ac_mode": 5,
        "fan_speed": 3,
    }
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=20.0,
    )

    # When: the automation tick evaluates the temperature
    service.run_once()

    # Then: the unknown mode is rejected without any command
    state = state_store.read()
    assert state["last_error"] == "Unknown mode: spring"
    assert client.run_scene_calls == []
    assert client.send_command_calls == []


def test_invalid_off_repeat_timestamp_clears_pending_task() -> None:
    # Given: a pending off-repeat task with an unparseable timestamp
    settings = _default_settings()
    initial_state = {
        "pending_off_repeat": {
            "remaining": 1,
            "interval_seconds": 10,
            "next_run_at": "not-a-date",
            "state_reason": "automation_off_outside_window",
        }
    }
    service, _client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=20.0,
        initial_state=initial_state,
    )

    # When: the automation tick processes the pending task
    service.run_once()

    # Then: the invalid task is cleared without raising
    assert state_store.read().get("pending_off_repeat") is None


def test_fan_mode_direct_fallback_when_scene_is_missing() -> None:
    # Given: fan mode enabled, no fan scene, and an aircon device id
    settings = _default_settings()
    settings["fan_mode_during_window"] = True
    settings["aircon_scenes"]["fan"] = ""
    service, client, _settings_store, state_store = _build_service(
        settings=settings,
        temperature=25.0,
        initial_state={
            "assumed_aircon_power": "on",
            "assumed_aircon_mode": 5,
        },
    )

    # When: the temperature exceeds max_temp + hysteresis
    service.run_once()

    # Then: a direct setAll fan command is sent as fallback
    assert client.run_scene_calls == []
    assert len(client.send_command_calls) == 1
    command = client.send_command_calls[0]
    assert command["command"] == "setAll"
    assert command["parameter"] == "21,4,3,on"
    state = state_store.read()
    assert state["assumed_aircon_mode"] == 4


def test_build_aircon_status_updates_normalizes_temperature() -> None:
    # Given: the API reports a float temperature for a heat setpoint
    body = {"power": "on", "mode": 5, "temperature": 24.0, "fanSpeed": 3}

    # When: the status body is mapped to state updates
    updates = _build_aircon_status_updates(body)

    # Then: the persisted parameter uses the integer form
    assert updates["assumed_aircon_parameter"] == "24,5,3,on"


def test_send_aircon_setall_reemits_legacy_float_parameter_once() -> None:
    # Given: the stored parameter uses the legacy float format and a string mode
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": "5",
        "assumed_aircon_parameter": "24.0,5,3,on",
    }
    service, client, _, state_store = _build_service(
        settings=_default_settings(),
        temperature=20.0,
        initial_state=initial_state,
    )

    # When: the automation requests the equivalent integer setpoint
    service._send_aircon_setall(
        "aircon-1",
        temperature=24.0,
        mode=5,
        fan_speed=3,
        power_state="on",
        trigger="test",
        reason="test",
    )

    # Then: the legacy parameter is not trusted and the canonical command is sent once
    assert client.send_command_calls[0]["parameter"] == "24,5,3,on"
    assert state_store.read()["assumed_aircon_parameter"] == "24,5,3,on"

    # When: the same setpoint is requested again
    service._send_aircon_setall(
        "aircon-1",
        temperature=24.0,
        mode=5,
        fan_speed=3,
        power_state="on",
        trigger="test",
        reason="test",
    )

    # Then: idempotency skips the duplicate now that the state is canonical
    assert len(client.send_command_calls) == 1


def test_send_aircon_setall_emits_integer_parameter_on_divergence() -> None:
    # Given: the unit is assumed to be at the physical fallback setpoint
    initial_state = {
        "assumed_aircon_power": "on",
        "assumed_aircon_mode": 5,
        "assumed_aircon_parameter": "18,5,3,on",
    }
    service, client, _, _ = _build_service(
        settings=_default_settings(),
        temperature=20.0,
        initial_state=initial_state,
    )

    # When: the automation targets 24°C
    service._send_aircon_setall(
        "aircon-1",
        temperature=24.0,
        mode=5,
        fan_speed=3,
        power_state="on",
        trigger="test",
        reason="test",
    )

    # Then: the emitted parameter is an integer string
    assert client.send_command_calls[0]["parameter"] == "24,5,3,on"


def test_resolve_temperature_profile_normalizes_target() -> None:
    # Given: the winter profile has a fractional target
    settings = _default_settings()
    settings["winter"]["target_temp"] = 24.6
    service, _, _, _ = _build_service(settings=settings, temperature=20.0)

    # When: the profile is resolved
    values, error = service._resolve_temperature_profile(settings, 20.0, "test")

    # Then: the runtime target is a rounded integer
    assert error is None
    assert values is not None
    assert values["target_temp"] == 25


