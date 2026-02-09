# Moteur d'Automatisation SwitchBot

**TL;DR**: Le moteur d'automatisation implémente une cascade à trois niveaux (IFTTT → Scènes → Commandes directes) avec idempotence des actions OFF et répétitions paramétrables pour garantir la fiabilité du contrôle climatique.

## Le Problème : Pourquoi cette Architecture ?

Vous construisez un système de contrôle climatique intelligent. Vous voulez que votre climatisation s'adapte automatiquement à la température, mais vous découvrez rapidement plusieurs problèmes :

1. **L'API SwitchBot native est instable** - Les commandes directes échouent aléatoirement
2. **Le quota API est limité** - Chaque appel consomme vos précieuses requêtes
3. **Les actions OFF répétées** - Votre système envoie des dizaines de commandes OFF identiques
4. **La gestion des fuseaux horaires** - Vos fenêtres horaires ne fonctionnent pas correctement lors des changements d'heure

Ces problèmes vous font perdre le contrôle de votre système et génèrent des factures API inattendues.

## La Solution : Architecture en Cascade avec Idempotence

### La Cascade IFTTT → Scènes → Commandes

Le système utilise une approche à trois niveaux avec fallback automatique :

```python
# switchbot_dashboard/automation.py - Lignes 600-650
def _trigger_aircon_action(self, action_key: str, state_reason: str) -> bool:
    """Déclenche une action de climatisation avec cascade à 3 niveaux."""
    
    # Niveau 1: Webhooks IFTTT (priorité)
    ifttt_webhooks = extract_ifttt_webhooks(self._settings)
    if ifttt_webhooks and action_key in ifttt_webhooks:
        webhook_url = ifttt_webhooks[action_key]
        if self._execute_ifttt_webhook(webhook_url, action_key, state_reason):
            return True
        logger.info(f"[automation] IFTTT webhook failed, falling back to scene")
    
    # Niveau 2: Scènes SwitchBot (fallback 1)
    aircon_scenes = extract_aircon_scenes(self._settings)
    if aircon_scenes and action_key in aircon_scenes:
        scene_id = aircon_scenes[action_key]
        if self._execute_aircon_scene(scene_id, action_key, state_reason):
            return True
        logger.warning(f"[automation] Scene execution failed, falling back to direct command")
    
    # Niveau 3: Commandes directes (fallback 2)
    return self._execute_aircon_direct_command(action_key, state_reason)
```

Cette approche résout plusieurs problèmes :
- **Fiabilité** : Si l'API SwitchBot échoue, les webhooks IFTTT fonctionnent toujours
- **Économie de quota** : Les webhooks IFTTT ne consomment pas votre quota SwitchBot
- **Flexibilité** : IFTTT peut déclencher des notifications, logs, et actions complexes

### Idempotence des Actions OFF

Pour éviter les déclenchements excessifs, le système combine deux gardes : état supposé et file d'attente.

```python
# switchbot_dashboard/automation.py - Lignes 825-837 (winter_off)
state = self._state_store.read()
if state.get("assumed_aircon_power") == "off":
    self._debug("Skipping winter_off: already assumed off", trigger=trigger)
    outcome = "already_off"
elif self._has_pending_off_repeat():
    self._debug("Skipping winter_off: off repeat already pending", trigger=trigger)
    outcome = "off_repeat_pending"
else:
    turned_off = self._perform_off_action(...)
    if turned_off:
        self._schedule_off_repeat_task(now, state_reason="automation_winter_off")
```

Le cycle de vie garantit qu'une seule commande OFF est envoyée par cycle :
1. **Premier OFF** → `assumed_aircon_power = "off"` + file d'attente créée
2. **Température stable** → `assumed_aircon_power == "off"` bloque les nouveaux déclenchements
3. **File active** → `_has_pending_off_repeat()` bloque les déclenchements concurrents
4. **Action ON** → `_clear_off_repeat_task()` + `assumed_aircon_power = "on"`
5. **Redémarrage** → État réinitialisé, file vide

## L'Implémentation : Configuration et Code

### Variables d'Environnement Essentielles

```bash
# .env
SCHEDULER_ENABLED=true
POLL_INTERVAL_SECONDS=60
TIMEZONE=Europe/Paris
```

### Configuration JSON Complète

