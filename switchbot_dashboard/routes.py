from __future__ import annotations

import datetime as dt
import hmac
import json
import os
import random
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    abort,
    session,
)

from .config_store import StoreError, JsonStore
from .postgres_store import PostgresStore
from .switchbot_api import SwitchBotApiError
from .extensions import limiter
from .aircon import AIRCON_SCENE_KEYS, AIRCON_SCENE_LABELS, extract_aircon_scenes as _extract_aircon_scenes
from .utils import (
    DEFAULT_TIMEZONE,
    _safe_int as _as_int,
    _safe_float as _as_float,
    _safe_bool as _as_bool,
    _utc_now_iso,
    _resolve_timezone,
    _parse_iso_datetime,
)

import contextlib

@contextlib.contextmanager
def _transaction_context(store: Any) -> Any:
    if hasattr(store, "transaction"):
        with store.transaction():
            yield
    else:
        yield


dashboard_bp = Blueprint("dashboard", __name__)
ROUTE_INDEX = "dashboard.index"

# Global StoreError handler (Q-04)
@dashboard_bp.app_errorhandler(StoreError)
def handle_store_error(error: StoreError) -> Any:
    current_app.logger.error(f"[store] Handled StoreError globally on blueprint: {error}")
    if request.path.startswith("/history/api/") or request.headers.get("Accept") == "application/json":
        return current_app.response_class(
            response=json.dumps({
                "error": "Service Indisponible",
                "message": "Le stockage de données est temporairement indisponible."
            }),
            status=503,
            mimetype="application/json"
        )
    return render_template("503.html"), 503


@dashboard_bp.before_request
def check_auth() -> Any:
    if request.endpoint in (
        "dashboard.login",
        "dashboard.logout",
        "dashboard.healthz",
        "dashboard.debug_state",
    ):
        return None

    if request.endpoint == "static" or (request.path and request.path.startswith("/static/")):
        return None

    password = current_app.config.get("DASHBOARD_PASSWORD")
    if not password:
        return None

    if not session.get("logged_in"):
        if request.path.startswith("/history/api/"):
            return current_app.response_class(
                response=json.dumps({"error": "Unauthorized"}),
                status=401,
                mimetype="application/json"
            )
        return redirect(url_for("dashboard.login"))


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

DEFAULT_QUOTA_WARNING_THRESHOLD = 250





def _localize_iso_timestamp(value: Any, timezone: dt.tzinfo) -> str | None:
    if not isinstance(value, str):
        return None
    parsed = _parse_iso_datetime(value)
    if parsed is None:
        return None
    return parsed.astimezone(timezone).isoformat()





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







def _build_quota_context(settings: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    api_requests_remaining = state.get("api_requests_remaining")
    api_requests_total = state.get("api_requests_total")
    api_requests_limit = state.get("api_requests_limit")
    api_quota_reset_at = state.get("api_quota_reset_at")

    raw_threshold = settings.get("api_quota_warning_threshold", DEFAULT_QUOTA_WARNING_THRESHOLD)
    try:
        quota_warning_threshold = int(raw_threshold)
    except (TypeError, ValueError):
        quota_warning_threshold = DEFAULT_QUOTA_WARNING_THRESHOLD
    if quota_warning_threshold < 0:
        quota_warning_threshold = 0

    show_quota_warning = (
        quota_warning_threshold > 0
        and isinstance(api_requests_remaining, (int, float))
        and api_requests_remaining is not None
        and api_requests_remaining <= quota_warning_threshold
    )

    return {
        "api_requests_remaining": api_requests_remaining,
        "api_requests_total": api_requests_total,
        "api_requests_limit": api_requests_limit,
        "api_quota_day": state.get("api_quota_day"),
        "api_quota_reset_at": api_quota_reset_at,
        "quota_warning_threshold": quota_warning_threshold,
        "show_quota_warning": show_quota_warning,
    }


def _build_scenes_context(settings: dict[str, Any]) -> tuple[dict[str, str], dict[str, bool]]:
    aircon_scenes = _extract_aircon_scenes(settings)
    missing_scenes = {key: not aircon_scenes[key] for key in AIRCON_SCENE_KEYS}
    return aircon_scenes, missing_scenes


@dashboard_bp.get("/")
def index() -> str:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]

    settings = settings_store.read()
    state = state_store.read()
    timezone = _resolve_timezone(settings)
    state_for_view = dict(state)
    localized_last_read_at = _localize_iso_timestamp(state.get("last_read_at"), timezone)
    if localized_last_read_at is not None:
        state_for_view["last_read_at"] = localized_last_read_at
    quota_context = _build_quota_context(settings, state)
    aircon_scenes, missing_scenes = _build_scenes_context(settings)

    return render_template(
        "index.html",
        state=state_for_view,
        settings=settings,
        **quota_context,
        aircon_scenes=aircon_scenes,
        missing_scenes=missing_scenes,
        aircon_scene_labels=AIRCON_SCENE_LABELS,
        aircon_scene_keys=AIRCON_SCENE_KEYS,
    )


