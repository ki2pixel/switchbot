[2026-01-09 15:59:00] - Initial architectural patterns

## Services & injections
- `create_app()` assemble et enregistre **JsonStore**, **SwitchBotClient**, **AutomationService**, **SchedulerService** dans `app.extensions`.  
- Règle : aucun accès direct aux fichiers ou au client HTTP depuis les vues; elles récupèrent un service déjà configuré via `current_app.extensions`.

## Stockage JSON atomique
- `JsonStore` sérialise tous les accès à `config/settings.json` et `config/state.json` avec un verrou `threading.Lock` et écriture via fichier temporaire `.tmp`.  
- TODO : imposer cette classe pour tout fichier persistant afin de prévenir les corruptions.

## Boucle d’automatisation
1. APScheduler (`BackgroundScheduler`) déclenche `AutomationService.run_once`.
2. Chaque tick lit les réglages, valide les identifiants, applique les fenêtres horaires et la logique d’hysteresis.
3. Les commandes SwitchBot sont envoyées uniquement après vérification du cooldown et de l’état supposé (pour éviter les doublons).
4. L’état opérationnel (température, dernière action, erreurs) est sauvegardé dans `state.json`.

## Gestion des erreurs & retries
- `SwitchBotClient` encapsule la signature HMAC, gère les retries sur HTTP 429/5xx et `statusCode` 190 avec `time.sleep`.
- Toute exception API devient `SwitchBotApiError` et est propagée jusqu’aux services qui la loguent via `state.json` ou `flash`.

## Validation et formulaires
- Les vues n’utilisent jamais directement `request.form`; elles passent par les helpers `_as_bool/_as_int/_as_float` pour normaliser et borner les valeurs.
- Les options exposées à l’UI (jours, horaires, températures, modes, vitesses) sont dérivées de constantes partagées dans `routes.py` (`DAY_CHOICES`, `TIME_CHOICES`, `TEMP_CHOICES`, etc.) pour garantir la parité entre validation et rendu.

## Sécurité & secrets
- Les tokens sont fournis exclusivement par `.env`. Aucun secret n’est stocké dans `settings.json` ou `state.json`.

## Documentation structurée
- La documentation suit une arborescence thématique (setup, configuration, UI, theming, tests) pour faciliter la maintenance.
- Chaque guide référence les autres et la Memory Bank pour tracer les décisions architecturales.
- Mise à jour automatique via `/enhance` et `/end` workflows pour synchronisation.

[2026-01-10 20:20:00] - Patterns alignés sur scènes SwitchBot, backend Redis et quotas locaux

## Services & injections
- `create_app()` assemble et enregistre **BaseStore** (filesystem `JsonStore` ou `RedisJsonStore`), **SwitchBotClient**, **AutomationService**, **SchedulerService** et **ApiQuotaTracker** dans `app.extensions`.  
- Les vues accèdent uniquement à ces services via `current_app.extensions` (jamais directement aux fichiers, au client HTTP ou au scheduler) et laissent `create_app()` gérer les bascules en cas de `StoreError`.

## Stockage multi-backend
- `BaseStore` expose une API homogène `read()/write()` pour `settings` et `state`.  
- `JsonStore` reste la référence locale : verrou `threading.Lock`, écriture via fichier temporaire `.tmp`, UTF-8.  
- `RedisJsonStore` assure la persistance sur Render/Upstash (TTL optionnel) et remonte les erreurs afin que l’app retombe automatiquement sur le filesystem.

## Boucle d’automatisation
- APScheduler (`BackgroundScheduler`) déclenche `AutomationService.run_once` (intervalle ≥15 s, `max_instances=1`, reschedule automatique sur changement de `poll_interval_seconds`).  
- Chaque tick met à jour `last_tick`, lit les réglages, valide scènes/IDs, applique fenêtres horaires + hysteresis puis poll Meter.  
- La commande privilégie les **scènes SwitchBot** (`aircon_scenes`, helper `aircon.py`) avec fallback `setAll`/`turnOff` si l’ID de scène manque.  
- Cooldown et état supposé (`assumed_aircon_*`) évitent les doublons; toutes les erreurs sont reflétées dans `state`.
- Flag de fraîcheur : `last_temperature_stale` / `last_temperature_stale_reason` signalent une température potentiellement obsolète (redeploys, erreurs API). `create_app()` marque à `true` au démarrage, puis `poll_meter()` le remet à `false` après lecture fraîche.
- **Scheduler robuste** : Démarrage conditionnel uniquement si `SCHEDULER_ENABLED=true` et pas en mode Flask dev reloader. Détection précise via `SERVER_SOFTWARE` pour distinguer Gunicorn de `flask run`. `reschedule()` gère gracieusement les appels sur scheduler non démarré.

## Gestion des erreurs & retries
- `SwitchBotClient` encapsule la signature HMAC, gère les retries sur HTTP 429/5xx et sur `statusCode` 190.  
- Les exceptions remontent en `SwitchBotApiError` pour être loguées proprement, et les métriques de quota sont mises à jour même en fallback.

