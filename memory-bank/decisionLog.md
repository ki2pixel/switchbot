[2026-07-16 20:47:00] - Remédiation backend complète : Phases P1 (Robustesse) et P2 (Durcissement)
- Décision :
  1. PERF-01/REL-03 — Parallélisme + Cache thread-safe : Les appels d'enrichissement des devices sont parallélisés via `ThreadPoolExecutor`. Le cache interne de `SwitchBotClient` est protégé par un `threading.Lock`. Les actions manuelles (`/actions/run_once`) retournent immédiatement 202 et s'exécutent en daemon thread. Rate-limit ajouté sur `/devices` (10/min).
  2. SEC-02/SEC-03 — Validation stricte des inputs : `scene_id` limité à 50 caractères alphanumériques. Températures bornées 10–35°C avec auto-swap si `min > max`. Format `HH:MM` validé par regex.
  3. REL-04/REL-05 — Retries robustes + timeouts Postgres : Retries exponentiels avec jitter uniquement sur GET ou erreurs 429/5xx/transport. Parsing du header `Retry-After`. Pool psycopg configuré avec `timeout=5.0` (checkout) et `statement_timeout=5000ms` (query).
  4. SEC-04/05/07 — TLS, logs, /debug/state : `sslmode=verify-full` activé depuis l'env. Masquage regex des credentials dans les logs de migration. `/debug/state` limité à 5 req/min.
  5. SEC-06 — Logout durci : Route `/logout` passée en POST-only. Bouton de déconnexion avec CSRF token dans `settings.html`. Support hachages Werkzeug (`pbkdf2:`, `scrypt:`, `argon2:`) pour `DASHBOARD_PASSWORD` via `check_password_hash`.
  6. MAIN-01/02 — Nettoyage : Suppression de la classe morte `SimpleTransactionContext`. `AGENTS.md` mis à jour pour clarifier la suppression définitive d'IFTTT.
- Motivation : Achever la totalité de la remédiation de l'audit backend. Prévenir les conditions de course sur le cache, les injections via inputs non validés, les fuites de connexions Postgres et les attaques CSRF sur le logout.
- Implémentation : Validée par 206 tests unitaires (dont 7 nouveaux couvrant les nouvelles validations et le support hachages).
- Implication : Le backend est entièrement durci (P0+P1+P2). La seule action restante côté déploiement est d'ajouter `PROXY_FIX_FOR=1` dans les variables Render.

[2026-07-16 20:45:00] - Décision : RATELIMIT_STORAGE_URI non nécessaire sur Render
- Contexte : L'utilisateur souhaitait vérifier si Redis était nécessaire pour le rate-limiting en production.
- Décision : `RATELIMIT_STORAGE_URI` est inutile car `gunicorn.conf.py` force `workers=1` quand `SCHEDULER_ENABLED=true`. Le stockage mémoire par défaut est donc suffisant et précis.
- `PROXY_FIX_FOR=1` reste indispensable sur Render pour résoudre correctement les IPs clientes derrière le proxy Render.

[2026-07-16 18:15:00] - Exécution des correctifs de la phase P0 (Concurrence, Verrous, Boot, Schéma, ProxyFix)
- Décision :
  1. Transactionnalité : Envelopper toutes les lectures/écritures d'état dans des blocs de transaction SQL (quota, routes directes, automation) et vider les caches CachedStoreWrapper à la fin de chaque tick pour éviter toute incohérence mémoire.
  2. SQL DDL automatique : Ajouter un ALTER TABLE idempotent au boot dans history_service.py pour passer last_action à VARCHAR(255).
  3. Fencing Token : Implémenter un jeton de verrou logique (automation_lock_token) dans le store d'état pour invalider et avorter proprement (via LockLostError) tout tick d'automatisation dont le verrou a expiré ou a été repris par un autre processus. Porter l'expiration du verrou à 5 minutes.
  4. Boot non bloquant : Lancer le premier poll_meter de boot et le premier tick du planificateur dans des threads daemon asynchrones en production pour éviter de bloquer le worker Gunicorn.
  5. ProxyFix : Appliquer le middleware Werkzeug ProxyFix conditionnellement derrière les proxys inverses (Render) configurés via la variable PROXY_FIX_FOR.