```json
{
  "ifttt_webhooks": {
    "winter": "https://maker.ifttt.com/trigger/switchbot_winter/with/key/YOUR_KEY",
    "summer": "https://maker.ifttt.com/trigger/switchbot_summer/with/key/YOUR_KEY",
    "fan": "https://maker.ifttt.com/trigger/switchbot_fan/with/key/YOUR_KEY",
    "off": "https://maker.ifttt.com/trigger/switchbot_off/with/key/YOUR_KEY"
  },
  "aircon_scenes": {
    "winter": "SCENE_WINTER_UUID",
    "summer": "SCENE_SUMMER_UUID", 
    "fan": "SCENE_FAN_UUID",
    "off": "SCENE_OFF_UUID"
  },
  "aircon_device_id": "02-202008110034-13",
  "off_repeat_count": 3,
  "off_repeat_interval_seconds": 10,
  "turn_off_outside_windows": true,
  "timezone": "Europe/Paris"
}
```

### Répétitions OFF Paramétrables

Pour garantir l'arrêt effectif, le système planifie des commandes OFF répétées avec file d'attente persistante :

```python
# switchbot_dashboard/automation.py - Lignes 403-430
def _schedule_off_repeat_task(self, now: dt.datetime, *, state_reason: str) -> None:
    """Planifie des commandes OFF répétées avec intervalle configurable."""
    settings = self._settings_store.read()
    repeat_count = int(settings.get("off_repeat_count", 1) or 1)
    if repeat_count <= 1:
        self._clear_off_repeat_task()
        return

    interval_seconds = int(settings.get("off_repeat_interval_seconds", 10) or 10)
    if interval_seconds < 1:
        interval_seconds = 1

    remaining = repeat_count - 1
    next_run_at = (_ensure_utc(now) + dt.timedelta(seconds=interval_seconds)).isoformat()

    state = self._state_store.read()
    state["pending_off_repeat"] = {
        "remaining": remaining,
        "interval_seconds": interval_seconds,
        "next_run_at": next_run_at,
        "state_reason": state_reason,
    }
    self._state_store.write(state)
```

L'état de la file d'attente est persisté via `state_store` :

```json
{
  "pending_off_repeat": {
    "remaining": 2,
    "interval_seconds": 10,
    "next_run_at": "2026-01-26T14:30:10Z",
    "state_reason": "automation_winter_off"
  }
}
```

### Boucle OFF Repeat

Chaque tick d'automatisation commence par drainer la file d'attente des répétitions OFF :

```python
# switchbot_dashboard/automation.py - Lignes 432-511
def _process_off_repeat_task(self, now: dt.datetime, *, trigger: str, webhooks, scenes, aircon_device_id) -> None:
    """Exécute les répétitions OFF planifiées si l'heure est venue."""
    state = self._state_store.read()
    task = state.get("pending_off_repeat")
    if not isinstance(task, dict):
        return

    remaining = int(task.get("remaining", 0) or 0)
    if remaining <= 0:
        self._clear_off_repeat_task()
        return

    next_run_raw = task.get("next_run_at")
    try:
        next_run_at = dt.datetime.fromisoformat(next_run_raw.replace("Z", "+00:00"))
    except ValueError:
        self._clear_off_repeat_task()
        return

    now_utc = _ensure_utc(now)
    if now_utc < _ensure_utc(next_run_at):
        return  # Pas encore l'heure

    # Exécution de l'action OFF
    success = self._perform_off_action(
        trigger=trigger,
        webhooks=webhooks,
        scenes=scenes,
        aircon_device_id=aircon_device_id,
        state_reason=task.get("state_reason", "automation_off_repeat"),
        force_direct=True,
    )

    if not success:
        self._clear_off_repeat_task()
        return

    # Reschedule du prochain OFF si remaining > 0
    remaining -= 1
    if remaining <= 0:
        self._clear_off_repeat_task()
        return

    next_run_at = (now_utc + dt.timedelta(seconds=interval_seconds)).isoformat()
    # Mise à jour atomique de la file d'attente
    # ...
```

Le SchedulerService maintient un intervalle de polling serré pendant les répétitions OFF pour garantir l'exécution en temps opportun.

### Gestion Timezone-Aware des Fenêtres

Le système gère correctement les fuseaux horaires et les traversées de minuit :

```python
# switchbot_dashboard/automation.py - Lignes 26-50
def _is_now_in_windows(time_windows: list[dict[str, Any]], now: dt.datetime) -> bool:
    """Évalue les fenêtres horaires dans le fuseau configuré."""
    
    for window in time_windows:
        days = window.get("days")
        if not isinstance(days, list):
            continue
        
        start_raw = window.get("start")
        end_raw = window.get("end")
        if not isinstance(start_raw, str) or not isinstance(end_raw, str):
            continue
        
        try:
            start = _parse_hhmm(start_raw)
            end = _parse_hhmm(end_raw)
        except ValueError:
            continue
        
        now_time = now.time().replace(tzinfo=None)
        
        if start <= end:
            if now.weekday() in days and start <= now_time <= end:
                return True
        else:
            # Gestion des fenêtres qui traversent minuit
            if now.weekday() in days and now_time >= start:
                return True
    
    return False
```

