# Progrès du Projet - SwitchBot Dashboard

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
