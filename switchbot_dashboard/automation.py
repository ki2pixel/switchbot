from __future__ import annotations

import contextlib
import copy
import datetime as dt
import logging
import threading
import time
from typing import Any, Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from flask import has_request_context, request

from .aircon import AIRCON_MODE_BY_ACTION, AIRCON_SCENE_LABELS, extract_aircon_scenes
from .config_store import BaseStore
from .switchbot_api import SwitchBotApiError, SwitchBotClient
from .utils import _safe_int, _utc_now_iso


class LockLostError(RuntimeError):
    """Raised when the automation lock has been acquired by another worker/process."""
    pass


def _parse_hhmm(value: str) -> dt.time:
    parts = value.strip().split(":")
    if len(parts) != 2:
        raise ValueError("Invalid HH:MM")

    hour = int(parts[0])
    minute = int(parts[1])
    return dt.time(hour=hour, minute=minute)


def _is_time_in_window(window: dict[str, Any], now: dt.datetime) -> bool:
    days = window.get("days")
    if not isinstance(days, list):
        return False

    start_raw = window.get("start")
    end_raw = window.get("end")
    if not isinstance(start_raw, str) or not isinstance(end_raw, str):
        return False

    try:
        start = _parse_hhmm(start_raw)
        end = _parse_hhmm(end_raw)
    except ValueError:
        return False
        
    now_time = now.time().replace(tzinfo=None)
    
    if start <= end:
        return now.weekday() in days and start <= now_time <= end
        
    if now.weekday() in days and now_time >= start:
        return True
        
    previous_weekday = (now - dt.timedelta(days=1)).weekday()
    return previous_weekday in days and now_time <= end


def _is_now_in_windows(time_windows: list[dict[str, Any]], now: dt.datetime) -> bool:
    return any(_is_time_in_window(w, now) for w in time_windows)



def _ensure_utc(value: dt.datetime) -> dt.datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=dt.timezone.utc)
    return value.astimezone(dt.timezone.utc)


def _is_virtual_aircon_device(aircon_device_id: str) -> bool:
    """Return True for virtual infrared remotes that reject status queries."""
    return len(aircon_device_id) > 12 and aircon_device_id.count("-") >= 2


def _is_assumed_fan_mode(state: dict[str, Any]) -> bool:
    """Return True when the assumed state already represents fan mode."""
    assumed_power = state.get("assumed_aircon_power", "")
    assumed_mode = state.get("assumed_aircon_mode")
    last_action = state.get("last_action", "")
    return assumed_power == "on" and (
        assumed_mode == 4 or "fan" in str(last_action).lower()
    )


def _build_aircon_status_updates(body: dict[str, Any]) -> dict[str, Any]:
    """Map a SwitchBot aircon status body to state-store updates."""
    power = body.get("power")
    mode = body.get("mode")
    temperature = body.get("temperature")
    fan_speed = body.get("fanSpeed")

    updates: dict[str, Any] = {"last_aircon_poll_at": _utc_now_iso()}
    if power is not None:
        updates["assumed_aircon_power"] = power
    if mode is not None:
        updates["assumed_aircon_mode"] = mode
    if (
        power is not None
        and mode is not None
        and temperature is not None
        and fan_speed is not None
    ):
        updates["assumed_aircon_parameter"] = (
            f"{temperature},{mode},{fan_speed},{power}"
        )
    return updates


logger = logging.getLogger(__name__)
OFF_REPEAT_STATE_KEY = "pending_off_repeat"
DEFAULT_TIMEZONE = "Europe/Paris"


def _format_details(details: dict[str, Any]) -> str:
    if not details:
        return ""
    serialized = []
    for key in sorted(details):
        value = details[key]
        serialized.append(f"{key}={value!r}")
    return " | ".join(serialized)


def _summarize_time_windows(time_windows: list[dict[str, Any]]) -> str:
    if not time_windows:
        return "none"
    segments: list[str] = []
    for window in time_windows:
        days = window.get("days")
        if isinstance(days, list):
            day_tokens = ",".join(str(day) for day in days)
        else:
            day_tokens = "?"
        start = window.get("start", "?")
        end = window.get("end", "?")
        segments.append(f"[{day_tokens}] {start}-{end}")
    return "; ".join(segments)


class CachedStoreWrapper:
    """Thread-local proxy store that caches reads during one execution context.

    The cache is strictly per-thread: the scheduler thread and HTTP worker
    threads must never observe or clear each other's cached snapshot. Sharing a
    single ``dict`` here corrupted state under concurrent ticks (AUD-CONC-01).
    """

    def __init__(self, store: BaseStore) -> None:
        self._store = store
        self._local = threading.local()

    def clear_cache(self) -> None:
        self._local.cache = None

    def read(self) -> dict[str, Any]:
        cache = getattr(self._local, "cache", None)
        if cache is None:
            cache = self._store.read()
            self._local.cache = cache
        return copy.deepcopy(cache)

    def write(self, data: dict[str, Any]) -> None:
        self._local.cache = copy.deepcopy(data)
        self._store.write(data)

    @contextlib.contextmanager
    def transaction(self) -> Any:
        self.clear_cache()
        try:
            if hasattr(self._store, "transaction"):
                with self._store.transaction():
                    yield
            else:
                yield
        finally:
            self.clear_cache()


