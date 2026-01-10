from __future__ import annotations

import datetime as dt
import logging
from typing import Any

from flask import has_request_context, request

from .aircon import AIRCON_SCENE_LABELS, extract_aircon_scenes
from .config_store import BaseStore
from .switchbot_api import SwitchBotApiError, SwitchBotClient


def _parse_hhmm(value: str) -> dt.time:
    parts = value.strip().split(":")
    if len(parts) != 2:
        raise ValueError("Invalid HH:MM")

    hour = int(parts[0])
    minute = int(parts[1])
    return dt.time(hour=hour, minute=minute)


def _is_now_in_windows(time_windows: list[dict[str, Any]], now: dt.datetime) -> bool:
    for window in time_windows:
        days = window.get("days")
        if not isinstance(days, list):
            continue

        start_raw = window.get("start")
        end_raw = window.get("end")
        if not isinstance(start_raw, str) or not isinstance(end_raw, str):
            continue

        try:
            start = _parse_hhmm(start_raw)
            end = _parse_hhmm(end_raw)
        except ValueError:
            continue
        now_time = now.time()

        if start <= end:
            if now.weekday() in days and start <= now_time <= end:
                return True
        else:
            if now.weekday() in days and now_time >= start:
                return True

            previous_weekday = (now - dt.timedelta(days=1)).weekday()
            if previous_weekday in days and now_time <= end:
                return True

    return False


def _utc_now_iso() -> str:
    return dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).isoformat()


logger = logging.getLogger(__name__)


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


