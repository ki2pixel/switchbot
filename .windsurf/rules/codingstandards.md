---
trigger: always_on
description: 
globs: 
---

---
description: Core Cursor rule for SwitchBot Dashboard v2 (Flask + offline-first frontend)
globs: ["**/*.py", "**/*.html", "**/*.js", "**/*.css"]
alwaysApply: true
---

# SwitchBot Dashboard v2 – Cursor Coding Standards

## Tech Stack
- **Backend**: Flask 2.x, APScheduler, custom services (`AutomationService`, `SchedulerService`), HMAC-signed SwitchBot REST client, IFTTT webhook client, ApiQuotaTracker, and HistoryService when PostgreSQL is available @switchbot_dashboard/__init__.py
- **Storage**: `PostgresStore` (primary) with psycopg_pool, automatic fallback to `JsonStore`; Redis backend is deprecated but still guarded @switchbot_dashboard/__init__.py
- **Frontend**: Jinja templates + Bootstrap bundle served from `static/vendor`, Chart.js with LTTB decimation, loaders.js pour le feedback UX, Space Grotesk, dark glassmorphism design tokens @switchbot_dashboard/templates/index.html @switchbot_dashboard/static/css/theme.css
- **Testing**: Pytest via `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest`, 85% coverage target avec focus automation/IFTTT/history/quota @docs/testing.md

## Code Style
- Always enable `from __future__ import annotations`, strict typing, and explicit return types for public APIs @switchbot_dashboard/__init__.py @switchbot_dashboard/automation.py
- Follow PEP 8 import order: stdlib → third-party → local modules (voir usage dans `switchbot_dashboard/__init__.py`)
- Keep functions single-responsibility; extract helpers (_as_bool/_as_int/_as_float) for input validation, never use `request.form` raw @switchbot_dashboard/routes.py
- Comments must describe WHY, not HOW; remove dead/commented code immédiatement (standard projet)
- Prefer descriptive names (`meter_device_id`, `assumed_aircon_power`) over abbreviations (convention projet)

## Project Structure
| Area | Responsibility |
| --- | --- |
| `app.py` | Bootstraps Flask app via `switchbot_dashboard.create_app()` |
| `switchbot_dashboard/__init__.py` | Wiring of stores, services, scheduler, and initial meter poll @switchbot_dashboard/__init__.py |
| `switchbot_dashboard/automation.py` | Core automation loop, hysteresis, IFTTT/scenes cascade, history recording @switchbot_dashboard/automation.py |
| `switchbot_dashboard/routes.py` | UI routes, settings validation, manual actions, history APIs @switchbot_dashboard/routes.py |
| `switchbot_dashboard/static/` | Offline-first assets (Bootstrap, FontAwesome, loaders, history charts) |
| `templates/*.html` | Dark themed pages with bottom navigation, loaders, quota banners @switchbot_dashboard/templates/index.html |

## Backend Patterns
### Store Selection & Failover
- Default to `PostgresStore`; log `[store]` errors and fall back to filesystem when `POSTGRES_URL`/health checks fail. Never call `open()` directly—access stores via `current_app.extensions["settings_store"|"state_store"]` @switchbot_dashboard/__init__.py.
- Redis is legacy-only; emit warnings and plan migration to PostgreSQL @switchbot_dashboard/__init__.py.

### Automation Cascade & Hysteresis
- Each scheduler tick (`AutomationService.run_once`) evaluates time windows, mode profiles, hysteresis, cooldowns, pending OFF repeats, and prioritizes IFTTT webhooks → SwitchBot scenes → direct device commands before taking action @switchbot_dashboard/automation.py.
- OFF automation outside windows must honor idempotence: skip when `assumed_aircon_power == "off"` and guard repeated OFF queues @switchbot_dashboard/automation.py.

