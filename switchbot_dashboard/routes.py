from __future__ import annotations

import datetime as dt
import json
from typing import Any

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    abort,
)

from .config_store import StoreError
from .switchbot_api import SwitchBotApiError


dashboard_bp = Blueprint("dashboard", __name__)


DAY_CHOICES: list[dict[str, Any]] = [
    {"value": 0, "label": "Mon"},
    {"value": 1, "label": "Tue"},
    {"value": 2, "label": "Wed"},
    {"value": 3, "label": "Thu"},
    {"value": 4, "label": "Fri"},
    {"value": 5, "label": "Sat"},
    {"value": 6, "label": "Sun"},
]


def _build_time_choices(step_minutes: int = 30) -> list[str]:
    """Generate 24h slot labels spaced by ``step_minutes`` for the time-window dropdowns rendered in index.html."""
    values: list[str] = []
    total_minutes = 24 * 60
    for minutes in range(0, total_minutes, step_minutes):
        hour = minutes // 60
        minute = minutes % 60
        values.append(f"{hour:02d}:{minute:02d}")
    return values


TIME_CHOICES = _build_time_choices()


def _build_temp_choices(start: float = 14.0, end: float = 32.0, step: float = 0.5) -> list[dict[str, Any]]:
    """Produce half-degree temperature options shared by the Winter/Summer dropdowns to keep the UI and validators aligned."""
    values: list[dict[str, Any]] = []
    scaled_start = int(start * 2)
    scaled_end = int(end * 2)
    scaled_step = max(1, int(step * 2))
    for scaled in range(scaled_start, scaled_end + 1, scaled_step):
        numeric_value = scaled / 2
        label = f"{numeric_value:.1f}".rstrip("0").rstrip(".")
        if label == "":
            label = "0"
        values.append({"value": numeric_value, "label": label})
    return values


TEMP_CHOICES = _build_temp_choices()

FAN_SPEED_CHOICES: list[dict[str, Any]] = [
    {"value": 1, "label": "Auto"},
    {"value": 2, "label": "Low"},
    {"value": 3, "label": "Medium"},
    {"value": 4, "label": "High"},
]

AC_MODE_CHOICES: list[dict[str, Any]] = [
    {"value": 1, "label": "Auto"},
    {"value": 2, "label": "Cool"},
    {"value": 3, "label": "Dry"},
    {"value": 4, "label": "Fan"},
    {"value": 5, "label": "Heat"},
]

AIRCON_SCENE_KEYS: tuple[str, ...] = ("winter", "summer", "fan", "off")
AIRCON_SCENE_LABELS: dict[str, str] = {
    "winter": "Aircon ON – Hiver",
    "summer": "Aircon ON – Été",
    "fan": "Aircon ON – Mode neutre",
    "off": "Aircon OFF – Scène",
}


def _utc_now_iso() -> str:
    return dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).isoformat()


def _as_bool(value: Any) -> bool:
    if value is None:
        return False

    if isinstance(value, bool):
        return value

    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _as_int(value: Any, default: int, minimum: int | None = None, maximum: int | None = None) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default

    if minimum is not None and parsed < minimum:
        return minimum

    if maximum is not None and parsed > maximum:
        return maximum

    return parsed


def _as_float(
    value: Any,
    default: float,
    minimum: float | None = None,
    maximum: float | None = None,
) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return default

    if minimum is not None and parsed < minimum:
        return minimum

    if maximum is not None and parsed > maximum:
        return maximum

    return parsed


def _get_time_window_form(settings: dict[str, Any]) -> dict[str, Any]:
    windows = settings.get("time_windows", [])
    window = windows[0] if windows else {}
    raw_days = window.get("days", [])
    days: list[int] = []
    if isinstance(raw_days, list):
        for token in raw_days:
            try:
                day = int(token)
            except (TypeError, ValueError):
                continue
            if 0 <= day <= 6:
                days.append(day)

    return {
        "days": days,
        "start": window.get("start", ""),
        "end": window.get("end", ""),
    }


