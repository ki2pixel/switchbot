from __future__ import annotations

import copy
import datetime as dt
from pathlib import Path

from flask import Flask

from bs4 import BeautifulSoup

from switchbot_dashboard.config_store import StoreError
from switchbot_dashboard.quota import ApiQuotaTracker
from switchbot_dashboard.routes import dashboard_bp


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
        self.running = True

    def reschedule(self) -> None:
        self.called = True

    def is_running(self) -> bool:
        return self.running


class DummyClient:
    def __init__(self) -> None:
        self.scene_calls: list[str] = []
        self.command_calls: list[dict[str, object]] = []
        self._quota_tracker: ApiQuotaTracker | None = None

    def attach_quota_tracker(self, tracker: ApiQuotaTracker) -> None:
        self._quota_tracker = tracker

    def _record_quota(self) -> None:
        if self._quota_tracker:
            self._quota_tracker.record_call()

    def run_scene(self, scene_id: str) -> None:
        self._record_quota()
        self.scene_calls.append(scene_id)

    def send_command(
        self,
        device_id: str,
        *,
        command: str,
        parameter: str = "default",
        command_type: str = "command",
    ) -> None:
        self._record_quota()
        self.command_calls.append(
            {
                "device_id": device_id,
                "command": command,
                "parameter": parameter,
                "command_type": command_type,
            }
        )


class DummyIFTTTClient:
    def __init__(self) -> None:
        self.webhook_calls: list[str] = []

    def trigger_webhook(self, webhook_url: str, *, event_data: dict | None = None) -> None:
        self.webhook_calls.append(webhook_url)


def _today_iso() -> str:
    return dt.datetime.utcnow().date().isoformat()


def _build_app(
    initial_settings: dict[str, object],
    *,
    initial_state: dict[str, object] | None = None,
    client: object | None = None,
) -> tuple[Flask, MemoryStore, MemoryStore, DummyScheduler, ApiQuotaTracker | None]:
    project_root = Path(__file__).resolve().parents[1]
    template_folder = project_root / "switchbot_dashboard" / "templates"
    app = Flask(__name__, template_folder=str(template_folder))
    app.secret_key = "test"

    settings_store = MemoryStore(initial_settings)
    state_store = MemoryStore(initial_state or {})
    scheduler = DummyScheduler()

    quota_tracker = ApiQuotaTracker(state_store)
    app.extensions["settings_store"] = settings_store
    app.extensions["state_store"] = state_store
    if isinstance(client, DummyClient):
        client.attach_quota_tracker(quota_tracker)
    app.extensions["switchbot_client"] = client or object()
    app.extensions["ifttt_client"] = DummyIFTTTClient()
    app.extensions["automation_service"] = object()
    app.extensions["scheduler_service"] = scheduler
    app.extensions["quota_tracker"] = quota_tracker

    app.register_blueprint(dashboard_bp)
    return app, settings_store, state_store, scheduler, quota_tracker


def _assert_quota_usage(
    state_store: MemoryStore,
    *,
    expected_used: int,
    limit: int = 10_000,
) -> dict[str, object]:
    state = state_store.read()
    assert state["api_requests_total"] == expected_used
    assert state["api_requests_remaining"] == max(limit - expected_used, 0)
    assert state.get("api_requests_limit", limit) == limit
    assert state["api_quota_day"] == _today_iso()
    return state


class FailingStore:
    def read(self) -> dict[str, object]:
        raise StoreError("boom")

    def write(self, _data: dict[str, object]) -> None:
        raise StoreError("boom")