#### Example – Time Window & OFF Automation
```python
in_window = _is_now_in_windows(time_windows, now)
if not in_window:
    self.poll_meter()
    if settings.get("turn_off_outside_windows", False):
        state = self._state_store.read()
        if state.get("assumed_aircon_power") == "off":
            self._debug("Skipping off automation outside window: already assumed off", trigger=trigger)
        elif self._cooldown_active(now):
            self._debug("Cooldown active, skipping off automation outside window", trigger=trigger)
        else:
            handled = self._perform_off_action(...)
            if handled:
                self._schedule_off_repeat_task(now, state_reason="automation_off_outside_window")
```
@switchbot_dashboard/automation.py

### IFTTT + Scene Execution
- `extract_ifttt_webhooks` and `extract_aircon_scenes` drive cascaded execution; `_execute_aircon_action` also follows webhook → scene → direct `turnOff` fallback while updating state store with reasons for observability @switchbot_dashboard/routes.py.
- Validate webhook URLs (HTTPS-only) and log failures; all manual and automated flows share the same cascade ensuring consistent quota usage @switchbot_dashboard/automation.py @switchbot_dashboard/routes.py.

### Scheduler & Services
- Inject services once in `create_app()` and stash them under `current_app.extensions` so blueprints never instantiate their own clients @switchbot_dashboard/__init__.py.
- Scheduler obeys `SCHEDULER_ENABLED` and avoids running inside Flask reloader parent; always call `scheduler_service.reschedule()` after settings mutations @switchbot_dashboard/__init__.py @switchbot_dashboard/routes.py.

### History & Quota Tracking
- HistoryService only initializes when the settings store is PostgreSQL; failures are logged but must not crash the app @switchbot_dashboard/__init__.py.
- Automation ticks record snapshots and cleanup 6h-old rows; quota snapshots are logged around every API request @switchbot_dashboard/automation.py.

## Frontend & UX
- Strict offline-first: ship Bootstrap, Chart.js, FontAwesome, and Space Grotesk from `static/vendor`; CDNs are forbidden @switchbot_dashboard/templates/index.html @switchbot_dashboard/static/css/theme.css.
- Keep HTML/Jinja and CSS separate (`theme.css`, page-specific sheets); only inline critical CSS for LCP improvements @switchbot_dashboard/templates/index.html.
- Always wrap interactions with loaders (POST forms, buttons, nav links) using `data-loader` + `static/js/loaders.js` to ensure 15s failsafe and spinner feedback @switchbot_dashboard/static/js/loaders.js.
- Chart.js visualizations must enable LTTB decimation and mobile-friendly height (≈180px) @switchbot_dashboard/templates/index.html @switchbot_dashboard/static/js/history.js.
- Bottom navigation stays sticky with icon-only mobile layout; page `actions.html` consolidates manual triggers @switchbot_dashboard/templates/index.html @switchbot_dashboard/templates/actions.html.

#### Example – Critical Jinja Structure (Quota Banner + Status Grid)
```html
<div class="quota-banner" role="status" aria-live="polite">
  <div class="quota-banner__main">
    <strong>Quota API restant</strong>
    <span class="text-muted">{{ quota.remaining }} requêtes</span>
  </div>
  <div>
    <span class="badge bg-warning">Reset {{ quota.reset_at }}</span>
  </div>
</div>
<section class="status-grid">
  {% for card in status_cards %}
    <article class="status-item" aria-live="polite">
      <h6>{{ card.label }}</h6>
      <p class="h4">{{ card.value }}</p>
    </article>
  {% endfor %}
</section>
```
@switchbot_dashboard/templates/index.html

