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
- **Backend** : Flask 2.x + APScheduler, services injectés (`AutomationService`, `SchedulerService`, `ApiQuotaTracker`, `HistoryService`).
- **Stockage** : `PostgresStore` (prioritaire) via psycopg_pool, fallback `JsonStore`. Redis conservé uniquement en compat.
- **Frontend** : Templates Jinja, assets offline-first depuis `static/vendor`, Chart.js avec décimation LTTB, loaders obligatoires.
- **Tests** : `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest`, objectif 85 %+ avec focus automation/IFTTT/history/quota (`docs/testing.md`).

## Windsurf Skill Usage
- **Skills locaux en premier** (`.continue/rules`) :
  - `add-feature` pour toute feature mêlant services/routes/templates.
  - `debugging-strategies` à consulter dès qu'un ticket implique bug, crash, performance ou investigation de logs.
  - `documentation` pour toute rédaction de documentation (README, docs/, guides Markdown), méthodologie TL;DR, problème-first, ❌/✅, trade-offs, Golden Rule.
  - `switchbot-api-dev` dès qu'on touche `switchbot_dashboard/switchbot_api.py` ou la signature HMAC/quota.
  - `automation-diagnostics` pour diagnostiquer `AutomationService` (fenêtres, hystérésis, off-repeat, timezone).
  - `scheduler-ops` pour gérer `SchedulerService` (start/stop/reschedule, healthchecks).
  - `postgres-store-maintenance` pour les migrations/bascule PostgresStore ↔ JsonStore.
  - `history-dashboard-updater` pour toute évolution HistoryService/API/frontend Chart.js.
  - `quota-alerting` pour modifier `ApiQuotaTracker`, le bandeau quota et les tests associés.
  - `loader-patterns` afin de garantir l'usage des loaders UI (data-loader, ARIA, failsafe).
  - `ifttt-cascade` pour orchestrer webhooks IFTTT → scènes → commandes directes.
  - `performance-audit-runbook` pour rejouer l'audit Core Web Vitals (critical CSS, resource hints, micro-interactions).
  - `render-service-manager` pour les opérations Render.com (déploiement, cron jobs, monitoring, variables d'environnement).
  - `postgres-ops-manager` pour les opérations PostgreSQL avancées (analyse santé, indexes, requêtes sécurisées, exploration schémas).
  - `render-postgres-integration` pour l'orchestration Render + PostgreSQL (migrations, backups, monitoring intégré).
  - `shrimp-task-manager` pour les opérations Shrimp Task Manager (planification, roadmapping, complexité).
  - `json-query-expert` pour les opérations JSON Query (manipulation, transformation, validation).
  - `fast-filesystem-ops` pour les opérations Fast Filesystem (lecture, écriture, suppression, renommage).
  - `sequentialthinking-logic` pour les opérations Sequential Thinking (analyse, planification, complexité).
- **Skills globaux** (`/home/kidpixel/.codeium/skills`) seulement si aucun équivalent local et selon la priorité :
  1. Backend/DB : `python-backend-architect`, `python-coding-standards`, `python-db-migrations`, `postgres-expert`.
  2. Frontend/UI : `frontend-design`, `css-layout-development`, `ui-component-builder`, `interaction-design-patterns`, `modern-vanilla-web`.
  3. Plateforme/Ops/Docs : `devops-sre-security`, `architecture-tools`, `code-doc`.
  4. Spécialisés : `html-tools`, `media-ai-pipeline`, `pdf-toolbox`, `engineering-features-for-machine-learning`, `slack-gif-creator` (uniquement sur demande explicite).
- **Exclusions** : ignorer `algorithmic-art`, `canvas-design` et tout skill artistique hors périmètre produit.
- **Escalade** : toujours commencer par les skills locaux puis monter l’échelle ci-dessus pour éviter prescriptions contradictoires.

## Code Style
- `from __future__ import annotations` + typage strict + retours explicites sur les APIs publiques.
- Ordre d’imports PEP 8 (stdlib → libs tierces → modules locaux).
- Fonctions à responsabilité unique ; utiliser `_as_bool/_as_int/_as_float` plutôt que `request.form` brut.
- Les commentaires expliquent le *pourquoi* ; supprimer immédiatement le code mort/commenté.
- Nommage descriptif (`meter_device_id`, `assumed_aircon_power`).

## Security
- **XSS Prevention** : Éviter `innerHTML` pour l'injection de contenu dynamique. Utiliser `textContent`, `createElement()`, ou des bibliothèques de templating sécurisées.
- **Input Validation** : Valider toutes les entrées utilisateur côté serveur avec les fonctions `_as_*`.
- **Secrets Management** : Jamais de clés API ou mots de passe en dur. Utiliser exclusivement les variables d'environnement.
- **HTTPS Only** : Toutes les URLs de webhooks doivent être HTTPS (validé dans `ifttt.py`).

## Project Structure (rappel)
| Zone | Rôle |
| --- | --- |
| `app.py` | Bootstrap Flask via `switchbot_dashboard.create_app()` |
| `switchbot_dashboard/__init__.py` | Wiring stores/services/scheduler & premier poll meter |
| `switchbot_dashboard/automation.py` | Boucle métier, cascade IFTTT → scènes → commandes, enregistrement history |
| `switchbot_dashboard/routes.py` | Routes UI, validation formulaire, actions manuelles |
| `switchbot_dashboard/static/` | Assets offline-first (Bootstrap, FontAwesome, loaders, history) |
| `templates/*.html` | Pages dark glassmorphism + bottom navigation |

## Backend Patterns
### Store Selection & Failover
- `PostgresStore` par défaut, logs `[store]` et fallback `JsonStore` uniquement en cas d’échec (`current_app.extensions["settings_store"|"state_store"]`).
- Sur incident Postgres (pool KO, SSL, timeout), consigner l’erreur, retenter côté scheduler, puis alerter si >3 échecs consécutifs.
- Redis legacy : conserver le warning, lecture seule tolérée mais aucune nouvelle feature ; planifier migration Postgres.

### Automation Cascade & Hysteresis
- Chaque tick (`AutomationService.run_once`) évalue fenêtres, hystérésis, cooldowns, files OFF et applique la cascade IFTTT → scènes → commandes directes.
- Hors créneaux : respecter l’idempotence (`assumed_aircon_power == "off"`) avant d’orchestrer `_schedule_off_repeat_task`.

### IFTTT + Scènes
- `extract_ifttt_webhooks` / `extract_aircon_scenes` fournissent la cascade. `_execute_aircon_action` met à jour l’état pour la traçabilité. Toutes les URLs webhooks doivent être HTTPS.

### Scheduler & Services
- Services injectés uniques dans `create_app()` (stores, clients, scheduler, automation). Aucun accès direct aux fichiers/clients depuis les blueprints.
- `SchedulerService` respecte `SCHEDULER_ENABLED`, évite le reloader Flask (`SERVER_SOFTWARE`), et `scheduler_service.reschedule()` doit suivre toute mutation (fenêtres horaires, `poll_interval_seconds`, bascule store).
- Tout nouveau service doit être ajouté à `app.extensions` avec clé stable + docstring courte pour guider les blueprints.

### History & Quota Tracking
- `HistoryService` uniquement lorsque `settings_store` est PostgreSQL ; logguer les erreurs sans faire tomber l’app.
- Chaque tick enregistre l’état et nettoie les entrées >6h; quotas API suivis autour de chaque requête.

## Frontend & UX
- Offline-first strict : Bootstrap/Chart.js/FontAwesome/Space Grotesk servis depuis `static/vendor` (aucun CDN).
- Templates et CSS séparés (`theme.css` + feuilles spécifiques). Inliner uniquement le CSS critique (LCP).
- Tous les formulaires/boutons/liens déclencheurs utilisent `data-loader` + `static/js/loaders.js` avec failsafe 15 s.
- Graphiques : Chart.js + décimation LTTB, hauteur mobile ≈180 px, resize géré via `static/js/history.js` (observer + decimation).
- Bottom navigation sticky, icônes seules sur mobile, page `actions.html` pour regrouper les triggers.
- Toute nouvelle page importe `_footer_nav.html` + `static/js/loaders.js`, fournit labels ARIA, et respecte les tokens glassmorphism (`theme.css`).
- Pour les snippets complets (quota banner, loaders, tokens CSS), voir `templates/index.html`, `static/js/loaders.js`, `static/css/theme.css`.

## Documentation Updates
- Chaque fois que vous créez ou modifiez de la documentation (README, docs/, guides Markdown), vous **devez** appliquer la méthodologie définie dans `.windsurf/skills/documentation/SKILL.md` (TL;DR d'abord, ouverture orientée problème, blocs ❌/✅, tableaux de compromis, Golden Rule). Considérez ce fichier skill comme la checklist de référence avant toute rédaction.

## Testing & Quality
- Commande canonique : `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest` (≥85 %).
- Cas critiques : bascule Postgres↔JsonStore, quotas API (429), cascade IFTTT, batch HistoryService + rendu Chart.js, résilience scheduler (`reschedule()` lorsque store indisponible).
- Hygiène logs : préfixes `[scheduler]`, `[api]`, `[history]`, `[store]`; jamais de secrets en clair.
- Ajouter un test ciblé pour chaque nouvelle validation `_as_*` ou service injecté (fixtures prêtes dans `tests/`).

## Anti-Patterns
1. IO direct (jamais de `open()` sur config/state) : utiliser les stores.
2. POST/actions sans loaders → régression UX.
3. Dépendances CDN → viole l’offline-first.
4. Commandes de scène sans cascade complète (webhook → scène → direct) → perte de quota/observabilité.

## Error Handling
- **Logging Obligatoire** : Jamais d'exceptions silencieuses (`except Exception: pass`). Toujours logger les erreurs avec contexte.
- **Gestion Défensive** : Attraper les exceptions spécifiques plutôt que `Exception` général, mais logger toujours.
- **Fail-Safe UX** : En cas d'erreur API, retourner des données vides plutôt que planter l'interface (pattern appliqué dans les routes history).

## Common Tasks
- **Pytest** : `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest`, viser ≥85 % (voir `docs/testing.md`).
- **Action IFTTT/Scène** : configurer `/settings`, valider via `_as_*`, déployer, vérifier `_execute_aircon_action` + flashs UI.
- **Bouton avec loader** : ajouter `data-loader`, importer `static/js/loaders.js`, tester overlay + failsafe 15 s + `aria-busy`.
- **Diagnostic automation** : lire `state_store`, analyser logs `[automation]`, vérifier snapshot et cleanup HistoryService si Postgres actif.

---
Utiliser ce fichier comme source Always-On : il capture les décisions d’architecture critiques, rappelle les pièges et référence les fichiers canoniques.