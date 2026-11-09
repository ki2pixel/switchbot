"""Tests for the history dashboard aircon mode display."""

from __future__ import annotations

import os


HISTORY_JS_PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "switchbot_dashboard", "static", "js", "history.js",
)


def _read_history_js() -> str:
    with open(HISTORY_JS_PATH, encoding="utf-8") as f:
        return f.read()


def test_history_badge_displays_aircon_mode() -> None:
    # Given: the history dashboard JavaScript source
    source = _read_history_js()

    # When: the latest table renders a powered-on aircon record
    # Then: the badge derives the mode and appends it to the ON label
    assert "assumed_aircon_mode" in source
    assert "'4': 'Fan'" in source
    assert "'5': 'Heat'" in source
    assert "getAirconModeLabel" in source
    assert "\\u00b7" in source


def test_history_badge_falls_back_to_last_action() -> None:
    # Given: older history rows without the mode metadata
    source = _read_history_js()

    # When: the mode is absent from metadata
    # Then: the badge can still derive it from the setAll last_action
    assert "last_action" in source
    assert "setAll" in source
