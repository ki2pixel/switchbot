"""Tests for frontend asset optimization and dead file removal.

Validates that dead files have been removed, Font Awesome Brands is gone,
fonts are converted to WOFF2, and no debug console.log remains.
"""
from __future__ import annotations

import os
import re


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
STATIC_DIR = os.path.join(PROJECT_ROOT, "switchbot_dashboard", "static")
JS_DIR = os.path.join(STATIC_DIR, "js")
CSS_DIR = os.path.join(STATIC_DIR, "css")
VENDOR_DIR = os.path.join(STATIC_DIR, "vendor")
FONTS_DIR = os.path.join(VENDOR_DIR, "fonts")
FA_WEBFONTS_DIR = os.path.join(VENDOR_DIR, "fontawesome", "webfonts")
FA_CSS_PATH = os.path.join(VENDOR_DIR, "fontawesome", "css", "all.min.css")


def _read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


class TestPerformanceAssets:
    """Tests de poids et de fichiers morts."""

    def test_no_dead_js_files(self):
        """Dead JS files identified in the audit must no longer exist (P2.2 fix)."""
        dead_files = [
            "bottom-nav.js",
            "performance-optimizer.js",
            "advanced-optimizer.js",
            "perf-worker.js",
        ]
        for filename in dead_files:
            path = os.path.join(JS_DIR, filename)
            assert not os.path.exists(path), f"Dead file must be removed: {filename}"

    def test_no_critical_css(self):
        """critical.css must be removed — it duplicates the inline CSS in
        index.html (P2.2, P3.1 fix)."""
        path = os.path.join(CSS_DIR, "critical.css")
        assert not os.path.exists(path), "critical.css must be removed"

    def test_no_fa_brands(self):
        """Font Awesome Brands files must not be present — no brand icons
        are used in the project (P1.3 fix)."""
        for filename in ["fa-brands-400.ttf", "fa-brands-400.woff2"]:
            path = os.path.join(FA_WEBFONTS_DIR, filename)
            assert not os.path.exists(path), f"FA Brands must be removed: {filename}"

    def test_no_fa_brands_in_css(self):
        """The FA CSS must not reference fa-brands-400 files (P1.3 fix)."""
        css = _read_file(FA_CSS_PATH)
        assert "fa-brands-400" not in css, (
            "all.min.css must not reference fa-brands-400"
        )

    def test_no_fa_solid_ttf(self):
        """fa-solid-900.ttf must be removed — WOFF2 is sufficient for all
        modern browsers (P1.3 fix)."""
        path = os.path.join(FA_WEBFONTS_DIR, "fa-solid-900.ttf")
        assert not os.path.exists(path), "fa-solid TTF must be removed"

    def test_space_grotesk_woff2_exists(self):
        """Space Grotesk fonts must be in WOFF2 format (P2.6 fix)."""
        for weight in ["Regular", "Medium", "SemiBold"]:
            woff2_path = os.path.join(FONTS_DIR, f"SpaceGrotesk-{weight}.woff2")
            ttf_path = os.path.join(FONTS_DIR, f"SpaceGrotesk-{weight}.ttf")
            assert os.path.exists(woff2_path), f"Missing WOFF2: SpaceGrotesk-{weight}.woff2"
            assert not os.path.exists(ttf_path), f"TTF must be removed: SpaceGrotesk-{weight}.ttf"

    def test_space_grotesk_css_references_woff2(self):
        """space-grotesk.css must reference .woff2 files, not .ttf (P2.6 fix)."""
        css_path = os.path.join(VENDOR_DIR, "css", "space-grotesk.css")
        css = _read_file(css_path)
        assert ".woff2" in css, "space-grotesk.css must reference WOFF2 files"
        assert ".ttf" not in css, "space-grotesk.css must not reference TTF files"

    def test_no_roboto_reference(self):
        """sticky-footer.css must not reference Roboto font — the project
        uses Space Grotesk exclusively (P2.6 fix)."""
        css_path = os.path.join(CSS_DIR, "sticky-footer.css")
        css = _read_file(css_path)
        assert "Roboto" not in css, "sticky-footer.css must not reference Roboto"


class TestSecurityFrontend:
    """Tests de sécurité frontend."""

    def test_no_debug_console_log_in_critical_js(self):
        """Critical JS files must not contain debug console.log statements
        (P3.17 fix). console.warn and console.error are acceptable."""
        critical_files = ["spa-router.js", "history.js", "loaders.js"]
        for filename in critical_files:
            path = os.path.join(JS_DIR, filename)
            source = _read_file(path)
            log_matches = re.findall(r'console\.log\(', source)
            assert len(log_matches) == 0, (
                f"Found {len(log_matches)} console.log() in {filename}"
            )

    def test_no_innerhtml_with_dynamic_data_in_history(self):
        """history.js must not use innerHTML with dynamic/interpolated data.
        Static string assignments are flagged as well since DOM API should
        be used instead (P2.3, P2.41 fix)."""
        path = os.path.join(JS_DIR, "history.js")
        source = _read_file(path)
        # Check for assignment to innerHTML
        assert not re.search(r"\.innerHTML\s*=", source), (
            "history.js should use DOM API instead of innerHTML"
        )

    def test_csp_header_includes_font_src(self):
        """The CSP header must include font-src 'self' directive (P3.16 fix)."""
        init_path = os.path.join(
            PROJECT_ROOT, "switchbot_dashboard", "__init__.py"
        )
        source = _read_file(init_path)
        assert "font-src 'self'" in source, (
            "CSP header must include font-src 'self'"
        )

    def test_history_uses_abort_controller(self):
        """history.js must use AbortController for fetch timeout (P3.6 fix)."""
        path = os.path.join(JS_DIR, "history.js")
        source = _read_file(path)
        assert "AbortController" in source, "history.js must use AbortController"
        assert "abort()" in source, "history.js must call abort()"

    def test_footer_height_token_defined(self):
        """theme.css must define --sb-footer-height for CTA positioning (P1.2 fix)."""
        css_path = os.path.join(CSS_DIR, "theme.css")
        css = _read_file(css_path)
        assert "--sb-footer-height" in css, (
            "theme.css must define --sb-footer-height token"
        )
