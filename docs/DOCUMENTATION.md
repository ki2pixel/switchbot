# SwitchBot Dashboard – Documentation Architecture & Metrics

> **Status**: COMPLETED (25 janvier 2026) - Refonte complète terminée
> 
> Generated using the `code-doc` skill (tree, cloc, radon) with Intelligent Exclusion workflow.  
> Scope: `/docs` excluding `archives/`, `audit/`, `IFTTT/`, `__pycache__`, `sticky_mobile_template`.

## Project Vital Signs

- **Files analyzed**: 16 Markdown files (excluding excluded directories)
- **Total lines**: 12,956 (10,578 code, 2,378 blank)
- **Language breakdown**: 100% Markdown
- **Average complexity (code)**: C (18.9) – see Complexity Hotspots below
- **Documentation density**: 660 lines per file (average)

## Architecture

### Directory Structure (annotated)

```
docs/
├── README.md                    # Index maître des guides (à réviser)
├── setup.md                     # Installation & démarrage (fondamental)
├── configuration.md             # Paramètres applicatifs (fondamental)
├── deployment.md                # Déploiement Render + CI/CD (fondamental)
├── testing.md                   # Tests manuels & unitaires (fondamental)
├── ui-guide.md                  # Guide interface utilisateur (UX)
├── theming.md                   # Thème sombre & CSS tokens (UX)
├── frontend-performance.md      # Optimisations UX & loaders (UX)
├── history-monitoring.md        # Dashboard temps réel Chart.js (UX)
├── frontend-mobile-audit.md     # Audit mobile complet (UX)
├── scheduler.md                 # APScheduler & production (backend)
├── postgresql-migration.md      # Migration Neon PostgreSQL (backend)
├── backend-audit-report.md      # Audit backend complet (backend)
├── ifttt-integration.md         # Webhooks & cascade (intégration)
├── switchbot/
│   ├── README.md                # API SwitchBot v1.1 (référence)
│   └── README-v1.0.md          # Ancienne version (à archiver)
├── cloc_stats.json              # Métriques volumétriques (généré)
├── cloc_stats.md                # Rapport lisible cloc (généré)
├── complexity_report.txt        # Hotspots radon (généré)
└── DOCUMENTATION.md             # Ce fichier (centralisation)
```

### File Responsibilities

| File | Primary Audience | Core Purpose |
|------|------------------|--------------|
| `README.md` | All users | Entry point & navigation |
| `setup.md` | Developers | Installation & first run |
| `configuration.md` | Operators | Settings & business logic |
| `deployment.md` | DevOps | Production deployment |
| `testing.md` | QA/Developers | Validation procedures |
| `ui-guide.md` | End users | Interface usage |
| `theming.md` | Frontend devs | CSS architecture |
| `frontend-performance.md` | Frontend devs | UX optimizations |
| `history-monitoring.md` | Users/Operators | Real-time monitoring |
| `frontend-mobile-audit.md` | Frontend devs | Mobile excellence |
| `scheduler.md` | DevOps | APScheduler config |
| `postgresql-migration.md` | DevOps | Database migration |
| `backend-audit-report.md` | Architects | Backend analysis |
| `ifttt-integration.md` | Operators | IFTTT setup |
| `switchbot/README.md` | Developers | API reference |

## Complexity Hotspots

Based on `radon cc` analysis of `switchbot_dashboard/` (excluding tests and templates):

### Critical (E) – Immediate attention
- `routes.py:update_settings` (411 lines) – Settings validation & persistence
- `automation.py:AutomationService.run_once` (658 lines) – Core automation loop

### High (C) – Monitor
- `routes.py:history_api_data` (801 lines) – History API endpoints
- `routes.py:_execute_aircon_action` (600 lines) – IFTTT/scene cascade
- `automation.py:_is_now_in_windows` (26 lines) – Time window logic
- `automation.py:_cooldown_active` (259 lines) – Cooldown management
- `automation.py:_process_off_repeat_task` (432 lines) – OFF repeat queue
- `history_service.py:HistoryService.get_history` (105 lines) – Data retrieval
- `switchbot_api.py:SwitchBotClient._request` (78 lines) – HTTP client
- `switchbot_api.py:SwitchBotClient._capture_quota_metadata` (197 lines) – Quota tracking
- `__init__.py:create_app` (106 lines) – App initialization

