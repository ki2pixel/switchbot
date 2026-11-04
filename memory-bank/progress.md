# Progrès du Projet - SwitchBot Dashboard

## Alignement docs always-on — 2026-11-04
- [x] [2026-11-04 16:24:55] - `AGENTS.md` et `codingstandards.md` alignés sur le code (IFTTT retiré, `ResilientStore`, `run_worker.py`, polling adaptatif, `_safe_*`, skills globaux, couverture 86 %).
- [x] [2026-11-04 16:24:55] - Nettoyage collateral : `ifttt-cascade` → `aircon-cascade`, `skills-integration.md`, `systemPatterns.md`, `automation-engine.md`, `docs/codex/integration-guide.md`, skills diagnostics/scheduler/postgres, docs associés.
- [x] [2026-11-04 16:24:55] - Validation : `pytest -q` → 314 passed, 1 skipped ; `git diff --check` OK.

## Refactor automation.py + switchbot_api.py — 2026-11-04
- [x] [2026-11-04 16:04:06] - `poll_aircon_status` découpé (statut virtuel, mapping body, sync état).
- [x] [2026-11-04 16:04:06] - `_perform_off_action` découpé (fan mode, fallback direct, off).
- [x] [2026-11-04 16:04:06] - `_process_off_repeat_task` découpé (lecture planification, replanification).
- [x] [2026-11-04 16:04:06] - `_evaluate_temperature` découpé (profil, zone neutre fan).
- [x] [2026-11-04 16:04:06] - `_run_once_impl` découpé (tick désactivé, hors fenêtre, lecture capteur).
- [x] [2026-11-04 16:04:06] - `_validate_https_base_url`, `_process_response`, `_request`, `_capture_quota_metadata` découpés.
- [x] [2026-11-04 16:04:06] - 13 tests de bordure ajoutés (API-01..08, AUTO-01..05), GWT.
- [x] [2026-11-04 16:04:06] - Validation : `ruff check` OK, **314 passed, 1 skipped** ; `automation.py` et `switchbot_api.py` sans bloc ≥ C ; moyenne projet A (3,64).
- [ ] Prochaine étape : traiter les C restants (`scheduler.py:_get_effective_interval_seconds`, `__init__.py:_configure_security`, `scripts/migrate_to_postgres.py:_read_and_validate_data`).

## Refactor routes.py — 2026-11-04
- [x] [2026-11-04 15:53:37] - `_update_time_windows` découpé (parsing jours, validation HH:MM).
- [x] [2026-11-04 15:53:37] - `_handle_direct_action` découpé (lock contextmanager, scène, off, setAll).
- [x] [2026-11-04 15:53:37] - `_parse_history_query_params` découpé (metrics, plage, granularité).
- [x] [2026-11-04 15:53:37] - `healthz` découpé (snapshot, payload, connectivité, réponse JSON).
- [x] [2026-11-04 15:53:37] - `history_api_data` découpé (payload indisponible/vide/erreur).
- [x] [2026-11-04 15:53:37] - 3 tests de bordure ajoutés (scheduler arrêté, historique vide, plage inversée).
- [x] [2026-11-04 15:53:37] - Validation : `ruff check` OK, **301 passed, 1 skipped** ; `routes.py` sans bloc ≥ C.
- [ ] Prochaine étape : traiter les C restants dans `automation.py` et `switchbot_api.py`.

## Refactor _build_store — 2026-11-04
- [x] [2026-11-04 15:46:47] - `_build_store` découpé en helpers (environnement, JSON, seuil, résilience, PostgreSQL).
- [x] [2026-11-04 15:46:47] - `_configure_security` réutilise `_resolve_environment`.
- [x] [2026-11-04 15:46:47] - 3 tests de bordure ajoutés (seuil invalide, Redis production, filesystem production).
- [x] [2026-11-04 15:46:47] - Validation : `ruff check` OK, **298 passed, 1 skipped** ; moyenne radon 14,35.
- [ ] Prochaine étape : traiter `_handle_direct_action` (C) et `_update_time_windows` (C) si une nouvelle passe est souhaitée.

