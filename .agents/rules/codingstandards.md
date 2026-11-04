---
trigger: always_on
description: Core AI rule for SwitchBot Dashboard v2 (Flask + offline-first frontend)
globs: 
---

# SwitchBot Dashboard v2 – AI Coding Standards

## Tech Stack
- **Backend** : Flask 2.x/3.x + APScheduler, services injectés via `app.extensions` (`settings_store`, `state_store`, `switchbot_client`, `automation_service`, `scheduler_service`, `quota_tracker` ; `history_service` si PostgreSQL). Sécurisé via `Flask-WTF` (CSRF) et `Flask-Limiter` (Rate Limiting).
- **Stockage** : `PostgresStore` (prioritaire) via `psycopg_pool`, `JsonStore` en secours **hors production**. En production, `ResilientStore` alerte et laisse répondre `503` par défaut (`STORE_RUNTIME_FALLBACK=false`). Le backend `redis` est retiré : `STORE_BACKEND=redis` est refusé en production et retombe sur JSON sinon.
- **Frontend** : Templates Jinja, assets offline-first depuis `static/vendor`, Chart.js avec décimation LTTB, loaders obligatoires.
- **Tests** : `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest`, objectif 85 %+ (actuellement ~86 % sur `switchbot_dashboard/`) avec focus automation/history/quota/scheduler (`docs/ops/testing-strategy.md`).