### Cache Timezone pour Performance

```python
# switchbot_dashboard/automation.py - Lignes 100-120
def _get_timezone(self) -> ZoneInfo:
    """Récupère le fuseau horaire avec cache."""
    
    timezone_key = self._settings.get("timezone", "Europe/Paris")
    
    # Cache pour éviter les résolutions répétées
    if (hasattr(self, '_cached_timezone_key') and 
        hasattr(self, '_cached_timezone_value') and
        self._cached_timezone_key == timezone_key):
        return self._cached_timezone_value
    
    try:
        tz = ZoneInfo(timezone_key)
        self._cached_timezone_key = timezone_key
        self._cached_timezone_value = tz
        return tz
    except ZoneInfoNotFoundError:
        logger.warning(f"[automation] Invalid timezone {timezone_key}, falling back to UTC")
        return ZoneInfo("UTC")
```

## Les Pièges : Erreurs Communes à Éviter

### ❌ Ignorer l'Idempotence et la File d'Attente
```python
# Dangereux : déclenchements multiples sans protection
if temperature > max_temp:
    trigger_off_action()  # Peut s'exécuter toutes les 60 secondes
```

### ✅ Implémenter la Double Garde
```python
# Sécurisé : état supposé + file d'attente
if temperature > max_temp and state.get("assumed_aircon_power") != "off" and not _has_pending_off_repeat():
    trigger_off_action()
    update_assumed_state("off")
    schedule_off_repeat_task(now, reason="automation_winter_off")
```

### ❌ Configuration Hardcodée
```python
# Fragile : pas de flexibilité
webhook_url = "https://maker.ifttt.com/trigger/switchbot_winter/with/key/STATIC_KEY"
```

### ✅ Configuration Centralisée
```python
# Robuste : configuration via settings.json
webhook_url = self._settings["ifttt_webhooks"].get(action_key)
```

### ❌ Oublier le Fallback
```python
# Risqué : single point of failure
def execute_action(action):
    return send_direct_command(action)  # Échec = pas d'action
```

### ✅ Cascade Complète
```python
# Fiable : fallback automatique
def execute_action(action):
    if not try_ifttt_webhook(action):
        if not try_scene(action):
            return send_direct_command(action)
    return True
```

### ❌ Gestion Naïve du Temps
```python
# Incorrect : ignore les fuseaux horaires
if 8 <= now.hour <= 22:  # Ne fonctionne pas avec les changements d'heure
```

### ✅ Timezone-Aware
```python
# Correct : gestion des fuseaux et traversées de minuit
if _is_now_in_windows(windows, now_with_timezone):
```

## Patterns de Logging pour le Débogage

Le système utilise des logs structurés avec préfixes `[automation]` :

```bash
# Début de cycle
[automation] Automation tick started | trigger=scheduler, interval=60s

# Évaluation fenêtres
[automation] Time window evaluation | in_window=true, windows=[0,1,2] 08:00-22:00

# Décision température
[automation] Winter mode triggered | current_temp=17.5, min_temp=18.0, target=20.0

# Action avec cascade
[automation] Using IFTTT webhook | action=winter, webhook_success=true
[automation] Using SwitchBot scene | action=winter, scene_success=true
[automation] Using direct command | action=winter, command=setAll

# Protection idempotence
[automation] Skipping winter_off: already assumed off

# Répétition OFF
[automation] Scheduled repeated off action | pending_repeats=2, interval=10s
[automation] Executing scheduled off repeat | remaining=1, state_reason=automation_winter_off

# Fin de cycle
[automation] Automation tick finished | outcome=winter_on, duration=1.2s
```

## Tableau Comparatif des Stratégies OFF

| Stratégie | Fiabilité | Usage quota | Complexité | Cas d'usage idéal |
|-----------|-----------|-------------|------------|-------------------|
| **OFF unique** | Moyenne | Minimal | Faible | Testing, fallback ultime |
| **OFF repeat file** | Élevée | Modéré | Moyenne | Production, arrêt garanti |
| **Cascade IFTTT** | Très élevée | Faible | Élevée | Production, résilience maximale |

## La Règle d'Or : État Centralisé, File d'Attente Décentralisée

Le moteur d'automatisation fonctionne parce qu'il maintient un état centralisé (`assumed_aircon_power`) tout en utilisant une file d'attente décentralisée (`pending_off_repeat`) pour les actions critiques. Cette séparation garantit la fiabilité tout en offrant une flexibilité maximale.

L'état vous protège contre les actions répétées; la file d'attente garantit l'exécution complète des séquences OFF. Ensemble, ils créent un système d'automatisation résilient qui fonctionne même lorsque les composants individuels échouent.