@dashboard_bp.get("/reglages")
def settings_page() -> str:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]

    settings = settings_store.read()
    state = state_store.read()
    time_window_form = _get_time_window_form(settings)
    quota_context = _build_quota_context(settings, state)
    aircon_scenes, missing_scenes = _build_scenes_context(settings)

    configured_scenes_count = sum(1 for value in aircon_scenes.values() if value)

    return render_template(
        "settings.html",
        settings=settings,
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
        quota_warning_threshold=quota_context["quota_warning_threshold"],
        configured_scenes_count=configured_scenes_count,
    )


@dashboard_bp.get("/quota")
def quota() -> str:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]

    settings = settings_store.read()
    state = state_store.read()
    quota_context = _build_quota_context(settings, state)

    return render_template("quota.html", **quota_context)


@dashboard_bp.post("/quota/refresh")
@limiter.limit("5 per minute")
def quota_refresh() -> Any:
    quota_tracker = current_app.extensions.get("quota_tracker")
    client = current_app.extensions.get("switchbot_client")
    if quota_tracker is None or client is None:
        flash("Suivi de quota ou client API indisponible.", "error")
        return redirect(url_for("dashboard.quota"))

    if client and hasattr(client, "get_devices"):
        try:
            client.get_devices()
            flash("Compteurs de quota mis à jour depuis l'API SwitchBot.", "success")
        except SwitchBotApiError as exc:
            flash(f"Erreur lors de l'appel API SwitchBot : {exc}", "error")
    else:
        quota_tracker.record_call()
        flash("Quota mis à jour.", "success")

    quota_tracker.refresh_snapshot()
    return redirect(url_for("dashboard.quota"))


@dashboard_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login() -> Any:
    if not current_app.config.get("DASHBOARD_PASSWORD"):
        return redirect(url_for(ROUTE_INDEX))

    if session.get("logged_in"):
        return redirect(url_for(ROUTE_INDEX))

    if request.method == "POST":
        from werkzeug.security import check_password_hash
        provided_password = request.form.get("password", "")
        expected_password = current_app.config.get("DASHBOARD_PASSWORD", "")
        
        # SEC-06: Support Werkzeug hashes (pbkdf2, scrypt, argon2)
        is_hashed = expected_password.startswith(("pbkdf2:", "scrypt:", "argon2:"))
        
        is_valid = False
        if is_hashed:
            is_valid = check_password_hash(expected_password, provided_password)
        elif provided_password and expected_password:
            is_valid = hmac.compare_digest(provided_password, expected_password)

        if is_valid:
            # Session rotation to prevent session fixation (S-07)
            old_session = dict(session)
            session.clear()
            for k, v in old_session.items():
                session[k] = v
            session["logged_in"] = True
            session.permanent = True
            flash("Connexion réussie.", "success")
            return redirect(url_for(ROUTE_INDEX))
        else:
            flash("Mot de passe incorrect.", "error")

    return render_template("login.html")


@dashboard_bp.post("/logout")
def logout() -> Any:
    session.pop("logged_in", None)
    flash("Déconnexion réussie.", "success")
    return redirect(url_for("dashboard.login"))


