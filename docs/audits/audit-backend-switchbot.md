# Audit Backend — SwitchBot Dashboard

**Date :** 2026-07-17
**Périmètre :** revue statique complète du backend Python (Flask) à partir de l'export Repomix du dépôt `SwitchBot` : `app.py`, `run_worker.py`, `switchbot_dashboard/` (`__init__.py`, `routes.py`, `automation.py`, `scheduler.py`, `switchbot_api.py`, `postgres_store.py`, `config_store.py`, `history_service.py`, `quota.py`, `aircon.py`, `utils.py`, `extensions.py`), `scripts/` (SQL + migration), configuration de déploiement (`Dockerfile`, `gunicorn.conf.py`, `requirements.txt`, `.env.example`), et la suite de tests (`tests/`).
**Méthode :** revue de code manuelle axée sécurité, fiabilité, concurrence, intégrité des données, performance, observabilité et maintenabilité. Les références renvoient aux fichiers réels du dépôt.

---

## 1. Résumé exécutif

L'application est un **dashboard personnel de domotique** (contrôle d'un climatiseur via l'API SwitchBot, avec automatisation thermostat par fenêtres horaires, hystérésis et cooldowns). Le code est **globalement soigné et nettement au-dessus de la moyenne des projets personnels** : protection CSRF complète, en-têtes de sécurité HTTP, comparaisons à temps constant, requêtes SQL paramétrées, validation des entrées, bascule Postgres/JSON avec fail-fast en production, 178 tests, conteneur non-root multi-étages.

L'audit révèle néanmoins **5 constats de sévérité élevée**, concentrés sur la **concurrence et l'intégrité de l'état** (perte de mises à jour, verrou d'automatisation perfectible), le **démarrage bloquant**, une **divergence de schéma SQL**, et le **rate limiting inefficace derrière un reverse proxy**. Aucun de ces constats n'est une faille exploitée à distance sans authentification ; en revanche plusieurs peuvent provoquer des **comportements domotiques erratiques** (double commande climatiseur, perte d'état) ou une **indisponibilité** (crashloop au démarrage, blocage des workers).

| Sévérité | Nombre | Thèmes dominants |
|---|---|---|
| Élevée | 5 | Concurrence/état, démarrage, schéma, rate limiting |
| Moyenne | 11 | Performance API, validations, retries, TLS, sessions, supervision |
| Faible / Info | 12 | Durcissement, dette, documentation, observabilité, tests |

**Priorité absolue (P0) :** fiabiliser le verrou et les écritures d'état (REL-01, DATA-01), rendre le démarrage non bloquant (REL-02), aligner le schéma `state_history` (DATA-02), activer `ProxyFix` (SEC-01).

---

## 2. Architecture constatée

- **Web :** Flask, blueprint unique `dashboard_bp`, templates Jinja, sessions cookie signées, Flask-WTF (CSRF global), Flask-Limiter (par IP), Gunicorn 1 worker sync × 2 threads (contrainte APScheduler).
- **Automatisation :** `SchedulerService` (APScheduler `BackgroundScheduler`, polling adaptatif) → `AutomationService.run_once` → cascade scènes SwitchBot → commandes directes (`setAll`/`turnOff`), avec verrou distribué persistant dans le state store.
- **Données :** `PostgresStore` (table `json_store`, document JSONB par `kind`, verrou ligne `FOR UPDATE`) avec fail-fast en production, `JsonStore` (fichier, écriture atomique tmp+rename) en dev ; `HistoryService` (table `state_history`, buffer + flush temporisé, rétention 6 h) ; `ApiQuotaTracker` (compteur journalier dans l'état).
- **Client API :** `SwitchBotClient` (HMAC-SHA256 v1.1, retries, caches 60 s, capture des en-têtes de quota).
- **Déploiement :** Docker non-root + healthcheck `/healthz` ; worker d'arrière-plan optionnel `run_worker.py`.

---

## 3. Constats détaillés

### 3.1 Sévérité élevée

#### REL-01 — Verrou d'automatisation : expiration fixe de 2 min et orphelins possibles
**Fichiers :** `switchbot_dashboard/automation.py` (`_acquire_lock`, `_release_lock`, `run_once`), `gunicorn.conf.py`, `switchbot_dashboard/switchbot_api.py` (`_request`).

Le verrou est un drapeau `automation_in_progress` + horodatage dans le state store, posé sous transaction `FOR UPDATE` (acquisition atomique, bien). Mais :

- l'expiration est **codée en dur à 2 minutes**, sans heartbeat de renouvellement ;
- un tick peut durer **plus de 2 minutes** en conditions dégradées : `poll_meter` (2 tentatives × timeout 15 s) + `poll_aircon_status(force=True)` (2 × 15 s) + une ou deux commandes (2 × 15 s chacune) + délais de retry → 90–150 s plausibles ; le timeout Gunicorn (120 s) peut en outre **tuer le worker en plein tick**, laissant le verrou orphelin jusqu'à expiration ;
- passé ce délai, un second exécuteur (le worker `run_worker.py`, ou une requête HTTP `/actions/*` sur un autre thread) peut **acquérir le verrou pendant que le premier tick tourne encore** → deux chaînes de décision concurrentes → double envoi de commande au climatiseur, écritures d'état entrelacées.

**Impact :** double commande domotique, incohérences d'état ; indisponibilité temporaire si le verrou reste orphelin (2 min de ticks refusés).
**Recommandation :** (1) plafonner explicitement la durée d'un tick (timeouts API plus courts, budget temps) sous les 120 s du worker ; (2) implémenter un verrou avec *fencing token* (compteur incrémenté à l'acquisition, vérifié à chaque écriture d'état) ou un heartbeat repoussant l'expiration ; (3) porter l'expiration au moins au-dessus du pire cas mesuré (`average_tick_duration` est déjà collecté — s'en servir pour calibrer) ; (4) journaliser toute acquisition par expiration comme un incident.

