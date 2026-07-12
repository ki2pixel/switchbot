"""Tests for SPA Router safety and non-regression.

Validates that spa-router.js correctly handles CSS deduplication,
global script filtering (with query strings), and script security.
"""
from __future__ import annotations

import os
import re


# Path to the SPA router source file
SPA_ROUTER_PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "switchbot_dashboard", "static", "js", "spa-router.js",
)


def _read_spa_router() -> str:
    with open(SPA_ROUTER_PATH, encoding="utf-8") as f:
        return f.read()


class TestSPARouterSafety:
    """Tests de non-régression pour le routeur SPA."""

    def test_global_scripts_filter_uses_pathname(self):
        """The globalScripts filter must strip query strings before matching
        (P1.1 fix — prevents re-execution of loaders.js?v=123)."""
        source = _read_spa_router()
        # The filter should use normalizeHref or URL.pathname, not raw endsWith
        assert "srcPath" in source or "normalizeHref" in source, (
            "globalScripts filter must normalize the URL path before comparison"
        )
        # Must not use raw src.endsWith without path normalization
        assert "src.endsWith(globalScript)" not in source or "srcPath.endsWith" in source

    def test_no_css_duplication_pattern(self):
        """The router must use a Set to track existing CSS and prevent duplicates
        (P1.1 fix — CSS deduplication via Set normalization)."""
        source = _read_spa_router()
        assert "existingCSS" in source, "Must maintain a Set of existing CSS pathnames"
        assert "new Set(" in source, "Must use a Set for CSS dedup"

    def test_script_src_validation(self):
        """loadScriptDynamic must validate same-origin before injection
        (P2.43 security fix)."""
        source = _read_spa_router()
        assert "url.origin !== location.origin" in source or \
               "url.origin !== globalThis.location.origin" in source, (
            "loadScriptDynamic must reject cross-origin scripts"
        )

    def test_no_css_selector_injection(self):
        """loadScriptDynamic must NOT use querySelector with string interpolation
        for script src lookup (CSS selector injection vulnerability)."""
        source = _read_spa_router()
        # Should not contain template literal in querySelector for script[src]
        assert 'querySelector(`script[src="${' not in source, (
            "Must not use querySelector with string interpolation for script lookup"
        )

    def test_double_footer_cleanup(self):
        """The router must remove duplicate #footer-bar from #app-content
        after SPA content replacement (P1.1 fix)."""
        source = _read_spa_router()
        assert "duplicateFooter" in source or "querySelector('#footer-bar')" in source, (
            "Must clean up duplicate footer after content replacement"
        )

    def test_focus_management_after_transition(self):
        """The router must move focus to #app-content after SPA transition
        for keyboard/screen-reader accessibility (P2.26 fix)."""
        source = _read_spa_router()
        assert "focus(" in source, "Must call focus() after content replacement"
        assert "tabindex" in source, "Must set tabindex=-1 on content container"

    def test_route_announcer_exists(self):
        """The router must announce route changes via an aria-live region
        for screen readers (P2.26 fix)."""
        source = _read_spa_router()
        assert "spa-route-announcer" in source, "Must have a route announcer element"
        assert "aria-live" in source, "Route announcer must use aria-live"

    def test_no_dead_scripts_in_global_list(self):
        """The globalScripts list must NOT contain removed files
        (bottom-nav.js, performance-optimizer.js, advanced-optimizer.js)."""
        source = _read_spa_router()
        assert "bottom-nav.js" not in source, "bottom-nav.js must be removed from globalScripts"
        assert "performance-optimizer.js" not in source, "performance-optimizer.js must be removed"
        assert "advanced-optimizer.js" not in source, "advanced-optimizer.js must be removed"

    def test_no_debug_console_log(self):
        """No debug console.log statements should remain in production code
        (P3.17 fix)."""
        source = _read_spa_router()
        # console.warn and console.error are acceptable for real warnings/errors
        log_matches = re.findall(r'console\.log\(', source)
        assert len(log_matches) == 0, (
            f"Found {len(log_matches)} console.log() calls in spa-router.js"
        )

    def test_preload_orphan_cleanup(self):
        """The router must remove orphaned preload links that are no longer
        needed after navigation (P1.1 fix)."""
        source = _read_spa_router()
        assert 'preload' in source and 'remove()' in source, (
            "Must clean up orphaned preload links"
        )