@dashboard_bp.get("/debug/state")
@limiter.limit("5 per minute")
def debug_state() -> Any:
    expected_token = current_app.config.get("STATE_DEBUG_TOKEN")
    
    auth_header = request.headers.get("Authorization")
    provided_token = None
    if auth_header and auth_header.startswith("Bearer "):
        provided_token = auth_header[7:].strip()

    if not expected_token or not provided_token:
        abort(404)

    if not hmac.compare_digest(provided_token, expected_token):
        abort(404)

    state_store = current_app.extensions["state_store"]
    state = state_store.read()

    # State Allowlist Filtering (S-08)
    STATE_ALLOWLIST = {
        "api_requests_total",
        "api_requests_today",
        "last_api_request_timestamp",
        "temperature",
        "humidity",
        "last_meter_timestamp",
        "assumed_aircon_power",
        "last_aircon_control_timestamp",
        "last_cooldown_timestamp",
        "automation_last_run_timestamp",
        "automation_last_status",
        "automation_disabled_until",
        "temperature_stale",
    }
    filtered_state = {k: v for k, v in state.items() if k in STATE_ALLOWLIST}

    return current_app.response_class(
        json.dumps(filtered_state, indent=2, ensure_ascii=False) + "\n",
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
    except StoreError:
        app.logger.exception("[health] store error")
        payload = {
            "status": "error",
            "details": "store_unavailable",
            "timestamp_utc": timestamp,
        }
        return app.response_class(
            json.dumps(payload) + "\n", mimetype="application/json", status=503
        )
    except Exception:  # pragma: no cover - defensive fallback
        app.logger.exception("[health] unexpected failure")
        payload = {
            "status": "error",
            "details": "unexpected_failure",
            "timestamp_utc": timestamp,
        }
        return app.response_class(
            json.dumps(payload) + "\n", mimetype="application/json", status=503
        )

    # Check Postgres connectivity
    postgres_configured = (os.environ.get("STORE_BACKEND", "postgres").strip().lower() == "postgres")
    postgres_connected = False
    
    if isinstance(settings_store, PostgresStore):
        postgres_connected = bool(settings_store.health_check())
    elif isinstance(settings_store, JsonStore):
        postgres_connected = False
    else:
        # For MemoryStore and other test mock stores, default to True so mock-based tests don't fail with 503
        postgres_connected = True
    
    # Get last scheduler tick
    last_scheduler_tick = None
    if getattr(scheduler_service, "last_tick_time", None) is not None:
        last_scheduler_tick = scheduler_service.last_tick_time.isoformat() + "Z"
        
    # Get average tick duration
    automation_service = app.extensions.get("automation_service")
    average_tick_duration = 0.0
    if automation_service:
        average_tick_duration = getattr(automation_service, "average_tick_duration", 0.0)
        
    status = "ok"
    if postgres_configured and not postgres_connected:
        status = "degraded"

    payload = {
        "status": status,
        "scheduler_running": scheduler_running,
        "automation_enabled": automation_enabled,
        "last_tick": last_tick,
        "last_scheduler_tick": last_scheduler_tick,
        "average_tick_duration_seconds": round(average_tick_duration, 4),
        "postgres_connected": postgres_connected,
        "timestamp_utc": timestamp,
    }

    scheduler_enabled = (os.environ.get("SCHEDULER_ENABLED", "true").strip().lower() == "true")
    if (postgres_configured and not postgres_connected) or (scheduler_enabled and not scheduler_running):
        status_code = 503
    else:
        status_code = 200

    return app.response_class(
        json.dumps(payload) + "\n", mimetype="application/json", status=status_code
    )


def _update_timezone(request_form: Any, settings: dict[str, Any]) -> None:
    timezone_raw = request_form.get("timezone")
    if timezone_raw is None:
        settings.setdefault("timezone", DEFAULT_TIMEZONE)
        return
        
    requested_timezone = str(timezone_raw).strip() or DEFAULT_TIMEZONE
    try:
        ZoneInfo(requested_timezone)
        settings["timezone"] = requested_timezone
    except ZoneInfoNotFoundError:
        flash(
            "Fuseau horaire invalide : utilisez un identifiant IANA (ex: Europe/Paris, UTC).",
            "error",
        )

def _update_time_windows(request_form: Any, settings: dict[str, Any]) -> None:
    time_window_days_raw = request_form.getlist("time_window_days")
    time_window_start = request_form.get("time_window_start", "").strip()
    time_window_end = request_form.get("time_window_end", "").strip()

    if not (time_window_days_raw or time_window_start or time_window_end):
        settings["time_windows"] = []
        return

    # SEC-03: Strict HH:MM format validation
    hhmm_pattern = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")
    if time_window_start and not hhmm_pattern.match(time_window_start):
        flash(
            "L'heure de début est invalide : utilisez le format HH:MM (ex: 08:30).",
            "error",
        )
        return
    if time_window_end and not hhmm_pattern.match(time_window_end):
        flash(
            "L'heure de fin est invalide : utilisez le format HH:MM (ex: 22:00).",
            "error",
        )
        return

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
            "Fenêtre horaire invalide : les jours doivent être compris entre 0 et 6 et les heures de début/fin sont obligatoires.",
            "error",
        )