---

#### DATA-01 — Perte de mises à jour sur le document d'état monolithique (lost updates)
**Fichiers :** `switchbot_dashboard/automation.py` (`CachedStoreWrapper`, `_update_state`, `_acquire_lock`), `switchbot_dashboard/quota.py` (`record_call`, `_normalize_state`), `switchbot_dashboard/routes.py` (`_update_state_on_success`, `_update_state_on_error`, `quota_refresh`), `switchbot_dashboard/postgres_store.py` (`write`).

Tout l'état runtime vit dans **un seul document JSONB** (`json_store`, `kind='state'`) remplacé intégralement à chaque écriture. Or :

- la quasi-totalité des écritures sont des **read-modify-write hors transaction** (`_update_state`, `ApiQuotaTracker.record_call`, `_update_state_on_success` des routes…) : deux écrivains concurrents (thread scheduler vs thread HTTP, ou web vs worker) s'écrasent mutuellement (last-write-wins) ;
- le `CachedStoreWrapper` de l'automation met en cache l'état et ne l'invalide **qu'au début de `run_once` et autour des transactions** ; les routes HTTP écrivent quant à elles dans le **store brut** (`app.extensions["state_store"]`). Scénario concret : une action manuelle écrit `assumed_aircon_power="off"` ; un `/quota/refresh` (qui passe par le wrapper partagé, cache potentiellement périmé) relit l'ancien document et réécrit l'ensemble des clés → **l'effet de l'action manuelle est perdu** jusqu'au prochain poll.

**Impact :** dérive entre état supposé et état réel du climatiseur, perte de compteurs de quota, comportements d'automatisation incohérents et difficiles à diagnostiquer.
**Recommandation :** (1) canaliser **toutes** les écritures d'état par des transactions (le mécanisme `FOR UPDATE` existe déjà) ou par des mises à jour partielles au niveau JSONB (`jsonb_set` sur clés précises) au lieu du remplacement de document ; (2) supprimer le cache partagé ou le rendre strictement *write-through invalidating* côté routes (ou faire passer les routes par le même wrapper) ; (3) à terme, éclater l'état en lignes/colonnes par domaine (quota, verrou, télémesure) pour limiter le champ des conflits.

---

#### REL-02 — Démarrage bloquant : appels réseau synchrones dans `create_app()`
**Fichiers :** `switchbot_dashboard/__init__.py` (`automation_service.poll_meter()` puis `scheduler_service.start()`), `switchbot_dashboard/scheduler.py` (`start` → `_run_tick_safe()` immédiat), `Dockerfile` (`HEALTHCHECK --start-period=5s`).

`create_app()` effectue un **poll API synchrone** au boot, puis `scheduler.start()` exécute **un tick complet immédiat et synchrone**. Gunicorn n'ouvre le socket qu'après l'évaluation de `create_app()`. Avec retries et timeouts (jusqu'à ~45 s par endpoint en cas d'API injoignable), le démarrage peut prendre **plusieurs dizaines de secondes**, alors que le healthcheck Docker n'accorde que 5 s de grâce (puis échecs toutes les 30 s).