def _extract_aircon_scenes(settings: dict[str, Any]) -> dict[str, str]:
    raw_scenes = settings.get("aircon_scenes", {})
    if not isinstance(raw_scenes, dict):
        raw_scenes = {}

    sanitized: dict[str, str] = {}
    for key in AIRCON_SCENE_KEYS:
        value = raw_scenes.get(key, "")
        sanitized[key] = str(value).strip() if isinstance(value, str) else ""
    return sanitized


@dashboard_bp.get("/")
def index() -> str:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]

    settings = settings_store.read()
    state = state_store.read()
    aircon_scenes = _extract_aircon_scenes(settings)
    missing_scenes = {key: not aircon_scenes[key] for key in AIRCON_SCENE_KEYS}

    time_window_form = _get_time_window_form(settings)
    api_requests_remaining = state.get("api_requests_remaining")
    api_requests_total = state.get("api_requests_total")

    return render_template(
        "index.html",
        settings=settings,
        state=state,
        aircon_scenes=aircon_scenes,
        missing_scenes=missing_scenes,
        aircon_scene_labels=AIRCON_SCENE_LABELS,
        time_window_form=time_window_form,
        day_choices=DAY_CHOICES,
        time_choices=TIME_CHOICES,
        temp_choices=TEMP_CHOICES,
        fan_speed_choices=FAN_SPEED_CHOICES,
        ac_mode_choices=AC_MODE_CHOICES,
        aircon_scene_keys=AIRCON_SCENE_KEYS,
        api_requests_remaining=api_requests_remaining,
        api_requests_total=api_requests_total,
    )


@dashboard_bp.get("/debug/state")
def debug_state() -> Any:
    expected_token = current_app.config.get("STATE_DEBUG_TOKEN")
    provided_token = request.args.get("token")

    if not expected_token or provided_token != expected_token:
        abort(404)

    state_store = current_app.extensions["state_store"]
    state = state_store.read()

    return current_app.response_class(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        mimetype="application/json",
    )


@dashboard_bp.get("/healthz")
def healthz() -> Any:
    app = current_app
    settings_store = app.extensions["settings_store"]
    state_store = app.extensions["state_store"]
    scheduler_service = app.extensions["scheduler_service"]

    timestamp = _utc_now_iso()

    try:
        settings = settings_store.read()
        state = state_store.read()
        scheduler_running = bool(scheduler_service.is_running())
        automation_enabled = bool(settings.get("automation_enabled", False))
        last_tick = state.get("last_tick")
    except StoreError as exc:
        app.logger.error("[health] store error: %s", exc)
        payload = {
            "status": "error",
            "details": "store_unavailable",
            "timestamp_utc": timestamp,
        }
        return app.response_class(
            json.dumps(payload) + "\n", mimetype="application/json", status=503
        )
    except Exception as exc:  # pragma: no cover - defensive fallback
        app.logger.exception("[health] unexpected failure")
        payload = {
            "status": "error",
            "details": "unexpected_failure",
            "timestamp_utc": timestamp,
        }
        return app.response_class(
            json.dumps(payload) + "\n", mimetype="application/json", status=503
        )

    payload = {
        "status": "ok",
        "scheduler_running": scheduler_running,
        "automation_enabled": automation_enabled,
        "last_tick": last_tick,
        "timestamp_utc": timestamp,
    }
    return app.response_class(
        json.dumps(payload) + "\n", mimetype="application/json", status=200
    )


