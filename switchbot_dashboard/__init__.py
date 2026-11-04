from __future__ import annotations

import atexit
import datetime
import logging
import os
from pathlib import Path
import secrets
import sys
import threading

from dotenv import load_dotenv

from flask import Flask, g

from flask_wtf.csrf import CSRFProtect
from psycopg_pool import ConnectionPool

from .automation import AutomationService
from .config_store import BaseStore, JsonStore, StoreError
from .postgres_store import PostgresStore, PostgresStoreError
from .store_resilience import ResilientStore
from .history_service import HistoryService
from .routes import dashboard_bp
from .scheduler import SchedulerService
from .quota import ApiQuotaTracker
from .switchbot_api import SwitchBotClient
from .extensions import limiter

load_dotenv()


def _running_under_wsgi_server() -> bool:
    """Return True when the app is served by a production WSGI runtime.

    ``FLASK_DEBUG`` is a development convenience flag, but deployment
    dashboards frequently inherit it from a local ``.env``. Detecting the
    actual runtime lets us ignore it where it would weaken security.
    """
    if os.environ.get("RENDER", "").strip().lower() in {"1", "true", "yes", "on"}:
        return True
    if os.environ.get("SERVER_SOFTWARE", "").strip():
        return True
    return "gunicorn" in sys.modules or "uwsgi" in sys.modules


def _env_flag(name: str, *, default: bool = False) -> bool:
    """Read a boolean environment flag using the project's accepted spellings."""
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _resolve_environment(app: Flask) -> tuple[bool, bool]:
    """Return ``(is_testing, is_production)`` for the current runtime."""
    is_testing = app.testing or os.environ.get("FLASK_ENV") == "testing"
    is_production = (
        os.environ.get("FLASK_ENV") == "production"
        or app.config.get("ENV") == "production"
        or (not app.debug and not app.testing)
    ) and not is_testing
    return is_testing, is_production


def _make_json_store(
    app: Flask, *, kind: str, default_path: str, path_env: str
) -> BaseStore:
    path = os.environ.get(path_env, default_path)
    app.logger.info("Using filesystem backend for %s store at %s", kind, path)
    return JsonStore(path)


def _read_failure_threshold() -> int:
    """Read STORE_FAILURE_THRESHOLD, defaulting to 3 on invalid values."""
    try:
        return max(1, int(os.environ.get("STORE_FAILURE_THRESHOLD", "3")))
    except ValueError:
        return 3


def _wrap_resilient_store(
    app: Flask,
    *,
    kind: str,
    store: BaseStore,
    default_path: str,
    path_env: str,
    is_production: bool,
) -> ResilientStore:
    """Wrap a healthy PostgreSQL store with runtime failure accounting."""
    allow_runtime_fallback = (not is_production) or _env_flag(
        "STORE_RUNTIME_FALLBACK"
    )
    fallback = None
    if allow_runtime_fallback:
        fallback_path = os.environ.get(path_env, default_path)
        fallback = JsonStore(fallback_path)
        app.logger.info(
            "[store] Runtime filesystem fallback configured for %s store at %s",
            kind,
            fallback_path,
        )

    return ResilientStore(
        primary=store,
        fallback=fallback,
        logger=app.logger,
        name=kind,
        failure_threshold=_read_failure_threshold(),
        allow_fallback=allow_runtime_fallback,
    )


