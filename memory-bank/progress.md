# Progrès du Projet - SwitchBot Dashboard

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
- Suite de tests : **207 tests passent**, 1 skipped.

## Prochaines étapes
1. Déploiement Render : ajouter `PROXY_FIX_FOR=1` dans les variables d'environnement Render.
2. Surveiller les métriques de production post-déploiement (rate limiting, logs `[store]`, `[api]`).
3. Envisager l'audit frontend (si besoin) ou nouvelles fonctionnalités.
