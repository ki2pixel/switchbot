# Audit Backend / Frontend — SwitchBot Dashboard v2

**Date de l'audit :** 2026-07-17
**Périmètre :** ensemble du dépôt (`app.py`, `switchbot_dashboard/`, `templates/`, `static/`, `scripts/`, `tests/`, `Dockerfile`, `gunicorn.conf.py`, `requirements.txt`)
**Méthode :** revue de code statique manuelle (17 000 lignes), traçage des flux d'authentification, de concurrence et de persistance, revue des templates/JS, de la configuration Docker et de la stratégie de tests. Aucune exécution dynamique (le code n'a pas été lancé).

---

## 1. Résumé exécutif

**Verdict global : bonne santé — 7,5/10.** Le projet affiche une maturité nettement supérieure à la moyenne des projets domotiques personnels : architecture en services injectés, sécurité prise au sérieux (CSRF, rate-limiting, fail-fast sur les secrets, comparaisons à temps constant), client API SwitchBot soigné (HMAC v1.1, backoff + jitter, respect de `Retry-After`), frontend offline-first accessible, et 187 tests automatisés.

**Aucune faille critique** (pas d'injection SQL, pas de contournement d'authentification, pas de secret en dur, pas d'exécution de code à distance).

**3 constats élevés** à traiter en priorité :

1. **La page 503 prévue en cas de panne PostgreSQL ne s'affichera jamais** : `PostgresStoreError` n'hérite pas de `StoreError`, le handler global ne la capture pas → erreurs 500 non maîtrisées (B-01).
2. **Le pool PostgreSQL partagé perd tous les timeouts** prévus par le garde-fou REL-05 → un ralentissement DB peut geler les workers Gunicorn (B-02).
3. **Récursion infinie côté frontend** dans `history.js` si l'utilisateur applique une période « Personnalisée » sans date de début → onglet gelé (F-01).

| Domaine | Note | Commentaire |
|---|---|---|
| Backend — architecture | 8,5/10 | Services clairs, transactions, failover Postgres→JSON, fail-fast prod |
| Backend — sécurité | 8/10 | Rien de critique ; CSP perfectible, rate-limit dépendant du proxy |
| Backend — fiabilité | 7/10 | Quelques races et écritures non transactionnelles |
| Frontend — sécurité | 8/10 | Aucune injection XSS dynamique ; CSP `unsafe-inline` à durcir |
| Frontend — qualité/UX | 7/10 | Bugs fonctionnels réels (récursion, `customEnd` ignoré, graphs irrécupérables) |
| Accessibilité | 8,5/10 | Skip-links, aria-live, focus management, reduced-motion : rare à ce niveau |
| Persistance / SQL | 7,5/10 | Requêtes paramétrées sûres ; DDL au boot, buffer perdu au shutdown |
| DevOps | 7/10 | Dockerfile propre (multi-stage, non-root) ; deps non pinnées, redis/bs4 superflus |
| Tests | 7,5/10 | 187 tests backend solides ; tests « frontend » purement statiques (regex), aucun test JS d'exécution |

**Légende des sévérités :** 🔴 Élevée · 🟠 Moyenne · 🟡 Basse · ⚪ Info

---

## 2. Cartographie de l'application

```
app.py / run_worker.py
   └─ create_app()  (switchbot_dashboard/__init__.py)
        ├─ Stores : PostgresStore (json_store table) ⇄ fallback JsonStore
        ├─ SwitchBotClient (HMAC SHA-256, retry, quota via headers)
        ├─ ApiQuotaTracker (compteur journalier persisté dans state)
        ├─ HistoryService (buffer → table state_history, rétention 6 h)
        ├─ AutomationService (tick : fenêtres horaires → hystérésis →
        │    cooldown → scène SwitchBot → fallback commande directe)
        ├─ SchedulerService (APScheduler, polling adaptatif)
        └─ Blueprint dashboard (routes.py) : UI Jinja + API /history/api/*
Frontend : templates Jinja autonomes (pas de layout commun),
           SPA router maison (pjax), loaders + intercepteurs CSRF,
           Chart.js local avec décimation LTTB.
```

Points d'architecture remarquables : injection via `app.extensions`, verrou d'automatisation distribué via la ligne `state` en base (`SELECT … FOR UPDATE`), polling adaptatif hors fenêtres, fallback gracieux Postgres → fichiers JSON (interdit en production, fail-fast explicite — très bien).

---

## 3. Constats détaillés — Backend

### 3.1 Sécurité

**Points forts (vérifiés dans le code) :**

- Authentification par mot de passe avec support des hash Werkzeug (`pbkdf2:`/`scrypt:`/`argon2:`) et comparaison à temps constant `hmac.compare_digest` en clair.
- Rate-limiting login `5/min`, routes d'action `10/min`, API history `30/min`.
- Protection CSRF globale Flask-WTF + injection automatique du jeton dans les intercepteurs `fetch`/XHR côté JS.
- Fail-fast au démarrage si `FLASK_SECRET_KEY` faible/absent ou `DASHBOARD_PASSWORD` manquant en production (avec liste de clés bannies).
- Headers de sécurité : `X-Content-Type-Options`, `X-Frame-Options: DENY`, `Referrer-Policy`, HSTS (hors debug), CSP.
- Cookies : `Secure` (hors debug), `SameSite=Lax`, `HttpOnly` (défaut Flask), session permanente 30 min, rotation de session au login.
- `/debug/state` : token Bearer obligatoire, 404 (et non 401/403) pour ne pas révéler l'existence de l'endpoint, allowlist de clés, refus du token en query string (testé).
- Validation serveur stricte de tous les inputs (`_as_int/_as_float/_as_bool` bornés, regex HH:MM, regex IDs appareils/scènes, timezone IANA validée, borne 10–35 °C, min≤max).
- SQL 100 % paramétré ; composition `psycopg.sql` avec `sql.Identifier`/`sql.Literal` — pas d'injection possible via `metrics`/`granularity` (allowlists).

#### 🔴 S-01 — CSP permissive : `script-src 'unsafe-inline'`
`__init__.py → set_security_headers`. La CSP autorise les scripts inline — elle est quasi inopérante contre le XSS. Elle est aujourd'hui **nécessaire** (scripts inline dans `index.html`, `executeInlineScript` du SPA router), donc non bloquante, mais : ajouter au minimum `object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, et planifier des nonces (`script-src 'nonce-…'`) à moyen terme.

#### 🟠 S-02 — Rate-limiting dépendant de la configuration proxy
`PROXY_FIX_FOR` est optionnel. Derrière un proxy (Render, nginx) **sans** cette variable, `get_remote_address` voit l'IP du proxy → tous les utilisateurs partagent le même bucket → lockout global au bout de 5 logins/min **et** inefficacité contre un attaquant. Le code avertit pour `memory://` mais pas pour l'absence de ProxyFix. **Reco :** détecter la présence de `X-Forwarded-For` sans ProxyFix configuré et logger un avertissement au boot.

#### 🟡 S-03 — `/healthz` non authentifié expose l'état interne
Statut scheduler, `automation_enabled`, `postgres_connected`, timestamps de tick. Divulgation faible, pratique courante, mais réduire au strict nécessaire (ou exiger le même Bearer que `/debug/state`).

#### 🟡 S-04 — `SESSION_COOKIE_SECURE` déduit du flag debug
`SESSION_COOKIE_SECURE = not app.debug and not app.testing`. Un déploiement « production-like » en HTTP local avec une vraie clé secrète rendra la connexion impossible (cookie Secure non transmis). Préférer une variable explicite `SESSION_COOKIE_SECURE=1` documentée.

#### 🟡 S-05 — Surface supply-chain
`redis>=5,<6` (backend abandonné) et `beautifulsoup4` (usage tests uniquement) sont dans `requirements.txt` de production ; aucune version pinnée (plages uniquement), pas de lockfile. Déplacer bs4 en dev, retirer redis, geler les versions (pip-tools/uv).

### 3.2 Fiabilité, concurrence, erreurs

#### 🔴 B-01 — Le handler d'erreurs 503 ne capturera jamais les erreurs PostgreSQL
`routes.py` : `@dashboard_bp.app_errorhandler(StoreError)`. Or `PostgresStoreError(RuntimeError)` (`postgres_store.py`) **ne dérive pas** de `StoreError(RuntimeError)` (`config_store.py`). En panne DB, `index()`, `settings_page()`, `actions_page()` (qui capture pourtant `StoreError` !), `update_settings()` lèvent une 500 brute au lieu de la page `503.html` prévue. Le handler `handle_store_error` et les `except StoreError` sont morts en production.
**Correctif :** `class PostgresStoreError(StoreError)` (ou enregistrer le handler pour les deux types).

#### 🔴 B-02 — Pool partagé créé sans les timeouts du garde-fou REL-05
Dans `__init__.py`, le pool partagé est créé avec seulement `conninfo, min_size, max_size, sslmode`. Les paramètres de `PostgresStore._initialize_pool` (`timeout=5.0` au checkout, `connect_timeout=5`, `statement_timeout=5000`) **sont perdus** dès que le pool partagé est utilisé — c'est-à-dire en production. Une requête qui se fige côté DB peut alors pendre indéfiniment (pas de `statement_timeout`) et épuiser les 2 threads Gunicorn.
**Correctif :** créer le pool partagé avec les mêmes kwargs que `_connection_params`.

#### 🟠 B-03 — « Polling adaptatif » impossible à désactiver via l'UI
`routes.py → update_settings` :
```python
settings["adaptive_polling_enabled"] = _as_bool(
    request.form.get("adaptive_polling_enabled", settings.get("adaptive_polling_enabled", True))
)
```
Une checkbox décochée n'est **pas envoyée** par le navigateur → le `get` retourne la valeur courante (`True`) → le réglage reste activé à jamais. Les autres checkbox utilisent le bon pattern (`request.form.get(...)` sans défaut → `None` → `False`).
**Correctif :** `_as_bool(request.form.get("adaptive_polling_enabled"))`.

#### 🟠 B-04 — Paramètre `limit` non borné sur `/history/api/data`
`_parse_history_query_params` : `limit = int(request_args.get("limit", 1000))` — aucune borne haute (contrairement à `/latest` qui borne à 100). Un client authentifié peut demander `limit=10^9` ; la plage `start`/`end` n'est pas bornée non plus. Impact réduit par la rétention de 6 h, mais borner à p. ex. 5 000 et valider `start < end`, `limit ≥ 1`.

#### 🟠 B-05 — Jeton de verrou partagé entre threads via un attribut d'instance
`AutomationService._current_lock_token` est un attribut d'instance lu/écrit par le thread scheduler, le thread `run_once` manuel et les threads de requêtes (`_handle_direct_action`). Un `run_once()` concurrent remet le jeton à `None` pendant qu'un autre tick l'utilise → la vérification de propriété du verrou dans `_update_state`/`_release_lock` peut être silencieusement contournée ou échouer à tort. Le verrou DB reste le vrai mutex (correct), mais ce jeton « optimistic check » n'est pas fiable.
**Reco :** passer le jeton en paramètre de la chaîne d'appels, ou `threading.local()`.

#### 🟠 B-06 — Écritures d'état non transactionnelles → pertes de mise à jour
`_clear_off_repeat_task`, `_schedule_off_repeat_task`, `_process_off_repeat_task` font `read()` → modification → `write()` **hors transaction**, alors que `ApiQuotaTracker` et les routes écrivent en transaction `FOR UPDATE` depuis d'autres threads. Entre le read et le write, une écriture concurrente (quota, action manuelle) est écrasée. Probabilité faible à cette échelle, impact : dérive des compteurs de quota / drapeaux perdus.
**Reco :** réutiliser `_update_state` (transactionnel) pour ces mutations.

#### 🟠 B-07 — Allowlist de `/debug/state` obsolète → endpoint quasi vide
Les clés autorisées (`temperature`, `humidity`, `last_meter_timestamp`, `automation_last_status`, …) ne correspondent pas aux clés réellement écrites (`last_temperature`, `last_humidity`, `last_read_at`, `last_action`, …). Seules `api_requests_total` et `assumed_aircon_power` passent : l'endpoint renvoie presque toujours `{}`. Soit l'allowlist est à mettre à jour, soit l'endpoint est à retirer.

#### 🟠 B-08 — Retry des POST sur erreurs transport → double exécution possible
`switchbot_api.py → _request` : « Transport errors are always retryable » — y compris pour `send_command`/`run_scene` (POST). Après un timeout où l'API a pu recevoir la commande, le retry rejoue l'ordre (clim IR : doublon généralement bénin mais réel). Les erreurs HTTP ne sont, elles, pas rejouées sur POST (bien). **Reco :** ne retryer les POST que sur échec de connexion avant envoi, ou documenter l'idempotence.

#### 🟠 B-09 — `/devices` : risque de timeout Gunicorn et consommation de quota
Pour chaque appareil, un appel `get_device_status` (timeout 15 s, jusqu'à 2 tentatives) par lots de 4 threads. Avec ~15 appareils lents : 4 lots × 30 s ≈ 120 s = `timeout` Gunicorn → worker tué (502). Chaque visite consomme aussi N appels de quota (cache 60 s seulement).
**Reco :** timeout réduit pour l'enrichissement, plafond d'appareils enrichis, ou enrichissement asynchrone côté client.

#### 🟠 B-10 — Le bouton « Rafraîchir les compteurs » peut ne rien rafraîchir
`/quota/refresh` appelle `client.get_devices()`, dont le résultat est **mis en cache 60 s** : dans la fenêtre de cache, aucun appel API n'est émis, aucun header de quota n'est capturé → seule la re-normalisation locale a lieu. Prévoir `get_devices(force=True)` pour ce cas d'usage.

#### 🟡 B-11 — Fallback commande directe absent des actions manuelles ON
L'automatisation rejoue un `setAll` direct si la scène échoue (`_handle_winter_mode`/`_handle_summer_mode`), mais les boutons manuels hiver/été/fan (`_handle_direct_action`) affichent seulement « scène échouée et pas de commande directe supportée ». Incohérence UX/métier — aligner sur le comportement de l'automatisation.

#### 🟡 B-12 — Code mock de démonstration dans `routes.py` (production)
`_generate_mock_history_data` + trois blocs mock dans les routes API. Inaccessibles en production (garde `debug/testing`, vérifiée) mais alourdissent le fichier et mélangent les responsabilités. Extraire dans un module de dev.

#### 🟡 B-13 — Duplication de `_transaction_context` (routes.py, quota.py) et patterns read/write
Factoriser dans `config_store.py`. Cosmétique.

#### ⚪ B-14 — Datetimes naïfs acceptés sur `/history/api/data`
`datetime.fromisoformat` sans tz → comparés en `timestamptz` (UTC DB). Le frontend envoie toujours du UTC (`toISOString`) ; documenter ou rejeter les dates naïves.

### 3.3 Client API SwitchBot (`switchbot_api.py`) — points forts

- Signature v1.1 correcte (`token + t + nonce`, HMAC-SHA256, base64), nonce UUID par requête.
- Backoff exponentiel plafonné (5 s) + jitter, respect de `Retry-After`, retry HTTP uniquement sur GET (idempotence) et sur 429/5xx ; statut 190 rejoué en GET seulement.
- Capture du quota via headers avec alias (`x-ratelimit-*`, `ratelimit-*`), fallback local en l'absence de headers, pas de double comptage (vérifié via `tracker_updated`).
- ⚪ Détail : en fin de boucle sur un 190 non résolu, l'erreur levée est générique (« SwitchBot request failed ») — le contexte 190 est perdu dans le message.

---

## 4. Constats détaillés — Frontend

### 4.1 Sécurité

**Points forts :** aucun `innerHTML` avec données dynamiques (un test le garantit pour `history.js`), tout passe par `textContent`/`createElement` ; Jinja auto-échappe ; SPA router valide la même origine avant injection de scripts et évite l'interpolation de sélecteurs CSS ; assets 100 % locaux (aucun CDN — résilience + vie privée) ; intercepteur CSRF global sur `fetch` et XHR.

#### 🟠 F-01 — 🔴 Récursion infinie dans `history.js → getTimeRangeStart()`
```javascript
case 'custom':
    const customStart = document.getElementById('customStart').value;
    return customStart ? new Date(customStart).toISOString() : this.getTimeRangeStart();
default:
    return this.getTimeRangeStart();
```
`this.currentFilters.timeRange` ne change pas pendant l'appel → « custom » sans date (ou toute valeur inattendue via `default`) = **récursion infinie, onglet gelé**. Sévérité élevée côté client car déclenchable par un simple clic sur « Appliquer » après avoir choisi « Personnalisé ».
**Correctif :** retourner `new Date(now - 6h).toISOString()` en fallback au lieu de rappeler la fonction.

#### 🟠 F-02 — Le champ « Fin » personnalisé est purement décoratif
`customEnd` est affiché mais jamais lu : `end: new Date().toISOString()` est codé en dur dans `loadHistoryData`. L'utilisateur croit filtrer une plage qu'il ne filtre pas. Utiliser `customEnd` (avec validation) ou retirer le champ.

#### 🟠 F-03 — Après une erreur API, les graphiques ne reviennent jamais
`renderChartErrorState` vide `.chart-container` (`textContent = ''`) → les `<canvas>` sont détruits ; les appels suivants à `chart.update()` s'exécutent sur des canvas hors DOM et l'erreur reste affichée jusqu'au rechargement complet de la page. Recréer les canvas (ou `chart.destroy()` + ré-init) lors de la reprise.

#### 🟡 F-04 — Bannières « Mode démonstration » empilées
`showMockDataWarning` insère une bannière à chaque `loadInitialData` (dont chaque retour d'onglet via `visibilitychange`) sans déduplication.

#### 🟡 F-05 — HTML malformé dans `settings.html`
Le `<div class="form-check form-switch mb-3">` de `automation_enabled` n'est jamais fermé ; le `<div class="row g-3">` suivant y est imbriqué par accident. Les navigateurs réparent, mais le DOM réel diffère du DOM voulu.

#### 🟡 F-06 — Règle CSS globale `[aria-hidden="true"] { display: none; }` (critical CSS d'`index.html`)
Guerre de spécificité avec FontAwesome (`.fas { display: inline-block }`) — ne fonctionne aujourd'hui que grâce à l'ordre de chargement des feuilles. Toute réorganisation cassera l'affichage des icônes ou des loaders. Restreindre la règle (p. ex. `.sb-loader-overlay[aria-hidden="true"]`).

#### 🟡 F-07 — `loaders.js` : `form.submit()` natif contourne la validation HTML5
`event.preventDefault()` puis `form.submit()` → les attributs `required` (login) et contraintes ne sont plus vérifiés côté client. Utiliser `form.requestSubmit()` après peinture du loader.

#### 🟡 F-08 — `updateStatus()` sans null-checks
`document.getElementById('statusIndicator')` etc. sont déréférencés directement ; tout renommage d'ID dans le template provoque un `TypeError` qui interrompt le flux.

#### 🟡 F-09 — Petits détails
- `py-lg-6` n'existe pas dans Bootstrap (classe morte dans `index.html`).
- Feuilles `sticky-*.css` chargées via `media="print"` + `onload` sans `<noscript>` de secours.
- Le thème forcé `dark` rend le `prefers-color-scheme` inopérant (assume dark-only — à assumer explicitement).
- Le SPA router refetch des **pages complètes** (pas de partials) : correct, mais coûteux ; envisager un header `X-Partial` pour ne rendre que `#app-content`.

### 4.2 Performance (bons points)

Décimation LTTB (100 points) sur Chart.js, `parsing:false`/`normalized:true`, animations coupées, `AbortController` avec timeout 10 s, mise en pause du polling via Page Visibility API, critical CSS inline + preload, cache 60 s sur les appels appareils, SPA sans rechargement. Travail de perf réel et mesuré — le seul vrai risque est côté backend (`/devices`, B-09).

### 4.3 Accessibilité (bons points)

Skip-links sur toutes les pages, `aria-live` pour flashes/loaders/changement de route, focus déplacé après transition SPA, descriptions textuelles dynamiques des graphiques (`aria-describedby`), `prefers-reduced-motion` respecté, cibles tactiles ≥ 44 px, rôles/labels corrects. Niveau rare sur ce type de projet. Reste : vérifier les contrastes des textes `text-muted` sur fond très sombre (mesure non réalisée ici) et F-06.

---

## 5. Persistance & SQL

| # | Sévérité | Constat |
|---|---|---|
| D-01 | 🟠 | `HistoryService._ensure_table_exists` exécute un `ALTER TABLE … TYPE VARCHAR(255)` **à chaque démarrage** (verrou DDL à chaque boot/redéploiement). À sortir du runtime (migration one-shot) avec un garde-fou `information_schema`. |
| D-02 | 🟡 | Buffer d'historique perdu à l'arrêt : pas de flush `atexit`/signal → jusqu'à ~60 s de mesures perdues à chaque déploiement. |
| D-03 | 🟡 | Rétention 6 h codée en dur (`retention_hours=6`) alors que l'UI propose « Dernières 24 h » — incohérence fonctionnelle. |
| D-04 | ⚪ | Index GIN sur `metadata` jamais requêté (coût d'écriture inutile à cette échelle) ; `idx_json_store_kind` redondant avec la PK. |
| D-05 | ⚪ | `state_history` n'a pas de contrainte de plausibilité ; `metadata.pending_off_repeat` sérialisé en JSONB — OK. |

Requêtes auditées (`get_history`, `get_aggregates`, `cleanup_old_records`, `get_latest_records`, upserts `json_store`) : **toutes paramétrées, pas d'injection**. Transactions `FOR UPDATE` correctes sur le verrou d'automatisation — c'est ce qui rend le double scheduler (web + `run_worker.py`) sûr en production.

---

## 6. DevOps & configuration

| # | Sévérité | Constat |
|---|---|---|
| O-01 | 🟡 | `requirements.txt` non pinné (plages) ; `redis` mort, `beautifulsoup4` dev-only en prod. |
| O-02 | 🟡 | Image de base `python:3.11-slim` non pinnée par digest. |
| O-03 | 🟠 | `gunicorn` : 1 worker / 2 threads. Justifié par APScheduler, mais deux requêtes `/devices` lentes (B-09) saturent le service. Documenter ou augmenter `threads` (le scheduler a son propre thread). |
| O-04 | ⚪ | `.coverage` commité dans le dépôt. |
| O-05 | ⚪ | Double scheduler web + `run_worker.py` : sûr grâce au verrou DB en Postgres ; fragile en fallback `JsonStore` multi-processus (désactivé en prod — acceptable, à documenter). |
| O-06 | ✅ | Dockerfile multi-stage, wheels précompilés, utilisateur non-root, `HEALTHCHECK` curl, `.dockerignore` exclut `.env` — propre. |

---

## 7. Tests

**187 fonctions de test**, organisation claire (`test_automation_service`, `test_backend_hardening`, `test_scheduler_service`, `test_switchbot_api`, `test_postgres_store`, …), couverture déclarée ~76 % (objectif 85 %). Les tests backend sont de vrais tests comportementaux (cooldowns adaptatifs, verrou de concurrence, failover stores, auth login hashé/clair, Bearer debug, quota, buffer history résilient).

Limites :
- Les tests « frontend » (`test_frontend_spa`, `test_frontend_loaders`, `test_frontend_accessibility`, `test_frontend_performance`) sont **statiques** : regex et BeautifulSoup sur le contenu des fichiers. Ils garantissent des patterns (pas d'`innerHTML`, présence d'ARIA) mais **aucun comportement JS n'est exécuté** → F-01/F-02/F-03 passent à travers. Recommander Playwright (ou au minimum des tests unitaires JS type Vitest pour `history.js`).
- Cas manquants identifiés : checkbox `adaptive_polling_enabled` décochée (B-03), `limit` hors bornes (B-04), erreur `PostgresStoreError` → 503 (B-01), `getTimeRangeStart('custom')` sans date (F-01).
- `conftest.py` patch proprement le pool Postgres ; `test_postgres_store.py` est le seul à toucher (en mock) la couche DB.

---

## 8. Plan d'action recommandé

**Semaine 1 (quick wins, < 1 j chacun) :**
1. `class PostgresStoreError(StoreError)` (B-01) + test 503.
2. Pool partagé avec `timeout=5.0`, `connect_timeout=5`, `statement_timeout=5000` (B-02).
3. Fix checkbox `adaptive_polling_enabled` (B-03).
4. Fix récursion `getTimeRangeStart` + fallback 6 h (F-01) ; brancher `customEnd` (F-02).
5. Borner `limit` et valider `start < end` (B-04).
6. Compléter la CSP : `object-src 'none'; base-uri 'none'; frame-ancestors 'none'` (S-01).

**Sprint suivant :**
7. Transactionnaliser les mutations `off_repeat` (B-06) ; jeton de verrou en `threading.local` (B-05).
8. Mettre à jour l'allowlist `/debug/state` (B-07) ; `get_devices(force=True)` pour `/quota/refresh` (B-10).
9. `/devices` : timeouts d'enrichissement réduits + plafond + doc quota (B-09) ; threads gunicorn (O-03).
10. Sortir l'`ALTER TABLE` du boot (D-01) ; flush `atexit` du buffer history (D-02).
11. Aligner la rétention 6 h / option 24 h (D-03) ; fallback `setAll` sur actions manuelles (B-11).

**Moyen terme :**
12. Tests navigateur Playwright sur parcours login → réglages → historique ; pinner les deps + retirer redis/bs4 (S-05) ; CSP à nonces ; avertissement ProxyFix absent (S-02).

---

## 9. Ce qui est déjà très bien (à ne pas casser)

- Fail-fast sur les secrets en production, avec liste de valeurs bannies.
- Verrou d'automatisation distribué transactionnel avec expiration de verrou mort (5 min) — rare et correct.
- Validation serveur systématique et bornée de tous les champs de réglages.
- Client API : idempotence des retries, jitter, `Retry-After`, quota par headers sans double comptage.
- Offline-first complet (aucun CDN), Chart.js optimisé, Page Visibility, AbortController.
- Accessibilité : aria-live, focus management, reduced-motion, descriptions de graphiques.
- Suite de tests backend orientée régressions (187 tests), y compris concurrence et failover.