def test_update_settings_persists_manual_presets_and_scenes() -> None:
    initial_settings = {
        "automation_enabled": False,
        "mode": "winter",
        "poll_interval_seconds": 120,
        "hysteresis_celsius": 0.3,
        "command_cooldown_seconds": 180,
        "action_on_cooldown_seconds": 0,
        "action_off_cooldown_seconds": 0,
        "turn_off_outside_windows": False,
        "meter_device_id": "meter",
        "aircon_device_id": "aircon",
        "winter": {"min_temp": 18.0, "max_temp": 24.0, "target_temp": 20.0, "fan_speed": 3, "ac_mode": 5},
        "summer": {"min_temp": 20.0, "max_temp": 28.0, "target_temp": 24.0, "fan_speed": 2, "ac_mode": 2},
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    app, settings_store, _state_store, scheduler, _tracker = _build_app(initial_settings)

    form = {
        "automation_enabled": "on",
        "mode": "summer",
        "poll_interval_seconds": "300",
        "hysteresis_celsius": "0.4",
        "command_cooldown_seconds": "200",
        "action_on_cooldown_seconds": "300",
        "action_off_cooldown_seconds": "90",
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
        "scene_winter_id": "scene-w",
        "scene_summer_id": "scene-s",
        "scene_fan_id": "scene-f",
        "scene_off_id": "scene-off",
        "timezone": "Europe/Paris",
        "api_quota_warning_threshold": "250",
    }

    with app.test_client() as client:
        response = client.post("/settings", data=form, follow_redirects=False)

    assert response.status_code == 302
    persisted = settings_store.read()
    assert persisted["aircon_scenes"] == {
        "winter": "scene-w",
        "summer": "scene-s",
        "fan": "scene-f",
        "off": "scene-off",
    }
    assert persisted["timezone"] == "Europe/Paris"
    assert persisted["api_quota_warning_threshold"] == 250
    assert persisted["command_cooldown_seconds"] == 200
    assert persisted["action_on_cooldown_seconds"] == 300
    assert persisted["action_off_cooldown_seconds"] == 90
    assert scheduler.called is True


def test_update_settings_rejects_invalid_timezone_and_keeps_previous() -> None:
    initial_settings = {
        "automation_enabled": False,
        "mode": "winter",
        "poll_interval_seconds": 120,
        "hysteresis_celsius": 0.3,
        "command_cooldown_seconds": 180,
        "action_on_cooldown_seconds": 0,
        "action_off_cooldown_seconds": 0,
        "turn_off_outside_windows": False,
        "timezone": "Europe/Paris",
        "meter_device_id": "meter",
        "aircon_device_id": "aircon",
        "winter": {"min_temp": 18.0, "max_temp": 24.0, "target_temp": 20.0, "fan_speed": 3, "ac_mode": 5},
        "summer": {"min_temp": 20.0, "max_temp": 28.0, "target_temp": 24.0, "fan_speed": 2, "ac_mode": 2},
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    app, settings_store, _state_store, _scheduler, _tracker = _build_app(initial_settings)

    form = {
        "automation_enabled": "on",
        "mode": "winter",
        "poll_interval_seconds": "300",
        "hysteresis_celsius": "0.4",
        "command_cooldown_seconds": "200",
        "action_on_cooldown_seconds": "0",
        "action_off_cooldown_seconds": "0",
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
        "scene_winter_id": "",
        "scene_summer_id": "",
        "scene_fan_id": "",
        "scene_off_id": "",
        "timezone": "Definitely/NotAZone",
        "api_quota_warning_threshold": "250",
    }

    with app.test_client() as client:
        response = client.post("/settings", data=form, follow_redirects=True)

    assert response.status_code == 200
    persisted = settings_store.read()
    assert persisted["timezone"] == "Europe/Paris"

    soup = BeautifulSoup(response.data, "html.parser")
    error = soup.select_one(".alert-danger")
    assert error is not None
    assert "Fuseau horaire invalide" in error.get_text()


def test_aircon_on_winter_runs_scene_and_updates_state() -> None:
    settings = {
        "mode": "winter",
        "aircon_device_id": "aircon",
        "aircon_scenes": {"winter": "scene-w", "summer": "", "fan": "", "off": ""},
    }
    dummy_client = DummyClient()
    app, settings_store, state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state={"assumed_aircon_power": "off"},
        client=dummy_client,
    )

    with app.test_client() as client:
        response = client.post("/actions/aircon_on_winter", follow_redirects=False)

    assert response.status_code == 302
    assert dummy_client.scene_calls == ["scene-w"]
    state = _assert_quota_usage(state_store, expected_used=1)
    assert state["assumed_aircon_power"] == "on"
    assert state["last_action"].startswith("scene(scene-w)")


def test_aircon_on_winter_reports_missing_scene_id() -> None:
    settings = {
        "mode": "winter",
        "aircon_device_id": "aircon",
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    dummy_client = DummyClient()
    app, _settings_store, state_store, _scheduler, _tracker = _build_app(
        settings,
        client=dummy_client,
    )

    with app.test_client() as client:
        response = client.post("/actions/aircon_on_winter", follow_redirects=True)

    assert response.status_code == 200
    assert dummy_client.scene_calls == []
    state = state_store.read()
    assert state.get("last_action") is None


def test_aircon_off_runs_off_scene_when_configured() -> None:
    settings = {
        "mode": "winter",
        "aircon_device_id": "aircon",
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": "scene-off"},
    }
    dummy_client = DummyClient()
    app, _settings_store, state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state={"assumed_aircon_power": "on"},
        client=dummy_client,
    )

    with app.test_client() as client:
        response = client.post("/actions/aircon_off", follow_redirects=False)

    assert response.status_code == 302
    assert dummy_client.scene_calls == ["scene-off"]
    state = _assert_quota_usage(state_store, expected_used=1)
    assert state["assumed_aircon_power"] == "off"
    assert state["last_action"].startswith("scene(scene-off)")


def test_healthz_returns_scheduler_state_and_tick() -> None:
    settings = {"automation_enabled": True}
    last_tick = "2026-01-10T15:30:00+00:00"
    state = {"last_tick": last_tick}
    app, _settings_store, _state_store, scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )
    scheduler.running = True

    with app.test_client() as client:
        response = client.get("/healthz")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert payload["scheduler_running"] is True
    assert payload["automation_enabled"] is True
    assert payload["last_tick"] == last_tick
    assert "timestamp_utc" in payload


