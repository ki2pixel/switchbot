# Contexte Actif

## Session 2026-11-04 — Remédiation Audit Backend V2
- **[2026-11-04 14:13:43] - Correctifs backend + frontend de l'audit `docs/audits/Audit Architectural_et_Technique_SwitchBot_Dashboard_V2.md`** :
  - **P0** : transactions `JsonStore`/`PostgresStore` réentrantes par thread (fin des deadlocks), verrou de ligne garanti par `INSERT ... ON CONFLICT`, cache `CachedStoreWrapper` en `threading.local()`, scheduler protégé dans `finally` + `replace_existing` sans `remove()`.
  - **P1** : validation SSRF de `SwitchBotClient._base_url`, capture quota avant retry 429, logs `[api]` sans headers, Session HTTP thread-local, `_as_int`/`_parse_iso_datetime` sur `/history/api/*`, `compare_digest` UTF-8, fencing des actions manuelles via `apply_state_updates`, migration PostgreSQL sans fuite de pool ni URL complète.
  - **P2** : `Decimal → float` et `COALESCE` dans les agrégats, `get_latest_records` borné par index, flush History hors verrou réseau, mode aircon conservé après scène, historique sur capteur indisponible, `/actions/run_once` borné à un thread.
  - **Failover runtime** : nouveau `ResilientStore` (3 échecs consécutifs, log CRITICAL, bascule JSON hors production, alerte seule en production). `HistoryService` et `/healthz` détectent le backend primaire.
  - **Frontend** : token CSRF limité au same-origin (`loaders.js`), scripts inline re-exécutés uniquement s'ils portent `data-spa-inline` (`spa-router.js` + `index.html`).
  - **Tests** : **285 passent**, 1 skipped. `AUD-TEST-01` corrigé : le test scheduler échouait à cause du clamp métier à 15 s, pas d'APScheduler/Gunicorn.
  - **Docs** : `.env.example` documente `STORE_RUNTIME_FALLBACK` et `STORE_FAILURE_THRESHOLD`.
- **[2026-11-04 14:31:00] - Nettoyage des index exécuté sur Supabase (production)** :
  - Connexion via `POSTGRES_URL` du `.env` (pooler `aws-1-eu-central-1`, PostgreSQL 17.6, db `postgres`). `psql` absent de la machine → exécution via `psycopg` 3.3.2.
  - Avant : `idx_json_store_kind` 16 kB sur `json_store` (2 lignes) ; `idx_state_history_metadata` **122 MB** GIN sur `state_history` (1 566 lignes).
  - `DROP INDEX CONCURRENTLY` sur les deux (autocommit requis). Vérification : les 2 index ont disparu, `state_history` passe de ~122 MB à 984 kB (total index inclus), données intactes (2 et 1 574 lignes).
  - Index utiles conservés : `json_store_pkey`, `idx_json_store_updated_at`, `state_history_pkey`, `idx_state_history_timestamp`, `idx_state_history_aircon_power`. `EXPLAIN ANALYZE` de `get_latest_records` → `Index Scan using idx_state_history_timestamp`, 1,05 ms.
  - Ré-instanciation de `PostgresStore` : les index supprimés ne sont **pas** recréés. `get_latest_records`/`get_aggregates` OK (types `float`).
  - Nouveau runner reproductible : `scripts/drop_redundant_indexes.py` (dry-run par défaut, `--apply` pour exécuter, `--index` pour cibler, lit `.env` ou `POSTGRES_URL`, `CONCURRENTLY` + autocommit).
- **[2026-11-04 14:41:41] - Diagnostic post-déploiement Render : `FLASK_DEBUG=1` actif en production** :
  - Symptômes relevés sur l'URL publique : cookie `session` **sans `Secure`**, aucun en-tête `Strict-Transport-Security`, et log `[store] Runtime filesystem fallback configured …` alors que `STORE_RUNTIME_FALLBACK` n'était pas activé.
  - Cause : `FLASK_DEBUG=1` (hérité du `.env` local) rend `app.debug=True` ; toute la logique `is_production` (cookies Secure, HSTS, garde-fous secret/password, politique de failover) en dépendait.
  - Fix : `_running_under_wsgi_server()` (gunicorn/uwsgi dans `sys.modules`, `RENDER=true`, `SERVER_SOFTWARE`) force `app.debug=False` au démarrage avec un WARNING `[security]`. En local (`flask run`), le debug reste actif.
  - `/healthz` expose désormais `store_fallback_enabled` ; `ResilientStore.fallback_enabled` ajouté.
  - Tests : **291 passent**, 1 skipped (WSGI-01..04 + séparation dev/prod du fallback runtime).
  - **Action ops restante** : retirer `FLASK_DEBUG` du dashboard Render, et vérifier que `STORE_RUNTIME_FALLBACK` n'y est pas activé. Si `FLASK_SECRET_KEY` est faible, le prochain démarrage échouera volontairement (« Security Violation »).