### Very High (D) – Architecture concern
- `switchbot_api.py:SwitchBotClient._request` – Core HTTP client with retries

**Documentation implications**: Guides covering these areas must include detailed explanations, troubleshooting sections, and reference to the Memory Bank decisions that shaped the implementation.

## Dependencies

### Core stack (from `requirements.txt`)
- `flask` – Web framework
- `requests` – HTTP client (SwitchBot API)
- `apscheduler` – Task scheduling
- `psycopg[binary]` – PostgreSQL adapter
- `psycopg-pool` – Connection pooling

### Documentation toolchain
- `tree` – Directory structure analysis
- `cloc` – Code counting metrics
- `radon` – Python complexity analysis

### Project references
- `.windsurf/rules/codingstandards.md` – Mandatory coding standards
- `memory-bank/*.md` – Architectural decisions & progress
- `/home/kidpixel/.codeium/skills/code-doc/SKILL.md` – Documentation methodology

## Refactoring Backlog (by priority)

### Phase 1 – Core Documentation (Days 1-2)
1. **README.md** – Transform into proper index with metrics links
2. **setup.md** – Align with coding standards, add troubleshooting
3. **configuration.md** – Map to Memory Bank decisions, simplify flow
4. **deployment.md** – Update with current Render/Neon patterns
5. **testing.md** – Reference pytest commands from standards

### Phase 2 – UX Documentation (Days 3-4)
6. **ui-guide.md** – Include loader patterns, bottom navigation
7. **theming.md** – Reference glassmorphism tokens from standards
8. **frontend-performance.md** – Link to Core Web Vitals optimizations
9. **history-monitoring.md** – Explain Chart.js integration
10. **frontend-mobile-audit.md** – Consolidate audit findings

### Phase 3 – Backend Documentation (Days 5-6)
11. **scheduler.md** – Document APScheduler production patterns
12. **postgresql-migration.md** – Update with Neon best practices
13. **backend-audit-report.md** – Reference complexity hotspots
14. **ifttt-integration.md** – Explain cascade architecture

### Phase 4 – Reference & Cleanup (Day 7)
15. **switchbot/README.md** – Update API v1.1 reference
16. **switchbot/README-v1.0.md** – Mark as legacy or archive

## Validation Checklist

- [x] All guides reference `.windsurf/rules/codingstandards.md`
- [x] Each guide includes "Decisions connexes" section with Memory Bank links
- [x] No references to excluded directories (`archives/`, `audit/`, `IFTTT/`)
- [x] Internal links verified with `markdown-link-check`
- [x] Markdown linted with `markdownlint`/`mdformat`
- [x] `cloc_stats.json` and `complexity_report.txt` referenced where relevant
- [x] Complexity hotspots have dedicated explanations in related guides
- [x] Memory Bank updated with refactoring progress
- [x] French terminology consistent across all documents

---

## Résumé de la refonte

**Phase 1 – Core Documentation** ✅ (5 fichiers)
- README.md, setup.md, configuration.md, deployment.md, testing.md

**Phase 2 – UX Documentation** ✅ (5 fichiers)
- ui-guide.md, theming.md, frontend-performance.md, history-monitoring.md, frontend-mobile-audit.md

**Phase 3 – Backend Documentation** ✅ (4 fichiers)
- scheduler.md, postgresql-migration.md, backend-audit-report.md, ifttt-integration.md

**Phase 4 – Reference & Cleanup** ✅ (2 fichiers)
- switchbot/README.md (v1.1), switchbot/README-v1.0.md (legacy)

**Total : 16 fichiers refaits** avec structure uniforme, références croisées, et conformité aux standards.

---

*Generated: 2026-01-25*  
*Methodology: code-doc skill with Intelligent Exclusion*  
*Scope: 16 files, 10,578 lines of documentation*  
*Status: COMPLETED*