def _update_profiles(request_form: Any, settings: dict[str, Any]) -> None:
    for key in ("winter", "summer"):
        profile = settings.get(key, {})
        if not isinstance(profile, dict):
            profile = {}

        # SEC-02: Temperature bounds (10-35°C) and min <= max validation
        profile["min_temp"] = _as_float(request_form.get(f"{key}_min_temp"), default=float(profile.get("min_temp", 0.0) or 0.0), minimum=10.0, maximum=35.0)
        profile["max_temp"] = _as_float(request_form.get(f"{key}_max_temp"), default=float(profile.get("max_temp", 0.0) or 0.0), minimum=10.0, maximum=35.0)
        profile["target_temp"] = _as_float(request_form.get(f"{key}_target_temp"), default=float(profile.get("target_temp", 0.0) or 0.0), minimum=10.0, maximum=35.0)

        if profile["min_temp"] > profile["max_temp"]:
            flash(
                f"Profil {key} : la température minimale ne peut pas dépasser la maximale. Valeurs inversées automatiquement.",
                "error",
            )
            profile["min_temp"], profile["max_temp"] = profile["max_temp"], profile["min_temp"]

        profile["fan_speed"] = _as_int(request_form.get(f"{key}_fan_speed"), default=int(profile.get("fan_speed", 3) or 3), minimum=1, maximum=4)
        profile["ac_mode"] = _as_int(request_form.get(f"{key}_ac_mode"), default=int(profile.get("ac_mode", 5 if key == "winter" else 2) or 0), minimum=0, maximum=5)

        settings[key] = profile