- Motivation : Résoudre les vulnérabilités de lost updates, de dépassement de capacité SQL, de dérives ou vols de verrous d'automatisation concurrents, de blocage des serveurs de production au démarrage, et de spoofing d'IPs clientes pour les limites de taux.
- Implémentation : Effectuée dans switchbot_dashboard/__init__.py, routes.py, automation.py, scheduler.py, et Dockerfile. Validée par 199 tests unitaires et d'intégration verts.
- Implication : Le backend est dorénavant à l'abri des conflits d'écritures concurrentes et des chevauchements d'exécution d'automatisation, démarre de façon fluide et fiable en production, et résout proprement ses IP clientes pour le rate limiting.

[2026-07-12 12:41:00] - Optimisation des performances, cache d'API et transactionnalité des routes (Phases 3-5)
- Décision : Centraliser les convertisseurs de types dans `utils.py`, utiliser un proxy contextuel de store `CachedStoreWrapper` pour éliminer les requêtes DB redondantes et garder la cohérence du quota tracker, implémenter un cache de 60s pour les requêtes d'appareils, conditionner l'enveloppement transactionnel pour supporter les MemoryStore de test, et intégrer PostgreSQL dans le workflow CI GitHub Actions.
- Motivation : Les requêtes d'appareils sur la page `/devices` engendraient un problème de requête N+1 surchargeant l'API SwitchBot. L'appel fréquent de quota snapshot dans la boucle d'automatisation lisait à chaque fois l'état depuis le store, provoquant des requêtes DB superflues. Les environnements de test utilisaient des instances MemoryStore simples sans support de transaction, et le workflow CI n'exécutait aucun test automatisé avec PostgreSQL.
- Implémentation :
  1. **Cache d'API** : Ajout d'un dictionnaire de cache de 60s sur `get_devices()` et `get_device_status()` dans `SwitchBotClient`. Plafonnement du sommeil de retry à 3s maximum lors des appels.
  2. **Cache de Store** : Introduction de `CachedStoreWrapper` qui intercepte les requêtes de lecture/écriture en mémoire tampon durant un tick unique. Partage automatique de la référence de store avec le `ApiQuotaTracker` pour garantir la cohérence des écritures.
  3. **Abstraction de Transaction** : Ajout de la fonction utilitaire `_transaction_context` dans `routes.py` pour supporter optionnellement les transactions, évitant les crashs sur les MemoryStores.
  4. **Qualité & Tests** : Unification des parsers numériques (`_safe_int`, etc.) dans `utils.py`. Configuration d'un service PostgreSQL dans `.github/workflows/build-and-push.yml` et configuration de `TEST_POSTGRES_URL` pour y exécuter `pytest`.
- Implication : L'application est hautement optimisée avec une réduction drastique des requêtes API/DB. La CI assure maintenant de manière autonome la non-régression sur base de données réelle.

[2026-07-12 10:35:00] - Remédiation des Vulnérabilités, SSL, Stockage et Concurrence du Backend (Phases 1-4)
- Décision : Implémenter l'authentification par session (mot de passe en clair DASHBOARD_PASSWORD), exiger SSL (sslmode) pour PostgreSQL, interdire le fallback JSON en production, isoler les transactions de ticks d'automatisation et introduire un verrou applicatif distribué en base de données.
- Motivation : L'audit backend de sécurité a mis en évidence l'absence d'authentification sur les routes d'action et de réglage, une configuration SSL PostgreSQL inopérante, des fallbacks JSON silencieux masquant les pannes de DB, des blocages de connexions psycopg dus aux transactions englobant des appels API lents, et un risque de collision entre les actions manuelles et l'automatisation.
- Implémentation :
  1. **Sécurité et Authentification** : Ajout d'une session-auth avec mot de passe, création de `/login` glassmorphic et `/logout`, et protection CSRF. Sécurisation de `/debug/state` via Bearer token dans l'en-tête Authorization.
  2. **Connexions BDD & Production** : Configuration explicite de `sslmode` dans les `kwargs` du psycopg ConnectionPool. Levée d'une erreur bloquante en production s'il y a un échec de connexion ou de health check.
  3. **Concurrence & Transactions** : Suppression des transactions psycopg enveloppant les appels réseau. Création d'un verrou applicatif distribué via les clés `automation_in_progress` et `automation_locked_at` de la base de données (sécurité de libération à 2 minutes).
  4. **Quotas & Limites** : Correction du quota d'historique (api_requests_total), appel de rafraîchissement quota réel via get_devices, et rate-limiting global par route sensible.