class AutomationService:
    """Core automation service for SwitchBot device control.

    Manages temperature monitoring, scene execution, and device automation
    with timezone-aware scheduling.

    Attributes:
        _settings_store: Persistent storage for configuration settings
        _state_store: Persistent storage for runtime state
        _client: SwitchBot API client with quota tracking
        _logger: Logger instance for structured logging

    Example:
        >>> service = AutomationService(settings_store, state_store, client)
        >>> service.run_once()  # Execute one automation cycle
    """
    def __init__(
        self,
        settings_store: BaseStore,
        state_store: BaseStore,
        switchbot_client: SwitchBotClient,
        *,
        history_service: Optional[Any] = None,  # HistoryService to avoid circular import
        logger: logging.Logger | None = None,
    ) -> None:
        self._settings_store = CachedStoreWrapper(settings_store)
        self._state_store = CachedStoreWrapper(state_store)
        self._client = switchbot_client
        self._history_service = history_service
        self._logger = logger or logging.getLogger(__name__)
        self._cached_timezone_key = None
        self._cached_timezone_value = None
        self._tick_durations: list[float] = []
        self._local = threading.local()

        # Share the wrapped state store with the quota tracker to ensure cache coherency (P-04)
        if hasattr(self._client, "_quota_tracker") and self._client._quota_tracker:
            if hasattr(self._client._quota_tracker, "_state_store"):
                self._client._quota_tracker._state_store = self._state_store

    def _update_state(self, **updates: Any) -> None:
        with self._state_store.transaction():
            state = self._state_store.read()
            if getattr(self._local, "current_lock_token", None) is not None:
                db_token = state.get("automation_lock_token")
                if db_token != self._local.current_lock_token:
                    raise LockLostError(
                        f"State update rejected: lock token mismatch (local={self._local.current_lock_token}, db={db_token})"
                    )
            state.update(updates)
            self._state_store.write(state)

    def apply_state_updates(self, **updates: Any) -> None:
        """Fencing-aware state update used by manual HTTP actions.

        The caller must hold the automation lock; this method rejects the
        write if another worker stole it in the meantime.
        """
        self._update_state(**updates)

    def _log(self, level: int, message: str, **details: Any) -> None:
        payload = "[automation] " + message
        formatted_details = _format_details(details)
        if formatted_details:
            payload = f"{payload} | {formatted_details}"
        self._logger.log(level, payload)

    def _debug(self, message: str, **details: Any) -> None:
        self._log(logging.DEBUG, message, **details)

    def _info(self, message: str, **details: Any) -> None:
        self._log(logging.INFO, message, **details)

    def _warning(self, message: str, **details: Any) -> None:
        self._log(logging.WARNING, message, **details)

    def _error(self, message: str, **details: Any) -> None:
        self._log(logging.ERROR, message, **details)

    def _detect_trigger_source(self) -> str:
        if has_request_context():
            endpoint = request.endpoint or "http_request"
            return f"http:{endpoint}"
        return "scheduler"

    def _get_timezone(self, settings: dict[str, Any], *, trigger: str) -> tuple[dt.tzinfo, str]:
        raw_timezone = settings.get("timezone")
        timezone_name = str(raw_timezone or "").strip() or DEFAULT_TIMEZONE
        cache_key = timezone_name
        if (
            self._cached_timezone_key == cache_key
            and self._cached_timezone_value is not None
        ):
            return self._cached_timezone_value

        try:
            timezone_obj = ZoneInfo(timezone_name)
            resolved_name = timezone_name
        except ZoneInfoNotFoundError:
            self._warning(
                "Invalid timezone; falling back to UTC",
                trigger=trigger,
                timezone=timezone_name,
            )
            timezone_obj = dt.timezone.utc
            resolved_name = "UTC"

        self._cached_timezone_key = cache_key
        self._cached_timezone_value = (timezone_obj, resolved_name)
        return timezone_obj, resolved_name

    def _log_quota_snapshot(self, context: str) -> None:
        state = self._state_store.read()
        self._debug(
            "Quota snapshot updated",
            context=context,
            api_requests_total=state.get("api_requests_total"),
            api_requests_remaining=state.get("api_requests_remaining"),
            api_requests_limit=state.get("api_requests_limit"),
            api_quota_day=state.get("api_quota_day"),
        )

    def _log_tick_completion(self, trigger: str, outcome: str, **details: Any) -> None:
        self._debug("Automation tick finished", trigger=trigger, outcome=outcome, **details)

    def poll_meter(self) -> dict[str, Any] | None:
        settings = self._settings_store.read()
        meter_id = str(settings.get("meter_device_id", "")).strip()
        trigger = self._detect_trigger_source()
        if not meter_id:
            self._warning(
                "Meter polling skipped: missing meter_device_id",
                trigger=trigger,
            )
            self._update_state(last_error="Missing meter_device_id", last_read_at=_utc_now_iso())
            return None

        self._debug("Polling SwitchBot meter", trigger=trigger, meter_device_id=meter_id)

        try:
            response = self._client.get_device_status(meter_id)
        except SwitchBotApiError as exc:
            self._update_state(
                last_error=str(exc),
                last_read_at=_utc_now_iso(),
                last_temperature_stale=True,
                last_temperature_stale_reason="api_error",
            )
            self._error(
                "Meter polling failed",
                trigger=trigger,
                meter_device_id=meter_id,
                error=str(exc),
            )
            self._log_quota_snapshot(context="meter_status_error")
            return None

        self._log_quota_snapshot(context="meter_status")

        body = response.get("body", {})
        temperature = body.get("temperature")
        humidity = body.get("humidity")

        self._update_state(
            last_temperature=temperature,
            last_humidity=humidity,
            last_read_at=_utc_now_iso(),
            last_error=None,
            last_temperature_stale=False,
            last_temperature_stale_reason=None,
        )
        self._debug(
            "Meter reading stored",
            trigger=trigger,
            temperature=temperature,
            humidity=humidity,
        )
        return {"temperature": temperature, "humidity": humidity}

    def _build_cached_aircon_status(
        self, state: dict[str, Any], *, trigger: str
    ) -> dict[str, Any]:
        """Reconstruct an aircon status payload from the persisted assumed state."""
        power = state.get("assumed_aircon_power")
        mode = state.get("assumed_aircon_mode")
        temperature: float | int | None = None
        fan_speed: int | None = None

        param = state.get("assumed_aircon_parameter")
        if param and isinstance(param, str):
            parts = param.split(",")
            if len(parts) >= 4:
                try:
                    temperature = float(parts[0]) if "." in parts[0] else int(parts[0])
                    if mode is None:
                        mode = int(parts[1])
                    fan_speed = int(parts[2])
                except (ValueError, IndexError) as exc:
                    self._debug(
                        "Failed to parse cached aircon parameter",
                        trigger=trigger,
                        parameter=param,
                        error=str(exc),
                    )

        return {
            "power": power,
            "mode": mode,
            "temperature": temperature,
            "fanSpeed": fan_speed,
        }

    def _aircon_poll_cooldown_active(
        self,
        *,
        now: dt.datetime,
        state: dict[str, Any],
        cooldown_minutes: int,
        trigger: str,
    ) -> bool:
        """Return True when the last successful poll is still within the cooldown."""
        last_aircon_poll_at = state.get("last_aircon_poll_at")
        if not last_aircon_poll_at or state.get("assumed_aircon_power") is None:
            return False

        try:
            last_poll = _ensure_utc(
                dt.datetime.fromisoformat(
                    str(last_aircon_poll_at).replace("Z", "+00:00")
                )
            )
        except ValueError as exc:
            self._debug(
                "Failed to parse last_aircon_poll_at",
                trigger=trigger,
                value=last_aircon_poll_at,
                error=str(exc),
            )
            return False

        return now - last_poll < dt.timedelta(minutes=cooldown_minutes)

    def _sync_aircon_status(
        self, updates: dict[str, Any], *, trigger: str
    ) -> None:
        """Persist only the status fields that differ from the assumed state."""
        current_state = self._state_store.read()
        changes = {
            key: value
            for key, value in updates.items()
            if current_state.get(key) != value
        }
        if not changes:
            return
        self._update_state(**changes)
        self._info(
            "Aircon state synchronized from API status",
            trigger=trigger,
            **changes,
        )

    def poll_aircon_status(self, aircon_device_id: str, *, force: bool = False) -> dict[str, Any] | None:
        """Poll the real-time status of the virtual Air Conditioner from SwitchBot API.

        Updates the state store with the actual physical state of the AC if any changes
        are detected, to avoid incorrect idempotency bypasses. Supports temporal cooldown caching.

        Args:
            aircon_device_id: The SwitchBot device ID of the Air Conditioner.
            force: If True, bypass the polling cooldown and query the API.

        Returns:
            The parsed status dictionary, or None if the request failed.
        """
        aircon_device_id = aircon_device_id.strip()
        trigger = self._detect_trigger_source()
        if not aircon_device_id:
            self._warning(
                "Aircon polling skipped: missing aircon_device_id",
                trigger=trigger,
            )
            return None

        now = dt.datetime.now(dt.timezone.utc)
        settings = self._settings_store.read()
        poll_cooldown_minutes = _safe_int(
            settings.get("aircon_poll_cooldown_minutes"), default=15
        )
        state = self._state_store.read()

        # Virtual infrared devices (IDs with length > 12 and at least 2 hyphens)
        # do not support status queries and would only waste quota.
        if _is_virtual_aircon_device(aircon_device_id):
            self._debug(
                "Aircon polling bypassed (virtual infrared remote doesn't support status queries)",
                trigger=trigger,
                aircon_device_id=aircon_device_id,
            )
            return self._build_cached_aircon_status(state, trigger=trigger)

        if not force and self._aircon_poll_cooldown_active(
            now=now,
            state=state,
            cooldown_minutes=poll_cooldown_minutes,
            trigger=trigger,
        ):
            self._debug(
                "Aircon polling bypassed (cooldown active)",
                trigger=trigger,
                aircon_device_id=aircon_device_id,
                last_aircon_poll_at=state.get("last_aircon_poll_at"),
            )
            return self._build_cached_aircon_status(state, trigger=trigger)

        self._debug(
            "Polling SwitchBot aircon status",
            trigger=trigger,
            aircon_device_id=aircon_device_id,
            force=force,
        )

        try:
            response = self._client.get_device_status(aircon_device_id)
        except SwitchBotApiError as exc:
            self._error(
                "Aircon polling failed",
                trigger=trigger,
                aircon_device_id=aircon_device_id,
                error=str(exc),
            )
            self._log_quota_snapshot(context="aircon_status_error")
            # Update last_aircon_poll_at on failure to avoid continuous poll loops on subsequent ticks
            self._update_state(last_aircon_poll_at=_utc_now_iso())
            return None

        self._log_quota_snapshot(context="aircon_status")

        body = response.get("body", {})
        self._sync_aircon_status(
            _build_aircon_status_updates(body), trigger=trigger
        )
        return {
            "power": body.get("power"),
            "mode": body.get("mode"),
            "temperature": body.get("temperature"),
            "fanSpeed": body.get("fanSpeed"),
        }

    def _cooldown_active(self, now: dt.datetime) -> bool:
        state = self._state_store.read()
        settings = self._settings_store.read()
        
        assumed_power = state.get("assumed_aircon_power", "")
        
        if assumed_power == "on":
            cooldown_seconds = _safe_int(settings.get("action_on_cooldown_seconds"), default=0)
            cooldown_type = "ON"
        else:
            cooldown_seconds = _safe_int(settings.get("action_off_cooldown_seconds"), default=0)
            cooldown_type = "OFF"
        
        default_cooldown = _safe_int(settings.get("command_cooldown_seconds"), default=0)
        if cooldown_seconds <= 0:
            if default_cooldown <= 0:
                return False
            cooldown_seconds = default_cooldown
            cooldown_type = "default"

        last_action_at = state.get("last_action_at")
        if not isinstance(last_action_at, str) or not last_action_at:
            return False

        try:
            last = dt.datetime.fromisoformat(last_action_at.replace("Z", "+00:00"))
        except ValueError:
            return False

        if last.tzinfo is None:
            last = last.replace(tzinfo=dt.timezone.utc)

        now_utc = now.astimezone(dt.timezone.utc)
        elapsed = now_utc - last
        remaining = dt.timedelta(seconds=cooldown_seconds) - elapsed
        
        if remaining > dt.timedelta(0):
            remaining_minutes = int(remaining.total_seconds() / 60)
            remaining_seconds = int(remaining.total_seconds() % 60)
            self._debug(
                f"Cooldown active ({cooldown_type} action)",
                remaining_time=f"{remaining_minutes}m{remaining_seconds}s",
                cooldown_seconds=cooldown_seconds,
            )
            return True
        
        return False

    def _send_aircon_off(self, aircon_device_id: str, *, trigger: str, reason: str, force: bool = False) -> bool:
        aircon_device_id = aircon_device_id.strip()
        if not aircon_device_id:
            self._warning("Cannot send turnOff: missing aircon_device_id", trigger=trigger, reason=reason)
            self._update_state(last_error="Missing aircon_device_id for turnOff command")
            return False

        state = self._state_store.read()
        if not force and state.get("assumed_aircon_power") == "off":
            self._debug("Skipping turnOff: already assumed off", trigger=trigger, reason=reason)
            return False

        self._debug("Requesting aircon turnOff", trigger=trigger, aircon_device_id=aircon_device_id, reason=reason)
        self._client.send_command(aircon_device_id, command="turnOff", parameter="default")
        self._log_quota_snapshot(context="turn_off")
        self._update_state(
            assumed_aircon_power="off",
            last_action="turnOff",
            last_action_at=_utc_now_iso(),
            last_error=None,
        )
        return True

    def _send_aircon_setall(
        self,
        aircon_device_id: str,
        temperature: float,
        mode: int,
        fan_speed: int,
        power_state: str,
        *,
        trigger: str,
        reason: str,
    ) -> None:
        aircon_device_id = aircon_device_id.strip()
        if not aircon_device_id:
            self._warning("Cannot send setAll: missing aircon_device_id", trigger=trigger, reason=reason)
            self._update_state(last_error="Missing aircon_device_id for setAll command")
            return

        state = self._state_store.read()
        parameter = f"{temperature},{mode},{fan_speed},{power_state}"
        if (
            state.get("assumed_aircon_power") == power_state
            and state.get("assumed_aircon_mode") == mode
            and state.get("assumed_aircon_parameter") == parameter
        ):
            self._debug(
                "Skipping setAll: desired state already assumed",
                trigger=trigger,
                aircon_device_id=aircon_device_id,
                reason=reason,
                parameter=parameter,
            )
            return

        self._debug(
            "Requesting aircon setAll",
            trigger=trigger,
            aircon_device_id=aircon_device_id,
            reason=reason,
            temperature=temperature,
            mode=mode,
            fan_speed=fan_speed,
            power_state=power_state,
        )
        self._client.send_command(
            aircon_device_id,
            command="setAll",
            parameter=parameter,
            command_type="command",
        )
        self._log_quota_snapshot(context="set_all")
        self._update_state(
            assumed_aircon_power=power_state,
            assumed_aircon_mode=mode,
            assumed_aircon_parameter=parameter,
            last_action=f"setAll({parameter})",
            last_action_at=_utc_now_iso(),
            last_error=None,
        )

    def _clear_off_repeat_task(self) -> None:
        with self._state_store.transaction():
            state = self._state_store.read()
            if state.pop(OFF_REPEAT_STATE_KEY, None) is not None:
                self._state_store.write(state)
                self._debug("Cleared pending off repeat task")

    def _has_pending_off_repeat(self) -> bool:
        state = self._state_store.read()
        task = state.get(OFF_REPEAT_STATE_KEY)
        if not isinstance(task, dict):
            return False
        remaining = _safe_int(task.get("remaining"), default=0)
        return remaining > 0

    def _schedule_off_repeat_task(self, now: dt.datetime, *, state_reason: str) -> None:
        settings = self._settings_store.read()
        repeat_count = _safe_int(settings.get("off_repeat_count"), default=1)
        if repeat_count <= 1:
            self._clear_off_repeat_task()
            return

        interval_seconds = _safe_int(settings.get("off_repeat_interval_seconds"), default=10)
        if interval_seconds < 1:
            interval_seconds = 1

        remaining = repeat_count - 1
        next_run_at = (_ensure_utc(now) + dt.timedelta(seconds=interval_seconds)).isoformat()

        with self._state_store.transaction():
            state = self._state_store.read()
            state[OFF_REPEAT_STATE_KEY] = {
                "remaining": remaining,
                "interval_seconds": interval_seconds,
                "next_run_at": next_run_at,
                "state_reason": state_reason,
            }
            self._state_store.write(state)
        self._debug(
            "Scheduled repeated off action",
            pending_repeats=remaining,
            interval_seconds=interval_seconds,
            state_reason=state_reason,
        )

    def _load_due_off_repeat(
        self, now: dt.datetime
    ) -> tuple[int, str, int] | None:
        """Return the due off-repeat schedule, clearing invalid or exhausted tasks."""
        state = self._state_store.read()
        task = state.get(OFF_REPEAT_STATE_KEY)
        if not isinstance(task, dict):
            return None

        remaining = _safe_int(task.get("remaining"), default=0)
        if remaining <= 0:
            self._clear_off_repeat_task()
            return None

        next_run_raw = task.get("next_run_at")
        if not isinstance(next_run_raw, str):
            self._clear_off_repeat_task()
            return None

        try:
            next_run_at = dt.datetime.fromisoformat(
                next_run_raw.replace("Z", "+00:00")
            )
        except ValueError:
            self._clear_off_repeat_task()
            return None

        if _ensure_utc(now) < _ensure_utc(next_run_at):
            return None

        state_reason = (
            str(task.get("state_reason", "automation_off_repeat")).strip()
            or "automation_off_repeat"
        )
        interval_seconds = max(
            _safe_int(task.get("interval_seconds"), default=10), 1
        )
        return remaining, state_reason, interval_seconds

    def _reschedule_off_repeat(
        self,
        now_utc: dt.datetime,
        *,
        remaining: int,
        interval_seconds: int,
        state_reason: str,
    ) -> str:
        """Persist the next off-repeat run and return its ISO timestamp."""
        next_run_at = (now_utc + dt.timedelta(seconds=interval_seconds)).isoformat()
        with self._state_store.transaction():
            state = self._state_store.read()
            state[OFF_REPEAT_STATE_KEY] = {
                "remaining": remaining,
                "interval_seconds": interval_seconds,
                "next_run_at": next_run_at,
                "state_reason": state_reason,
            }
            self._state_store.write(state)
        return next_run_at

    def _process_off_repeat_task(
        self,
        now: dt.datetime,
        *,
        trigger: str,
        scenes: dict[str, str],
        aircon_device_id: str,
    ) -> None:
        schedule = self._load_due_off_repeat(now)
        if schedule is None:
            return

        remaining, state_reason, interval_seconds = schedule
        self._debug(
            "Executing scheduled off repeat",
            trigger=trigger,
            state_reason=state_reason,
            remaining_before=remaining,
        )

        settings = self._settings_store.read()
        time_windows = settings.get("time_windows", [])
        if not isinstance(time_windows, list):
            time_windows = []
        in_window = _is_now_in_windows(time_windows, now)

        success = self._perform_off_action(
            trigger=trigger,
            scenes=scenes,
            aircon_device_id=aircon_device_id,
            state_reason=state_reason,
            force_direct=True,
            inside_window=in_window,
        )

        if not success:
            self._warning(
                "Off repeat action failed; clearing schedule",
                trigger=trigger,
                state_reason=state_reason,
            )
            self._clear_off_repeat_task()
            return

        remaining -= 1
        if remaining <= 0:
            self._clear_off_repeat_task()
            return

        next_run_at = self._reschedule_off_repeat(
            _ensure_utc(now),
            remaining=remaining,
            interval_seconds=interval_seconds,
            state_reason=state_reason,
        )
        self._debug(
            "Off repeat rescheduled",
            trigger=trigger,
            remaining=remaining,
            next_run_at=next_run_at,
        )

    def _send_direct_fan_mode(
        self,
        settings: dict[str, Any],
        *,
        aircon_device_id: str,
        trigger: str,
        state_reason: str,
    ) -> bool:
        """Send a direct setAll in fan mode when no scene is configured."""
        mode = str(settings.get("mode", "winter")).strip().lower()
        profile = settings.get(mode, {})
        if not isinstance(profile, dict):
            profile = {}
        target_temp = float(profile.get("target_temp", 22.0) or 22.0)
        fan_speed = _safe_int(profile.get("fan_speed"), default=3)

        try:
            self._send_aircon_setall(
                aircon_device_id,
                temperature=target_temp,
                mode=4,
                fan_speed=fan_speed,
                power_state="on",
                trigger=trigger,
                reason=state_reason,
            )
            return True
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
            self._error(
                "SwitchBot API error during direct fan mode fallback",
                trigger=trigger,
                error=str(exc),
                state_reason=state_reason,
            )
            return False

    def _try_fan_mode_action(
        self,
        settings: dict[str, Any],
        *,
        trigger: str,
        scenes: dict[str, str],
        aircon_device_id: str,
        state_reason: str,
        force_direct: bool,
    ) -> bool | None:
        """Run the fan-mode branch; return None when the off branch must run."""
        state = self._state_store.read()
        if not force_direct and _is_assumed_fan_mode(state):
            self._debug(
                "Skipping off/fan action: already assumed in fan mode",
                trigger=trigger,
                state_reason=state_reason,
            )
            return False

        handled = self._trigger_aircon_action(
            action_key="fan",
            state_reason=state_reason,
            assumed_power="on",
            trigger=trigger,
            scenes=scenes,
            aircon_device_id=aircon_device_id,
        )
        if handled:
            self._update_state(assumed_aircon_mode=4)
            return True

        if aircon_device_id:
            return self._send_direct_fan_mode(
                settings,
                aircon_device_id=aircon_device_id,
                trigger=trigger,
                state_reason=state_reason,
            )
        return None

    def _perform_off_action(
        self,
        *,
        trigger: str,
        scenes: dict[str, str],
        aircon_device_id: str,
        state_reason: str,
        force_direct: bool = False,
        inside_window: bool = False,
    ) -> bool:
        settings = self._settings_store.read()

        if bool(settings.get("fan_mode_during_window", False)) and inside_window:
            fan_result = self._try_fan_mode_action(
                settings,
                trigger=trigger,
                scenes=scenes,
                aircon_device_id=aircon_device_id,
                state_reason=state_reason,
                force_direct=force_direct,
            )
            if fan_result is not None:
                return fan_result

        if not force_direct:
            state = self._state_store.read()
            if state.get("assumed_aircon_power") == "off":
                self._debug(
                    "Skipping off action: already assumed off",
                    trigger=trigger,
                    state_reason=state_reason,
                )
                return False

        handled = self._trigger_aircon_action(
            action_key="off",
            state_reason=state_reason,
            assumed_power="off",
            trigger=trigger,
            scenes=scenes,
            aircon_device_id=aircon_device_id,
        )
        if handled:
            return True

        if not aircon_device_id:
            return False

        try:
            return self._send_aircon_off(
                aircon_device_id,
                trigger=trigger,
                reason=state_reason,
                force=force_direct,
            )
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
            self._error(
                "SwitchBot API error during direct turnOff",
                trigger=trigger,
                error=str(exc),
                state_reason=state_reason,
            )
            return False

    def _trigger_scene(
        self,
        action_key: str,
        scene_id: str,
        state_reason: str,
        assumed_power: str,
        trigger: str,
        aircon_device_id: str,
    ) -> bool:
        friendly_scene = AIRCON_SCENE_LABELS.get(action_key, action_key)
        if not scene_id:
            if aircon_device_id:
                self._debug(f"No scene override configured for {friendly_scene}, will use direct API commands", trigger=trigger, action_key=action_key)
                return False

            self._update_state(last_error=f"Missing scene for {friendly_scene} in API Direct mode")
            self._warning("Skipping automation: no scene configured in API Direct mode", trigger=trigger, action_key=action_key)
            return False

        self._debug("Using SwitchBot scene", trigger=trigger, action_key=action_key, scene_id=scene_id, state_reason=state_reason)
        try:
            self._client.run_scene(scene_id)
            self._log_quota_snapshot(context=f"scene_{action_key}")
            self._update_state(
                assumed_aircon_power=assumed_power,
                assumed_aircon_mode=AIRCON_MODE_BY_ACTION.get(action_key),
                assumed_aircon_parameter=None,
                last_action=f"scene({scene_id}) ({state_reason})",
                last_action_at=_utc_now_iso(),
                last_error=None,
            )
            return True
        except SwitchBotApiError as exc:
            self._error("Scene execution failed", trigger=trigger, action_key=action_key, scene_id=scene_id, error=str(exc))
            if aircon_device_id:
                self._warning("Falling back to direct command within direct mode", trigger=trigger, action_key=action_key)
            else:
                self._update_state(last_error=str(exc))
            return False

    def _trigger_aircon_action(
        self,
        *,
        action_key: str,
        state_reason: str,
        assumed_power: str,
        trigger: str,
        scenes: dict[str, str],
        aircon_device_id: str = "",
    ) -> bool:
        return self._trigger_scene(
            action_key,
            scenes.get(action_key, "").strip(),
            state_reason,
            assumed_power,
            trigger,
            aircon_device_id.strip(),
        )

    def _acquire_lock(self) -> bool:
        """
        Acquire the concurrency lock in the state store.
        Returns True if the lock was successfully acquired, False otherwise.
        """
        owner_label = "scheduler" if not has_request_context() else f"http:{request.endpoint}"
        
        def _check_and_set() -> bool:
            state = self._state_store.read()
            is_locked = state.get("automation_in_progress", False)
            locked_at_str = state.get("automation_locked_at")
            
            is_expired = False
            if is_locked and locked_at_str:
                try:
                    locked_at = dt.datetime.fromisoformat(locked_at_str)
                    if locked_at.tzinfo is None:
                        locked_at = locked_at.replace(tzinfo=dt.timezone.utc)
                    now_utc = dt.datetime.now(dt.timezone.utc)
                    if now_utc - locked_at > dt.timedelta(minutes=5):
                        is_expired = True
                        self._warning(
                            "Automation lock acquired by expiration (stale lock detected)",
                            locked_at=locked_at_str,
                            locked_by=state.get("automation_lock_owner"),
                            now=now_utc.isoformat(),
                        )
                except Exception as exc:
                    self._warning("Failed to parse automation_locked_at", error=str(exc))
                    is_expired = True
            
            if is_locked and not is_expired:
                return False
                
            lock_token = _safe_int(state.get("automation_lock_token"), default=0) + 1
            state["automation_in_progress"] = True
            state["automation_locked_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
            state["automation_lock_owner"] = owner_label
            state["automation_lock_token"] = lock_token
            self._state_store.write(state)
            self._local.current_lock_token = lock_token
            return True

        if hasattr(self._state_store, "transaction"):
            try:
                with self._state_store.transaction():
                    return _check_and_set()
            except Exception as exc:
                self._error("Failed to acquire lock via transaction", error=str(exc))
                return False
        else:
            return _check_and_set()

    def _release_lock(self) -> None:
        """Release the concurrency lock in the state store."""
        
        def _clear_lock() -> None:
            state = self._state_store.read()
            current_token = getattr(self._local, "current_lock_token", None)
            db_token = state.get("automation_lock_token")
            # Only release if we are still the owner and the token matches (or if it is not locked)
            if not state.get("automation_in_progress") or (db_token == current_token and current_token is not None):
                state["automation_in_progress"] = False
                state["automation_locked_at"] = None
                state["automation_lock_owner"] = None
                self._state_store.write(state)
            else:
                self._warning(
                    "Skipping lock release: token mismatch or not owned",
                    local_token=current_token,
                    db_token=db_token,
                )

        if hasattr(self._state_store, "transaction"):
            try:
                with self._state_store.transaction():
                    _clear_lock()
            except Exception as exc:
                self._error("Failed to release lock via transaction", error=str(exc))
        else:
            _clear_lock()

    def run_once(self) -> None:
        start_time = time.perf_counter()
        self._local.current_lock_token = None
        
        # Clear store caches for this tick (P-04)
        if hasattr(self._settings_store, "clear_cache"):
            self._settings_store.clear_cache()
        if hasattr(self._state_store, "clear_cache"):
            self._state_store.clear_cache()
        
        if not self._acquire_lock():
            self._debug("Skipping automation cycle: lock is held by another process")
            return

        try:
            self._run_once_impl()
        except LockLostError as exc:
            self._warning("Aborted automation tick: lock was lost or stolen", error=str(exc))
        finally:
            try:
                self._release_lock()
            except Exception as exc:
                self._error("Error releasing lock", error=str(exc))
            finally:
                self._local.current_lock_token = None
                if hasattr(self._settings_store, "clear_cache"):
                    self._settings_store.clear_cache()
                if hasattr(self._state_store, "clear_cache"):
                    self._state_store.clear_cache()
                
            duration = time.perf_counter() - start_time
            self._tick_durations.append(duration)
            if len(self._tick_durations) > 10:
                self._tick_durations.pop(0)

    @property
    def average_tick_duration(self) -> float:
        if not self._tick_durations:
            return 0.0
        return sum(self._tick_durations) / len(self._tick_durations)

    def _handle_winter_mode(
        self, current_temp: float, min_temp: float, max_temp: float, hysteresis: float, trigger: str, scenes: dict[str, str], aircon_id: str, target_temp: float, ac_mode: int, fan_speed: int, now: dt.datetime
    ) -> str:
        if current_temp <= (min_temp - hysteresis):
            self._debug("Winter mode: below min threshold", trigger=trigger, threshold=min_temp - hysteresis)
            if aircon_id:
                self.poll_aircon_status(aircon_id, force=True)
            self._clear_off_repeat_task()
            executed = self._trigger_aircon_action(action_key="winter", state_reason="automation_winter_on", assumed_power="on", trigger=trigger, scenes=scenes, aircon_device_id=aircon_id)
            if not executed and aircon_id:
                self._send_aircon_setall(aircon_id, temperature=target_temp, mode=ac_mode, fan_speed=fan_speed, power_state="on", trigger=trigger, reason="automation_winter_on")
            return "winter_on"
        elif current_temp >= (max_temp + hysteresis):
            self._debug("Winter mode: above max threshold", trigger=trigger, threshold=max_temp + hysteresis)
            if aircon_id:
                self.poll_aircon_status(aircon_id, force=True)
            return self._handle_off_action("automation_winter_off", trigger, scenes, aircon_id, now)
        return "no_action"

    def _handle_summer_mode(
        self, current_temp: float, min_temp: float, max_temp: float, hysteresis: float, trigger: str, scenes: dict[str, str], aircon_id: str, target_temp: float, ac_mode: int, fan_speed: int, now: dt.datetime
    ) -> str:
        if current_temp >= (max_temp + hysteresis):
            self._debug("Summer mode: above max threshold", trigger=trigger, threshold=max_temp + hysteresis)
            if aircon_id:
                self.poll_aircon_status(aircon_id, force=True)
            self._clear_off_repeat_task()
            executed = self._trigger_aircon_action(action_key="summer", state_reason="automation_summer_on", assumed_power="on", trigger=trigger, scenes=scenes, aircon_device_id=aircon_id)
            if not executed and aircon_id:
                self._send_aircon_setall(aircon_id, temperature=target_temp, mode=ac_mode, fan_speed=fan_speed, power_state="on", trigger=trigger, reason="automation_summer_on")
            return "summer_on"
        elif current_temp <= (min_temp - hysteresis):
            self._debug("Summer mode: below min threshold", trigger=trigger, threshold=min_temp - hysteresis)
            if aircon_id:
                self.poll_aircon_status(aircon_id, force=True)
            return self._handle_off_action("automation_summer_off", trigger, scenes, aircon_id, now)
        return "no_action"

    def _handle_off_action(self, state_reason: str, trigger: str, scenes: dict[str, str], aircon_id: str, now: dt.datetime) -> str:
        state = self._state_store.read()
        if state.get("assumed_aircon_power") == "off":
            self._debug(f"Skipping {state_reason}: already assumed off", trigger=trigger)
            return "already_off"
        if self._has_pending_off_repeat():
            self._debug(f"Skipping {state_reason}: off repeat already pending", trigger=trigger)
            return "off_repeat_pending"
        turned_off = self._perform_off_action(trigger=trigger, scenes=scenes, aircon_device_id=aircon_id, state_reason=state_reason, inside_window=True)
        if turned_off:
            self._schedule_off_repeat_task(now, state_reason=state_reason)
            return state_reason.replace("automation_", "")
        return "no_action"

    def _resolve_temperature_profile(
        self,
        settings: dict[str, Any],
        current_temp: float,
        trigger: str,
    ) -> tuple[dict[str, Any] | None, str | None]:
        """Validate the active profile and return its normalized values."""
        mode = str(settings.get("mode", "winter")).strip().lower()
        profile = settings.get(mode, {})
        if not isinstance(profile, dict):
            profile = {}

        hysteresis = float(settings.get("hysteresis_celsius", 0.0) or 0.0)

        try:
            min_temp = float(profile.get("min_temp"))
            max_temp = float(profile.get("max_temp"))
            target_temp = float(profile.get("target_temp"))
            ac_mode = _safe_int(profile.get("ac_mode"), default=5)
            fan_speed = _safe_int(profile.get("fan_speed"), default=3)
        except (TypeError, ValueError):
            self._update_state(
                last_error=f"Invalid profile configuration for mode: {mode}"
            )
            self._error(
                "Invalid automation profile configuration",
                trigger=trigger,
                mode=mode,
            )
            return None, "invalid_profile"

        if min_temp > max_temp:
            self._update_state(
                last_error=f"Invalid thresholds: min_temp > max_temp ({mode})"
            )
            self._error(
                "Invalid temperature thresholds",
                trigger=trigger,
                mode=mode,
                min_temp=min_temp,
                max_temp=max_temp,
            )
            return None, "invalid_thresholds"

        self._debug(
            "Temperature evaluation",
            trigger=trigger,
            mode=mode,
            current_temp=current_temp,
            min_temp=min_temp,
            max_temp=max_temp,
            hysteresis=hysteresis,
            target_temp=target_temp,
        )
        return {
            "mode": mode,
            "min_temp": min_temp,
            "max_temp": max_temp,
            "target_temp": target_temp,
            "ac_mode": ac_mode,
            "fan_speed": fan_speed,
            "hysteresis": hysteresis,
        }, None

    def _handle_fan_neutral_zone(
        self,
        settings: dict[str, Any],
        *,
        trigger: str,
        scenes: dict[str, str],
        aircon_id: str,
    ) -> str | None:
        """Start fan mode when the neutral zone would otherwise do nothing."""
        if not bool(settings.get("fan_mode_during_window", False)):
            return None

        state = self._state_store.read()
        if state.get("assumed_aircon_power") != "off":
            return None

        if aircon_id:
            self.poll_aircon_status(aircon_id, force=True)
        self._perform_off_action(
            trigger=trigger,
            scenes=scenes,
            aircon_device_id=aircon_id,
            state_reason="automation_fan_neutral_zone",
            inside_window=True,
        )
        return "fan_neutral_zone"

    def _evaluate_temperature(
        self,
        current_temp: float,
        settings: dict[str, Any],
        trigger: str,
        now: dt.datetime,
        scenes: dict[str, str],
        aircon_id: str,
    ) -> str:
        values, profile_error = self._resolve_temperature_profile(
            settings, current_temp, trigger
        )
        if values is None:
            return profile_error or "invalid_profile"

        if self._cooldown_active(now):
            self._debug("Cooldown active — skipping automation", trigger=trigger)
            return "cooldown"

        try:
            if values["mode"] == "winter":
                result = self._handle_winter_mode(
                    current_temp,
                    values["min_temp"],
                    values["max_temp"],
                    values["hysteresis"],
                    trigger,
                    scenes,
                    aircon_id,
                    values["target_temp"],
                    values["ac_mode"],
                    values["fan_speed"],
                    now,
                )
            elif values["mode"] == "summer":
                result = self._handle_summer_mode(
                    current_temp,
                    values["min_temp"],
                    values["max_temp"],
                    values["hysteresis"],
                    trigger,
                    scenes,
                    aircon_id,
                    values["target_temp"],
                    values["ac_mode"],
                    values["fan_speed"],
                    now,
                )
            else:
                self._update_state(last_error=f"Unknown mode: {values['mode']}")
                self._error(
                    "Unknown automation mode",
                    trigger=trigger,
                    mode=values["mode"],
                )
                return "invalid_mode"

            if result == "no_action":
                neutral = self._handle_fan_neutral_zone(
                    settings,
                    trigger=trigger,
                    scenes=scenes,
                    aircon_id=aircon_id,
                )
                if neutral:
                    return neutral
            return result
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
            self._error(
                "SwitchBot API error during automation",
                trigger=trigger,
                error=str(exc),
            )
            return "api_error"

    def _run_disabled_tick(self, timezone_name: str, *, trigger: str) -> None:
        """Poll the meter and record history when automation is disabled."""
        self._debug("Automation disabled — polling meter only", trigger=trigger)
        self.poll_meter()
        self._record_history_snapshot(timezone_name, trigger=trigger)
        self._log_tick_completion(trigger, outcome="disabled")

    def _run_outside_window_tick(
        self,
        settings: dict[str, Any],
        *,
        now: dt.datetime,
        timezone_name: str,
        trigger: str,
        scenes: dict[str, str],
        aircon_id: str,
    ) -> None:
        """Handle a tick that falls outside the configured time windows."""
        self._debug("Outside configured window — polling meter", trigger=trigger)
        self.poll_meter()
        outcome = "noop"

        if settings.get("turn_off_outside_windows", False):
            state = self._state_store.read()
            if state.get("assumed_aircon_power") == "off":
                self._debug(
                    "Skipping off automation outside window: already assumed off",
                    trigger=trigger,
                )
                outcome = "already_off"
            elif self._cooldown_active(now):
                self._debug(
                    "Cooldown active, skipping off automation outside window",
                    trigger=trigger,
                )
            else:
                if aircon_id:
                    self.poll_aircon_status(aircon_id, force=True)
                handled = self._perform_off_action(
                    trigger=trigger,
                    scenes=scenes,
                    aircon_device_id=aircon_id,
                    state_reason="automation_off_outside_window",
                    inside_window=False,
                )
                if handled:
                    self._schedule_off_repeat_task(
                        now, state_reason="automation_off_outside_window"
                    )
                    outcome = "turned_off_outside_window"
        else:
            outcome = "outside_window"

        self._record_history_snapshot(timezone_name, trigger=trigger)
        self._log_tick_completion(trigger, outcome=outcome)

    def _resolve_meter_temperature(
        self,
        reading: dict[str, Any] | None,
        *,
        timezone_name: str,
        trigger: str,
    ) -> float | None:
        """Return the meter temperature or abort the tick with history/logging."""
        if not reading or reading.get("temperature") is None:
            self._debug(
                "Meter reading unavailable; aborting automation tick",
                trigger=trigger,
            )
            self._record_history_snapshot(timezone_name, trigger=trigger)
            self._log_tick_completion(trigger, outcome="missing_meter")
            return None

        try:
            return float(reading["temperature"])
        except (TypeError, ValueError):
            self._update_state(last_error="Invalid temperature reading")
            self._error(
                "Invalid temperature reading returned by meter",
                trigger=trigger,
                value=reading.get("temperature"),
            )
            self._record_history_snapshot(timezone_name, trigger=trigger)
            self._log_tick_completion(trigger, outcome="invalid_temperature")
            return None

    def _run_once_impl(self) -> None:
        trigger = self._detect_trigger_source()
        self._update_state(last_tick=_utc_now_iso())
        settings = self._settings_store.read()
        timezone_info, timezone_name = self._get_timezone(settings, trigger=trigger)
        now = dt.datetime.now(dt.timezone.utc).astimezone(timezone_info)
        poll_interval = _safe_int(settings.get("poll_interval_seconds"), default=0)
        automation_enabled = bool(settings.get("automation_enabled", False))

        scenes = extract_aircon_scenes(settings)
        aircon_id = str(settings.get("aircon_device_id", "")).strip()

        self._debug(
            "Automation tick started",
            trigger=trigger,
            poll_interval_seconds=poll_interval,
            automation_enabled=automation_enabled,
            timezone=timezone_name,
            now_local=now.isoformat(),
        )

        self._process_off_repeat_task(
            now,
            trigger=trigger,
            scenes=scenes,
            aircon_device_id=aircon_id,
        )

        if not automation_enabled:
            self._run_disabled_tick(timezone_name, trigger=trigger)
            return

        time_windows = settings.get("time_windows", [])
        if not isinstance(time_windows, list):
            time_windows = []

        in_window = _is_now_in_windows(time_windows, now)

        self._debug(
            "Time window evaluation",
            trigger=trigger,
            in_window=in_window,
            time_windows=_summarize_time_windows(time_windows),
            turn_off_outside_windows=bool(settings.get("turn_off_outside_windows", False)),
            timezone=timezone_name,
            now_local=now.isoformat(),
        )

        if not in_window:
            self._run_outside_window_tick(
                settings,
                now=now,
                timezone_name=timezone_name,
                trigger=trigger,
                scenes=scenes,
                aircon_id=aircon_id,
            )
            return

        reading = self.poll_meter()
        if aircon_id:
            self.poll_aircon_status(aircon_id)

        current_temp = self._resolve_meter_temperature(
            reading, timezone_name=timezone_name, trigger=trigger
        )
        if current_temp is None:
            return

        outcome = self._evaluate_temperature(
            current_temp, settings, trigger, now, scenes, aircon_id
        )
        self._log_tick_completion(trigger, outcome=outcome)
        self._record_history_snapshot(timezone_name, trigger=trigger)

    def _record_history_snapshot(self, timezone_name: str, *, trigger: str) -> None:
        """Persist the current state to the history buffer.

        Called on every tick that reached the meter polling stage, including
        ticks where automation is disabled or outside the configured time
        windows, so the charts do not show multi-hour gaps.
        """
        if not self._history_service:
            return
        try:
            current_state = self._state_store.read()
            self._history_service.record_state(current_state, timezone_name)
        except Exception as exc:
            self._warning("Failed to record state in history", trigger=trigger, error=str(exc))
