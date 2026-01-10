from __future__ import annotations

import datetime as dt
import logging
from typing import Any

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


class AutomationService:
    def __init__(
        self,
        settings_store: BaseStore,
        state_store: BaseStore,
        switchbot_client: SwitchBotClient,
    ) -> None:
        self._settings_store = settings_store
        self._state_store = state_store
        self._client = switchbot_client

    def _update_state(self, **updates: Any) -> None:
        state = self._state_store.read()
        state.update(updates)
        self._state_store.write(state)

    def poll_meter(self) -> dict[str, Any] | None:
        settings = self._settings_store.read()
        meter_id = str(settings.get("meter_device_id", "")).strip()
        if not meter_id:
            self._update_state(last_error="Missing meter_device_id", last_read_at=_utc_now_iso())
            return None

        try:
            response = self._client.get_device_status(meter_id)
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc), last_read_at=_utc_now_iso())
            return None

        body = response.get("body", {})
        temperature = body.get("temperature")
        humidity = body.get("humidity")

        self._update_state(
            last_temperature=temperature,
            last_humidity=humidity,
            last_read_at=_utc_now_iso(),
            last_error=None,
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

    def _send_aircon_off(self, aircon_device_id: str) -> None:
        state = self._state_store.read()
        if state.get("assumed_aircon_power") == "off":
            return

        self._client.send_command(aircon_device_id, command="turnOff", parameter="default")
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
    ) -> None:
        state = self._state_store.read()
        parameter = f"{temperature},{mode},{fan_speed},{power_state}"
        if (
            state.get("assumed_aircon_power") == power_state
            and state.get("assumed_aircon_mode") == mode
            and state.get("assumed_aircon_parameter") == parameter
        ):
            return

        self._client.send_command(
            aircon_device_id,
            command="setAll",
            parameter=parameter,
            command_type="command",
        )
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
    ) -> bool:
        friendly = AIRCON_SCENE_LABELS.get(scene_key, scene_key)
        scene_id = str(scene_id or "").strip()
        if not scene_id:
            self._update_state(last_error=f"Missing scene id for {friendly}")
            logger.warning("Skipping %s automation: no scene configured", scene_key)
            return False

        try:
            self._client.run_scene(scene_id)
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
            logger.error("Scene %s execution failed: %s", scene_key, exc)
            return False

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
        now = dt.datetime.now()
        self._update_state(last_tick=_utc_now_iso())
        settings = self._settings_store.read()

        if not settings.get("automation_enabled", False):
            self.poll_meter()
            return

        time_windows = settings.get("time_windows", [])
        if not isinstance(time_windows, list):
            time_windows = []

        in_window = _is_now_in_windows(time_windows, now)
        scenes = extract_aircon_scenes(settings)
        aircon_id = str(settings.get("aircon_device_id", "")).strip()

        if not in_window:
            self.poll_meter()
            if settings.get("turn_off_outside_windows", False):
                if not self._cooldown_active(now):
                    try:
                        off_scene_id = scenes.get("off", "")
                        handled = False
                        if off_scene_id:
                            handled = self._run_aircon_scene(
                                off_scene_id,
                                scene_key="off",
                                state_reason="automation_off_outside_window",
                                assumed_power="off",
                            )
                        if not handled:
                            if aircon_id:
                                self._send_aircon_off(aircon_id)
                            else:
                                self._update_state(
                                    last_error="Missing OFF scene and aircon_device_id"
                                )
                    except SwitchBotApiError as exc:
                        self._update_state(last_error=str(exc))
            return

        reading = self.poll_meter()
        if not reading or reading.get("temperature") is None:
            return

        try:
            current_temp = float(reading["temperature"])
        except (TypeError, ValueError):
            self._update_state(last_error="Invalid temperature reading")
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
            return

        if min_temp > max_temp:
            self._update_state(last_error=f"Invalid thresholds: min_temp > max_temp ({mode})")
            return

        if self._cooldown_active(now):
            return

        try:
            if mode == "winter":
                if current_temp <= (min_temp - hysteresis):
                    scene_id = scenes.get("winter", "")
                    executed = False
                    if scene_id:
                        executed = self._run_aircon_scene(
                            scene_id,
                            scene_key="winter",
                            state_reason="automation_winter_on",
                            assumed_power="on",
                        )
                    if not executed:
                        if aircon_id:
                            self._send_aircon_setall(
                                aircon_id,
                                temperature=target_temp,
                                mode=ac_mode,
                                fan_speed=fan_speed,
                                power_state="on",
                            )
                        else:
                            self._update_state(
                                last_error="Missing winter scene and aircon_device_id"
                            )
                elif current_temp >= (max_temp + hysteresis):
                    off_scene_id = scenes.get("off", "")
                    turned_off = False
                    if off_scene_id:
                        turned_off = self._run_aircon_scene(
                            off_scene_id,
                            scene_key="off",
                            state_reason="automation_winter_off",
                            assumed_power="off",
                        )
                    if not turned_off:
                        if aircon_id:
                            self._send_aircon_off(aircon_id)
                        else:
                            self._update_state(
                                last_error="Missing OFF scene and aircon_device_id"
                            )
            elif mode == "summer":
                if current_temp >= (max_temp + hysteresis):
                    scene_id = scenes.get("summer", "")
                    executed = False
                    if scene_id:
                        executed = self._run_aircon_scene(
                            scene_id,
                            scene_key="summer",
                            state_reason="automation_summer_on",
                            assumed_power="on",
                        )
                    if not executed:
                        if aircon_id:
                            self._send_aircon_setall(
                                aircon_id,
                                temperature=target_temp,
                                mode=ac_mode,
                                fan_speed=fan_speed,
                                power_state="on",
                            )
                        else:
                            self._update_state(
                                last_error="Missing summer scene and aircon_device_id"
                            )
                elif current_temp <= (min_temp - hysteresis):
                    off_scene_id = scenes.get("off", "")
                    turned_off = False
                    if off_scene_id:
                        turned_off = self._run_aircon_scene(
                            off_scene_id,
                            scene_key="off",
                            state_reason="automation_summer_off",
                            assumed_power="off",
                        )
                    if not turned_off:
                        if aircon_id:
                            self._send_aircon_off(aircon_id)
                        else:
                            self._update_state(
                                last_error="Missing OFF scene and aircon_device_id"
                            )
            else:
                self._update_state(last_error=f"Unknown mode: {mode}")
        except SwitchBotApiError as exc:
            self._update_state(last_error=str(exc))
