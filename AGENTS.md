# AGENTS.md - Core Project Instructions for Codex

## 1. Tech Stack & Architecture
- **Backend**: Flask 2.x/3.x + APScheduler, services injected via `app.extensions` (`AutomationService`, `SchedulerService`, `ApiQuotaTracker`, `HistoryService`). Secured with `Flask-WTF` (CSRF) and `Flask-Limiter`.
- **Database**: `PostgresStore` (preferred) using `psycopg_pool`, fallback to `JsonStore` in case of Postgres failure.
- **Frontend**: Jinja templates, offline-first assets in `static/vendor` (no CDN allowed), Chart.js with LTTB decimation.
- **SPA Router**: Intercept clicks via `spa-router.js` without full page reload. Re-bind listeners during page transitions.
- **CSRF**: Automate CSRF token injection in global Fetch/XHR interceptors.

## 2. Store & Connection Management
- **Postgres Failover**: Log `[store]` issues, retry in scheduler, alert if >3 consecutive failures before fallback.
- **Pool Management**: Explicitly manage transaction contexts from `psycopg_pool`. Always ensure connections are released using `with self.pool.connection() as conn:` or equivalent.

## 3. Automation & API Integration
- **Cascade**: Tick calls evaluate timezone windows, hysteresis, cooldowns, and execute cascade: Scrapes -> Scenes -> Direct commands.
- **IFTTT**: (Deprecated/Removed) IFTTT integration is no longer part of this product. Ignore any legacy documentation or security expectations related to it.
- **Quotas**: Track API quotas around every request using `ApiQuotaTracker`. Refresh quotas using `get_devices`.

## 4. Frontend & UX Standards
- **Offline First**: All assets (Bootstrap, FontAwesome, Chart.js) must be local in `static/vendor`.
- **Loaders**: Interactive elements and forms must use `data-loader` from `static/js/loaders.js` (15s failsafe, `aria-busy`).
- **CSS**: Separate critical inline CSS (LCP) from `theme.css` and page-specific stylesheets.

## 5. Memory Bank Protocol (Codex Adaptive)
- **Selective Pull**: Only load `/home/kidpixel/SwitchBot/memory-bank/activeContext.md` first. Only load `productContext.md` or `systemPatterns.md` if the task requires deep design/architecture.
- **File Structure**:
  - `activeContext.md`: Session state, next steps, active blockers.
  - `progress.md`: Work status (completed, in progress, next).
  - `decisionLog.md`: Technical choices, rationale, alternatives.
  - `systemPatterns.md`: Design patterns, architecture.
  - `productContext.md`: Overall scope, target user, goals.
- **Writing**: Update memory bank at task completion or on `UMB` command. Always log with timestamp `[YYYY-MM-DD HH:MM:SS] - [Summary]`.
- **Paths**: Always use absolute paths in `/home/kidpixel/SwitchBot/memory-bank/`.

## 6. Security & Execution Guidelines
- **Input Validation**: Strictly validate inputs with `_as_int`, `_as_bool`, `_as_float`.
- **Secrets**: Never hardcode API keys or passwords. Use environment variables.
- **SSRF**: Strictly block private IP resolutions and local loopbacks in webhook URLs.
- **Sandboxing & Commands**:
  - Never execute `cd` commands.
  - Run pytest with: `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest`.
  - Starlark rules in `.codex/rules/development.rules` define pre-approved commands.

## 7. Destructive Operations Protocol
- For destructive actions (deletions, bulk edits, DB wipes):
  1. Present a dry-run target list/hierarchy.
  2. Clarify the impact scope and top examples.
  3. Obtain explicit confirmation: "Do you want to execute this operation?".
- Absolutely reject any out-of-root writes, deletions in `.git/`, `.env`, or operations with parent references `..`.