@dashboard_bp.post("/settings")
@limiter.limit("5 per minute")
def update_settings() -> Any:
    """Handle settings form submission and validation.

    Processes form data from the settings page, validates all inputs,
    and persists changes to the settings store.

    Returns:
        Redirect to settings page with success or error flash messages

    Raises:
        StoreError: If settings cannot be read or written
    """
    settings_store = current_app.extensions["settings_store"]
    scheduler_service = current_app.extensions["scheduler_service"]

    with _transaction_context(settings_store):
        settings = settings_store.read()
        current_aircon_scenes = _extract_aircon_scenes(settings)

        settings["automation_enabled"] = _as_bool(request.form.get("automation_enabled"))
        
        # Mode Validation (S-05)
        mode = str(request.form.get("mode", settings.get("mode", "winter"))).strip().lower()
        if mode not in ("winter", "summer"):
            flash("Le mode sélectionné est invalide (doit être 'winter' ou 'summer').", "error")
            return redirect(url_for("dashboard.settings_page"))
        settings["mode"] = mode


        settings["poll_interval_seconds"] = _as_int(
            request.form.get("poll_interval_seconds"),
            default=int(settings.get("poll_interval_seconds", 120) or 120),
            minimum=60,
            maximum=3600,
        )

        settings["adaptive_polling_enabled"] = _as_bool(
            request.form.get("adaptive_polling_enabled", settings.get("adaptive_polling_enabled", True))
        )
        settings["idle_poll_interval_seconds"] = _as_int(
            request.form.get("idle_poll_interval_seconds"),
            default=int(settings.get("idle_poll_interval_seconds", 600) or 600),
            minimum=300,
            maximum=86_400,
        )
        settings["poll_warmup_minutes"] = _as_int(
            request.form.get("poll_warmup_minutes"),
            default=int(settings.get("poll_warmup_minutes", 15) or 15),
            minimum=0,
            maximum=24 * 60,
        )
        settings["aircon_poll_cooldown_minutes"] = _as_int(
            request.form.get("aircon_poll_cooldown_minutes"),
            default=int(settings.get("aircon_poll_cooldown_minutes", 15) or 15),
            minimum=1,
            maximum=24 * 60,
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
        settings["action_on_cooldown_seconds"] = _as_int(
            request.form.get("action_on_cooldown_seconds"),
            default=int(settings.get("action_on_cooldown_seconds", 0) or 0),
            minimum=0,
            maximum=3600,
        )
        settings["action_off_cooldown_seconds"] = _as_int(
            request.form.get("action_off_cooldown_seconds"),
            default=int(settings.get("action_off_cooldown_seconds", 0) or 0),
            minimum=0,
            maximum=3600,
        )
        settings["off_repeat_count"] = _as_int(
            request.form.get("off_repeat_count"),
            default=int(settings.get("off_repeat_count", 1) or 1),
            minimum=1,
            maximum=10,
        )
        settings["off_repeat_interval_seconds"] = _as_int(
            request.form.get("off_repeat_interval_seconds"),
            default=int(settings.get("off_repeat_interval_seconds", 10) or 10),
            minimum=1,
            maximum=600,
        )

        settings["turn_off_outside_windows"] = _as_bool(request.form.get("turn_off_outside_windows"))
        settings["fan_mode_during_window"] = _as_bool(request.form.get("fan_mode_during_window"))

        _update_timezone(request.form, settings)

        settings["api_quota_warning_threshold"] = _as_int(
            request.form.get("api_quota_warning_threshold"),
            default=int(settings.get("api_quota_warning_threshold", DEFAULT_QUOTA_WARNING_THRESHOLD) or DEFAULT_QUOTA_WARNING_THRESHOLD),
            minimum=0,
            maximum=10_000,
        )

        # Device IDs Validation (S-06)
        device_id_pattern = re.compile(r"^[a-zA-Z0-9:-]*$")
        meter_device_id = str(request.form.get("meter_device_id", "")).strip()
        aircon_device_id = str(request.form.get("aircon_device_id", "")).strip()

        if len(meter_device_id) > 50 or not device_id_pattern.match(meter_device_id):
            flash("L'ID du capteur est invalide (caractères alphanumériques/tirets/deux-points, max 50 caractères).", "error")
            return redirect(url_for("dashboard.settings_page"))

        if len(aircon_device_id) > 50 or not device_id_pattern.match(aircon_device_id):
            flash("L'ID du climatiseur est invalide (caractères alphanumériques/tirets/deux-points, max 50 caractères).", "error")
            return redirect(url_for("dashboard.settings_page"))

        settings["meter_device_id"] = meter_device_id
        settings["aircon_device_id"] = aircon_device_id

        _update_time_windows(request.form, settings)
        _update_profiles(request.form, settings)

        # SEC-02: Scene ID regex validation
        scene_id_pattern = re.compile(r"^[a-zA-Z0-9\-]*$")
        updated_aircon_scenes: dict[str, str] = {}
        for key in AIRCON_SCENE_KEYS:
            raw_scene_id = str(
                request.form.get(f"scene_{key}_id", current_aircon_scenes.get(key, ""))
            ).strip()
            if raw_scene_id and (len(raw_scene_id) > 50 or not scene_id_pattern.match(raw_scene_id)):
                flash(
                    f"L'ID de scène '{key}' est invalide (alphanumérique et tirets uniquement, max 50 caractères).",
                    "error",
                )
                return redirect(url_for("dashboard.settings_page"))
            updated_aircon_scenes[key] = raw_scene_id

        settings["aircon_scenes"] = updated_aircon_scenes

        settings_store.write(settings)

    scheduler_service.reschedule()

    flash("Paramètres enregistrés.")
    return redirect(url_for(ROUTE_INDEX))


@dashboard_bp.post("/actions/run_once")
@limiter.limit("10 per minute")
def run_once() -> Any:
    """Execute a single automation cycle manually.

    Triggers the automation service to run one complete cycle
    of temperature monitoring and device control.
    The tick runs in a background thread to avoid blocking the HTTP response.

    Returns:
        Redirect to home page with success flash message
    """
    automation_service = current_app.extensions["automation_service"]
    app = current_app._get_current_object()  # type: ignore[attr-defined]

    def _run_async() -> None:
        with app.app_context():
            try:
                automation_service.run_once()
            except Exception as exc:
                app.logger.warning("[run_once] async tick failed: %s", exc)

    threading.Thread(target=_run_async, name="manual_run_once", daemon=True).start()
    flash("Cycle d'automatisation lancé en arrière-plan.")
    return redirect(url_for(ROUTE_INDEX))


@dashboard_bp.post("/actions/aircon_off")
@limiter.limit("10 per minute")
def aircon_off() -> Any:
    return _execute_aircon_action(
        "off",
        state_reason="manual_off",
        flash_label="Climatisation arrêtée.",
        assumed_power="off",
    )


def _update_state_on_success(
    state_store: Any, assumed_power: str, action_desc: str, assumed_mode: int | None = None
) -> None:
    with _transaction_context(state_store):
        state = state_store.read()
        state.update({
            "assumed_aircon_power": assumed_power,
            "assumed_aircon_mode": assumed_mode,
            "assumed_aircon_parameter": None,
            "last_action": action_desc,
            "last_action_at": _utc_now_iso(),
            "last_error": None
        })
        state_store.write(state)


def _update_state_on_error(state_store: Any, error_msg: str) -> None:
    with _transaction_context(state_store):
        state = state_store.read()
        state["last_error"] = error_msg
        state_store.write(state)


def _handle_direct_action(
    action_key: str, scene_id: str, aircon_id: str, state_reason: str, flash_label: str, assumed_power: str
) -> Any:
    automation_service = current_app.extensions.get("automation_service")
    has_lock_support = automation_service and hasattr(automation_service, "_acquire_lock")
    if has_lock_support:
        if not automation_service._acquire_lock():
            flash("Action impossible : un cycle d'automatisation ou une autre commande est en cours. Veuillez réessayer.", "error")
            return redirect(url_for(ROUTE_INDEX))

    try:
        client = current_app.extensions["switchbot_client"]
        state_store = current_app.extensions["state_store"]

        assumed_mode = None
        if action_key == "fan":
            assumed_mode = 4
        elif action_key == "winter":
            assumed_mode = 5
        elif action_key == "summer":
            assumed_mode = 2

        if scene_id:
            try:
                client.run_scene(scene_id)
                _update_state_on_success(
                    state_store,
                    assumed_power,
                    f"scene({scene_id}) ({state_reason})",
                    assumed_mode=assumed_mode,
                )
                flash(flash_label)
                return redirect(url_for(ROUTE_INDEX))
            except SwitchBotApiError as exc:
                if not aircon_id:
                    _update_state_on_error(state_store, str(exc))
                    flash(str(exc), "error")
                    return redirect(url_for(ROUTE_INDEX))
                current_app.logger.warning(f"Scene execution failed for {action_key}: {exc}. Falling back to direct command.")

        if action_key == "off":
            if not aircon_id:
                flash("aircon_device_id manquant pour commande directe", "error")
                return redirect(url_for(ROUTE_INDEX))
            try:
                client.send_command(aircon_id, command="turnOff", parameter="default", command_type="command")
                _update_state_on_success(state_store, "off", f"turnOff ({state_reason})")
                flash(flash_label)
            except SwitchBotApiError as exc:
                _update_state_on_error(state_store, str(exc))
                flash(str(exc), "error")
            return redirect(url_for(ROUTE_INDEX))

        if not scene_id:
            action_label = AIRCON_SCENE_LABELS.get(action_key, action_key)
            flash(f"Aucune scène configurée pour {action_label} en mode API Direct.", "error")
        else:
            flash(f"Impossible d'exécuter l'action {action_key} : scène échouée et pas de commande directe supportée", "error")
            
        return redirect(url_for(ROUTE_INDEX))
    finally:
        if has_lock_support:
            automation_service._release_lock()


def _execute_aircon_action(
    action_key: str,
    *,
    state_reason: str,
    flash_label: str,
    assumed_power: str = "unknown",
) -> Any:
    settings_store = current_app.extensions["settings_store"]
    settings = settings_store.read()
    scene_id = _extract_aircon_scenes(settings).get(action_key, "").strip()
    aircon_id = str(settings.get("aircon_device_id", "")).strip()
    return _handle_direct_action(action_key, scene_id, aircon_id, state_reason, flash_label, assumed_power)


@dashboard_bp.post("/actions/aircon_on")
@limiter.limit("10 per minute")
def aircon_on() -> Any:
    """Route to the current mode scene for backward compatibility."""
    settings_store = current_app.extensions["settings_store"]
    settings = settings_store.read()
    mode = str(settings.get("mode", "winter")).strip().lower()
    scene_key = mode if mode in AIRCON_SCENE_KEYS else "winter"
    return _execute_aircon_action(
        scene_key,
        state_reason=f"manual_{scene_key}",
        flash_label=f"Action {scene_key} exécutée.",
    )


@dashboard_bp.post("/actions/aircon_on_winter")
@limiter.limit("10 per minute")
def aircon_on_winter() -> Any:
    return _execute_aircon_action(
        "winter",
        state_reason="manual_winter",
        flash_label="Mode hiver activé.",
        assumed_power="on",
    )


@dashboard_bp.post("/actions/aircon_on_summer")
@limiter.limit("10 per minute")
def aircon_on_summer() -> Any:
    return _execute_aircon_action(
        "summer",
        state_reason="manual_summer",
        flash_label="Mode été activé.",
        assumed_power="on",
    )


@dashboard_bp.post("/actions/aircon_on_fan")
@limiter.limit("10 per minute")
def aircon_on_fan() -> Any:
    return _execute_aircon_action(
        "fan",
        state_reason="manual_fan",
        flash_label="Mode ventilateur activé.",
        assumed_power="on",
    )


def _enrich_device_status(client: Any, device: dict[str, Any]) -> None:
    device_id = device.get("deviceId")
    if not device_id:
        return
    try:
        status_data = client.get_device_status(device_id)
        status_body = status_data.get("body", {}) if isinstance(status_data, dict) else {}
        if status_body:
            for key in ["onlineStatus", "battery", "version", "firmwareVersion"]:
                if key in status_body:
                    device[key] = status_body[key]
                    if key == "version":
                        device["firmwareVersion"] = status_body[key]
    except SwitchBotApiError as status_exc:
        current_app.logger.warning(f"Failed to fetch status for {device_id}: {status_exc}")


@dashboard_bp.get("/devices")
@limiter.limit("10 per minute")
def devices() -> str:
    client = current_app.extensions["switchbot_client"]
    data = None
    error = None

    try:
        data = client.get_devices()
        body = data.get("body", {}) if isinstance(data, dict) else {}
        device_list = body.get("deviceList") if isinstance(body, dict) else None
        
        if device_list:
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = {
                    executor.submit(_enrich_device_status, client, device): device
                    for device in device_list
                }
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as exc:
                        current_app.logger.warning(
                            "[devices] status enrichment error: %s", exc
                        )
    except SwitchBotApiError as exc:
        error = str(exc)

    return render_template("devices.html", data=data, error=error)


@dashboard_bp.post("/actions/quick_off")
@limiter.limit("10 per minute")
def quick_off() -> Any:
    settings_store = current_app.extensions["settings_store"]
    
    with _transaction_context(settings_store):
        settings = settings_store.read()
        settings["automation_enabled"] = False
        settings_store.write(settings)
    
    return _execute_aircon_action(
        "off",
        state_reason="quick_off",
        flash_label="Automatisation désactivée et climatisation éteinte.",
        assumed_power="off",
    )


@dashboard_bp.get("/history")
def history_page() -> str:
    return render_template("history.html")


@dashboard_bp.get("/actions")
def actions_page() -> str:
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]
    
    try:
        settings = settings_store.read()
    except StoreError:
        settings = {}
    
    try:
        state = state_store.read()
    except StoreError:
        state = {}
    
    # Get scene configuration for status display
    aircon_scenes = settings.get("aircon_scenes", {})
    missing_scenes = {
        key: not aircon_scenes.get(key)
        for key in ["winter", "summer", "fan", "off"]
    }
    
    return render_template(
        "actions.html",
        settings=settings,
        state=state,
        missing_scenes=missing_scenes,
    )


