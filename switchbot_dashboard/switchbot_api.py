from __future__ import annotations

import base64
import hashlib
import hmac
import time
import uuid
import logging
from dataclasses import dataclass
from typing import Any

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


class SwitchBotClient:
    def __init__(
        self,
        token: str,
        secret: str,
        base_url: str | None = None,
        retry_attempts: int = 2,
        retry_delay_seconds: int = 10,
    ) -> None:
        self._token = token.strip()
        self._secret = secret.strip()
        self._base_url = (base_url or "https://api.switch-bot.com").rstrip("/")
        self._retry_attempts = max(int(retry_attempts), 1)
        self._retry_delay_seconds = max(int(retry_delay_seconds), 0)
        self._last_quota: dict[str, int] | None = None

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

    def _request(self, method: str, path: str, json_body: dict[str, Any] | None = None) -> Any:
        url = f"{self._base_url}{path}"
        last_error: Exception | None = None

        for attempt_index in range(self._retry_attempts):
            headers = self._build_headers()
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=json_body,
                    timeout=15,
                )
            except requests.RequestException as exc:
                last_error = exc
                if attempt_index < (self._retry_attempts - 1) and self._retry_delay_seconds > 0:
                    time.sleep(self._retry_delay_seconds)
                    continue

                raise SwitchBotApiError(f"SwitchBot request failed: {exc}") from exc

            logger.debug(
                "SwitchBot %s %s → HTTP %s headers=%s",
                method,
                path,
                response.status_code,
                dict(response.headers),
            )

            retryable_http = response.status_code == 429 or 500 <= response.status_code <= 599
            if retryable_http and attempt_index < (self._retry_attempts - 1):
                if self._retry_delay_seconds > 0:
                    time.sleep(self._retry_delay_seconds)
                continue

            try:
                data = response.json()
            except ValueError as exc:
                raise SwitchBotApiError(
                    f"Invalid JSON response from SwitchBot ({response.status_code})."
                ) from exc

            self._capture_quota_metadata(response)

            if response.status_code >= 400:
                raise SwitchBotApiError(
                    f"SwitchBot HTTP {response.status_code}: {data!r}"
                )

            if not isinstance(data, dict) or "statusCode" not in data:
                raise SwitchBotApiError(f"Unexpected SwitchBot response: {data!r}")

            status_code = data.get("statusCode")
            if status_code == 100:
                return data

            if status_code == 190 and attempt_index < (self._retry_attempts - 1):
                if self._retry_delay_seconds > 0:
                    time.sleep(self._retry_delay_seconds)
                continue

            raise SwitchBotApiError(f"SwitchBot API error: {data!r}")

        if last_error is not None:
            raise SwitchBotApiError(f"SwitchBot request failed: {last_error}") from last_error

        raise SwitchBotApiError("SwitchBot request failed")

    def get_devices(self) -> Any:
        return self._request("GET", "/v1.1/devices")

    def get_device_status(self, device_id: str) -> Any:
        device_id = device_id.strip()
        if not device_id:
            raise SwitchBotApiError("Missing device_id")

        return self._request("GET", f"/v1.1/devices/{device_id}/status")

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

        return self._request("POST", f"/v1.1/scenes/{scene_id}/execute")

    def _capture_quota_metadata(self, response: Response) -> None:
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

        if limit is None and remaining is None:
            logger.debug("SwitchBot quota headers absent on latest response.")
            return

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