def _build_postgres_store(
    app: Flask,
    *,
    kind: str,
    default_path: str,
    path_env: str,
    pool: ConnectionPool | None,
    is_production: bool,
) -> BaseStore:
    """Build the PostgreSQL store, falling back to JSON outside production."""
    postgres_url = os.environ.get("POSTGRES_URL", "").strip()
    if not postgres_url and not pool:
        if is_production:
            raise PostgresStoreError(
                "PostgreSQL URL is required in production environment."
            )
        app.logger.error(
            "[store] STORE_BACKEND=postgres but no POSTGRES_URL configured. "
            "Falling back to filesystem for %s store.",
            kind,
        )
        return _make_json_store(
            app, kind=kind, default_path=default_path, path_env=path_env
        )

    try:
        ssl_mode = os.environ.get("POSTGRES_SSL_MODE", "require").strip()
        store = PostgresStore(
            connection_string=postgres_url if pool is None else None,
            kind=kind,
            logger=app.logger,
            ssl_mode=ssl_mode,
            pool=pool,
        )

        if store.health_check():
            app.logger.info("[store] Using PostgreSQL backend for %s store", kind)
            return _wrap_resilient_store(
                app,
                kind=kind,
                store=store,
                default_path=default_path,
                path_env=path_env,
                is_production=is_production,
            )

        if is_production:
            store.close()
            raise PostgresStoreError(
                f"PostgreSQL health check failed for {kind} store in production."
            )

        app.logger.error(
            "[store] PostgreSQL health check failed for %s store. "
            "Falling back to filesystem.",
            kind,
        )
        store.close()
        return _make_json_store(
            app, kind=kind, default_path=default_path, path_env=path_env
        )

    except PostgresStoreError:
        if is_production:
            raise
        app.logger.exception(
            "[store] PostgreSQL backend unavailable for %s store. "
            "Falling back to filesystem.",
            kind,
        )
        return _make_json_store(
            app, kind=kind, default_path=default_path, path_env=path_env
        )


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
    _, is_production = _resolve_environment(app)

    if selected_backend == "postgres":
        return _build_postgres_store(
            app,
            kind=kind,
            default_path=default_path,
            path_env=path_env,
            pool=pool,
            is_production=is_production,
        )

    if selected_backend == "redis":
        if is_production:
            raise PostgresStoreError(
                "Redis backend is deprecated and not supported in production."
            )
        app.logger.warning(
            "[store] Redis backend is deprecated. Consider migrating to PostgreSQL. "
            "Using filesystem fallback for %s store.",
            kind,
        )
        return _make_json_store(
            app, kind=kind, default_path=default_path, path_env=path_env
        )

    if is_production:
        raise PostgresStoreError(
            "Filesystem fallback is disabled in production. "
            "PostgreSQL store must be configured."
        )
    return _make_json_store(
        app, kind=kind, default_path=default_path, path_env=path_env
    )


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


def _is_pytest_runtime() -> bool:
    """Return True when the current process is a pytest run."""
    return "pytest" in sys.modules or any("pytest" in arg for arg in sys.argv)


def _configure_security(app: Flask) -> tuple[bool, bool]:
    """Apply debug, cookie, secret and password guards.

    Returns ``(is_testing, is_production)`` so callers can reuse the resolved
    environment without recomputing the same conditions.
    """
    # A stray FLASK_DEBUG=1 must never relax production guards when the app is
    # actually served by gunicorn/uwsgi. Those guards include Secure session
    # cookies, HSTS, password/secret enforcement and the store failover policy.
    if _running_under_wsgi_server():
        if app.debug:
            app.logger.warning(
                "[security] FLASK_DEBUG is set while running under a WSGI server; "
                "forcing app.debug=False so production guards stay enabled"
            )
        app.debug = False

    app.config["SESSION_COOKIE_SECURE"] = not app.debug and not app.testing
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=30)

    flask_secret = os.environ.get("FLASK_SECRET_KEY")
    insecure_keys = {
        "dev-local-only",
        "change-me",
        "default",
        "secret",
        "password",
        "key",
        "admin",
    }
    is_insecure = not flask_secret or str(flask_secret).strip().lower() in insecure_keys

    if (
        is_insecure
        and not app.debug
        and not app.testing
        and not _is_pytest_runtime()
    ):
        raise RuntimeError(
            "Security Violation: FLASK_SECRET_KEY must be set in production "
            "(secure value required)"
        )
    app.secret_key = flask_secret or "dev-local-only"
    app.config["STATE_DEBUG_TOKEN"] = os.environ.get("STATE_DEBUG_TOKEN", "").strip()

    is_testing, is_production = _resolve_environment(app)

    dashboard_password = os.environ.get("DASHBOARD_PASSWORD", "").strip()
    if not dashboard_password and is_production and not _is_pytest_runtime():
        raise RuntimeError(
            "Security Violation: DASHBOARD_PASSWORD must be set in production"
        )
    app.config["DASHBOARD_PASSWORD"] = dashboard_password
    return is_testing, is_production