def _generate_mock_history_data(start: dt.datetime, end: dt.datetime) -> list[dict[str, Any]]:
    mock_data = []
    current = start
    while current <= end:
        mock_data.append({
            "timestamp": current.isoformat() + "Z",
            "temperature": round(20 + random.random() * 10, 1),
            "humidity": round(40 + random.random() * 20, 1),
            "assumed_aircon_power": random.choice(["on", "off", "unknown"]),
            "last_action": random.choice(["automation_winter_on", "automation_summer_on", "automation_winter_off", None]),
            "api_requests_today": random.randint(100, 200),
            "error_count": random.randint(0, 2)
        })
        current += dt.timedelta(minutes=5)
    return mock_data

def _parse_history_query_params(request_args: Any) -> tuple[dt.datetime, dt.datetime, list[str], str, int]:
    start_str = request_args.get("start")
    end_str = request_args.get("end")
    metrics_param = request_args.get("metrics")
    granularity = request_args.get("granularity", "minute")
    limit = int(request_args.get("limit", 1000))

    metrics = []
    if metrics_param:
        if isinstance(metrics_param, str):
            metrics = [m.strip() for m in metrics_param.split(",") if m.strip()]
        else:
            metrics = metrics_param

    if not start_str or not end_str:
        end = dt.datetime.now(dt.timezone.utc)
        start = end - dt.timedelta(hours=6)
    else:
        start = dt.datetime.fromisoformat(start_str.replace("Z", "+00:00"))
        end = dt.datetime.fromisoformat(end_str.replace("Z", "+00:00"))

    valid_granularities = ["minute", "5min", "15min", "hour"]
    if granularity not in valid_granularities:
        granularity = "minute"

    return start, end, metrics, granularity, limit

