from __future__ import annotations

from typing import Any, Dict

AIRCON_SCENE_KEYS: tuple[str, ...] = ("winter", "summer", "fan", "off")
AIRCON_SCENE_LABELS: dict[str, str] = {
    "winter": "Aircon ON – Hiver",
    "summer": "Aircon ON – Été",
    "fan": "Aircon ON – Mode neutre",
    "off": "Aircon OFF – Scène",
}
AIRCON_MODE_BY_ACTION: dict[str, int] = {
    "winter": 5,
    "summer": 2,
    "fan": 4,
}


def extract_aircon_scenes(settings: dict[str, Any]) -> Dict[str, str]:
    """Return a sanitized mapping of configured aircon scenes."""

    raw_scenes = settings.get("aircon_scenes", {})
    if not isinstance(raw_scenes, dict):
        raw_scenes = {}

    sanitized: dict[str, str] = {}
    for key in AIRCON_SCENE_KEYS:
        value = raw_scenes.get(key, "")
        sanitized[key] = str(value).strip() if isinstance(value, str) else ""
    return sanitized


def normalize_aircon_temperature(value: Any) -> int:
    """Return a SwitchBot-compatible integer temperature.

    The IR ``setAll`` command expects an integer. ``round`` avoids truncating
    floating-point noise such as ``23.999999`` down to ``23``.
    """
    return int(round(float(value)))


def build_aircon_parameter(
    temperature: Any,
    mode: Any,
    fan_speed: Any,
    power_state: Any,
) -> str:
    """Build the canonical ``"{temperature},{mode},{fan_speed},{power}"``."""
    return (
        f"{normalize_aircon_temperature(temperature)},"
        f"{int(mode)},{int(fan_speed)},{power_state}"
    )


def normalize_aircon_parameter(parameter: str | None) -> str | None:
    """Normalize a stored ``setAll`` parameter, including legacy floats.

    Returns the original value when it is not a valid four-field parameter so
    corrupted state is never silently rewritten.
    """
    if not isinstance(parameter, str):
        return parameter
    parts = parameter.split(",")
    if len(parts) != 4:
        return parameter
    try:
        return build_aircon_parameter(parts[0], parts[1], parts[2], parts[3])
    except (TypeError, ValueError):
        return parameter


def parse_aircon_parameter(
    parameter: str | None,
) -> tuple[int, int, int, str] | None:
    """Parse a canonical or legacy parameter, returning ``None`` if invalid."""
    normalized = normalize_aircon_parameter(parameter)
    if not isinstance(normalized, str):
        return None
    parts = normalized.split(",")
    if len(parts) != 4:
        return None
    try:
        return int(parts[0]), int(parts[1]), int(parts[2]), parts[3]
    except ValueError:
        return None
