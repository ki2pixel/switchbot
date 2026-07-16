from __future__ import annotations

import base64
import hashlib
import hmac
import time
import threading
import uuid
import logging
from dataclasses import dataclass
from typing import Any, Protocol

import requests
from requests import Response


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SwitchBotResponse:
    status_code: int
    message: str
    body: Any


class SwitchBotApiError(RuntimeError):
    pass


class QuotaTracker(Protocol):
    def record_call(self, *, increment: int = 1) -> None:
        ...

    def record_from_headers(self, *, limit: int | None, remaining: int | None) -> bool:
        ...


class SwitchBotClient:
    def __init__(
        self,
        token: str,
        secret: str,
        base_url: str | None = None,
        retry_attempts: int = 2,
        retry_delay_seconds: int = 10,
        quota_tracker: QuotaTracker | None = None,
    ) -> None:
        self._token = token.strip()
        self._secret = secret.strip()
        self._base_url = (base_url or "https://api.switch-bot.com").rstrip("/")
        self._retry_attempts = max(int(retry_attempts), 1)
        self._retry_delay_seconds = max(int(retry_delay_seconds), 0)
        self._last_quota: dict[str, int] | None = None
        self._quota_tracker = quota_tracker
        # Caches for API calls (P-01)
        self._status_cache: dict[str, tuple[float, Any]] = {}
        self._devices_cache: tuple[float, Any] | None = None
        self._cache_lock = threading.Lock()

    def _build_headers(self) -> dict[str, str]:
        if not self._token or not self._secret:
            raise SwitchBotApiError(
                "Missing SwitchBot credentials. Set SWITCHBOT_TOKEN and SWITCHBOT_SECRET."
            )

        t = int(round(time.time() * 1000))
        nonce = str(uuid.uuid4())
        string_to_sign = f"{self._token}{t}{nonce}".encode("utf-8")
        secret_bytes = self._secret.encode("utf-8")
        sign = base64.b64encode(
            hmac.new(secret_bytes, msg=string_to_sign, digestmod=hashlib.sha256).digest()
        ).decode("utf-8")

        return {
            "Authorization": self._token,
            "Content-Type": "application/json; charset=utf-8",
            "t": str(t),
            "sign": sign,
            "nonce": nonce,
        }

    def _process_response(self, response: Response, path: str, tracker_updated: bool) -> tuple[bool, Any]:
        """Returns (retry_needed, data)."""
        if response.status_code >= 400:
            try:
                data = response.json()
            except ValueError as exc:
                raise SwitchBotApiError(
                    f"SwitchBot HTTP {response.status_code}: invalid JSON error payload."
                ) from exc
            raise SwitchBotApiError(f"SwitchBot HTTP {response.status_code}: {data!r}")

        try:
            data = response.json()
        except ValueError as exc:
            raise SwitchBotApiError(
                f"Invalid JSON response from SwitchBot ({response.status_code})."
            ) from exc

        if not isinstance(data, dict) or "statusCode" not in data:
            raise SwitchBotApiError(f"Unexpected SwitchBot response: {data!r}")

        status_code = data.get("statusCode")
        logger.debug(
            "SwitchBot API payload parsed: statusCode=%s message=%s path=%s",
            status_code,
            data.get("message"),
            path,
        )
        if status_code == 100:
            if self._quota_tracker and not tracker_updated:
                self._quota_tracker.record_call()
            return False, data

        if status_code == 190:
            return True, None

        raise SwitchBotApiError(f"SwitchBot API error: {data!r}")

    def _request(self, method: str, path: str, json_body: dict[str, Any] | None = None, *, timeout: float = 15) -> Any:
        import random as _rand

        url = f"{self._base_url}{path}"
        last_error: Exception | None = None
        is_get = method.upper() == "GET"

        for attempt_index in range(self._retry_attempts):
            headers = self._build_headers()
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=json_body,
                    timeout=timeout,
                )
            except requests.RequestException as exc:
                # REL-04: Transport errors are always retryable
                last_error = exc
                if attempt_index < (self._retry_attempts - 1) and self._retry_delay_seconds > 0:
                    delay = min(self._retry_delay_seconds * (2 ** attempt_index), 5)
                    delay += _rand.uniform(0, 0.5)  # jitter
                    time.sleep(delay)
                    continue

                raise SwitchBotApiError(f"SwitchBot request failed: {exc}") from exc

            logger.debug(
                "SwitchBot %s %s → HTTP %s headers=%s",
                method,
                path,
                response.status_code,
                dict(response.headers),
            )

            # REL-04: Only retry on GETs for HTTP-level errors (429, 5xx)
            retryable_http = response.status_code == 429 or 500 <= response.status_code <= 599
            if retryable_http and is_get and attempt_index < (self._retry_attempts - 1):
                delay = self._parse_retry_after(response, attempt_index)
                time.sleep(delay)
                continue

            tracker_updated = self._capture_quota_metadata(response)

            retry_needed, data = self._process_response(response, path, tracker_updated)
            if retry_needed and is_get and attempt_index < (self._retry_attempts - 1):
                delay = self._parse_retry_after(response, attempt_index)
                time.sleep(delay)
                continue
                
            if not retry_needed:
                return data

        if last_error is not None:
            raise SwitchBotApiError(f"SwitchBot request failed: {last_error}") from last_error

        raise SwitchBotApiError("SwitchBot request failed")

    def _parse_retry_after(self, response: Response, attempt_index: int) -> float:
        """Parse Retry-After header with exponential backoff and jitter (REL-04)."""
        import random as _rand

        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                delay = min(float(retry_after), 5.0)
            except (ValueError, TypeError):
                delay = min(self._retry_delay_seconds * (2 ** attempt_index), 5.0)
        else:
            delay = min(self._retry_delay_seconds * (2 ** attempt_index), 5.0)
        delay += _rand.uniform(0, 0.5)  # jitter
        return delay

    def get_devices(self) -> Any:
        now = time.monotonic()
        with self._cache_lock:
            if self._devices_cache is not None:
                cached_time, cached_val = self._devices_cache
                if now - cached_time < 60.0:
                    return cached_val

        devices = self._request("GET", "/v1.1/devices")
        with self._cache_lock:
            self._devices_cache = (now, devices)
        return devices

    def get_scenes(self) -> Any:
        return self._request("GET", "/v1.1/scenes")

    def get_device_status(self, device_id: str) -> Any:
        device_id = device_id.strip()
        if not device_id:
            raise SwitchBotApiError("Missing device_id")

        # 60s cache to avoid N+1 API abuse on /devices page (P-01)
        now = time.monotonic()
        with self._cache_lock:
            if device_id in self._status_cache:
                cached_time, cached_val = self._status_cache[device_id]
                if now - cached_time < 60.0:
                    return cached_val

        status = self._request("GET", f"/v1.1/devices/{device_id}/status")
        with self._cache_lock:
            self._status_cache[device_id] = (now, status)
        return status

    def send_command(
        self,
        device_id: str,
        command: str,
        parameter: str = "default",
        command_type: str = "command",
    ) -> Any:
        device_id = device_id.strip()
        if not device_id:
            raise SwitchBotApiError("Missing device_id")

        body = {
            "command": command,
            "parameter": parameter,
            "commandType": command_type,
        }
        return self._request("POST", f"/v1.1/devices/{device_id}/commands", json_body=body)

    def run_scene(self, scene_id: str) -> Any:
        scene_id = scene_id.strip()
        if not scene_id:
            raise SwitchBotApiError("Missing scene_id")

        return self._request("POST", f"/v1.1/scenes/{scene_id}/execute", json_body={})

    def _capture_quota_metadata(self, response: Response) -> bool:
        header_map = {key.lower(): value for key, value in response.headers.items()}
        limit_raw = (
            header_map.get("x-ratelimit-limit")
            or header_map.get("x-rate-limit-limit")
            or header_map.get("ratelimit-limit")
        )
        remaining_raw = (
            header_map.get("x-ratelimit-remaining")
            or header_map.get("x-rate-limit-remaining")
            or header_map.get("ratelimit-remaining")
        )

        limit = self._safe_int(limit_raw)
        remaining = self._safe_int(remaining_raw)

        if getattr(response, "status_code", None) == 429:
            remaining = 0

        tracker_updated = False
        if limit is None and remaining is None:
            if self._quota_tracker:
                self._quota_tracker.record_call()
                tracker_updated = True
            logger.debug("SwitchBot quota headers absent on latest response.")
            return tracker_updated

        self._last_quota = {}
        if limit is not None:
            self._last_quota["limit"] = limit
        if remaining is not None:
            self._last_quota["remaining"] = remaining

        logger.info(
            "SwitchBot quota snapshot captured: remaining=%s limit=%s",
            remaining if remaining is not None else "unknown",
            limit if limit is not None else "unknown",
        )

        if self._quota_tracker:
            tracker_updated = self._quota_tracker.record_from_headers(limit=limit, remaining=remaining)

        return tracker_updated

    @staticmethod
    def _safe_int(value: str | None) -> int | None:
        if value is None:
            return None
        try:
            return int(value)
        except (TypeError, ValueError):
            return None

    def get_last_quota_snapshot(self) -> dict[str, int] | None:
        if self._last_quota is None:
            return None
        return dict(self._last_quota)