@dashboard_bp.get("/history/api/data")
@limiter.limit("30 per minute")
def history_api_data() -> Any:
    history_service = current_app.extensions.get("history_service")
    if not history_service:
        if not current_app.debug and not current_app.testing:
            return {
                "error": "Service Historique indisponible. La base de données PostgreSQL est déconnectée."
            }, 503
        
        end = dt.datetime.now(dt.timezone.utc)
        start = end - dt.timedelta(hours=6)
        mock_data = _generate_mock_history_data(start, end)
        
        return {
            "data": mock_data,
            "start": start.isoformat() + "Z",
            "end": end.isoformat() + "Z",
            "granularity": "minute",
            "metrics": ["temperature", "humidity", "assumed_aircon_power"],
            "count": len(mock_data),
            "mock": True
        }

    try:
        start, end, metrics, granularity, limit = _parse_history_query_params(request.args)

        # Get historical data
        data = history_service.get_history(start, end, metrics, granularity, limit)
        
        # Return empty data structure if no data found
        if not data:
            return {
                "data": [],
                "start": start.isoformat(),
                "end": end.isoformat(),
                "granularity": granularity,
                "metrics": metrics or ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
                "count": 0,
                "message": "No historical data available yet"
            }
        
        return {
            "data": data,
            "start": start.isoformat(),
            "end": end.isoformat(),
            "granularity": granularity,
            "metrics": metrics or ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
            "count": len(data),
        }

    except ValueError as exc:
        return {"error": f"Invalid parameters: {exc}"}, 400
    except Exception:
        current_app.logger.exception("[history] API error")
        # Return empty data structure on error to avoid breaking the frontend
        return {
            "data": [],
            "start": start.isoformat() if 'start' in locals() else dt.datetime.now(dt.timezone.utc).isoformat(),
            "end": end.isoformat() if 'end' in locals() else dt.datetime.now(dt.timezone.utc).isoformat(),
            "granularity": "minute",
            "metrics": ["timestamp", "temperature", "humidity", "assumed_aircon_power"],
            "count": 0,
            "message": "Error retrieving data"
        }


