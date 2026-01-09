import os
from pathlib import Path

from flask import Flask

from .automation import AutomationService
from .config_store import JsonStore
from .scheduler import SchedulerService
from .switchbot_api import SwitchBotClient
from .routes import dashboard_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev")

    project_root = Path(__file__).resolve().parents[1]
    settings_path = os.environ.get(
        "SWITCHBOT_SETTINGS_PATH", str(project_root / "config" / "settings.json")
    )
    state_path = os.environ.get(
        "SWITCHBOT_STATE_PATH", str(project_root / "config" / "state.json")
    )

    settings_store = JsonStore(settings_path)
    state_store = JsonStore(state_path)

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

    client = SwitchBotClient(
        token=token,
        secret=secret,
        retry_attempts=retry_attempts,
        retry_delay_seconds=retry_delay_seconds,
    )

    automation_service = AutomationService(
        settings_store=settings_store,
        state_store=state_store,
        switchbot_client=client,
    )

    scheduler_service = SchedulerService(
        settings_store=settings_store,
        tick_callable=automation_service.run_once,
    )

    app.extensions["settings_store"] = settings_store
    app.extensions["state_store"] = state_store
    app.extensions["switchbot_client"] = client
    app.extensions["automation_service"] = automation_service
    app.extensions["scheduler_service"] = scheduler_service

    app.register_blueprint(dashboard_bp)

    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    if not debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        scheduler_service.start()

    return app
