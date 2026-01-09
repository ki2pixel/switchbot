[2026-01-09 15:58:00] - Initial project overview

## Vision
- Fournir un dashboard Flask local qui orchestre la lecture de capteurs SwitchBot et pilote un climatiseur IR virtuel.
- Priorité à la résilience locale : toutes les décisions d’automatisation (hysteresis, créneaux) sont calculées côté serveur.

## Composants principaux
1. **app.py** – bootstrap Flask minimal qui délègue à `switchbot_dashboard.create_app()`.
2. **switchbot_dashboard/** – logique cœur :
   - `__init__.py` assemble les services et démarre le scheduler.
   - `automation.AutomationService` gère la boucle métier (lecture Meter, décisions chauffage/clim).
   - `switchbot_api.SwitchBotClient` encapsule les appels REST (signatures HMAC, retries).
   - `config_store.JsonStore` assure l’accès atomique aux fichiers JSON (`config/settings.json`, `config/state.json`).
   - `scheduler.SchedulerService` planifie `AutomationService.run_once` via APScheduler.
   - `routes.py` expose le dashboard (formulaires de config, actions manuelles).
3. **config/** – `settings.json` (paramètres persistés) et `state.json` (télémétrie/dernière action).
4. **docs/** – documentation structurée thématique :
   - `README.md` : index des guides
   - `setup.md` : installation et lancement
   - `configuration.md` : paramètres et validation
   - `ui-guide.md` : interface et interactions
   - `theming.md` : styles et thème sombre
   - `testing.md` : tests manuels et sécurité

## Flux d’automatisation
1. Scheduler déclenche `AutomationService.run_once` à intervalle `poll_interval_seconds` (>=15 s).
2. Lecture du capteur Meter → mise à jour `state.json`.
3. Si l’automatisation est active et dans une fenêtre horaire valide, comparaison des seuils (min/max + hysteresis) contre la température courante.
4. Envoi de commandes IR (« turnOff » ou « setAll ») via `SwitchBotClient`, avec cooldown et mémorisation de l’état supposé pour éviter les doublons.

## Configuration et sécurité
- Les identifiants SwitchBot proviennent de `.env` (`SWITCHBOT_TOKEN`, `SWITCHBOT_SECRET`), jamais sérialisés en clair.
- Les réglages métiers sont modifiables via l’UI (ventilation, mode hiver/été, hysteresis, fenêtres horaires).
- Les fichiers JSON sont verrouillés et écrits de manière atomique pour prévenir la corruption en cas d’arrêt brutal.

## Observabilité & tests à privilégier
- `state.json` journalise les dernières lectures/erreurs pour inspection depuis l’UI.
- Tests recommandés (docs/README.md) : validation des paramètres, transitions des seuils, fiabilité du cooldown, gestion des erreurs API (429/5xx/190).

[2026-01-09 16:20:00] - UX mobile & formulaires guidés

- L’écran principal (`switchbot_dashboard/templates/index.html`) est orienté mobile-first : nouvelle carte Settings, gradient léger et contrôles tactiles (switchs, badges).
- Le paramétrage des fenêtres horaires se fait via cases à cocher jour par jour (`DAY_CHOICES`) et menus déroulants 24 h (`TIME_CHOICES`) fournis par `routes.py`.
- Les profils Winter/Summer reposent sur des dropdowns bornés (températures `TEMP_CHOICES`, modes `AC_MODE_CHOICES`, ventilation `FAN_SPEED_CHOICES`) garantissant la cohérence entre UI et validation persistée.
- Les constantes partagées côté backend évitent les divergences avec `config/settings.json` et facilitent l’extension future (ex. pas de 0,5 °C).