@dashboard_bp.get("/history/api/aggregates")
@limiter.limit("30 per minute")
def history_api_aggregates() -> Any:
    """API endpoint for aggregated statistics."""
    history_service = current_app.extensions.get("history_service")
    if not history_service:
        if not current_app.debug and not current_app.testing:
            return {
                "error": "Service Historique indisponible. La base de données PostgreSQL est déconnectée."
            }, 503
        
        # Return mock aggregates when service is not available
        return {
            "period_hours": 6,
            "aggregates": {
                "total_records": random.randint(50, 100),
                "avg_temperature": round(20 + random.random() * 10, 1),
                "min_temperature": round(18 + random.random() * 2, 1),
                "max_temperature": round(28 + random.random() * 2, 1),
                "avg_humidity": round(40 + random.random() * 20, 1),
                "min_humidity": round(35 + random.random() * 5, 1),
                "max_humidity": round(60 + random.random() * 5, 1),
                "common_aircon_state": random.choice(["on", "off"]),
                "distinct_actions": random.randint(2, 4),
                "total_errors": random.randint(0, 5),
                "max_api_requests": random.randint(150, 250)
            },
            "mock": True
        }

    try:
        period_hours = int(request.args.get("period_hours", 1))
        if period_hours < 1 or period_hours > 24:
            period_hours = 1

        aggregates = history_service.get_aggregates(period_hours)
        
        # Return empty aggregates if no data
        if not aggregates:
            return {
                "period_hours": period_hours,
                "aggregates": {
                    "total_records": 0,
                    "avg_temperature": 0,
                    "min_temperature": 0,
                    "max_temperature": 0,
                    "avg_humidity": 0,
                    "min_humidity": 0,
                    "max_humidity": 0,
                    "common_aircon_state": "unknown",
                    "distinct_actions": 0,
                    "total_errors": 0,
                    "max_api_requests": 0
                },
                "message": "No historical data available yet"
            }
        
        return {
            "period_hours": period_hours,
            "aggregates": aggregates,
        }

    except Exception:
        current_app.logger.exception("[history] Aggregates API error")
        # Return empty aggregates on error to avoid breaking the frontend
        return {
            "period_hours": 1,
            "aggregates": {
                "total_records": 0,
                "avg_temperature": 0,
                "min_temperature": 0,
                "max_temperature": 0,
                "avg_humidity": 0,
                "min_humidity": 0,
                "max_humidity": 0,
                "common_aircon_state": "unknown",
                "distinct_actions": 0,
                "total_errors": 0,
                "max_api_requests": 0
            },
            "message": "Error retrieving data"
        }


@dashboard_bp.get("/history/api/latest")
@limiter.limit("30 per minute")
def history_api_latest() -> Any:
    history_service = current_app.extensions.get("history_service")
    if not history_service:
        if not current_app.debug and not current_app.testing:
            return {
                "error": "Service Historique indisponible. La base de données PostgreSQL est déconnectée."
            }, 503
        
        # Return mock latest records when service is not available
        mock_latest = []
        for i in range(10):
            timestamp = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=i * 5)
            mock_latest.append({
                "id": i + 1,
                "timestamp": timestamp.isoformat() + "Z",
                "temperature": round(20 + random.random() * 10, 1),
                "humidity": round(40 + random.random() * 20, 1),
                "assumed_aircon_power": random.choice(["on", "off", "unknown"]),
                "last_action": random.choice(["automation_winter_on", "automation_summer_on", "automation_winter_off", None]),
                "error_count": random.randint(0, 2),
                "metadata": {
                    "last_read_at": timestamp.isoformat() + "Z",
                    "automation_active": random.choice([True, False])
                }
            })
        
        return {
            "latest": mock_latest,
            "count": len(mock_latest),
            "mock": True
        }

    try:
        limit = int(request.args.get("limit", 10))
        if limit < 1 or limit > 100:
            limit = 10

        latest = history_service.get_latest_records(limit)
        
        # Return empty latest if no data
        if not latest:
            return {
                "latest": [],
                "count": 0,
                "message": "No historical data available yet"
            }
        
        return {
            "latest": latest,
            "count": len(latest),
        }

    except Exception:
        current_app.logger.exception("[history] Latest API error")
        # Return empty latest on error to avoid breaking the frontend
        return {
            "latest": [],
            "count": 0,
            "message": "Error retrieving data"
        }