## Gestion des erreurs & retries
- `SwitchBotClient` encapsule la signature HMAC, gère les retries sur HTTP 429/5xx et sur `statusCode` 190.  
- Les exceptions remontent en `SwitchBotApiError` pour être loguées proprement, et les métriques de quota sont mises à jour même en fallback.

## Validation et formulaires
- Les vues passent par `_as_bool/_as_int/_as_float` pour normaliser les entrées, interdisant l’accès brut à `request.form`.  
- Les choix (jours, horaires, températures, modes, vitesses, scènes) proviennent des constantes partagées dans `routes.py` pour garantir la parité validation/UI.

## Quotas & observabilité
- `ApiQuotaTracker` (basé sur `state_store`) enregistre le quota quotidien : fallback local (`record_call`) ou snapshot depuis les headers `X-RateLimit-*`. Les champs (`api_requests_*`, `api_quota_day`, `api_quota_reset_at`) alimentent le bandeau d’alerte configurable (`api_quota_warning_threshold`).  
- `SwitchBotClient` loggue et transmet systématiquement les métadonnées de quota pour faciliter les diagnostics.  
- `/healthz` expose l’état du scheduler (`is_running()`), du dernier tick et du store sans lire directement les fichiers, afin de fournir un monitoring léger.

## Sécurité & secrets
- Les tokens et identifiants sensibles restent dans `.env`; aucun secret n’est persisté dans `settings` ou `state`.  
- Principe du moindre privilège : seules les clés utiles sont exposées dans les vues/JSON renvoyés.

## Documentation structurée
- Les guides thématiques (`docs/setup.md`, `configuration.md`, `ui-guide.md`, `theming.md`, `testing.md`, `deployment.md`) décrivent ces patterns.  
- Toute évolution majeure (scènes, quotas, backend Redis, health check) doit être tracée dans la Memory Bank et reliée aux guides.

## Gestion timezone-aware des fenêtres horaires
- AutomationService utilise `zoneinfo` pour interpréter les fenêtres horaires dans le fuseau configuré (défaut Europe/Paris), indépendamment du serveur UTC.
- _get_timezone() valide l'identifiant IANA et retombe sur UTC si invalide, avec logs d'avertissement.
- run_once() calcule now en astimezone pour _is_now_in_windows, assurant la cohérence avec l'heure locale.

[2026-01-14 12:45:00] - Patterns PostgreSQL Neon et simplification architecture

## Services & injections
- `create_app()` assemble et enregistre **BaseStore** (PostgreSQL `PostgresStore` recommandé, filesystem `JsonStore` fallback, `RedisJsonStore` déprécié), **SwitchBotClient**, **AutomationService**, **SchedulerService** et **ApiQuotaTracker** dans `app.extensions`.  
- Les vues accèdent uniquement à ces services via `current_app.extensions` (jamais directement aux fichiers, au client HTTP ou au scheduler) et laissent `create_app()` gérer les bascules en cas de `PostgresStoreError` ou `StoreError`.

## Stockage PostgreSQL primaire avec fallback
- `BaseStore` expose une API homogène `read()/write()` pour `settings` et `state`.  
- `PostgresStore` est le backend principal : connection pooling `psycopg_pool.ConnectionPool`, schéma JSONB, table `json_store` avec indexation, SSL/TLS obligatoire pour Neon.  
- `JsonStore` reste le fallback local : verrou `threading.Lock`, écriture via fichier temporaire `.tmp`, UTF-8.  
- `RedisJsonStore` est déprécié mais fonctionnel avec warning dans les logs.  

## Stockage avec bascule automatique (FailoverStore) - Déprécié
- `FailoverStore` implémentait une bascule transparente entre deux backends Redis (primaire/secondaire) avec cooldown de 60 secondes.
- Remplacé par PostgreSQL unique plus fiable et plus simple.

## Cascade de déclenchement IFTTT → Scènes → Commandes
- `AutomationService._trigger_aircon_action()` implémente une cascade à trois niveaux pour les actions de climatisation.
- **Niveau 1** : Webhooks IFTTT (priorité, pas de quota SwitchBot, validation HTTPS obligatoire).
- **Niveau 2** : Scènes SwitchBot (fallback si webhook échoue ou absent).
- **Niveau 3** : Commandes directes `setAll`/`turnOff` (dernier recours, nécessite `aircon_device_id`).
- Logs détaillés pour tracer le chemin d'exécution choisi et les raisons des fallbacks.

## Répétition OFF avec file d'attente
- `AutomationService` planifie des commandes OFF répétées via `_schedule_off_repeat_task()` avec état `pending_off_repeat`.
- Structure d'état dans `state.json` : `{remaining, interval_seconds, next_run_at, state_reason}`.
- Protection idempotence : aucune nouvelle action OFF si `assumed_aircon_power == "off"`.
- Les actions ON annulent automatiquement les files d'attente OFF via `_clear_off_repeat_task()`.