@dashboard_bp.post("/settings")
def update_settings() -> Any:
    settings_store = current_app.extensions["settings_store"]
    scheduler_service = current_app.extensions["scheduler_service"]

    settings = settings_store.read()
    current_aircon_scenes = _extract_aircon_scenes(settings)

    settings["automation_enabled"] = _as_bool(request.form.get("automation_enabled"))
    settings["mode"] = str(request.form.get("mode", settings.get("mode", "winter"))).strip().lower()

    settings["poll_interval_seconds"] = _as_int(
        request.form.get("poll_interval_seconds"),
        default=int(settings.get("poll_interval_seconds", 120) or 120),
        minimum=15,
        maximum=3600,
    )

    settings["hysteresis_celsius"] = _as_float(
        request.form.get("hysteresis_celsius"),
        default=float(settings.get("hysteresis_celsius", 0.3) or 0.3),
        minimum=0.0,
        maximum=5.0,
    )

    settings["command_cooldown_seconds"] = _as_int(
        request.form.get("command_cooldown_seconds"),
        default=int(settings.get("command_cooldown_seconds", 180) or 180),
        minimum=0,
        maximum=3600,
    )

    settings["turn_off_outside_windows"] = _as_bool(request.form.get("turn_off_outside_windows"))

    settings["meter_device_id"] = str(request.form.get("meter_device_id", "")).strip()
    settings["aircon_device_id"] = str(request.form.get("aircon_device_id", "")).strip()

    time_window_days_raw = request.form.getlist("time_window_days")
    time_window_start = request.form.get("time_window_start", "").strip()
    time_window_end = request.form.get("time_window_end", "").strip()

    if time_window_days_raw or time_window_start or time_window_end:
        try:
            parsed_days = [
                int(token.strip())
                for token in time_window_days_raw
                if token.strip() != ""
            ]
        except ValueError:
            parsed_days = []

        parsed_days = sorted({day for day in parsed_days if 0 <= day <= 6})

        if parsed_days and time_window_start and time_window_end:
            settings["time_windows"] = [
                {
                    "days": parsed_days,
                    "start": time_window_start,
                    "end": time_window_end,
                }
            ]
        else:
            flash(
                "Invalid time window: days must be 0-6 and start/end required.",
                "error",
            )
    else:
        settings["time_windows"] = []

    for key in ("winter", "summer"):
        profile = settings.get(key, {})
        if not isinstance(profile, dict):
            profile = {}

        profile["min_temp"] = _as_float(request.form.get(f"{key}_min_temp"), default=float(profile.get("min_temp", 0.0) or 0.0))
        profile["max_temp"] = _as_float(request.form.get(f"{key}_max_temp"), default=float(profile.get("max_temp", 0.0) or 0.0))
        profile["target_temp"] = _as_float(request.form.get(f"{key}_target_temp"), default=float(profile.get("target_temp", 0.0) or 0.0))
        profile["fan_speed"] = _as_int(request.form.get(f"{key}_fan_speed"), default=int(profile.get("fan_speed", 3) or 3), minimum=1, maximum=4)
        profile["ac_mode"] = _as_int(request.form.get(f"{key}_ac_mode"), default=int(profile.get("ac_mode", 5 if key == "winter" else 2) or 0), minimum=0, maximum=5)

        settings[key] = profile

    updated_aircon_scenes: dict[str, str] = {}
    for key in AIRCON_SCENE_KEYS:
        updated_aircon_scenes[key] = str(
            request.form.get(f"scene_{key}_id", current_aircon_scenes.get(key, ""))
        ).strip()

    settings["aircon_scenes"] = updated_aircon_scenes

    settings_store.write(settings)
    scheduler_service.reschedule()

    flash("Settings saved.")
    return redirect(url_for("dashboard.index"))


@dashboard_bp.post("/actions/run_once")
def run_once() -> Any:
    automation_service = current_app.extensions["automation_service"]

    automation_service.run_once()
    flash("Automation tick executed.")
    return redirect(url_for("dashboard.index"))


@dashboard_bp.post("/actions/aircon_off")
def aircon_off() -> Any:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]
    client = current_app.extensions["switchbot_client"]

    settings = settings_store.read()
    scenes = _extract_aircon_scenes(settings)
    off_scene_id = scenes.get("off", "")
    if off_scene_id:
        return _execute_aircon_scene(
            "off",
            state_reason="manual_off_scene",
            flash_label="Scène OFF exécutée.",
            assumed_power="off",
        )

    aircon_id = str(settings.get("aircon_device_id", "")).strip()
    if not aircon_id:
        flash("Missing aircon_device_id", "error")
        return redirect(url_for("dashboard.index"))
    try:
        client.send_command(aircon_id, command="turnOff", parameter="default", command_type="command")
    except SwitchBotApiError as exc:
        state = state_store.read()
        state["last_error"] = str(exc)
        state_store.write(state)
        flash(str(exc), "error")
        return redirect(url_for("dashboard.index"))

    state = state_store.read()
    state["assumed_aircon_power"] = "off"
    state["assumed_aircon_mode"] = None
    state["assumed_aircon_parameter"] = None
    state["last_action"] = "turnOff (manual)"
    state["last_action_at"] = _utc_now_iso()
    state["last_error"] = None
    state_store.write(state)

    flash("Aircon turnOff sent.")
    return redirect(url_for("dashboard.index"))


