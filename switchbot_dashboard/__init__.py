from __future__ import annotations

import logging
import os
from pathlib import Path

from flask import Flask
from redis import Redis
from redis.exceptions import RedisError

from .automation import AutomationService
from .config_store import BaseStore, JsonStore, RedisJsonStore, StoreError
from .ifttt import IFTTTWebhookClient
from .routes import dashboard_bp
from .scheduler import SchedulerService
from .quota import ApiQuotaTracker
from .switchbot_api import SwitchBotClient


def _build_store(
    app: Flask,
    *,
    kind: str,
    default_path: str,
    path_env: str,
) -> BaseStore:
    backend = os.environ.get("STORE_BACKEND", "filesystem").strip().lower()
    selected_backend = backend or "filesystem"

    def _make_json_store() -> BaseStore:
        path = os.environ.get(path_env, default_path)
        app.logger.info("Using filesystem backend for %s store at %s", kind, path)
        return JsonStore(path)

    if selected_backend != "redis":
        return _make_json_store()

    redis_url = os.environ.get("REDIS_URL", "").strip()
    if not redis_url:
        app.logger.error(
            "STORE_BACKEND=redis but REDIS_URL is missing. Falling back to filesystem for %s store.",
            kind,
        )
        return _make_json_store()

    redis_prefix = os.environ.get("REDIS_PREFIX", "switchbot_dashboard").strip() or "switchbot_dashboard"
    ttl_env = os.environ.get("REDIS_TTL_SECONDS", "").strip()
    ttl_seconds: int | None = None
    if ttl_env:
        try:
            ttl_seconds = max(int(ttl_env), 1)
        except ValueError:
            app.logger.warning("Invalid REDIS_TTL_SECONDS=%s. Ignoring TTL configuration.", ttl_env)

    try:
        redis_client = Redis.from_url(redis_url)
        redis_client.ping()
    except (RedisError, ValueError) as exc:
        app.logger.error(
            "Redis backend unavailable for %s store (%s). Falling back to filesystem.",
            kind,
            exc,
        )
        return _make_json_store()

    key = f"{redis_prefix}:{kind}"
    store: BaseStore = RedisJsonStore(redis_client, key=key, ttl_seconds=ttl_seconds)

    try:
        store.read()
    except StoreError as exc:
        app.logger.error(
            "Redis backend misconfigured for %s store (%s). Falling back to filesystem.",
            kind,
            exc,
        )
        return _make_json_store()

    app.logger.info("Using Redis backend for %s store (key=%s)", kind, key)
    return store


def _mark_temperature_stale(app: Flask, state_store: BaseStore, *, reason: str) -> None:
    try:
        state = state_store.read()
    except StoreError as exc:
        app.logger.warning("Unable to read state to mark temperature stale: %s", exc)
        return

    state["last_temperature_stale"] = True
    state["last_temperature_stale_reason"] = reason

    try:
        state_store.write(state)
    except StoreError as exc:
        app.logger.warning("Unable to persist temperature stale flag: %s", exc)


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev")
    app.config["STATE_DEBUG_TOKEN"] = os.environ.get("STATE_DEBUG_TOKEN", "").strip()

    log_level_raw = os.environ.get("LOG_LEVEL", "info").strip().upper()
    log_level = getattr(logging, log_level_raw, logging.INFO)
    logging.getLogger().setLevel(log_level)
    app.logger.setLevel(log_level)

    project_root = Path(__file__).resolve().parents[1]
    default_settings_path = str(project_root / "config" / "settings.json")
    default_state_path = str(project_root / "config" / "state.json")

    settings_store = _build_store(
        app,
        kind="settings",
        default_path=default_settings_path,
        path_env="SWITCHBOT_SETTINGS_PATH",
    )
    state_store = _build_store(
        app,
        kind="state",
        default_path=default_state_path,
        path_env="SWITCHBOT_STATE_PATH",
    )

    poll_interval_env = os.environ.get("SWITCHBOT_POLL_INTERVAL_SECONDS")
    if poll_interval_env:
        try:
            poll_interval_seconds = max(15, int(poll_interval_env))
        except ValueError:
            poll_interval_seconds = None
        else:
            settings = settings_store.read()
            if settings.get("poll_interval_seconds") != poll_interval_seconds:
                settings["poll_interval_seconds"] = poll_interval_seconds
                settings_store.write(settings)

    token = os.environ.get("SWITCHBOT_TOKEN", "")
    secret = os.environ.get("SWITCHBOT_SECRET", "")

    retry_attempts_raw = os.environ.get("SWITCHBOT_RETRY_ATTEMPTS", "2")
    retry_delay_raw = os.environ.get("SWITCHBOT_RETRY_DELAY_SECONDS", "10")
    try:
        retry_attempts = int(retry_attempts_raw)
    except ValueError:
        retry_attempts = 2

    try:
        retry_delay_seconds = int(retry_delay_raw)
    except ValueError:
        retry_delay_seconds = 10

    quota_tracker = ApiQuotaTracker(state_store=state_store)

    client = SwitchBotClient(
        token=token,
        secret=secret,
        retry_attempts=retry_attempts,
        retry_delay_seconds=retry_delay_seconds,
        quota_tracker=quota_tracker,
    )

    ifttt_client = IFTTTWebhookClient(timeout=10.0, logger_instance=app.logger)

    automation_service = AutomationService(
        settings_store=settings_store,
        state_store=state_store,
        switchbot_client=client,
        ifttt_client=ifttt_client,
    )

    scheduler_service = SchedulerService(
        settings_store=settings_store,
        tick_callable=automation_service.run_once,
        logger=app.logger,
    )

    app.extensions["settings_store"] = settings_store
    app.extensions["state_store"] = state_store
    app.extensions["switchbot_client"] = client
    app.extensions["ifttt_client"] = ifttt_client
    app.extensions["automation_service"] = automation_service
    app.extensions["scheduler_service"] = scheduler_service
    app.extensions["quota_tracker"] = quota_tracker

    app.register_blueprint(dashboard_bp)

    _mark_temperature_stale(app, state_store, reason="app_start")
    try:
        automation_service.poll_meter()
    except Exception as exc:  # pragma: no cover - defensive safeguard
        app.logger.warning("Initial meter poll failed: %s", exc)

    scheduler_enabled = os.environ.get("SCHEDULER_ENABLED", "true").strip().lower()

    if scheduler_enabled == "true":
        is_flask_dev_reloader_parent = (
            os.environ.get("FLASK_DEBUG", "").strip().lower() not in ("", "0", "false")
            and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
            and not os.environ.get("SERVER_SOFTWARE")
        )

        if is_flask_dev_reloader_parent:
            app.logger.info("[scheduler] Skipping start in Flask development reloader parent process")
        else:
            scheduler_service.start()
            app.logger.info("[scheduler] APScheduler enabled and started")
    else:
        app.logger.info("[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false")

    return app