- Implication : Le backend est désormais complètement sécurisé, robuste face aux conflits de concurrence et protégé contre la rétention indue de connexions de base de données.


[2026-05-27 13:22:00] - Remédiation Phase 3 : Scalabilité & Expérience Native (Frontend)
- Décision : Déporter le monitoring continu de performances (FPS, JS Heap) vers un Web Worker dédié (`perf-worker.js`) et implémenter un routeur asynchrone natif (`spa-router.js`) pour éliminer les rechargements complets de pages (SPA Light).
- Motivation : Les calculs de FPS continus sur le thread principal consommaient de la CPU et risquaient de causer des micro-saccades lors du rendu des graphiques. De plus, les rechargements complets de pages lors du changement de menu nuisaient à la fluidité ressentie comme "native".
- Implémentation :
  1. **Web Worker** : Création de `static/js/perf-worker.js` gérant l'agrégation glissante des metrics et l'émission d'avertissements de performance. Remplacement des calculs lourds de `performance-optimizer.js` par un simple comptage de frames envoyé toutes les 10s au worker.
  2. **SPA Light Router** : Création de `static/js/spa-router.js` interceptant les clics de navigation, effectuant un fetch AJAX de fragment, remplaçant `#app-content` avec effet de fondu (150ms), gérant nativement `pushState`/`popstate`, mettant à jour la bottom navigation, et ré-évaluant à chaud les scripts spécifiques de la page (après leur mise en conformité `document.readyState` pour history.js, settings.js et alerts.js).
  3. **Standardisation HTML** : Enveloppement des sections centrales de tous les templates dans un conteneur `#app-content` unifié.
- Implication : L'application offre désormais un rendu asynchrone instantané et soyeux type application native (sans aucun rechargement complet), tout en soulageant totalement le thread principal des calculs de monitoring. Zéro dépendance externe lourde requise, parfaite compatibilité offline-first conservée.


[2026-07-04 15:05:00] - Durcissement de la sécurité et observabilité du Backend (Phases A, B, C)
- Décision : Appliquer les préconisations d'isolement de secrets, durcissement du démarrage Flask, sécurisation SSRF DNS pour IFTTT, bufferisation amortie en mémoire de l'historique et enrichissement de `/healthz`.
- Motivation : L'audit a révélé des failles potentielles de fuite de secrets de configuration locale, de contrefaçon de cookies de session Flask (clés par défaut), de rebonds SSRF internes, ainsi qu'un manque d'observabilité de la latence du planificateur de ticks.
- Implémentation :
  1. **Sécurité & Secrets** : Déplacement de la clé IFTTT de settings.json vers l'environnement. Durcissement de `validate_webhook_url` pour résoudre le DNS des webhooks IFTTT et rejeter les adresses privées/locales. Blocage du démarrage en production avec `FLASK_SECRET_KEY` non sécurisée.
  2. **Refactoring & Tests** : Validation systématique de la property `pool` de `PostgresStore`, fermeture sécurisée des curseurs sur échec transactionnel, et création d'une suite de tests `tests/test_backend_hardening.py` couvrant ces sécurités.
  3. **Amortissement & Observabilité** : Rétention en mémoire tampon (max 100) en cas d'erreur d'écriture d'historique PostgreSQL avec planification automatique de retries. Route `/healthz` enrichie avec la connectivité PostgreSQL réelle, la latence moyenne de tick et le dernier tick APScheduler (retourne 503 si dégradé).
- Implication : Le backend est désormais conforme aux meilleures pratiques de sécurité de production et d'isolation des secrets. Il tolère les micro-coupures de base de données PostgreSQL sans perte de données d'historique immédiates et offre aux outils de monitoring un diagnostic riche.

[Archives Q1 2026](file:///home/kidpixel/SwitchBot/memory-bank/archives/decisionLog_2026Q1.md)