class AutomationService:
    def __init__(
        self,
        settings_store: BaseStore,
        state_store: BaseStore,
        switchbot_client: SwitchBotClient,
        *,
        logger: logging.Logger | None = None,
    ) -> None:
        self._settings_store = settings_store
        self._state_store = state_store
        self._client = switchbot_client
        self._logger = logger or logging.getLogger(__name__)

    def _update_state(self, **updates: Any) -> None:
        state = self._state_store.read()
        state.update(updates)
        self._state_store.write(state)

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

    def _cooldown_active(self, now: dt.datetime) -> bool:
        state = self._state_store.read()
        cooldown_seconds = int(self._settings_store.read().get("command_cooldown_seconds", 0) or 0)
        if cooldown_seconds <= 0:
            return False

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
        return (now_utc - last) < dt.timedelta(seconds=cooldown_seconds)

    def _send_aircon_off(self, aircon_device_id: str, *, trigger: str, reason: str) -> None:
        aircon_device_id = aircon_device_id.strip()
        if not aircon_device_id:
            self._warning("Cannot send turnOff: missing aircon_device_id", trigger=trigger, reason=reason)
            self._update_state(last_error="Missing aircon_device_id for turnOff command")
            return

        state = self._state_store.read()
        if state.get("assumed_aircon_power") == "off":
            self._debug("Skipping turnOff: already assumed off", trigger=trigger, reason=reason)
            return

        self._debug("Requesting aircon turnOff", trigger=trigger, aircon_device_id=aircon_device_id, reason=reason)
        self._client.send_command(aircon_device_id, command="turnOff", parameter="default")
        self._log_quota_snapshot(context="turn_off")
        self._update_state(
            assumed_aircon_power="off",
            last_action="turnOff",
            last_action_at=_utc_now_iso(),
            last_error=None,
        )

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

    def _run_aircon_scene(
        self,
        scene_id: str,
        *,
        scene_key: str,
        state_reason: str,
        assumed_power: str,
        trigger: str,
    ) -> bool:
        friendly = AIRCON_SCENE_LABELS.get(scene_key, scene_key)
        scene_id = str(scene_id or "").strip()
        if not scene_id:
            self._update_state(last_error=f"Missing scene id for {friendly}")
            self._warning("Skipping automation scene: not configured", trigger=trigger, scene_key=scene_key)
            return False

        self._debug(
            "Requesting aircon scene",
            trigger=trigger,
            scene_key=scene_key,
            scene_id=scene_id,
            state_reason=state_reason,
        )
        try:
            self._client.run_scene(scene_id)
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
            self._error(
                "Scene execution failed",
                trigger=trigger,
                scene_key=scene_key,
                scene_id=scene_id,
                error=str(exc),
            )
            return False

        self._log_quota_snapshot(context=f"scene_{scene_key}")
        self._update_state(
            assumed_aircon_power=assumed_power,
            assumed_aircon_mode=None,
            assumed_aircon_parameter=None,
            last_action=f"scene({scene_id}) ({state_reason})",
            last_action_at=_utc_now_iso(),
            last_error=None,
        )
        return True

    def run_once(self) -> None:
        trigger = self._detect_trigger_source()
        now = dt.datetime.now()
        self._update_state(last_tick=_utc_now_iso())
        settings = self._settings_store.read()
        poll_interval = int(settings.get("poll_interval_seconds", 0) or 0)
        automation_enabled = bool(settings.get("automation_enabled", False))
        outcome = "noop"

        self._debug(
            "Automation tick started",
            trigger=trigger,
            poll_interval_seconds=poll_interval,
            automation_enabled=automation_enabled,
        )

        if not automation_enabled:
            self._debug("Automation disabled — polling meter only", trigger=trigger)
            self.poll_meter()
            self._log_tick_completion(trigger, outcome="disabled")
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
        )

        scenes = extract_aircon_scenes(settings)
        aircon_id = str(settings.get("aircon_device_id", "")).strip()

        if not in_window:
            self._debug("Outside configured window — polling meter", trigger=trigger)
            self.poll_meter()
            if settings.get("turn_off_outside_windows", False):
                if self._cooldown_active(now):
                    self._debug("Cooldown active, skipping off automation outside window", trigger=trigger)
                else:
                    try:
                        off_scene_id = scenes.get("off", "")
                        handled = False
                        if off_scene_id:
                            handled = self._run_aircon_scene(
                                off_scene_id,
                                scene_key="off",
                                state_reason="automation_off_outside_window",
                                assumed_power="off",
                                trigger=trigger,
                            )
                        if not handled:
                            if aircon_id:
                                self._send_aircon_off(
                                    aircon_id,
                                    trigger=trigger,
                                    reason="outside_window",
                                )
                            else:
                                self._update_state(
                                    last_error="Missing OFF scene and aircon_device_id"
                                )
                    except SwitchBotApiError as exc:
                        self._update_state(last_error=str(exc))
                        self._error(
                            "SwitchBot API error while turning off outside window",
                            trigger=trigger,
                            error=str(exc),
                        )
                    else:
                        outcome = "turned_off_outside_window"
            else:
                outcome = "outside_window"
            self._log_tick_completion(trigger, outcome=outcome)
            return

        reading = self.poll_meter()
        if not reading or reading.get("temperature") is None:
            self._debug("Meter reading unavailable; aborting automation tick", trigger=trigger)
            self._log_tick_completion(trigger, outcome="missing_meter")
            return

        try:
            current_temp = float(reading["temperature"])
        except (TypeError, ValueError):
            self._update_state(last_error="Invalid temperature reading")
            self._error("Invalid temperature reading returned by meter", trigger=trigger, value=reading.get("temperature"))
            self._log_tick_completion(trigger, outcome="invalid_temperature")
            return

        mode = str(settings.get("mode", "winter")).strip().lower()
        profile = settings.get(mode, {})
        if not isinstance(profile, dict):
            profile = {}

        hysteresis = float(settings.get("hysteresis_celsius", 0.0) or 0.0)

        try:
            min_temp = float(profile.get("min_temp"))
            max_temp = float(profile.get("max_temp"))
            target_temp = float(profile.get("target_temp"))
            ac_mode = int(profile.get("ac_mode"))
            fan_speed = int(profile.get("fan_speed"))
        except (TypeError, ValueError):
            self._update_state(last_error=f"Invalid profile configuration for mode: {mode}")
            self._error("Invalid automation profile configuration", trigger=trigger, mode=mode)
            self._log_tick_completion(trigger, outcome="invalid_profile")
            return

        if min_temp > max_temp:
            self._update_state(last_error=f"Invalid thresholds: min_temp > max_temp ({mode})")
            self._error("Invalid temperature thresholds", trigger=trigger, mode=mode, min_temp=min_temp, max_temp=max_temp)
            self._log_tick_completion(trigger, outcome="invalid_thresholds")
            return

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

        if self._cooldown_active(now):
            self._debug("Cooldown active — skipping automation", trigger=trigger)
            self._log_tick_completion(trigger, outcome="cooldown")
            return

        decision_taken = False

        try:
            if mode == "winter":
                if current_temp <= (min_temp - hysteresis):
                    self._debug("Winter mode: below min threshold", trigger=trigger, threshold=min_temp - hysteresis)
                    scene_id = scenes.get("winter", "")
                    executed = False
                    if scene_id:
                        executed = self._run_aircon_scene(
                            scene_id,
                            scene_key="winter",
                            state_reason="automation_winter_on",
                            assumed_power="on",
                            trigger=trigger,
                        )
                    if not executed:
                        if aircon_id:
                            self._send_aircon_setall(
                                aircon_id,
                                temperature=target_temp,
                                mode=ac_mode,
                                fan_speed=fan_speed,
                                power_state="on",
                                trigger=trigger,
                                reason="automation_winter_on",
                            )
                        else:
                            self._update_state(
                                last_error="Missing winter scene and aircon_device_id"
                            )
                    decision_taken = True
                    outcome = "winter_on"
                elif current_temp >= (max_temp + hysteresis):
                    self._debug("Winter mode: above max threshold", trigger=trigger, threshold=max_temp + hysteresis)
                    off_scene_id = scenes.get("off", "")
                    turned_off = False
                    if off_scene_id:
                        turned_off = self._run_aircon_scene(
                            off_scene_id,
                            scene_key="off",
                            state_reason="automation_winter_off",
                            assumed_power="off",
                            trigger=trigger,
                        )
                    if not turned_off:
                        if aircon_id:
                            self._send_aircon_off(
                                aircon_id,
                                trigger=trigger,
                                reason="automation_winter_off",
                            )
                        else:
                            self._update_state(
                                last_error="Missing OFF scene and aircon_device_id"
                            )
                    decision_taken = True
                    outcome = "winter_off"
            elif mode == "summer":
                if current_temp >= (max_temp + hysteresis):
                    self._debug("Summer mode: above max threshold", trigger=trigger, threshold=max_temp + hysteresis)
                    scene_id = scenes.get("summer", "")
                    executed = False
                    if scene_id:
                        executed = self._run_aircon_scene(
                            scene_id,
                            scene_key="summer",
                            state_reason="automation_summer_on",
                            assumed_power="on",
                            trigger=trigger,
                        )
                    if not executed:
                        if aircon_id:
                            self._send_aircon_setall(
                                aircon_id,
                                temperature=target_temp,
                                mode=ac_mode,
                                fan_speed=fan_speed,
                                power_state="on",
                                trigger=trigger,
                                reason="automation_summer_on",
                            )
                        else:
                            self._update_state(
                                last_error="Missing summer scene and aircon_device_id"
                            )
                    decision_taken = True
                    outcome = "summer_on"
                elif current_temp <= (min_temp - hysteresis):
                    self._debug("Summer mode: below min threshold", trigger=trigger, threshold=min_temp - hysteresis)
                    off_scene_id = scenes.get("off", "")
                    turned_off = False
                    if off_scene_id:
                        turned_off = self._run_aircon_scene(
                            off_scene_id,
                            scene_key="off",
                            state_reason="automation_summer_off",
                            assumed_power="off",
                            trigger=trigger,
                        )
                    if not turned_off:
                        if aircon_id:
                            self._send_aircon_off(
                                aircon_id,
                                trigger=trigger,
                                reason="automation_summer_off",
                            )
                        else:
                            self._update_state(
                                last_error="Missing OFF scene and aircon_device_id"
                            )
                    decision_taken = True
                    outcome = "summer_off"
            else:
                self._update_state(last_error=f"Unknown mode: {mode}")
                self._error("Unknown automation mode", trigger=trigger, mode=mode)
                outcome = "invalid_mode"
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
            self._error("SwitchBot API error during automation", trigger=trigger, error=str(exc))
            self._log_tick_completion(trigger, outcome="api_error")
            return

        if not decision_taken:
            self._debug("No automation action needed — thresholds not crossed", trigger=trigger)
            outcome = "no_action"

        self._log_tick_completion(trigger, outcome=outcome)
