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

