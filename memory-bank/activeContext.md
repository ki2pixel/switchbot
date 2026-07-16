# Contexte Actif

## Session 2026-07-16 — Remédiation Audit Frontend/Backend
### Derniers changements accomplis

**Phase 1 (Frontend Resilience & Initialization) — TERMINÉE**
- **F-01** : Fix récursion infinie dans `history.js` avec Chart.js.
- **F-02** : Handling des erreurs via overlay UI.
- **B-01** : Correction `PostgresStoreError` pour fallback `JsonStore`.
- **B-02** : CSP stricte et token CSRF injecté via `spa-router.js`.
- **B-08/B-09** : Validation des types booléens et bornes API.
- **S-04** : Nettoyage `history_service.py` sur 24h et flush `atexit`.

**Phase 2 (Core Backend Logic & Consistency) — TERMINÉE**
- **B-05/B-06** : `threading.local()` pour token lock ; wrappage `off_repeat` dans `state_store.transaction()`.
- **B-07/B-11** : Fallback manuel sur `setAll` et allowlist `/debug/state`.
- **B-10** : `force=True` bypass de cache sur `get_devices()`.
- **D-01** : Opération DDL sécurisée via `information_schema`.

**Phase 3 (DevOps & Pipeline Validation) — TERMINÉE**
- **S-05/O-01** : `redis` et `beautifulsoup4` séparés de `requirements.txt` en `requirements-dev.txt`.
- **O-03** : Config `gunicorn.conf.py` optimisée (`worker_class = gthread`, 4 threads, timeout 30s).

### État de la base de tests
- **207 tests passent**, aucun rouge.

## Objectifs actuels
- **Terminé.** Toutes les phases de remédiation prévues dans `implementation_plan.md` ont été complétées avec succès.

## Note configuration Render
- `PROXY_FIX_FOR=1` : **à configurer** dans l'interface Render (Render met un proxy devant l'app).
- `RATELIMIT_STORAGE_URI` : **non nécessaire** — Gunicorn est forcé à 1 seul worker quand le scheduler APScheduler est actif (voir `gunicorn.conf.py`), donc le stockage mémoire par défaut suffit.