- **[2026-11-04 14:49:41] - CI GitHub Actions : échec `test_build_store_disables_runtime_fallback_in_production`** :
  - Cause : la CI exporte `FLASK_ENV=testing` pour toute la session pytest ; `_build_store` en déduit `is_testing=True`, donc `is_production=False`, donc le fallback JSON est armé. En local la variable est absente, le test passait.
  - Fix : les deux tests de `TestStoreFailoverAndBuild` font désormais `monkeypatch.delenv("FLASK_ENV"/"FLASK_DEBUG")` avant de simuler la production. Commentaire ajouté pour éviter la régression.
  - Validation : suite complète rejouée avec `FLASK_ENV=testing FLASK_DEBUG=0` (conditions CI) → **291 passed, 1 skipped**.

## Session 2026-11-04 — Remédiation Audit Frontend V2
- **[2026-11-04 13:20:00] - Correctif ordre CSS (cartes claires après navigation SPA)** :
  - Cause : `index.html` chargeait `theme.css` **avant** `bootstrap.min.css`. En SPA, cet ordre était conservé ; `.card { background-color: var(--bs-card-bg) }` (Bootstrap, blanc) écrasait `.card { background: var(--sb-glass-bg) }` (theme sombre). Au survol, `.card:hover` reprenait le dessus → fond clair puis sombre.
  - Fix : réordonnancement des preloads d'`index.html` (bootstrap → space-grotesk → theme → index → sticky-*), aligné sur tous les autres templates.
  - `spa-router.js` : `sticky-cards.css` traité comme feuille page-specific (nettoyage en quittant l'accueil).
  - Tests : `TestStylesheetOrder` (vendor avant theme, page CSS après theme) — **228 tests passent**.
- **[2026-11-04 13:00:00] - Correction des constats vérifiés de `docs/audits/Audit_Frontend_SwitchBot_Dashboard_V2.md`** :
  - **AUD-02** : helper `_utc_iso_z()` dans `utils.py` ; suppression des 6 concaténations `.isoformat() + "Z"` (healthz + mocks history).
  - **AUD-03** : garde `response.redirected → /login` + `401` dans `spa-router.js`, resynchronisation du token CSRF, redirection `401` dans `history.js`.
  - **AUD-05** : helper `_record_history_snapshot()` appelé aussi hors fenêtre et automation désactivée (fin des trous de graphiques).
  - **AUD-06** : `/history/api/*` renvoie 200 + payload vide `degraded: true` au lieu de 503.
  - **AUD-08** : transitions composite-only, shimmer en `translateX`, suppression des couches GPU permanentes, `:focus-visible` contrastés, chevrons CSS sans texte.
  - **AUD-09** : CSP `script-src` à nonce par requête (plus de `unsafe-inline`), rétention `HISTORY_RETENTION_HOURS` (défaut 24h) + docs alignées.
  - **Non retenus (constats infirmés)** : AUD-01 (`static/vendor` présent et versionné), AUD-04 (alias de tokens déjà dans `theme.css`), AUD-07 partiel (`history.css` et `theme.css` gèrent déjà `prefers-reduced-motion`), destruction Chart.js déjà en place.
  - Validation navigateur : SPA aller/retour OK, aucune violation CSP, redirection de session expirée OK.
  - Tests : **226 passent**, 1 skipped.

## Session 2026-11-04 — Nettoyage Configurations IDE & Push GitHub
- **[2026-11-04 12:05:00] - Nettoyage configs legacy & migration vers .agents/** :
  - Suppression des dossiers et fichiers de configuration obsolètes (`.cline/`, `.clinerules/`, `.windsurf/`, `.codex/rules/development.rules`, `.zencoder/`, `repomix.config.json`).
  - Validation des frontmatters dans `.agents/skills/`.
  - Exécution complète des tests : 207 passants, 1 ignoré.
  - Configuration du helper Git via `gh auth setup-git` (HTTPS) et bascule du remote origin.
  - Commit et push réussis sur `origin/main` (`f16e776`).

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