**Impact :** readiness très lente ; sur un orchestrateur qui redémarre les conteneurs unhealthy, **risque de boucle de redémarrage** si l'API SwitchBot est lente au boot ; le même coût est payé par `run_worker.py`.
**Recommandation :** rendre le poll initial et le premier tick **asynchrones** (thread différé, ou premier tick planifié à `now + 1 s` au lieu de synchrone), et porter `--start-period` à 30–60 s. Vérifier en outre que le healthcheck ne dépend pas de la fraîcheur du premier poll.

---

#### DATA-02 — Divergence de schéma `state_history.last_action` (VARCHAR(50) vs VARCHAR(255))
**Fichiers :** `scripts/create_history_table.sql` (`last_action VARCHAR(50)`), `switchbot_dashboard/history_service.py` (`_ensure_table_exists` : `VARCHAR(255)`).

Les actions réellement écrites sont du type `scene(<scene_id>) (automation_off_outside_window)` — **> 50 caractères**. Si la table a été créée par le script SQL (provisionnement manuel ou CI), chaque INSERT échoue ; le buffer d'historique retente indéfiniment puis **jette les enregistrements au-delà de 100** (cap mémoire). L'échec est logué mais silencieux côté produit.

**Impact :** historique de monitoring perdu en continu selon l'origine du provisionnement ; symptômes difficiles à relier à la cause.
**Recommandation :** unifier la définition (255 partout), supprimer la duplication script/code (source unique de schéma), et introduire de vraies **migrations versionnées** (Alembic) plutôt que `CREATE TABLE IF NOT EXISTS`.

---

#### SEC-01 — Rate limiting par IP sans `ProxyFix` ; stockage `memory://`
**Fichiers :** `switchbot_dashboard/extensions.py` (`key_func=get_remote_address`), `switchbot_dashboard/__init__.py` (`RATELIMIT_STORAGE_URI` défaut `memory://`), aucun `ProxyFix` dans le code.

Derrière un reverse proxy (topologie Docker/Render typique), `request.remote_addr` est **l'IP du proxy** : tous les clients partagent les mêmes compteurs. Conséquences symétriques : un seul utilisateur (ou attaquant) épuise le quota `/login` de 5/min **pour tout le monde** (déni de service entre utilisateurs) ; à l'inverse, un attaquant qui contourne le proxy n'est plus limité par IP réelle. Le warning prod sur `memory://` est utile mais ne traite pas le cas multi-processus web + worker.

**Impact :** verrouillage collectif de l'authentification ou contournement des limites.
**Recommandation :** activer `werkzeug.middleware.proxy_fix.ProxyFix` (paramétré par le nombre de proxies de confiance, via env) **uniquement** derrière un proxy de confiance, documenter le réglage, et passer le stockage du limiter à Redis/Postgres en production multi-processus.

---

### 3.2 Sévérité moyenne

#### PERF-01 — `/devices` non limité, N+1 appels API séquentiels, caches non thread-safe
`routes.py` (`devices`, `_enrich_device_status`), `switchbot_api.py` (`_status_cache`, `_devices_cache`).
La page appelle `get_devices()` puis `get_device_status()` **pour chaque appareil, séquentiellement** (timeout 15 s pièce). Sans rate limit sur la route, chaque requête hors cache (60 s) multiplie la consommation de quota SwitchBot et peut figer la page des dizaines de secondes. Les dicts de cache ne sont pas verrouillés (accès concurrents des 2 threads Gunicorn → appels dupliqués). **Reco :** limiter la route (ex. 10/min), paralléliser ou borner le nombre d'enrichissements, protéger les caches par un lock (ou `threading.RLock`).

#### REL-03 — Actions longues exécutées dans la requête HTTP
`routes.py` (`run_once`, `_handle_direct_action`), `gunicorn.conf.py` (`threads = 2`, `timeout = 120`).
`/actions/run_once` et les actions aircon exécutent tout le cycle API **en ligne** ; deux requêtes simultanées suffisent à saturer les 2 threads. Un timeout worker en plein cycle laisse le verrou orphelin (cf. REL-01) et l'utilisateur sans retour. **Reco :** basculer en traitement asynchrone (202 + job, ou délégation au scheduler via un drapeau `run_once_requested`), réduire les timeouts API pour les actions manuelles.