def test_healthz_returns_503_when_store_unavailable() -> None:
    settings = {"automation_enabled": False}
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(settings)
    failing = FailingStore()
    app.extensions["settings_store"] = failing
    app.extensions["state_store"] = failing

    with app.test_client() as client:
        response = client.get("/healthz")

    assert response.status_code == 503
    payload = response.get_json()
    assert payload["status"] == "error"
    assert payload["details"] == "store_unavailable"


def test_quick_off_prefers_scene_and_disables_automation() -> None:
    settings = {
        "automation_enabled": True,
        "mode": "winter",
        "aircon_device_id": "aircon",
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": "scene-off"},
    }
    dummy_client = DummyClient()
    app, settings_store, state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state={"assumed_aircon_power": "on"},
        client=dummy_client,
    )

    with app.test_client() as client:
        response = client.post("/actions/quick_off", follow_redirects=False)

    assert response.status_code == 302
    assert dummy_client.scene_calls == ["scene-off"]
    persisted_settings = settings_store.read()
    assert persisted_settings["automation_enabled"] is False
    state = _assert_quota_usage(state_store, expected_used=1)
    assert state["assumed_aircon_power"] == "off"
    assert state["last_action"].startswith("scene(scene-off)")


def test_quick_off_multiple_calls_accumulate_quota_usage() -> None:
    settings = {
        "automation_enabled": True,
        "mode": "winter",
        "aircon_device_id": "aircon",
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": "scene-off"},
    }
    dummy_client = DummyClient()
    app, settings_store, state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state={"assumed_aircon_power": "on"},
        client=dummy_client,
    )

    with app.test_client() as client:
        client.post("/actions/quick_off", follow_redirects=False)
        client.post("/actions/quick_off", follow_redirects=False)

    state = _assert_quota_usage(state_store, expected_used=2)
    assert state["assumed_aircon_power"] == "off"
    assert state["last_action"].endswith("(quick_off)")
    persisted_settings = settings_store.read()
    assert persisted_settings["automation_enabled"] is False


