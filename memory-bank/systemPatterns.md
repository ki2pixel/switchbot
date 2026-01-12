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