#### SEC-02 — `scene_id` non validé (injection de chemin vers l'API SwitchBot)
`routes.py` (`update_settings` : `scene_{key}_id` stocké brut), `switchbot_api.py` (`run_scene` : `POST /v1.1/scenes/{scene_id}/execute`).
Contrairement à `device_id` (regex + longueur), les identifiants de scène ne subissent **aucune validation**. Un identifiant contenant `/`, `..` ou des paramètres forgerait un chemin arbitraire sur `api.switch-bot.com` (SSRF borné au domaine, authentification requise — risque modéré). **Reco :** appliquer la même regex alphanumérique/tirets que `device_id`.

#### SEC-03 — Validations métier incomplètes à la soumission des paramètres
`routes.py` (`_update_profiles`, `_update_time_windows`).
`min_temp > max_temp` est accepté puis ne sera détecté qu'au runtime (automation en échec) ; les heures de fenêtre ne sont pas validées au format `HH:MM` (une valeur invalide rend la fenêtre **silencieusement inactive** via `_is_time_in_window`) ; les températures ne sont pas bornées. **Reco :** valider `min ≤ target ≤ max`, le format horaire (`_parse_hhmm`), et borner les températures (ex. 10–35 °C) avec messages d'erreur explicites.

#### REL-04 — Retries non idempotents et politique de retry perfectible
`switchbot_api.py` (`_request`).
Les POST (`send_command`, `run_scene`) sont **retentés** sur 429/5xx/190/exception réseau : si la première tentative a abouti côté serveur mais que la réponse s'est perdue, la commande est **exécutée deux fois** (bénin pour un climatiseur, mais pattern dangereux). `Retry-After` n'est pas respecté sur 429, pas de jitter (thundering herd entre web et worker), et le quota fallback est incrémenté **par tentative** (surcomptage conservateur). **Reco :** ne retenter que les GET et les erreurs avant envoi ; honorer `Retry-After` ; backoff exponentiel + jitter ; clarifier la sémantique de comptage.

#### REL-05 — Pool PostgreSQL sans timeouts d'attente ni de requête
`__init__.py` (`ConnectionPool(min_size=1, max_size=10)`), `postgres_store.py`, `history_service.py`.
Aucun `timeout` d'acquisition de connexion ni `statement_timeout` : si le pool est épuisé ou la base lente, les requêtes HTTP et les threads **bloquent indéfiniment** (jusqu'au timeout Gunicorn). **Reco :** `ConnectionPool(..., timeout=5)`, `options="-c statement_timeout=5000"`, et surveillance du nombre de connexions.

#### SEC-04 — TLS PostgreSQL en `require` sans vérification d'identité
`__init__.py` / `postgres_store.py` (`POSTGRES_SSL_MODE` défaut `require`).
`sslmode=require` chiffre sans vérifier le certificat → MITM possible sur le chemin DB. **Reco :** `verify-full` avec le CA du fournisseur (Neon le publie), en conservant `require` comme dernier recours documenté.