## AI Skill Usage
- **Skills locaux en premier** (`.agents/skills`) :
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
  - `performance-audit-runbook` pour rejouer l'audit Core Web Vitals (critical CSS, resource hints, micro-interactions).
  - `render-service-manager` pour les opérations Render.com (déploiement, cron jobs, monitoring, variables d'environnement).
  - `postgres-ops-manager` pour les opérations PostgreSQL avancées (analyse santé, indexes, requêtes sécurisées, exploration schémas).
  - `render-postgres-integration` pour l'orchestration Render + PostgreSQL (migrations, backups, monitoring intégré).
  - `shrimp-task-manager` pour les opérations Shrimp Task Manager (planification, roadmapping, complexité).
  - `json-query-expert` pour les opérations JSON Query (manipulation, transformation, validation).
  - `fast-filesystem-ops` pour les opérations Fast Filesystem (lecture, écriture, suppression, renommage).
  - `sequentialthinking-logic` pour les opérations Sequential Thinking (analyse, planification, complexité).
- **Skills globaux** (`/home/kidpixel/.agents/skills` ou `/home/kidpixel/.claude/skills`) seulement si aucun équivalent local :
  1. Planification/recherche : `plan`, `research`.
  2. Frontend/UI : `frontend-design`.
  3. Navigateur/tests : `playwright`, `agent-browser`.
  4. Revue : `cross-review`, `zen-review`, `zen-comprehensive-review` (sur demande explicite).
  5. Méta : `init`, `skill-creator`.
- **Exclusions** : ignorer tout skill artistique hors périmètre produit.
- **Escalade** : toujours commencer par les skills locaux puis monter l’échelle ci-dessus pour éviter prescriptions contradictoires.

## Code Style
- `from __future__ import annotations` + typage strict + retours explicites sur les APIs publiques.
- Ordre d’imports PEP 8 (stdlib → libs tierces → modules locaux).
- Fonctions à responsabilité unique ; utiliser `_safe_bool/_safe_int/_safe_float` (`utils.py`, alias `_as_*` dans `routes.py`) plutôt que `request.form` brut.
- Les commentaires expliquent le *pourquoi* ; supprimer immédiatement le code mort/commenté.
- Nommage descriptif (`meter_device_id`, `assumed_aircon_power`).

## Security
- **XSS Prevention** : Éviter `innerHTML` pour l'injection de contenu dynamique. Utiliser `textContent`, `createElement()`, ou des bibliothèques de templating sécurisées.
- **Input Validation** : Valider toutes les entrées utilisateur côté serveur avec les fonctions `_safe_*` (alias `_as_*` dans `routes.py`).
- **Secrets Management** : Jamais de clés API ou mots de passe en dur. Utiliser exclusivement les variables d'environnement.
- **SSRF Defense** :
  - ✅ Validation stricte de `SwitchBotClient.base_url` : HTTPS obligatoire, credentials/fragments/query interdits.
  - ✅ Blocage explicite des hostnames locaux et des IP privées, loopback, link-local, réservées ou multicast.
- **Timing Attacks** :
  - ✅ Comparaisons à temps constant (`hmac.compare_digest`) pour le mot de passe de connexion et le token `STATE_DEBUG_TOKEN`.

## Project Structure (rappel)
| Zone | Rôle |
| --- | --- |
| `app.py` | Bootstrap Flask via `switchbot_dashboard.create_app()` |
| `switchbot_dashboard/__init__.py` | Wiring stores/services/scheduler & premier poll meter |
| `switchbot_dashboard/automation.py` | Boucle métier, cascade scènes → commandes directes, enregistrement history |
| `switchbot_dashboard/aircon.py` | Normalisation des scènes aircon (`winter`, `summer`, `fan`, `off`) |
| `switchbot_dashboard/store_resilience.py` | `ResilientStore` : comptage d'échecs, alerte et bascule conditionnelle |
| `switchbot_dashboard/utils.py` | Helpers `_safe_int`, `_safe_bool`, `_safe_float`, timezone et ISO |
| `run_worker.py` | Worker autonome pour exécuter le scheduler hors du service web |
| `switchbot_dashboard/routes.py` | Routes UI, validation formulaire, actions manuelles |
| `switchbot_dashboard/static/` | Assets offline-first (Bootstrap, FontAwesome, loaders, history) |
| `switchbot_dashboard/templates/*.html` | Pages dark glassmorphism + bottom navigation |

## Backend Patterns
### Store Selection & Failover
- `PostgresStore` par défaut, enveloppé par `ResilientStore` (`current_app.extensions["settings_store"|"state_store"]`).
- Sur incident Postgres (pool KO, SSL, timeout), `ResilientStore` compte les échecs, log `[store] CRITICAL` au 3e (`STORE_FAILURE_THRESHOLD`) et bascule vers `JsonStore` uniquement si autorisé (hors production ou `STORE_RUNTIME_FALLBACK=true`) ; sinon les routes répondent `503`.
- Redis est retiré : aucun client Redis n'est instancié ; `STORE_BACKEND=redis` est refusé en production et retombe sur JSON hors production.

### PostgreSQL Pool Management
- ✅ Manipuler explicitement les contextes de transaction du `psycopg_pool`.
- ✅ Garantir la libération des connexions (via `with self.pool.connection() as conn:` ou en gérant manuellement `__enter__`/`__exit__`).

### Automation Cascade & Hysteresis
- Chaque tick (`AutomationService.run_once`) évalue fenêtres, hystérésis, cooldowns, files OFF et applique la cascade scènes → commandes directes.
- Hors créneaux : respecter l’idempotence (`assumed_aircon_power == "off"`) avant d’orchestrer `_schedule_off_repeat_task`.

### Scènes Aircon
- `extract_aircon_scenes` (`aircon.py`) normalise les clés `winter`, `summer`, `fan`, `off`. `_trigger_scene` exécute la scène, `_trigger_aircon_action` orchestre le fallback vers `_send_aircon_setall` / `_send_aircon_off`. `_execute_aircon_action` dans `routes.py` est réservé aux actions manuelles.

### Scheduler & Services
- Services injectés uniques dans `create_app()` (stores, clients, scheduler, automation). Aucun accès direct aux fichiers/clients depuis les blueprints.
- `SchedulerService` respecte `SCHEDULER_ENABLED`, évite le reloader Flask (`SERVER_SOFTWARE`), gère le polling adaptatif (`in_window`, `warmup`, `idle`, `pending_off_repeat`, `fixed`) et `scheduler_service.reschedule()` doit suivre toute mutation de settings (fenêtres horaires, `poll_interval_seconds`, paramètres d'automatisation). `run_worker.py` permet de découpler le scheduler du service web (`docs/core/deployment.md`).
- Tout nouveau service doit être ajouté à `app.extensions` avec clé stable + docstring courte pour guider les blueprints.

### History & Quota Tracking
- `HistoryService` uniquement lorsque le backend primaire de `settings_store` est PostgreSQL ; logguer les erreurs sans faire tomber l’app.
- Chaque tick enregistre l’état (y compris hors fenêtre horaire et automation désactivée) ; le nettoyage au-delà de `HISTORY_RETENTION_HOURS` (24 h par défaut) est planifié toutes les heures par le scheduler. Quotas API suivis autour de chaque requête.

## Frontend & UX
- Offline-first strict : Bootstrap/Chart.js/FontAwesome/Space Grotesk servis depuis `static/vendor` (aucun CDN).
- Templates et CSS séparés (`theme.css` + feuilles spécifiques). Inliner uniquement le CSS critique (LCP).
- Tous les formulaires, boutons et liens déclenchant une action réseau ou une navigation utilisent `data-loader` + `static/js/loaders.js` avec failsafe 15 s (les actions purement locales, comme la copie d'ID, peuvent s'en passer).
- **SPA Router & Cycle de vie** :
  - ✅ Interception des liens `a[data-loader]` par `loaders.js`, navigation déléguée à `spa-router.js` sans rechargement complet du DOM.
  - ✅ Scripts de page ré-exécutés par `spa-router.js` (IIFE type `settings.js`) ; les scripts inline doivent porter `data-spa-inline` + nonce CSP.
  - ✅ Re-liaison explicite des écouteurs d'événements lors des transitions de page.
- **Protection CSRF** :
  - ✅ Exploitation des intercepteurs globaux Fetch/XHR pour injecter automatiquement le token CSRF sur toute modification d'état, adossé à `Flask-WTF` (`CSRFProtect`).
- Graphiques : Chart.js `responsive: true` + décimation LTTB, hauteur mobile ≈180 px (`static/css/history.css`), sans `ResizeObserver` dédié.
- Bottom navigation sticky, icônes seules sur mobile, page `actions.html` pour regrouper les triggers.
- Toute nouvelle page importe `_footer_nav.html` + `static/js/loaders.js`, fournit labels ARIA, et respecte les tokens glassmorphism (`theme.css`).
- Pour les snippets complets (quota banner, loaders, tokens CSS), voir `templates/index.html`, `static/js/loaders.js`, `static/css/theme.css`.

## Documentation Updates
- Chaque fois que vous créez ou modifiez de la documentation (README, docs/, guides Markdown), vous **devez** appliquer la méthodologie définie dans `.agents/skills/documentation/SKILL.md` (TL;DR d'abord, ouverture orientée problème, blocs ❌/✅, tableaux de compromis, Golden Rule). Considérez ce fichier skill comme la checklist de référence avant toute rédaction.

## Testing & Quality
- Commande canonique : `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest` (≥85 %).
- Cas critiques : bascule Postgres↔JsonStore, quotas API (429), cascade scènes → commandes, batch HistoryService + rendu Chart.js, résilience scheduler (`reschedule()` lorsque store indisponible).
- Hygiène logs : préfixes `[scheduler]`, `[api]`, `[history]`, `[store]`; jamais de secrets en clair.
- Ajouter un test ciblé pour chaque nouvelle validation `_safe_*` / `_as_*` ou service injecté (fixtures prêtes dans `tests/`).

## Anti-Patterns
1. IO direct (jamais de `open()` sur config/state) : utiliser les stores.
2. POST/actions sans loaders → régression UX.
3. Dépendances CDN → viole l’offline-first.
4. Commandes de scène sans fallback direct (scène → direct) → perte de quota/observabilité.
5. ❌ Utiliser `window.location.reload()` ou des balises `<a href="...">` standards forçant le rafraîchissement au lieu de s'intégrer au SPA Router.
6. ❌ Omettre les en-têtes CSRF sur les appels asynchrones personnalisés.
7. ❌ Utiliser des context managers invalides ou implicites sur le pool `psycopg_pool` sans garantir la libération des connexions.

## Error Handling
- **Logging Obligatoire** : Jamais d'exceptions silencieuses (`except Exception: pass`). Toujours logger les erreurs avec contexte.
- **Gestion Défensive** : Attraper les exceptions spécifiques plutôt que `Exception` général, mais logger toujours.
- **Fail-Safe UX** : En cas d'erreur API, retourner des données vides plutôt que planter l'interface (pattern appliqué dans les routes history).

## Common Tasks
- **Pytest** : `source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest`, viser ≥85 % (voir `docs/ops/testing-strategy.md`).
- **Action Scène** : configurer la page `/reglages` (POST `/settings`), valider via `_as_*`, déployer, vérifier `_execute_aircon_action` + flashs UI.
- **Bouton avec loader** : ajouter `data-loader`, importer `static/js/loaders.js`, tester overlay + failsafe 15 s + `aria-busy`.
- **Diagnostic automation** : lire `state_store`, analyser logs `[automation]`, vérifier snapshot et job de cleanup HistoryService si Postgres actif.

---
Utiliser ce fichier comme source Always-On : il capture les décisions d’architecture critiques, rappelle les pièges et référence les fichiers canoniques.