# SwitchBot Dashboard - Agent Guide

> **AI Agent Context**: This document provides essential information for AI coding agents working on the SwitchBot Dashboard project. The dashboard is a Flask-based home automation system for controlling SwitchBot smart devices (thermometers and air conditioners).

---

## Project Overview

SwitchBot Dashboard is a Python web application that automates climate control using SwitchBot IoT devices. It monitors temperature/humidity via SwitchBot Meter devices and controls air conditioning units based on configurable thresholds, time windows, and seasonal modes (winter/summer).

### Key Capabilities

- **Temperature-based automation**: Turn AC on/off based on min/max thresholds with hysteresis
- **Three-tier action cascade**: IFTTT webhooks → SwitchBot scenes → Direct device commands
- **API quota tracking**: Local quota estimation (SwitchBot API doesn't expose quota headers)
- **Timezone-aware scheduling**: Configurable time windows with IANA timezone support
- **Historical monitoring**: 6-hour data retention with Chart.js visualization
- **Adaptive polling**: Dynamic interval adjustment based on activity windows

## 🧠 Operational Skills & Runbooks (The Router)

When dealing with specific tasks, you **MUST** consult the specialized runbooks located in `.sixthskills/`. Use this table to route each request and explicitly state “Applying methodology from [Skill Name]...” before execution.

| Context / User Intent | Target Skill File (load with @) | Key Focus |
|:---|:---|:---|
| **Bug / Error / Crash** | `.sixthskills/debugging-strategies/SKILL.md` | Scientific method, log analysis, reproduction |
| **New Feature / Add capability** | `.sixthskills/add-feature/SKILL.md` | Service injection, route validation, UI loaders |
| **Performance / Slow / LCP** | `.sixthskills/performance-audit-runbook/SKILL.md` | Critical CSS, resource hints, LTTB decimation |
| **Database / Migration / Store** | `.sixthskills/postgres-store-maintenance/SKILL.md` | PostgresStore health, JsonStore fallback |
| **API / Quota / HMAC** | `.sixthskills/switchbot-api-dev/SKILL.md` | HMAC signature, X-RateLimit headers |
| **Automation / Schedule / Tick** | `.sixthskills/automation-diagnostics/SKILL.md` | Time windows, hysteresis, off-repeat logic |
| **Frontend / UI / Loader** | `.sixthskills/loader-patterns/SKILL.md` | `data-loader`, `loaders.js`, ARIA attributes |
| **History / Charts** | `.sixthskills/history-dashboard-updater/SKILL.md` | LTTB decimation, batch flush, Chart.js config |

### Global Skills Fallback (when no local skill matches)

If no `.sixthskills/` skill matches the task, use global skills in this priority order:

| Priority | Domain | Skills (load from `/home/kidpixel/.codeium/skills`) |
|----------|--------|---------------------------------------------------|
| 1 | Backend/DB | `python-backend-architect`, `python-coding-standards`, `python-db-migrations`, `postgres-expert` |
| 2 | Frontend/UI | `frontend-design`, `css-layout-development`, `ui-component-builder`, `interaction-design-patterns`, `modern-vanilla-web` |
| 3 | Platform/Ops/Docs | `devops-sre-security`, `architecture-tools`, `code-doc` |
| 4 | Specialized | `html-tools`, `media-ai-pipeline`, `pdf-toolbox`, `engineering-features-for-machine-learning`, `slack-gif-creator` (explicit request only) |

**Exclusions**: Never use `algorithmic-art`, `canvas-design`, or any artistic skill outside product scope.

---

## Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Runtime | Python | 3.11+ |
| Web Framework | Flask | 2.3+ |
| Scheduler | APScheduler | 3.10+ |
| HTTP Client | requests | 2.31+ |
| Database | PostgreSQL (psycopg) | 3.2+ |
| Connection Pool | psycopg-pool | 3.3+ |
| Server | Gunicorn | 21.2+ |
| Container | Docker | - |

---

## Project Structure

```
/home/kidpixel/SwitchBot/
├── app.py                          # Application entry point
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container image definition
├── gunicorn.conf.py               # Gunicorn production config
├── .env.example                   # Environment variable template
├── repomix.config.json            # Code bundling configuration
│
├── switchbot_dashboard/           # Main application package
│   ├── __init__.py                # Flask app factory, store initialization
│   ├── routes.py                  # Flask blueprints (1000+ lines)
│   ├── automation.py              # Core automation service (934 lines)
│   ├── scheduler.py               # APScheduler wrapper service
│   ├── switchbot_api.py           # SwitchBot API v1.1 client
│   ├── config_store.py            # Storage abstraction (JSON, Redis)
│   ├── postgres_store.py          # PostgreSQL backend implementation
│   ├── history_service.py         # Historical data collection
│   ├── quota.py                   # API quota tracking
│   ├── ifttt.py                   # IFTTT webhook client
│   ├── aircon.py                  # Aircon constants/labels
│   ├── templates/                 # Jinja2 HTML templates
│   │   ├── index.html             # Dashboard home
│   │   ├── settings.html          # Configuration page
│   │   ├── history.html           # Historical charts
│   │   ├── actions.html           # Manual controls
│   │   ├── devices.html           # Device listing
│   │   └── quota.html             # Quota status
│   └── static/                    # Static assets
│       ├── css/
│       ├── js/
│       └── vendor/                # Bootstrap, Chart.js
│
├── tests/                         # pytest test suite
│   ├── conftest.py                # Test fixtures (auto-mocks PostgreSQL)
│   ├── test_app_init.py
│   ├── test_automation_service.py
│   ├── test_dashboard_routes.py
│   ├── test_scheduler_service.py
│   ├── test_history_service.py
│   ├── test_postgres_store.py
│   ├── test_ifttt.py
│   └── ...
│
├── config/                        # Runtime configuration
│   ├── settings.json              # User settings (device IDs, thresholds)
│   └── state.json                 # Runtime state (temperature, quota)
│
├── docs/                          # Documentation (French)
│   ├── README.md                  # Documentation index
│   ├── core/                      # Getting started guides
│   ├── architecture/              # Technical deep dives
│   ├── guides/                    # User guides
│   └── ops/                       # Operations & troubleshooting
│
├── scripts/                       # Utility scripts
│   └── migrate_to_postgres.py     # Data migration tool
│
└── .github/workflows/             # CI/CD
    └── build-and-push.yml         # Docker build + Render deploy
```

---

## Configuration

### Environment Variables (`.env`)

```bash
# Required: SwitchBot API v1.1 credentials
SWITCHBOT_TOKEN=your_token_here
SWITCHBOT_SECRET=your_secret_here

# Retry configuration
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10

# Polling configuration
SWITCHBOT_POLL_INTERVAL_SECONDS=60

# Scheduler control
SCHEDULER_ENABLED=true

# Flask settings
FLASK_SECRET_KEY=change-me
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
FLASK_DEBUG=0

# Storage backend: postgres (recommended) or filesystem
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:pass@host:5432/db?sslmode=require
POSTGRES_SSL_MODE=require

# Timezone (IANA identifier)
TIMEZONE=Europe/Paris
```

### Settings File (`config/settings.json`)

Key configuration sections:
- `automation_enabled`: Master switch for automation
- `mode`: "winter" or "summer" operation mode
- `poll_interval_seconds`: Base polling frequency (min 15s)
- `hysteresis_celsius`: Temperature buffer to prevent oscillation
- `winter`/`summer`: Mode-specific temperature thresholds and AC settings
- `time_windows`: Array of {days, start, end} for active periods
- `meter_device_id`: SwitchBot Meter device ID
- `aircon_device_id`: Air conditioner device ID
- `aircon_scenes`: Scene IDs for winter/summer/fan/off actions
- `ifttt_webhooks`: Webhook URLs for IFTTT integration

---

## Build and Test Commands

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your credentials
```

### Running the Application

```bash
# Development mode
python app.py

# Production mode (with Gunicorn)
gunicorn -c gunicorn.conf.py 'switchbot_dashboard:create_app()'

# Docker
docker build -t switchbot-dashboard .
docker run -p 8000:8000 --env-file .env switchbot-dashboard
```

### Testing

```bash
# Canonical command (always use this)
source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest

# With coverage
source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest --cov=switchbot_dashboard --cov-report=term-missing

# Run specific test file
source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest tests/test_automation_service.py -v

# Run with verbose output
source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest -v --tb=short
```

#### Critical Test Scenarios (must cover)
- Bascule PostgresStore ↔ JsonStore
- API quota handling (429 responses)
- IFTTT → scenes → commands cascade
- HistoryService batch flush + Chart.js rendering
- Scheduler resilience (`reschedule()` when store unavailable)

#### Test Quality Target
- Minimum 85% coverage
- Focus: automation/IFTTT/history/quota tests
- Log hygiene: prefixes `[scheduler]`, `[api]`, `[history]`, `[store]`

> **Note**: Tests automatically mock PostgreSQL connections via `conftest.py`. Only `test_postgres_store.py` attempts real connections.

### Health Check

```bash
# Verify application health
curl http://localhost:5000/healthz

# Expected response:
# {"status": "ok", "scheduler_running": true, "automation_enabled": true, ...}
```

### 🛠️ Diagnostic Scripts (Run via CLI)

- **Snapshot State**: `python .sixthskills/automation-diagnostics/scripts/state_snapshot.py`
- **Check Scheduler**: `python .sixthskills/scheduler-ops/scripts/scheduler_snapshot.py`
- **Check Quota**: `python .sixthskills/quota-alerting/scripts/quota_snapshot.py`
- **Preview API Headers**: `python .sixthskills/switchbot-api-dev/scripts/preview_headers.py`

---

## 🛡️ Critical Implementation Rules (Non-Negotiable)

### 1. Backend Architecture
- **Service Injection Only**: Never instantiate services or HTTP clients inside routes; retrieve them from `current_app.extensions[...]`.
- **Storage Discipline**: `PostgresStore` (Neon) is mandatory. `JsonStore` is allowed solely as emergency fallback when Postgres is unavailable.
- **Input Validation**: Always funnel user input through `_as_bool`, `_as_int`, `_as_float`. Direct `request.form` access is forbidden.

### 2. Frontend & UX (Offline-First)
- **Zero CDN Policy**: Serve Bootstrap, Chart.js, Font Awesome, fonts, and utilities from `switchbot_dashboard/static/vendor/`.
- **Loader Pattern**: Every POST/form/link triggering actions must include `data-loader` to activate the 15 s failsafe overlay handled by `static/js/loaders.js`.
- **CSS Hygiene**: No inline styles (outside critical CSS). Persist styles in `static/css/theme.css` or dedicated stylesheets.

### 3. Automation Logic
- **Hysteresis Enforcement**: Respect `settings["hysteresis_celsius"]` to prevent oscillation.
- **Cascade Protocol**: Execute actions strictly in order: IFTTT Webhook → SwitchBot Scene → Direct Command.
- **Timezone Discipline**: Use the configured `TIMEZONE` (IANA) for every schedule calculation; never rely on server locale.

> These guardrails supersede any conflicting guidance. Deviations require explicit approval plus updates to `.sixthrules/01-coding-standards.md` and Memory Bank logs.

---

## 🎯 Code Style Guidelines

- **Typing strict**: `from __future__ import annotations` + explicit return types on public APIs
- **Import order**: PEP 8 (stdlib → third-party → local modules)
- **Single responsibility**: Functions should do one thing; use `_as_bool/_as_int/_as_float` instead of raw `request.form`
- **Comments explain why**: Delete dead/commented code immediately; comments explain rationale, not mechanics
- **Descriptive naming**: Use clear names like `meter_device_id`, `assumed_aircon_power`

## 🚫 Anti-Patterns (Never Do These)

1. **Direct file IO**: Never use `open()` on config/state files; use stores instead
2. **POST/actions without loaders**: UX regression; always include `data-loader`
3. **CDN dependencies**: Violates offline-first; serve from `static/vendor`
4. **Incomplete scene cascade**: Missing webhook → scene → direct flow loses quota/observability

---

## Testing Strategy

### Test Architecture

| Layer | Purpose | Examples |
|-------|---------|----------|
| Unit | Validators, converters | `_as_bool`, `_as_int`, `_as_float` |
| Integration | Service interactions | IFTTT→scenes→commands cascade |
| E2E | UI, quotas, resilience | Route handlers, health checks |

### Key Test Patterns

1. **Mock external services**: Never call real SwitchBot API or IFTTT in tests
2. **Use fixtures**: Shared setup in `conftest.py` (auto-mocks PostgreSQL)
3. **Test cascade logic**: Verify IFTTT→scene→command fallback behavior
4. **Validate state transitions**: Check state.json updates after actions
5. **Test timezone handling**: Use fixed UTC datetimes, not `datetime.now()`

### Critical Test Scenarios

- Automation with/without time windows
- Cooldown periods between actions
- Hysteresis temperature thresholds
- Off-repeat scheduling logic
- Quota tracking and reset
- Store failover (PostgreSQL → JSON)

---

## Security Considerations

### Secrets Management

- **NEVER** commit `.env` files (see `.gitignore`)
- Store tokens only in environment variables
- Use `STATE_DEBUG_TOKEN` for debug endpoint access control
- `FLASK_SECRET_KEY` must be changed in production

### API Security

- SwitchBot API uses HMAC-SHA256 authentication (handled in `switchbot_api.py`)
- IFTTT webhooks validate HTTPS URLs only
- Debug state endpoint (`/debug/state`) requires token authentication

### Input Validation

- All form inputs validated in `routes.py` with `_as_int`, `_as_float`, `_as_bool`
- Timezone validated against IANA database
- Device IDs sanitized (strip whitespace)
- Webhook URLs validated (HTTPS scheme required)

---

## Deployment

### Docker

```bash
docker build -t ghcr.io/ki2pixel/switchbot:latest .
docker push ghcr.io/ki2pixel/switchbot:latest
```

### Render (Configured via GitHub Actions)

Pushes to `main` branch automatically:
1. Build Docker image
2. Push to GitHub Container Registry
3. Trigger Render deployment via API

Required secrets:
- `RENDER_API_KEY`
- `RENDER_SERVICE_ID`

### Gunicorn Configuration

- Single worker (`workers=1`) to prevent APScheduler conflicts
- 2 threads for I/O-bound operations
- 120s timeout for SwitchBot API calls
- Logs to stdout/stderr

---

## Architecture Notes

### Automation Cascade

When automation triggers an action, the system tries in order:

1. **IFTTT Webhook** - Zero quota cost, external automation
2. **SwitchBot Scene** - Native app configurations
3. **Direct Command** - `setAll` or `turnOff` as last resort

### Adaptive Polling

The `SchedulerService` adjusts polling intervals:
- **In window**: Base interval (default 60s)
- **Warmup**: Base interval (15 min before window starts)
- **Idle**: Extended interval (default 600s) outside windows
- **Off-repeat pending**: Base interval (ensure timely repeat)

### State Management

Runtime state persisted across restarts:
- `last_temperature`, `last_humidity`: Latest sensor readings
- `assumed_aircon_power`: Tracked AC state (on/off/unknown)
- `api_requests_total`, `api_requests_remaining`: Quota tracking
- `pending_off_repeat`: Scheduled repeat-off tasks

---

## Troubleshooting

### Common Issues

1. **Scheduler not starting**: Check `SCHEDULER_ENABLED=true` and Flask debug mode
2. **PostgreSQL connection fails**: Falls back to JSON files automatically
3. **Quota warnings**: Monitor via dashboard banner or `/quota` endpoint
4. **Temperature stale**: Check meter device ID and API credentials
5. **Automation not triggering**: Verify time windows and timezone settings

### Debug Endpoints

- `/healthz` - System health status
- `/debug/state?token=XXX` - Raw state dump (requires `STATE_DEBUG_TOKEN`)

### Log Analysis

Filter logs by component:
```bash
tail -f app.log | grep "\[automation\]"
tail -f app.log | grep "\[scheduler\]"
tail -f app.log | grep "\[postgres\]"
```

---

## 💾 Memory Bank Protocol

The project relies on persistent context stored in `memory-bank/`.

1. **Start of Task**: Read `memory-bank/activeContext.md` (plus other core files) to align on current objectives and constraints.
2. **End of Task**: If anything changed, you MUST update:
   - `memory-bank/progress.md` — task status and outcomes.
   - `memory-bank/decisionLog.md` — any architectural or process decision.
   - `memory-bank/activeContext.md` — recent changes, open issues, next steps.

---

## 📝 Documentation Workflow

Whenever you create or modify documentation (README, docs/, guides Markdown), you **must** apply the methodology defined in `.windsurf/skills/documentation/SKILL.md`:

- **TL;DR first**: 1-2 sentences, bold key insight
- **Problem-first opening**: Drop reader into pain scenario, not definitions
- **❌/✅ comparison blocks**: Show bad then good code
- **Trade-off tables**: Summarize approach comparisons
- **Golden Rule**: One memorable principle at the end

> **Reference**: See `.windsurf/skills/documentation/SKILL.md` for the complete checklist before writing.

---

## Documentation

All documentation is in French and organized by purpose:

| Directory | Content |
|-----------|---------|
| `docs/core/` | Getting started, configuration, deployment |
| `docs/architecture/` | Automation engine, scheduler, storage, quotas |
| `docs/guides/` | UI navigation, IFTTT setup, monitoring |
| `docs/ops/` | Testing strategy, troubleshooting, performance |

---

## Language Note

The project documentation and UI text are primarily in **French**. Code comments and docstrings may use English or French. Variable names and code structure use English.
