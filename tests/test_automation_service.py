from __future__ import annotations

import copy
import logging
from typing import Any

import datetime as dt
from unittest.mock import MagicMock, patch
from zoneinfo import ZoneInfo

from switchbot_dashboard.automation import AutomationService, _is_now_in_windows
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

    # 1. State store initially assumes the AC is already set to COOL (mode=2, temp=22.5, speed=4, power=on).
    # If the service didn't poll, it would skip sending commands due to idempotency.
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
    assert call["parameter"] == "22.5,2,4,on"

    # Finally, the state store must be updated to the new targeted state
    final_state = state_store.read()
    assert final_state["assumed_aircon_power"] == "on"
    assert final_state["assumed_aircon_mode"] == 2
    assert final_state["assumed_aircon_parameter"] == "22.5,2,4,on"


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
            "temperature": 24.0,
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