def _configure_logging(app: Flask) -> None:
    log_level_raw = os.environ.get("LOG_LEVEL", "info").strip().upper()
    log_level = getattr(logging, log_level_raw, logging.INFO)
    logging.getLogger().setLevel(log_level)
    app.logger.setLevel(log_level)


def _init_extensions(app: Flask, *, is_production: bool) -> None:
    """Initialize CSRF protection and the rate limiter."""
    csrf = CSRFProtect()
    csrf.init_app(app)

    app.config.setdefault("RATELIMIT_ENABLED", not app.testing)
    app.config.setdefault(
        "RATELIMIT_STORAGE_URI",
        os.environ.get("RATELIMIT_STORAGE_URI", "memory://"),
    )
    limiter.init_app(app)

    if is_production and app.config.get("RATELIMIT_STORAGE_URI", "").startswith(
        "memory://"
    ):
        app.logger.warning(
            "[api] RATELIMIT_STORAGE_URI is set to memory:// in production. "
            "Under multi-worker Gunicorn environments, rate limits will not be shared between workers."
        )


def _init_shared_pool(app: Flask) -> ConnectionPool | None:
    """Create the shared PostgreSQL pool when the backend is configured for it."""
    store_backend = os.environ.get("STORE_BACKEND", "postgres").strip().lower()
    if store_backend != "postgres":
        return None

    postgres_url = os.environ.get("POSTGRES_URL", "").strip()
    if not postgres_url:
        return None

    try:
        ssl_mode = os.environ.get("POSTGRES_SSL_MODE", "require").strip()
        shared_pool = ConnectionPool(
            conninfo=postgres_url,
            min_size=1,
            max_size=10,
            timeout=5.0,
            open=True,
            kwargs={
                "sslmode": ssl_mode,
                "connect_timeout": 5,
                "options": "-c statement_timeout=5000",
            },
        )
        app.logger.info("[store] Shared connection pool initialized successfully")

        @atexit.register
        def close_shared_pool() -> None:
            try:
                shared_pool.close()
                logging.getLogger().info(
                    "[store] Shared connection pool closed successfully via atexit"
                )
            except Exception as exc:
                logging.getLogger().warning(
                    "[store] Error closing shared connection pool via atexit (%s)", exc
                )

        return shared_pool
    except Exception:
        app.logger.exception("[store] Failed to initialize shared connection pool")
        return None


def _apply_poll_interval_override(settings_store: BaseStore) -> None:
    """Apply SWITCHBOT_POLL_INTERVAL_SECONDS to settings.json at startup."""
    poll_interval_env = os.environ.get("SWITCHBOT_POLL_INTERVAL_SECONDS")
    if not poll_interval_env:
        return

    try:
        poll_interval_seconds = max(15, int(poll_interval_env))
    except ValueError:
        return

    settings = settings_store.read()
    if settings.get("poll_interval_seconds") != poll_interval_seconds:
        settings["poll_interval_seconds"] = poll_interval_seconds
        settings_store.write(settings)


def _init_history_service(
    app: Flask, settings_store: BaseStore
) -> HistoryService | None:
    """Create HistoryService when a PostgreSQL backend is available."""
    primary_settings_store = getattr(settings_store, "primary", settings_store)
    app.logger.info(f"[history] Settings store type: {type(settings_store)}")
    app.logger.info(
        f"[history] Is PostgresStore: {isinstance(primary_settings_store, PostgresStore)}"
    )

    if not isinstance(primary_settings_store, PostgresStore):
        app.logger.warning(
            "[history] HistoryService disabled: PostgreSQL backend not available"
        )
        return None

    try:
        retention_hours_raw = os.environ.get("HISTORY_RETENTION_HOURS", "24")
        try:
            retention_hours = max(1, int(retention_hours_raw))
        except ValueError:
            retention_hours = 24
        history_service = HistoryService(
            connection_pool=primary_settings_store.pool,
            logger=app.logger,
            retention_hours=retention_hours,
        )
        app.logger.info(
            "[history] HistoryService initialized with PostgreSQL backend (retention=%sh)",
            retention_hours,
        )

        @atexit.register
        def flush_history_buffer() -> None:
            try:
                history_service.flush_pending_records(force=True)
                logging.getLogger().info("[history] History buffer flushed via atexit")
            except Exception as exc:
                logging.getLogger().warning(
                    "[history] Error flushing history buffer via atexit (%s)", exc
                )

        return history_service
    except Exception:
        app.logger.exception("[history] Failed to initialize HistoryService")
        return None