#### Example – Loader Failsafe JS Pattern
```javascript
const FAILSAFE_TIMEOUT_MS = 15000;
const scheduleLoaderFailsafe = (element, cleanupCallback) => {
    clearLoaderFailsafe(element);
    const timerId = window.setTimeout(() => {
        loaderFailsafes.delete(element);
        cleanupCallback();
    }, FAILSAFE_TIMEOUT_MS);
    loaderFailsafes.set(element, timerId);
};
form.addEventListener('submit', (event) => {
    const submitButton = form.querySelector('button[type="submit"]');
    event.preventDefault();
    showGlobalLoader();
    showLoader(submitButton);
    submitButton.textContent = 'Chargement...';
    submitButton.disabled = true;
    setTimeout(() => { form.submit(); }, 1000);
    scheduleLoaderFailsafe(submitButton, finalizeSubmission);
});
```
@switchbot_dashboard/static/js/loaders.js

#### Example – Glassmorphism Token Definition
```css
:root {
  color-scheme: dark;
  --sb-card: rgba(9, 14, 30, 0.92);
  --sb-card-border: rgba(138, 180, 255, 0.2);
  --sb-glass-bg: rgba(255, 255, 255, 0.05);
  --sb-glass-border: rgba(255, 255, 255, 0.1);
  --sb-glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  --sb-bottom-nav-height: 60px;
  --sb-bottom-nav-shadow: 0 -4px 20px rgba(0, 0, 0, 0.3);
}
```
@switchbot_dashboard/static/css/theme.css

## Testing & Quality
- Run the canonical Pytest command and keep coverage ≥85%; prioritize unit coverage pour conversions/validators, integration coverage pour le flux automation → DB → UI @docs/testing.md.
- Critical scenarios: Postgres ↔ JsonStore failover, API quota 429 simulation, IFTTT webhook fallback tree, history batch flush & Chart.js rendering @docs/testing.md.
- Lint/log hygiene: use `[scheduler]`, `[api]`, `[history]`, `[store]` prefixes and never log secrets (voir `switchbot_dashboard/__init__.py` logging section).

## Anti-Patterns
1. **Direct filesystem IO**: Never `open()` config/state—always go through BaseStore @switchbot_dashboard/__init__.py.
2. **Bypassing loaders**: All POST/actions without loaders.js regress UX requirements; enforce `data-loader` attributes @switchbot_dashboard/static/js/loaders.js.
3. **CDN dependencies**: Importing Bootstrap/Chart.js/FontAwesome from CDN violates offline-first contract; serve from `static/vendor` only @switchbot_dashboard/templates/index.html.
4. **Scene commands without cascade**: Always honor webhook → scene → direct command to preserve quotas and observability @switchbot_dashboard/routes.py.

## Common Tasks
| Tâche | Étapes |
| --- | --- |
| Lancer la suite Pytest | 1. `source /mnt/venv_ext4/venv_switchbot/bin/activate` <br> 2. `python -m pytest` <br> 3. Vérifier ≥85% de couverture et corriger les régressions @docs/testing.md |
| Ajouter une action IFTTT/Scène | 1. Ouvrir `/settings` et fournir les URLs HTTPS + IDs de scène (`winter/summer/fan/off`). <br> 2. Valider via `_as_*` helpers (automatic). <br> 3. Déployer; vérifier `_execute_aircon_action` cascade et flashs côté UI @switchbot_dashboard/routes.py |
| Instrumenter un nouveau bouton avec loader | 1. Ajouter `data-loader` sur `<form>`/`<button>`/`<a>`. <br> 2. Importer `loaders.js` si page nouvelle. <br> 3. Vérifier overlay + failsafe 15s et `aria-busy` @switchbot_dashboard/static/js/loaders.js |
| Diagnostiquer un tick d'automatisation | 1. Inspecter `state.json` via store (`state_store.read()`). <br> 2. Consulter logs `[automation]` pour outcome (`_log_tick_completion`). <br> 3. Confirmer history snapshot/cleanup si Postgres actif @switchbot_dashboard/automation.py |

---
Utilise ce fichier comme source principale pour les assistants Cursor : il capture les décisions d'architecture critiques, fournit des extraits prêts à l'emploi et rappelle les pièges à éviter. Copie ce contenu dans `.windsurf/rules/codingstandards.md` lorsque tu dois synchroniser les règles Always-On.