def _execute_aircon_scene(
    scene_key: str,
    *,
    state_reason: str,
    flash_label: str,
    assumed_power: str = "unknown",
) -> Any:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]
    client = current_app.extensions["switchbot_client"]

    settings = settings_store.read()
    scenes = _extract_aircon_scenes(settings)
    scene_id = scenes.get(scene_key, "")

    if not scene_id:
        scene_label = AIRCON_SCENE_LABELS.get(scene_key, scene_key)
        flash(f"Missing scene id for {scene_label}", "error")
        return redirect(url_for("dashboard.index"))

    try:
        client.run_scene(scene_id)
    except SwitchBotApiError as exc:
        state = state_store.read()
        state["last_error"] = str(exc)
        state_store.write(state)
        flash(str(exc), "error")
        return redirect(url_for("dashboard.index"))

    state = state_store.read()
    state["assumed_aircon_power"] = assumed_power
    state["assumed_aircon_mode"] = None
    state["assumed_aircon_parameter"] = None
    state["last_action"] = f"scene({scene_id}) ({state_reason})"
    state["last_action_at"] = _utc_now_iso()
    state["last_error"] = None
    state_store.write(state)

    flash(flash_label)
    return redirect(url_for("dashboard.index"))


@dashboard_bp.post("/actions/aircon_on")
def aircon_on() -> Any:
    """Route to the current mode scene for backward compatibility."""
    settings_store = current_app.extensions["settings_store"]
    settings = settings_store.read()
    mode = str(settings.get("mode", "winter")).strip().lower()
    scene_key = mode if mode in AIRCON_SCENE_KEYS else "winter"
    return _execute_aircon_scene(
        scene_key,
        state_reason=f"manual_{scene_key}_scene",
        flash_label=f"Scène {scene_key} exécutée.",
    )


@dashboard_bp.post("/actions/aircon_on_winter")
def aircon_on_winter() -> Any:
    return _execute_aircon_scene(
        "winter",
        state_reason="manual_winter_scene",
        flash_label="Scène hiver exécutée.",
    )


@dashboard_bp.post("/actions/aircon_on_summer")
def aircon_on_summer() -> Any:
    return _execute_aircon_scene(
        "summer",
        state_reason="manual_summer_scene",
        flash_label="Scène été exécutée.",
    )


@dashboard_bp.post("/actions/aircon_on_fan")
def aircon_on_fan() -> Any:
    return _execute_aircon_scene(
        "fan",
        state_reason="manual_fan_scene",
        flash_label="Scène ventilateur exécutée.",
    )


@dashboard_bp.get("/devices")
def devices() -> str:
    client = current_app.extensions["switchbot_client"]

    data = None
    error = None

    try:
        data = client.get_devices()
    except SwitchBotApiError as exc:
        error = str(exc)

    return render_template("devices.html", data=data, error=error)


@dashboard_bp.post("/actions/quick_winter")
def quick_winter() -> Any:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]
    client = current_app.extensions["switchbot_client"]

    settings = settings_store.read()
    settings["mode"] = "winter"
    settings["automation_enabled"] = True
    settings_store.write(settings)

    aircon_id = str(settings.get("aircon_device_id", "")).strip()
    if not aircon_id:
        flash("Missing aircon_device_id", "error")
        return redirect(url_for("dashboard.index"))

    winter = settings.get("winter", {})
    if not isinstance(winter, dict):
        winter = {}

    target_temp = float(winter.get("target_temp", 26.0) or 26.0)
    ac_mode = int(winter.get("ac_mode", 5) or 5)
    fan_speed = int(winter.get("fan_speed", 3) or 3)
    parameter = f"{target_temp},{ac_mode},{fan_speed},on"

    try:
        client.send_command(aircon_id, command="setAll", parameter=parameter, command_type="command")
    except SwitchBotApiError as exc:
        state = state_store.read()
        state["last_error"] = str(exc)
        state_store.write(state)
        flash(str(exc), "error")
        return redirect(url_for("dashboard.index"))

    state = state_store.read()
    state["assumed_aircon_power"] = "on"
    state["assumed_aircon_mode"] = ac_mode
    state["assumed_aircon_parameter"] = parameter
    state["last_action"] = f"setAll({parameter}) (quick_winter)"
    state["last_action_at"] = _utc_now_iso()
    state_store.write(state)

    flash("Winter mode enabled and heat command sent.")
    return redirect(url_for("dashboard.index"))