## Refactor Complexité — 2026-11-04
- [x] [2026-11-04 15:38:17] - `update_settings` découpé en helpers de section ; sorti des hotspots radon.
- [x] [2026-11-04 15:38:17] - `poll_aircon_status` : cache/cooldown extraits, complexité E → C.
- [x] [2026-11-04 15:38:17] - `create_app` : initialisation découpée en 10 helpers ; complexité F supprimée.
- [x] [2026-11-04 15:38:17] - 4 tests TWM-01..06 (fenêtre traversant minuit) avec structure Given/When/Then.
- [x] [2026-11-04 15:38:17] - Validation : `ruff check` OK, **295 passed, 1 skipped**.
- [ ] Prochaine étape : réduire `_build_store` (D) si une nouvelle passe de complexité est planifiée.

## Docs Updater — 2026-11-04
- [x] [2026-11-04 15:28:12] - Audit statique (tree, cloc, radon) : 18 fichiers Python, 4 637 lignes, complexité moyenne C (17,84).
- [x] [2026-11-04 15:28:12] - Alignement docs/code : README, ui-navigation, automation-engine, quota-management, scheduler.
- [x] [2026-11-04 15:28:12] - Remplacement des références de tests et d'APIs inexistantes (ops, monitoring).
- [ ] Prochaine étape : rejouer la suite pytest après tout changement de code (aucun code applicatif modifié ici).

## Phase Remédiation Audit Backend V2 (2026-11-04) — COMPLÈTE ✔
- [x] [2026-11-04 14:13:43] - AUD-DB-01/CONC-01 : transactions réentrantes + cache thread-local.
- [x] [2026-11-04 14:13:43] - AUD-SCHED-01 : reschedule protégé, job conservé, test périodique honnête.
- [x] [2026-11-04 14:13:43] - AUD-SEC-01/API-01/API-02 : SSRF, quota avant retry, logs `[api]`, Session thread-local.
- [x] [2026-11-04 14:13:43] - AUD-SEC-05/06 : validation `/history/api/*`, UTF-8, booléens.
- [x] [2026-11-04 14:13:43] - AUD-CONC-02/03 : fencing des actions manuelles, run_once borné.
- [x] [2026-11-04 14:13:43] - AUD-DB-02 : `ResilientStore` + alerte/bascule contrôlée.
- [x] [2026-11-04 14:13:43] - AUD-DB-03/04/05/06/PERF-01/SQL-01 : migration, logs, verrou History, Decimal, index.
- [x] [2026-11-04 14:13:43] - AUD-AUTO-01/02/TEST-01 : mode scène, historique capteur, test scheduler.
- [x] [2026-11-04 14:13:43] - AUD-SEC-02/03 : CSRF same-origin + marqueur `data-spa-inline`.
- [x] [2026-11-04 14:31:00] - Nettoyage production Supabase : `DROP INDEX CONCURRENTLY` sur `idx_json_store_kind` et `idx_state_history_metadata` (122 Mo libérés), runner `scripts/drop_redundant_indexes.py`.
- [x] [2026-11-04 14:31:00] - **285 tests passent**, 1 skipped.
- [x] [2026-11-04 14:41:41] - `FLASK_DEBUG` neutralisé sous WSGI : cookies `Secure`, HSTS et garde-fous production rétablis ; fallback JSON runtime désactivé en prod par défaut.
- [x] [2026-11-04 14:41:41] - **291 tests passent**, 1 skipped.
- [x] [2026-11-04 14:49:41] - Tests de failover rendus indépendants de `FLASK_ENV=testing` exporté par la CI.

## Phase Remédiation Audit Frontend V2 (2026-11-04) — COMPLÈTE ✔
- [x] [2026-11-04 13:00:00] - AUD-02 : timestamps ISO-8601 valides (`_utc_iso_z`) sur healthz et mocks history.
- [x] [2026-11-04 13:00:00] - AUD-03 : garde redirection session expirée + refresh CSRF dans le routeur SPA et history.js.
- [x] [2026-11-04 13:00:00] - AUD-05 : `record_state()` exécuté aussi hors fenêtre / automation désactivée.
- [x] [2026-11-04 13:00:00] - AUD-06 : API history fail-safe (200 + data vide + `degraded`).
- [x] [2026-11-04 13:00:00] - AUD-08 : CSS composite-only, focus-visible, chevrons accessibles, reduced-motion.
- [x] [2026-11-04 13:00:00] - AUD-09 : CSP nonce par requête, rétention configurable 24h, docs skills alignées.
- [x] [2026-11-04 13:00:00] - AUD-01/04/07 : constats infirmés après vérification (aucune modification nécessaire).
- [x] [2026-11-04 13:20:00] - Fix ordre CSS : vendor avant `theme.css` (cartes claires après navigation SPA) + test `TestStylesheetOrder`.