#### SEC-05 — Fuite partielle d'identifiants dans les logs de migration
`scripts/migrate_to_postgres.py` (`logger.info(f"PostgreSQL URL: {args.postgres_url[:20]}...")`).
Les 20 premiers caractères de `postgresql://user:password@…` incluent le début du couple user/mot de passe. **Reco :** ne logger que schéma + hôte (parser l'URL), jamais le préfixe brut.

#### SEC-06 — Sessions non révocables, logout en GET, mot de passe en clair
`routes.py` (`login`, `logout`), `__init__.py` (sessions cookie), `.env.example`.
Les sessions sont des cookies signés stateless : impossible de révoquer une session volée avant expiration (30 min, atténuant) ; le changement de `DASHBOARD_PASSWORD` ne ferme pas les sessions existantes ; `/logout` en GET est CSRF-able (impact faible) ; le mot de passe vit en clair dans l'environnement (choix courant en auto-hébergement, à assumer). **Reco :** passer `/logout` en POST, documenter la rotation (changer aussi `FLASK_SECRET_KEY` invalide toutes les sessions — à préciser dans le runbook), et optionnellement accepter un hash Werkzeug du mot de passe.

#### OPS-01 — `run_worker.py` sans watchdog ; risque de double scheduler
`run_worker.py`, `gunicorn.conf.py`, `.env.example`.
Le worker boucle sur `sleep(1)` sans supervision : si le scheduler interne meurt, le process reste « sain » sans rien faire. Si `SCHEDULER_ENABLED=true` côté web **et** worker (mauvaise configuration), deux schedulers tournent — mitigé par le verrou DB, mais avec ticks fantaisistes et I/O gaspillés. **Reco :** healthcheck fichier/périodique dans le worker, garde-fou explicite au démarrage (refus de démarrer si le verrou « scheduler » est déjà détenu durablement), documentation de la topologie attendue.

#### SEC-07 — `/debug/state` sans rate limiting
`routes.py` (`debug_state`).
Endpoint exempté de l'auth session (par design, token Bearer + comparaison constante + allowlist — bien) mais **sans limiter** : brute-force du token possible sans friction. **Reco :** `@limiter.limit("5 per minute")`.

---

### 3.3 Sévérité faible / informative

| ID | Constat | Détail & recommandation |
|---|---|---|
| SEC-08 | CSP permissive | `script-src/style-src 'unsafe-inline'` (`__init__.py`). Autoescape Jinja partout (aucun `\| safe` trouvé), mais passer à des nonces/hashes réduirait le risque XSS résiduel. |
| SEC-09 | Erreurs API brutes dans les flashs | `routes.py` affiche `str(exc)` (corps SwitchBot avec IDs d'appareils) et le stocke dans `last_error`. Mapper vers des messages génériques + log détaillé. |
| SEC-10 | `/healthz` non authentifié | Divulgue l'état opérationnel (postgres, scheduler). Acceptable en interne ; à durcir si exposition publique (token ou réseau privé). |
| SEC-11 | Réinitialisation de quota en jour UTC | `quota.py` : vérifier que la fenêtre de reset SwitchBot est bien minuit UTC, sinon compteurs décalés. |
| OPS-02 | Dépendances non épinglées | `requirements.txt` en plages (`Flask>=2.3,<4`), pas de lock/hashes ; `redis` (déprécié) et `beautifulsoup4` (tests uniquement) installés en production ; image `python:3.11-slim` non pinnée par digest. Reco : `pip-compile`/uv + extras `dev`, pin par digest. |
| OPS-03 | Observabilité limitée | Pas de métriques, pas de request-id, logs non structurés. Reco : logs JSON, corrélation requête, export Prometheus minimal (`/metrics` protégé). |
| MAIN-01 | Documentation divergente du code | `AGENTS.md` et `codingstandards.md` décrivent une cascade **IFTTT** (`extract_ifttt_webhooks`, blocage SSRF des IP privées) **absente du code** — la fonction n'existe pas. Mettre à jour la doc (ou réintroduire la feature avec ses défenses) pour éviter un faux sentiment de sécurité. |
| MAIN-02 | Code mort | `SimpleTransactionContext` (`config_store.py`) inutilisé ; mocks d'historique en mode debug (`routes.py`) à isoler explicitement. |
| DATA-03 | Pas de migrations versionnées | Schéma géré par `IF NOT EXISTS` (cf. DATA-02) ; rétention historique 6 h codée en dur dans `create_app` (à rendre configurable) ; cap buffer 100 → perte acceptée mais à tracer en métrique. |
| DATA-04 | `JsonStore` perfectible | Pas de fsync avant rename ; `JSONDecodeError` non convertie en `StoreError` (500 brut possible) ; permissions fichier héritées de l'umask. |
| TEST-01 | Couverture et intégration | Couverture déclarée ~76 % vs objectif 85 % ; `test_postgres_store.py` figure dans l'arborescence mais son contenu est absent de l'export audité — à vérifier : il semble être le seul test non mocké du pool (conftest l'exclut du patch). CSRF désactivé dans plusieurs tests de routes → la couverture CSRF réelle est limitée. Reco : tests d'intégration Postgres via testcontainers, mesure de couverture en CI. |
| UX-01 | Redirection incohérente | Succès de `POST /settings` → `index` au lieu de la page réglages ; les flashs d'erreur de validation renvoient bien vers les réglages. |

---

## 4. Points forts (à conserver)

- **Sécurité applicative** : CSRF global (Flask-WTF) + jetons meta + intercepteurs Fetch/XHR ; cookies `Secure`/`SameSite=Lax`, durée 30 min, **rotation de session anti-fixation** ; `hmac.compare_digest` pour mot de passe et token debug ; **allowlist explicite** sur `/debug/state` ; en-têtes `X-Content-Type-Options`, `X-Frame-Options: DENY`, `Referrer-Policy`, HSTS en prod ; **fail-fast** si `FLASK_SECRET_KEY`/`DASHBOARD_PASSWORD` manquants en production.
- **Injection** : SQL intégralement paramétré (`psycopg.sql.Identifier/Literal`), métriques et granularités en listes blanches ; aucune injection SQL identifiée ; Jinja auto-échappé.
- **Validation** : helpers `_safe_int/_safe_float/_safe_bool` avec bornes appliqués systématiquement ; `device_id` par regex ; timezone IANA vérifiée ; mode allowlisté.
- **Résilience de stockage** : verrou ligne `FOR UPDATE` pour les transactions, bascule Postgres→JSON en dev avec health-check, écriture fichier atomique (tmp+rename), buffer d'historique avec retry et cap mémoire.
- **Client API** : signature HMAC v1.1 correcte, capture des en-têtes de quota, caches 60 s anti-N+1, retries configurables.
- **Métier** : idempotence bien pensée (état supposé, hystérésis, cooldowns différenciés ON/OFF, off-repeat, polling adaptatif avec warmup), scheduler `max_instances=1` + `coalesce`.
- **Tests & livraison** : 178 tests (sécurité, bascule store, scheduler, routes, frontend), Dockerfile multi-étages non-root, `.dockerignore` propre, healthcheck intégré.

---

## 5. Plan de remédiation priorisé

### P0 — Cette semaine (risque domotique / disponibilité)
1. **DATA-01** — Canaliser toutes les écritures d'état sous transaction (ou `jsonb_set` partiel) ; aligner routes et automation sur le même chemin d'écriture ; invalider le cache partagé à chaque écriture externe.
2. **REL-01** — Plafonner la durée d'un tick sous le timeout worker ; verrou à heartbeat ou fencing token ; alerte sur acquisition par expiration.
3. **REL-02** — Poll initial et premier tick asynchrones ; `--start-period` ≥ 30 s dans le healthcheck.
4. **DATA-02** — Aligner `last_action` sur VARCHAR(255) partout ; source unique de schéma.
5. **SEC-01** — `ProxyFix` conditionné par env + documentation proxy ; limiter Redis/Postgres en multi-processus.

### P1 — Ce mois (robustesse)
6. **PERF-01 / REL-03** — Rate limit `/devices`, paralléliser l'enrichissement, verrouiller les caches ; actions longues en asynchrone (202) ou timeouts API réduits côté HTTP.
7. **SEC-02 / SEC-03** — Valider `scene_id`, `min ≤ max`, format `HH:MM`, bornes températures.
8. **REL-04 / REL-05** — Retries idempotents + `Retry-After` + jitter ; timeouts pool (`timeout=5`, `statement_timeout`).
9. **SEC-04 / SEC-05 / SEC-07** — `verify-full` Postgres ; log d'URL assaini ; limiter `/debug/state`.
10. **OPS-01** — Watchdog worker + garde anti-double scheduler.

### P2 — Trimestre (durcissement & hygiène)
11. **SEC-06 / SEC-08 / SEC-09** — Logout en POST, runbook rotation de session, CSP à nonces, messages d'erreur génériques.
12. **OPS-02 / OPS-03** — Lock des dépendances + digest d'image ; logs structurés + métriques minimales.
13. **MAIN-01 / MAIN-02** — Synchroniser documentation et code (IFTTT), retirer le code mort.
14. **DATA-03 / DATA-04 / TEST-01** — Alembic, rétention configurable, fsync/StoreError JsonStore, tests d'intégration testcontainers + couverture CI ≥ 85 %.

---

## 6. Annexes

### 6.1 Écarts documentation ↔ implémentation
- `AGENTS.md` §3 et `codingstandards.md` promettent « cascade IFTTT → scènes → commandes » et « blocage des IP privées pour webhooks » : **aucune trace d'IFTTT ni de `extract_ifttt_webhooks` dans le code** ; la cascade réelle est scènes → commandes directes.
- `AGENTS.md` §2 impose « alerter si >3 échecs consécutifs avant fallback » : non implémenté tel quel (le fallback est décidé au boot par health-check).
- `codingstandards.md` indique ~76 % de couverture pour une cible 85 %.

### 6.2 Notes de périmètre
- Audit statique sur export Repomix ; `tests/test_postgres_store.py` est listé dans l'arborescence mais son contenu n'est pas inclus dans l'export — les constats de couverture de la couche transactionnelle sont à confirmer contre le dépôt réel.
- Aucun test dynamique (fuzzing des routes, charge) n'a été exécuté ; les constats de concurrence sont déduits de l'analyse du code.
