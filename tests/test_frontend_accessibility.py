"""Tests for WCAG 2.1 AA accessibility compliance.

Validates that all templates have proper semantic structure, skip-links,
screen-reader utilities, and ARIA attributes.
"""
from __future__ import annotations

import glob
import os
import re


TEMPLATES_DIR = os.path.join(
    os.path.dirname(__file__), "..",
    "switchbot_dashboard", "templates",
)
THEME_CSS_PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "switchbot_dashboard", "static", "css", "theme.css",
)
LOADERS_JS_PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "switchbot_dashboard", "static", "js", "loaders.js",
)


def _read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def _all_templates() -> list[str]:
    """Return absolute paths of all HTML templates (excluding partials)."""
    return sorted(
        p for p in glob.glob(os.path.join(TEMPLATES_DIR, "*.html"))
        if not os.path.basename(p).startswith("_")
    )


class TestAccessibilityCompliance:
    """Tests WCAG 2.1 AA."""

    def test_sr_only_defined_in_theme_css(self):
        """The .sr-only class must be defined in theme.css to guarantee
        availability before Bootstrap loads asynchronously (P2.5 fix)."""
        css = _read_file(THEME_CSS_PATH)
        assert ".sr-only" in css, ".sr-only must be defined in theme.css"
        assert ".visually-hidden" in css, ".visually-hidden alias must be defined"

    def test_skip_link_present_in_main_templates(self):
        """A skip-link must be present in each main template for keyboard
        navigation (P3.3 fix). Partials (_footer_nav.html) are excluded."""
        for path in _all_templates():
            name = os.path.basename(path)
            content = _read_file(path)
            # 503.html may not have a skip-link since it's an error page
            # login.html is standalone — check anyway
            assert "Aller au contenu principal" in content or "id=\"app-content\"" in content or "#app-content" in content, (
                f"Template {name} is missing a skip-link"
            )

    def test_main_landmark_on_key_pages(self):
        """Key pages must have a <main> element for landmark navigation (P3.3 fix)."""
        for name in ["login.html", "503.html"]:
            path = os.path.join(TEMPLATES_DIR, name)
            content = _read_file(path)
            assert "<main" in content, f"{name} must have a <main> element"

    def test_history_table_has_scope(self):
        """All <th> elements in history.html must have scope='col' (P3.3 fix)."""
        path = os.path.join(TEMPLATES_DIR, "history.html")
        content = _read_file(path)
        th_tags = re.findall(r"<th\b[^>]*>", content)
        assert len(th_tags) > 0, "history.html must have <th> elements"
        for th in th_tags:
            assert 'scope=' in th, f"<th> missing scope attribute: {th}"

    def test_footer_icons_have_aria_hidden(self):
        """Decorative Font Awesome icons in the footer must have
        aria-hidden='true' (P3.3 fix)."""
        path = os.path.join(TEMPLATES_DIR, "_footer_nav.html")
        content = _read_file(path)
        icon_tags = re.findall(r'<i class="fas [^"]*"[^>]*>', content)
        assert len(icon_tags) > 0, "Footer must have FA icons"
        for tag in icon_tags:
            assert 'aria-hidden="true"' in tag, (
                f"Decorative icon missing aria-hidden: {tag}"
            )

    def test_settings_heading_hierarchy(self):
        """Profil hiver/été and Scènes favorites headings must be h3, not h2, to maintain
        proper heading hierarchy (P3.3 fix)."""
        path = os.path.join(TEMPLATES_DIR, "settings.html")
        content = _read_file(path)
        # Direct check: no h2 containing "Profil" or "Scènes"
        assert not re.search(r"<h2[^>]*>.*?Profil", content), "Profil headings must use h3, not h2"
        assert not re.search(r"<h2[^>]*>.*?Sc\u00e8nes", content), "Scenes headings must use h3, not h2"

    def test_loaders_aria_live_region(self):
        """loaders.js must create an aria-live region for loader announcements
        (P2.1 fix)."""
        source = _read_file(LOADERS_JS_PATH)
        assert "aria-live" in source, "loaders.js must use aria-live for announcements"
        assert "announceLoader" in source or "liveRegion" in source, (
            "loaders.js must have a loader announcement function"
        )

    def test_loaders_no_artificial_delay(self):
        """Form submission must not have a 1-second artificial delay (P3.18 fix)."""
        source = _read_file(LOADERS_JS_PATH)
        # Should use requestAnimationFrame, not setTimeout with 1000
        assert "setTimeout(() =>" not in source or "1000" not in source.split("form.submit")[0][-200:], (
            "Form submission should use requestAnimationFrame, not setTimeout(1000)"
        )