def test_index_shows_quota_banner_when_threshold_hit() -> None:
    settings = {
        "api_quota_warning_threshold": 100,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {
        "api_requests_remaining": 50,
        "api_quota_day": _today_iso(),
    }
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, "html.parser")
    banner = soup.select_one(".quota-banner")
    assert banner is not None
    assert "50" in banner.get_text()


def test_index_shows_quota_banner_when_remaining_equals_threshold() -> None:
    settings = {
        "api_quota_warning_threshold": 100,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {
        "api_requests_remaining": 100,
        "api_quota_day": _today_iso(),
    }
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, "html.parser")
    banner = soup.select_one(".quota-banner")
    assert banner is not None


def test_index_hides_quota_banner_when_threshold_disabled() -> None:
    settings = {
        "api_quota_warning_threshold": 0,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {
        "api_requests_remaining": 0,
        "api_quota_day": _today_iso(),
    }
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, "html.parser")
    banner = soup.select_one(".quota-banner")
    assert banner is None


def test_index_renders_quota_threshold_field_without_alert() -> None:
    settings = {
        "automation_enabled": False,
        "mode": "winter",
        "api_quota_warning_threshold": 350,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {
        "api_requests_total": 100,
        "api_requests_remaining": 9_900,
        "api_requests_limit": 10_000,
        "api_quota_day": _today_iso(),
    }
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, "html.parser")
    alert = soup.select_one(".quota-alert")
    assert alert is None
    # Le seuil est désormais éditable depuis /reglages uniquement.
    threshold_field = soup.select_one("#api_quota_warning_threshold")
    assert threshold_field is None


def test_quota_page_displays_alert_when_threshold_hit() -> None:
    settings = {
        "api_quota_warning_threshold": 100,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {
        "api_requests_total": 9_950,
        "api_requests_remaining": 50,
        "api_requests_limit": 10_000,
        "api_quota_day": _today_iso(),
        "api_quota_reset_at": "2026-01-11T00:00:00+00:00",
    }
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.get("/quota")

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, "html.parser")
    title = soup.select_one("h1")
    assert title is not None
    assert "Quota API quotidien" in title.get_text()
    remaining_value = soup.select_one(".metric-value")
    assert remaining_value is not None
    assert "50" in remaining_value.get_text()


def test_settings_page_renders_form_fields() -> None:
    settings = {
        "automation_enabled": True,
        "mode": "winter",
        "poll_interval_seconds": 180,
        "command_cooldown_seconds": 120,
        "hysteresis_celsius": 0.4,
        "api_quota_warning_threshold": 200,
        "turn_off_outside_windows": True,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {"api_requests_remaining": 5000}
    app, _settings_store, _state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.get("/reglages")

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, "html.parser")
    title = soup.select_one("h1")
    assert title is not None
    assert "Réglages" in title.get_text()
    form = soup.select_one("form.settings-form")
    assert form is not None
    assert form.get("method") == "post"
    threshold_input = form.select_one("#api_quota_warning_threshold")
    assert threshold_input is not None
    assert threshold_input.get("value") == "200"


def test_quota_refresh_normalizes_state_and_shows_flash() -> None:
    settings = {
        "api_quota_warning_threshold": 100,
        "aircon_scenes": {"winter": "", "summer": "", "fan": "", "off": ""},
    }
    state = {
        "api_quota_day": "2000-01-01",
        "api_requests_total": 9000,
        "api_requests_remaining": 1000,
        "api_requests_limit": 10_000,
    }
    app, _settings_store, state_store, _scheduler, _tracker = _build_app(
        settings,
        initial_state=state,
    )

    with app.test_client() as client:
        response = client.post("/quota/refresh", follow_redirects=True)

    assert response.status_code == 200
    refreshed_state = state_store.read()
    assert refreshed_state["api_quota_day"] == _today_iso()
    assert refreshed_state["api_requests_total"] == 1
    assert refreshed_state["api_requests_limit"] == 10_000
    assert refreshed_state["api_requests_remaining"] == 9_999
    soup = BeautifulSoup(response.data, "html.parser")
    success = soup.select_one(".alert-success")
    assert success is not None
    assert "Quota mis à jour" in success.get_text()