## Phase Maintenance & Clean-up (2026-11-04) — COMPLÈTE ✔
- [x] [2026-11-04 12:05:00] - Nettoyage des configs IDE legacy (.cline, .windsurf, .codex, .zencoder) et consolidation dans `.agents/`.
- [x] [2026-11-04 12:05:00] - Configuration push Git HTTPS via `gh` CLI et push sur `origin/main` (`f16e776`).

## Phase P0 (Disponibilité / Concurrence) — COMPLÈTE ✔
- [x] DATA-02: Align SQL Schema for last_action (2026-07-16)
- [x] DATA-01: Transactional State Updates (lost updates) (2026-07-16)
- [x] REL-01: Lock Renewals and Fencing Token (2026-07-16)
- [x] REL-02: Non-blocking Boot and Async First Tick (2026-07-16)
- [x] SEC-01: Werkzeug ProxyFix and Rate Limiting Configuration (2026-07-16)

## Phase P1 (Robustesse & Sécurité) — COMPLÈTE ✔
- [x] PERF-01 / REL-03: Thread-safe Cache, Parallelism & Shorter HTTP timeouts (2026-07-16)
- [x] SEC-02 / SEC-03: Input validation for scene_id, min_temp, max_temp & HH:MM (2026-07-16)
- [x] REL-04 / REL-05: Jittered exponential retries & Postgres pool timeouts (2026-07-16)
- [x] SEC-04 / SEC-05 / SEC-07: verify-full TLS, log credential scrubbing & /debug/state limit (2026-07-16)

## Phase P2 (Durcissement & Cycle de vie) — COMPLÈTE ✔
- [x] SEC-06: /logout POST-only + bouton CSRF + hachages Werkzeug (2026-07-16)
- [x] MAIN-01: Suppression SimpleTransactionContext (code mort) (2026-07-16)
- [x] MAIN-02: AGENTS.md — IFTTT officiellement marqué comme retiré (2026-07-16)

## Phase 1 (Frontend Resilience & Initialization) — COMPLÈTE ✔
- [x] F-01: Fix récursion infinie dans `history.js` avec Chart.js (2026-07-16)
- [x] F-02: Handling des erreurs via overlay UI (2026-07-16)
- [x] B-01: Correction `PostgresStoreError` pour fallback `JsonStore` (2026-07-16)
- [x] B-02: CSP stricte et token CSRF injecté via `spa-router.js` (2026-07-16)
- [x] B-08/B-09: Validation des types booléens et bornes API (2026-07-16)
- [x] S-04: Nettoyage `history_service.py` sur 24h et flush `atexit` (2026-07-16)

## Phase 2 (Core Backend Logic & Consistency) — COMPLÈTE ✔
- [x] B-05/B-06: `threading.local()` pour token lock ; wrappage `off_repeat` dans transaction (2026-07-16)
- [x] B-07/B-11: Fallback manuel sur `setAll` et allowlist `/debug/state` (2026-07-16)
- [x] B-10: `force=True` bypass de cache sur `get_devices()` (2026-07-16)
- [x] D-01: Opération DDL sécurisée via `information_schema` (2026-07-16)

## Phase 3 (DevOps & Pipeline Validation) — COMPLÈTE ✔
- [x] S-05/O-01: `redis` et `beautifulsoup4` séparés de `requirements.txt` en `requirements-dev.txt` (2026-07-16)
- [x] O-03: Config `gunicorn.conf.py` optimisée (2026-07-16)

## État global
- **Toutes les phases de la remédiation backend et frontend sont complètes.**
- Suite de tests : **226 tests passent**, 1 skipped.

## Prochaines étapes
1. Déploiement Render : ajouter `PROXY_FIX_FOR=1` et éventuellement `HISTORY_RETENTION_HOURS=24` dans les variables d'environnement Render.
2. Surveiller les métriques de production post-déploiement (rate limiting, logs `[store]`, `[api]`, violations CSP).
3. Envisager l'audit frontend (si besoin) ou nouvelles fonctionnalités.
