from __future__ import annotations

from switchbot_dashboard.aircon import (
    build_aircon_parameter,
    normalize_aircon_parameter,
    parse_aircon_parameter,
)
from switchbot_dashboard.routes import AIRCON_SCENE_KEYS, _extract_aircon_scenes


def test_extract_aircon_scenes_returns_empty_strings_when_missing() -> None:
    scenes = _extract_aircon_scenes({})

    assert scenes == {key: "" for key in AIRCON_SCENE_KEYS}


def test_extract_aircon_scenes_trims_and_validates_values() -> None:
    settings = {
        "aircon_scenes": {
            "winter": "  abc-123  ",
            "summer": 42,
            "fan": "fan-scene",
            "off": "  999-off ",
        }
    }

    scenes = _extract_aircon_scenes(settings)

    assert scenes["winter"] == "abc-123"
    assert scenes["summer"] == ""
    assert scenes["fan"] == "fan-scene"
    assert scenes["off"] == "999-off"


def test_build_aircon_parameter_formats_integer_temperature() -> None:
    # Given: a target temperature stored as a float
    # When: the setAll parameter is built
    parameter = build_aircon_parameter(24.0, 5, 3, "on")

    # Then: the temperature is serialized as an integer
    assert parameter == "24,5,3,on"


def test_build_aircon_parameter_rounds_float_noise() -> None:
    # Given: a target temperature affected by floating-point noise
    # When: the setAll parameter is built
    parameter = build_aircon_parameter(23.999999, 5, 3, "on")

    # Then: rounding prevents truncation to 23
    assert parameter == "24,5,3,on"


def test_normalize_aircon_parameter_upgrades_legacy_float() -> None:
    # Given: a legacy state parameter containing a float temperature
    # When: the parameter is normalized
    parameter = normalize_aircon_parameter("24.0,5,3,on")

    # Then: the canonical integer form is returned
    assert parameter == "24,5,3,on"


def test_normalize_aircon_parameter_keeps_invalid_value() -> None:
    # Given: invalid or empty stored values
    # When: the parameter is normalized
    # Then: invalid values are preserved and empty values stay None
    assert normalize_aircon_parameter("not-a-param") == "not-a-param"
    assert normalize_aircon_parameter(None) is None


def test_parse_aircon_parameter_returns_tuple_or_none() -> None:
    # Given: canonical, legacy and invalid parameter strings
    # When: the parameter is parsed
    # Then: valid parameters yield integers and invalid ones yield None
    assert parse_aircon_parameter("24.0,5,3,on") == (24, 5, 3, "on")
    assert parse_aircon_parameter("not-a-param") is None