def _register_security_headers(app: Flask) -> None:
    """Register the per-request CSP nonce and HTTP security headers."""

    @app.before_request
    def _generate_csp_nonce() -> None:
        """Issue a fresh CSP nonce for every request.

        A per-request nonce lets ``script-src`` drop ``'unsafe-inline'`` while
        still allowing the small amount of first-party inline bootstrapping
        code in the templates.
        """
        g.csp_nonce = secrets.token_urlsafe(16)

    @app.context_processor
    def _inject_csp_nonce() -> dict[str, str]:
        return {"csp_nonce": getattr(g, "csp_nonce", "")}

    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        nonce = getattr(g, "csp_nonce", "")
        script_src = "'self'"
        if nonce:
            script_src += f" 'nonce-{nonce}'"
        # style-src keeps 'unsafe-inline': templates rely on style="" attributes
        # and adding a nonce would make browsers ignore 'unsafe-inline'.
        response.headers["Content-Security-Policy"] = (
            f"default-src 'self'; script-src {script_src}; "
            "style-src 'self' 'unsafe-inline'; font-src 'self'; "
            "img-src 'self' data:; connect-src 'self'; "
            "object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
        )
        if not app.debug and not app.testing:
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains"
            )
        return response


def _start_initial_poll(
    app: Flask, automation_service: AutomationService, *, is_testing: bool
) -> None:
    """Run the first meter poll synchronously in tests, asynchronously otherwise."""
    if is_testing or _is_pytest_runtime():
        try:
            automation_service.poll_meter()
        except Exception as exc:  # pragma: no cover
            app.logger.warning("Initial meter poll failed (sync testing): %s", exc)
        return

    def run_initial_poll_async() -> None:
        with app.app_context():
            try:
                automation_service.poll_meter()
            except Exception as exc:  # pragma: no cover
                app.logger.warning("Initial meter poll failed (async): %s", exc)

    threading.Thread(
        target=run_initial_poll_async, name="initial_meter_poll", daemon=True
    ).start()


def _configure_scheduler(
    app: Flask,
    scheduler_service: SchedulerService,
    history_service: HistoryService | None,
) -> None:
    """Start APScheduler unless disabled or running in the Flask reloader parent."""
    scheduler_enabled = os.environ.get("SCHEDULER_ENABLED", "true").strip().lower()
    if scheduler_enabled != "true":
        app.logger.info("[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false")
        return

    is_flask_dev_reloader_parent = (
        os.environ.get("FLASK_DEBUG", "").strip().lower() not in ("", "0", "false")
        and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
        and not os.environ.get("SERVER_SOFTWARE")
    )
    if is_flask_dev_reloader_parent:
        app.logger.info(
            "[scheduler] Skipping start in Flask development reloader parent process"
        )
        return

    scheduler_service.start()
    app.logger.info("[scheduler] APScheduler enabled and started")

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


def _configure_proxy_fix(app: Flask) -> None:
    """Apply Werkzeug ProxyFix behind reverse proxies if configured."""
    proxy_fix_for = os.environ.get("PROXY_FIX_FOR", "").strip()
    if not proxy_fix_for:
        return

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
    app.logger.info(
        "[security] ProxyFix middleware applied (trusted proxies: %d)", num_proxies
    )


def create_app() -> Flask:
    app = Flask(__name__)
    is_testing, is_production = _configure_security(app)
    _configure_logging(app)
    _init_extensions(app, is_production=is_production)

    # Initialize shared connection pool for PostgreSQL if selected
    shared_pool = _init_shared_pool(app)

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

    _apply_poll_interval_override(settings_store)

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
    history_service = _init_history_service(app, settings_store)

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

    _register_security_headers(app)

    _mark_temperature_stale(app, state_store, reason="app_start")
    _start_initial_poll(app, automation_service, is_testing=is_testing)
    _configure_scheduler(app, scheduler_service, history_service)
    _configure_proxy_fix(app)

    return app