@dashboard_bp.post("/actions/quick_summer")
def quick_summer() -> Any:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]
    client = current_app.extensions["switchbot_client"]

    settings = settings_store.read()
    settings["mode"] = "summer"
    settings["automation_enabled"] = True
    settings_store.write(settings)

    aircon_id = str(settings.get("aircon_device_id", "")).strip()
    if not aircon_id:
        flash("Missing aircon_device_id", "error")
        return redirect(url_for("dashboard.index"))

    summer = settings.get("summer", {})
    if not isinstance(summer, dict):
        summer = {}

    target_temp = float(summer.get("target_temp", 24.0) or 24.0)
    ac_mode = int(summer.get("ac_mode", 2) or 2)
    fan_speed = int(summer.get("fan_speed", 3) or 3)
    parameter = f"{target_temp},{ac_mode},{fan_speed},on"

    try:
        client.send_command(aircon_id, command="setAll", parameter=parameter, command_type="command")
    except SwitchBotApiError as exc:
        state = state_store.read()
        state["last_error"] = str(exc)
        state_store.write(state)
        flash(str(exc), "error")
        return redirect(url_for("dashboard.index"))

    state = state_store.read()
    state["assumed_aircon_power"] = "on"
    state["assumed_aircon_mode"] = ac_mode
    state["assumed_aircon_parameter"] = parameter
    state["last_action"] = f"setAll({parameter}) (quick_summer)"
    state["last_action_at"] = _utc_now_iso()
    state_store.write(state)

    flash("Summer mode enabled and cool command sent.")
    return redirect(url_for("dashboard.index"))


@dashboard_bp.post("/actions/quick_off")
def quick_off() -> Any:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]
    client = current_app.extensions["switchbot_client"]

    settings = settings_store.read()
    settings["automation_enabled"] = False
    settings_store.write(settings)

    scenes = _extract_aircon_scenes(settings)
    off_scene_id = scenes.get("off", "")

    if off_scene_id:
        try:
            client.run_scene(off_scene_id)
        except SwitchBotApiError as exc:
            state = state_store.read()
            state["last_error"] = str(exc)
            state_store.write(state)
            flash(str(exc), "error")
            return redirect(url_for("dashboard.index"))
        state = state_store.read()
        state["assumed_aircon_power"] = "off"
        state["assumed_aircon_mode"] = None
        state["assumed_aircon_parameter"] = None
        state["last_action"] = f"scene({off_scene_id}) (quick_off)"
        state["last_action_at"] = _utc_now_iso()
        state["last_error"] = None
        state_store.write(state)
        flash("Automation disabled and OFF scene executed.")
        return redirect(url_for("dashboard.index"))

    aircon_id = str(settings.get("aircon_device_id", "")).strip()
    if not aircon_id:
        flash("Missing aircon_device_id", "error")
        return redirect(url_for("dashboard.index"))

    try:
        client.send_command(aircon_id, command="turnOff", parameter="default", command_type="command")
    except SwitchBotApiError as exc:
        state = state_store.read()
        state["last_error"] = str(exc)
        state_store.write(state)
        flash(str(exc), "error")
        return redirect(url_for("dashboard.index"))

    state = state_store.read()
    state["assumed_aircon_power"] = "off"
    state["assumed_aircon_mode"] = None
    state["assumed_aircon_parameter"] = None
    state["last_action"] = "turnOff (quick_off)"
    state["last_action_at"] = _utc_now_iso()
    state["last_error"] = None
    state_store.write(state)

    flash("Automation disabled and aircon turned off.")
    return redirect(url_for("dashboard.index"))
