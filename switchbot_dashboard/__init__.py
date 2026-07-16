from __future__ import annotations

import atexit
import datetime
import logging
import os
from pathlib import Path
import sys
import threading

from dotenv import load_dotenv

from flask import Flask

from flask_wtf.csrf import CSRFProtect
from psycopg_pool import ConnectionPool

from .automation import AutomationService
from .config_store import BaseStore, JsonStore, StoreError
from .postgres_store import PostgresStore, PostgresStoreError
from .history_service import HistoryService
from .routes import dashboard_bp
from .scheduler import SchedulerService
from .quota import ApiQuotaTracker
from .switchbot_api import SwitchBotClient
from .extensions import limiter

load_dotenv()


def _build_store(
    app: Flask,
    *,
    kind: str,
    default_path: str,
    path_env: str,
    pool: ConnectionPool | None = None,
) -> BaseStore:
    backend = os.environ.get("STORE_BACKEND", "postgres").strip().lower()
    selected_backend = backend or "postgres"
    is_testing = app.testing or os.environ.get("FLASK_ENV") == "testing"
    is_production = (os.environ.get("FLASK_ENV") == "production" or app.config.get("ENV") == "production" or (not app.debug and not app.testing)) and not is_testing

    def _make_json_store() -> BaseStore:
        path = os.environ.get(path_env, default_path)
        app.logger.info("Using filesystem backend for %s store at %s", kind, path)
        return JsonStore(path)

    # PostgreSQL backend (preferred)
    if selected_backend == "postgres":
        postgres_url = os.environ.get("POSTGRES_URL", "").strip()
        if not postgres_url and not pool:
            if is_production:
                raise PostgresStoreError("PostgreSQL URL is required in production environment.")
            app.logger.error(
                "[store] STORE_BACKEND=postgres but no POSTGRES_URL configured. Falling back to filesystem for %s store.",
                kind,
            )
            return _make_json_store()

        try:
            ssl_mode = os.environ.get("POSTGRES_SSL_MODE", "require").strip()
            store = PostgresStore(
                connection_string=postgres_url if pool is None else None,
                kind=kind,
                logger=app.logger,
                ssl_mode=ssl_mode,
                pool=pool,
            )
            
            # Health check
            if store.health_check():
                app.logger.info("[store] Using PostgreSQL backend for %s store", kind)
                return store
            else:
                if is_production:
                    store.close()
                    raise PostgresStoreError(f"PostgreSQL health check failed for {kind} store in production.")
                app.logger.error(
                    "[store] PostgreSQL health check failed for %s store. Falling back to filesystem.",
                    kind,
                )
                store.close()
                return _make_json_store()
                
        except PostgresStoreError:
            if is_production:
                raise
            app.logger.exception(
                "[store] PostgreSQL backend unavailable for %s store. Falling back to filesystem.",
                kind,
            )
            return _make_json_store()

    # Legacy Redis support (deprecated)
    elif selected_backend == "redis":
        if is_production:
            raise PostgresStoreError("Redis backend is deprecated and not supported in production.")
        app.logger.warning(
            "[store] Redis backend is deprecated. Consider migrating to PostgreSQL. Using filesystem fallback for %s store.",
            kind,
        )
        return _make_json_store()

    # Filesystem fallback
    if is_production:
        raise PostgresStoreError("Filesystem fallback is disabled in production. PostgreSQL store must be configured.")
    return _make_json_store()


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
    
    # Configure session cookie options (S-02)
    app.config["SESSION_COOKIE_SECURE"] = not app.debug and not app.testing
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=30)

    flask_secret = os.environ.get("FLASK_SECRET_KEY")
    insecure_keys = {"dev-local-only", "change-me", "default", "secret", "password", "key", "admin"}
    is_insecure = not flask_secret or str(flask_secret).strip().lower() in insecure_keys

    if is_insecure and not app.debug and not app.testing:
        is_pytest = "pytest" in sys.modules or any("pytest" in arg for arg in sys.argv)
        if not is_pytest:
            raise RuntimeError("Security Violation: FLASK_SECRET_KEY must be set in production (secure value required)")
    app.secret_key = flask_secret or "dev-local-only"
    app.config["STATE_DEBUG_TOKEN"] = os.environ.get("STATE_DEBUG_TOKEN", "").strip()
    
    dashboard_password = os.environ.get("DASHBOARD_PASSWORD", "").strip()
    is_pytest = "pytest" in sys.modules or any("pytest" in arg for arg in sys.argv)
    is_testing = app.testing or os.environ.get("FLASK_ENV") == "testing"
    is_production = (os.environ.get("FLASK_ENV") == "production" or app.config.get("ENV") == "production" or (not app.debug and not app.testing)) and not is_testing
    if not dashboard_password and is_production and not is_pytest:
        raise RuntimeError("Security Violation: DASHBOARD_PASSWORD must be set in production")
    app.config["DASHBOARD_PASSWORD"] = dashboard_password

    log_level_raw = os.environ.get("LOG_LEVEL", "info").strip().upper()
    log_level = getattr(logging, log_level_raw, logging.INFO)
    logging.getLogger().setLevel(log_level)
    app.logger.setLevel(log_level)

    # Initialize CSRF Protection globally
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Initialize Rate Limiter
    app.config.setdefault("RATELIMIT_ENABLED", not app.testing)
    app.config.setdefault("RATELIMIT_STORAGE_URI", os.environ.get("RATELIMIT_STORAGE_URI", "memory://"))
    limiter.init_app(app)

    # Durcissement Rate Limiter (S-04)
    if is_production and app.config.get("RATELIMIT_STORAGE_URI", "").startswith("memory://"):
        app.logger.warning(
            "[api] RATELIMIT_STORAGE_URI is set to memory:// in production. "
            "Under multi-worker Gunicorn environments, rate limits will not be shared between workers."
        )

    # Initialize shared connection pool for PostgreSQL if selected
    shared_pool = None
    store_backend = os.environ.get("STORE_BACKEND", "postgres").strip().lower()
    if store_backend == "postgres":
        postgres_url = os.environ.get("POSTGRES_URL", "").strip()
        if postgres_url:
            try:
                ssl_mode = os.environ.get("POSTGRES_SSL_MODE", "require").strip()
                shared_pool = ConnectionPool(
                    conninfo=postgres_url,
                    min_size=1,
                    max_size=10,
                    kwargs={"sslmode": ssl_mode},
                )
                app.logger.info("[postgres] Shared connection pool initialized successfully")
                
                # Register atexit shutdown handler
                @atexit.register
                def close_shared_pool() -> None:
                    try:
                        shared_pool.close()
                        logging.getLogger().info("[postgres] Shared connection pool closed successfully via atexit")
                    except Exception as exc:
                        logging.getLogger().warning("[postgres] Error closing shared connection pool via atexit (%s)", exc)
            except Exception:
                app.logger.exception("[postgres] Failed to initialize shared connection pool")

    project_root = Path(__file__).resolve().parents[1]
    default_settings_path = str(project_root / "config" / "settings.json")
    default_state_path = str(project_root / "config" / "state.json")

    settings_store = _build_store(
        app,
        kind="settings",
        default_path=default_settings_path,
        path_env="SWITCHBOT_SETTINGS_PATH",
        pool=shared_pool,
    )
    state_store = _build_store(
        app,
        kind="state",
        default_path=default_state_path,
        path_env="SWITCHBOT_STATE_PATH",
        pool=shared_pool,
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


    # Initialize HistoryService if PostgreSQL is available
    history_service = None
    app.logger.info(f"[history] Settings store type: {type(settings_store)}")
    app.logger.info(f"[history] Is PostgresStore: {isinstance(settings_store, PostgresStore)}")
    
    if isinstance(settings_store, PostgresStore):
        try:
            history_service = HistoryService(
                connection_pool=settings_store.pool,
                logger=app.logger,
                retention_hours=6,
            )
            app.logger.info("[history] HistoryService initialized with PostgreSQL backend")
        except Exception:
            app.logger.exception("[history] Failed to initialize HistoryService")
    else:
        app.logger.warning("[history] HistoryService disabled: PostgreSQL backend not available")

    automation_service = AutomationService(
        settings_store=settings_store,
        state_store=state_store,
        switchbot_client=client,
        history_service=history_service,
    )

    scheduler_service = SchedulerService(
        settings_store=settings_store,
        tick_callable=automation_service.run_once,
        state_store=state_store,
        logger=app.logger,
    )

    app.extensions["settings_store"] = settings_store
    app.extensions["state_store"] = state_store
    app.extensions["switchbot_client"] = client
    app.extensions["automation_service"] = automation_service
    app.extensions["scheduler_service"] = scheduler_service
    app.extensions["quota_tracker"] = quota_tracker
    if history_service:
        app.extensions["history_service"] = history_service

    app.register_blueprint(dashboard_bp)

    # HTTP Security Headers (S-01)
    @app.after_request
    def set_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline'; font-src 'self'; "
            "img-src 'self' data:; connect-src 'self'"
        )
        if not app.debug and not app.testing:
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response

    _mark_temperature_stale(app, state_store, reason="app_start")
    
    # Run the initial poll in a background thread to make startup non-blocking (REL-02)
    is_testing = app.testing or os.environ.get("FLASK_ENV") == "testing" or "pytest" in sys.modules
    if is_testing:
        try:
            automation_service.poll_meter()
        except Exception as exc:  # pragma: no cover
            app.logger.warning("Initial meter poll failed (sync testing): %s", exc)
    else:
        def run_initial_poll_async():
            with app.app_context():
                try:
                    automation_service.poll_meter()
                except Exception as exc:  # pragma: no cover
                    app.logger.warning("Initial meter poll failed (async): %s", exc)
        threading.Thread(target=run_initial_poll_async, name="initial_meter_poll", daemon=True).start()

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
            
            # Register hourly history cleanup job (A-04)
            if history_service:
                scheduler = scheduler_service.get_scheduler()
                if scheduler:
                    scheduler.add_job(
                        func=history_service.cleanup_old_records,
                        trigger="interval",
                        hours=1,
                        id="history_cleanup",
                        replace_existing=True,
                    )
                    app.logger.info("[scheduler] Registered hourly history cleanup job")
    else:
        app.logger.info("[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false")

    # Apply Werkzeug ProxyFix behind reverse proxies if configured (SEC-01)
    proxy_fix_for = os.environ.get("PROXY_FIX_FOR", "").strip()
    if proxy_fix_for:
        try:
            num_proxies = int(proxy_fix_for)
        except ValueError:
            num_proxies = 1
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(
            app.wsgi_app,
            x_for=num_proxies,
            x_proto=num_proxies,
            x_host=num_proxies,
            x_port=num_proxies,
            x_prefix=num_proxies,
        )
        app.logger.info("[security] ProxyFix middleware applied (trusted proxies: %d)", num_proxies)

    return app
