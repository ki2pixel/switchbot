# AGENTS.md - Core Project Instructions for Codex

## 1. Tech Stack & Architecture
- **Backend**: Flask 2.x/3.x + APScheduler, services injected via `app.extensions` (`settings_store`, `state_store`, `switchbot_client`, `automation_service`, `scheduler_service`, `quota_tracker`; `history_service` only when PostgreSQL is the primary store). Secured with `Flask-WTF` (CSRF) and `Flask-Limiter`.
- **Database**: `PostgresStore` (preferred) via `psycopg_pool`. `JsonStore` is the fallback **outside production**; in production a boot failure raises, and a runtime failure triggers `ResilientStore` alerting + `503` unless `STORE_RUNTIME_FALLBACK=true`.
- **Frontend**: Jinja templates, offline-first assets in `static/vendor` (no CDN allowed), Chart.js with LTTB decimation.
- **SPA Router**: `loaders.js` intercepts `a[data-loader]` clicks and delegates to `spa-router.js`, which swaps `#app-content` and re-executes page scripts without a full reload.
- **CSRF**: Automate CSRF token injection in global Fetch/XHR interceptors.

## 2. Store & Connection Management
- **Postgres Failover**: `ResilientStore` logs `[store]` issues, emits `CRITICAL` at `STORE_FAILURE_THRESHOLD` (default 3) consecutive failures, and switches to JSON only when allowed (non-production or `STORE_RUNTIME_FALLBACK=true`); otherwise routes keep returning `503`.
- **Pool Management**: Explicitly manage transaction contexts from `psycopg_pool`. Always ensure connections are released using `with self.pool.connection() as conn:` or equivalent.
- **Worker deployment**: `run_worker.py` starts a standalone scheduler process with `SCHEDULER_ENABLED=true`; use it when the web service runs with `SCHEDULER_ENABLED=false` (see `docs/core/deployment.md`).

## 3. Automation & API Integration
- **Cascade**: Tick calls evaluate timezone windows, hysteresis, cooldowns, and off-repeat, then execute Scenes (`aircon_scenes`) → Direct commands (`send_command`), with OFF idempotence.
- **Scheduler**: `SchedulerService` supports adaptive polling (`in_window`, `warmup`, `idle`, `pending_off_repeat`, `fixed`) and must be rescheduled after settings mutations.
- **IFTTT**: (Deprecated/Removed) IFTTT integration is no longer part of this product. Ignore any legacy documentation or security expectations related to it.
- **Quotas**: Track API quotas around every request with `ApiQuotaTracker`; quota headers are captured on every response, and `get_devices` is a common refresh path.

## 4. Frontend & UX Standards
- **Offline First**: All assets (Bootstrap, FontAwesome, Chart.js, Space Grotesk) must be local in `static/vendor`.
- **Loaders**: Network/navigation interactive elements and forms must use `data-loader` from `static/js/loaders.js` (15s failsafe, `aria-busy`); purely local actions may skip it.
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
- **Input Validation**: Use `_safe_int`, `_safe_bool`, `_safe_float` from `utils.py` (aliased as `_as_*` in `routes.py`) instead of raw `request.form`.
- **Secrets**: Never hardcode API keys or passwords. Use environment variables.
- **SSRF**: Reject non-HTTPS URLs, credentials-in-URL, local hostnames, and private/loopback/reserved IPs for operator-provided `SwitchBotClient.base_url`.
- **Sandboxing & Commands**:
  - Never execute `cd` commands.
  - Run pytest with: `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest`.
  - Project rules live in `.agents/rules/*.md` (the legacy `.codex/rules/development.rules` was removed).

## 7. Destructive Operations Protocol
- For destructive actions (deletions, bulk edits, DB wipes):
  1. Present a dry-run target list/hierarchy.
  2. Clarify the impact scope and top examples.
  3. Obtain explicit confirmation: "Do you want to execute this operation?".
- Absolutely reject any out-of-root writes, deletions in `.git/`, `.env`, or operations with parent references `..`.