## Validation et normalisation des webhooks IFTTT
- `extract_ifttt_webhooks()` normalise les URLs et garantit la structure des 4 clés (winter, summer, fan, off).
- `validate_webhook_url()` impose HTTPS uniquement et vérifie la validité de l'URL.
- `IFTTTWebhookClient` gère les timeouts (10s par défaut) et les erreurs réseau avec logs structurés.

[2026-01-15 11:47:00] - Patterns de correction du dashboard d'historique

## Correction des bugs d'affichage du dashboard
- **Chargement environnement** : Ajout de `load_dotenv()` au début de `create_app()` pour garantir la disponibilité des variables PostgreSQL.
- **Simplification SQL** : Remplacement des requêtes `GROUP BY` complexes par des requêtes simples évitant les erreurs PostgreSQL.
- **Conversion types** : Pattern pour convertir les chaînes PostgreSQL en nombres JavaScript (`parseFloat()` avant `.toFixed()`).
- **Parsing paramètres** : Gestion des paramètres métriques comme chaînes séparées par virgules dans les routes API.
- **Interface épurée** : Pattern de suppression des éléments superflus pour maintenir une expérience utilisateur cohérente.

## Frontend monitoring simplifié
- **Graphiques conservés** : Température & Humidité (pleine largeur) + État Climatisation (pleine largeur, hauteur limitée).
- **Cartes de statut** : Température et humidité moyennes avec conversion et affichage correct des valeurs.
- **Tableau optimisé** : 5 colonnes (suppression colonne erreurs), format responsive.
- **Filtres simplifiés** : 3 checkboxes (température, humidité, climatisation) sans métriques superflues.

## Service d'historique monitoring
- `HistoryService` utilise le connection pool PostgreSQL existant pour stocker/récupérer les données historiques dans la table `state_history`.  
- Initialisation conditionnelle dans `create_app()` : service créé uniquement si `PostgresStore` disponible, avec fallback gracieux vers données mockées.  
- Intégration transparente dans `AutomationService.run_once()` : enregistrement automatique de l'état après chaque tick d'automatisation.  
- API REST robuste : 3 endpoints `/history/api/*` avec gestion d'erreurs complète, retour de données vides valides quand aucune donnée disponible.  
- Frontend responsive : Chart.js avec filtres interactifs, graphiques animés, mise à jour temps réel, thème sombre cohérent.

## Table d'historique PostgreSQL optimisée
- Table `state_history` avec indexes temporels optimisés pour les requêtes de monitoring.  
- Schéma complet : timestamp, temperature, humidity, assumed_aircon_power, last_action, api_requests_today, error_count, last_temperature_stale, timezone, metadata JSONB.  
- Rétention 6 heures alignée sur PITR Neon avec cleanup automatique via `HistoryService`.  
- Utilisation du connection pool existant pour éviter les connexions multiples.

## Frontend monitoring avec Chart.js
- Dashboard responsive avec thème sombre cohérent et accessibilité WCAG.  
- Graphiques animés : température/humidité combinés, état climatisation, usage API, distribution erreurs.  
- Filtres interactifs : plages horaires personnalisées, granularité (minute/5min/15min/heure), sélection de métriques.  
- Mise à jour temps réel avec polling automatique et gestion d'état de chargement.  
- Gestion d'erreurs robuste : affichage de données vides valides quand aucune donnée disponible, messages informatifs.


## Patterns de performance et résilience (post-audit backend)

### Batch insert HistoryService
- `HistoryService` utilise un buffer thread-safe (`_pending_records`) avec verrou `_pending_lock` pour accumuler les enregistrements.
- Flush automatique sur `batch_size` atteint ou via timer (`flush_interval_seconds`).
- Remplacement de `psycopg.extras.execute_values` par SQL manuel pour éviter les dépendances dépréciées.
- Méthodes `_flush_pending_records_locked()` et `_build_record_tuple()` pour la construction optimisée des tuples.

### Wrapper try/catch global SchedulerService
- `SchedulerService._run_tick_safe()` enveloppe `_tick_callable` dans un try/catch global.
- Toutes les exceptions sont loguées avec `exc_info=True` sans crasher le scheduler.
- Utilisé dans `start()` (tick immédiat) et `_schedule_or_reschedule_locked()` (ticks périodiques).

### Cache timezone AutomationService
- `AutomationService` maintient un cache simple : `_cached_timezone_key` et `_cached_timezone_value`.
- `_get_timezone()` vérifie le cache avant résolution `ZoneInfo`, stocke le résultat.
- Invalidation automatique lors du changement des settings (nouvelle clé de cache).

### Tests robustes avec mocks centralisés
- `tests/conftest.py` fournit une fixture autouse pour patcher `ConnectionPool` et `_ensure_table_exists`.
- `PostgresStore` tests utilisent des mocks dédiés avec reset entre chaque test.
- `FakePostgresStore` dans les tests d'intégration pour éviter les connexions réelles.
- `BaseStore` marqué `@runtime_checkable` pour les assertions isinstance dans les tests.

