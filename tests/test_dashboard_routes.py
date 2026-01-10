from __future__ import annotations

import copy

from flask import Flask

from switchbot_dashboard.routes import DEFAULT_AIRCON_PRESETS, dashboard_bp


class MemoryStore:
    def __init__(self, initial: dict[str, object]) -> None:
        self._data = copy.deepcopy(initial)

    def read(self) -> dict[str, object]:
        return copy.deepcopy(self._data)

    def write(self, new_data: dict[str, object]) -> None:
        self._data = copy.deepcopy(new_data)


class DummyScheduler:
    def __init__(self) -> None:
        self.called = False

    def reschedule(self) -> None:
        self.called = True


def _build_app(initial_settings: dict[str, object]) -> tuple[Flask, MemoryStore, DummyScheduler]:
    app = Flask(__name__)
    app.secret_key = "test"

    settings_store = MemoryStore(initial_settings)
    state_store = MemoryStore({})
    scheduler = DummyScheduler()

    app.extensions["settings_store"] = settings_store
    app.extensions["state_store"] = state_store
    app.extensions["switchbot_client"] = object()
    app.extensions["automation_service"] = object()
    app.extensions["scheduler_service"] = scheduler

    app.register_blueprint(dashboard_bp)
    return app, settings_store, scheduler


def test_update_settings_persists_manual_presets() -> None:
    initial_settings = {
        "automation_enabled": False,
        "mode": "winter",
        "poll_interval_seconds": 120,
        "hysteresis_celsius": 0.3,
        "command_cooldown_seconds": 180,
        "turn_off_outside_windows": False,
        "meter_device_id": "meter",
        "aircon_device_id": "aircon",
        "winter": {"min_temp": 18.0, "max_temp": 24.0, "target_temp": 20.0, "fan_speed": 3, "ac_mode": 5},
        "summer": {"min_temp": 20.0, "max_temp": 28.0, "target_temp": 24.0, "fan_speed": 2, "ac_mode": 2},
        "aircon_presets": copy.deepcopy(DEFAULT_AIRCON_PRESETS),
    }
    app, settings_store, scheduler = _build_app(initial_settings)

    form = {
        "automation_enabled": "on",
        "mode": "summer",
        "poll_interval_seconds": "300",
        "hysteresis_celsius": "0.4",
        "command_cooldown_seconds": "200",
        "turn_off_outside_windows": "on",
        "meter_device_id": "meter",
        "aircon_device_id": "aircon",
        "winter_min_temp": "18",
        "winter_max_temp": "24",
        "winter_target_temp": "21",
        "winter_ac_mode": "5",
        "winter_fan_speed": "3",
        "summer_min_temp": "20",
        "summer_max_temp": "28",
        "summer_target_temp": "23",
        "summer_ac_mode": "2",
        "summer_fan_speed": "3",
        "manual_winter_target_temp": "26",
        "manual_winter_ac_mode": "5",
        "manual_winter_fan_speed": "4",
        "manual_summer_target_temp": "19",
        "manual_summer_ac_mode": "2",
        "manual_summer_fan_speed": "2",
    }

    with app.test_client() as client:
        response = client.post("/settings", data=form, follow_redirects=False)

    assert response.status_code == 302
    persisted = settings_store.read()
    assert persisted["aircon_presets"] == {
        "winter": {"target_temp": 26.0, "ac_mode": 5, "fan_speed": 4},
        "summer": {"target_temp": 19.0, "ac_mode": 2, "fan_speed": 2},
    }
    assert scheduler.called is True
