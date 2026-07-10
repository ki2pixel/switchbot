# Moteur d'Automatisation SwitchBot

**TL;DR**: Le moteur d'automatisation implémente une cascade à deux niveaux (Scènes favorites → Commandes Directes API) avec idempotence des actions OFF et répétitions paramétrables pour garantir la fiabilité du contrôle climatique.

## Le Problème : Pourquoi cette Architecture ?

Vous construisez un système de contrôle climatique intelligent. Vous voulez que votre climatisation s'adapte automatiquement à la température, mais vous découvrez rapidement plusieurs problèmes :

1. **L'API SwitchBot native est instable** - Les commandes directes échouent aléatoirement
2. **Le quota API est limité** - Chaque appel consomme vos précieuses requêtes
3. **Les actions OFF répétées** - Votre système envoie des dizaines de commandes OFF identiques
4. **La gestion des fuseaux horaires** - Vos fenêtres horaires ne fonctionnent pas correctement lors des changements d'heure

Ces problèmes vous font perdre le contrôle de votre système et génèrent des requêtes API inutiles.

## La Solution : Architecture en Cascade avec Idempotence

### La Cascade Scènes → Commandes Directes

Le système utilise une approche à deux niveaux avec fallback automatique :

```python
# switchbot_dashboard/automation.py
def _trigger_aircon_action(self, action_key: str, state_reason: str) -> bool:
    """Déclenche une action de climatisation avec cascade à 2 niveaux."""
    
    # Niveau 1: Scènes SwitchBot (priorité)
    aircon_scenes = extract_aircon_scenes(self._settings)
    if aircon_scenes and action_key in aircon_scenes:
        scene_id = aircon_scenes[action_key]
        if self._trigger_scene(scene_id, action_key, state_reason):
            return True
        logger.warning(f"[automation] Scene execution failed, falling back to direct command")
    
    # Niveau 2: Commandes directes (fallback)
    return self._send_aircon_direct_command(action_key, state_reason)
```

Cette approche résout plusieurs problèmes :
- **Fiabilité** : Si la commande directe échoue, la scène favorite (exécutée côté cloud SwitchBot) peut être tentée d'abord, ou inversement.
- **Économie de quota** : Le déclenchement de scènes reste optimisé et les gardes d'idempotence évitent les appels superflus.

### Idempotence des Actions OFF

Pour éviter les déclenchements excessifs, le système combine deux gardes : état supposé et file d'attente.

```python
# switchbot_dashboard/automation.py
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
POLL_INTERVAL_SECONDS=120
TIMEZONE=Europe/Paris
```

### Configuration JSON Complète

```json
{
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
# switchbot_dashboard/automation.py
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
# switchbot_dashboard/automation.py
def _process_off_repeat_task(self, now: dt.datetime, *, trigger: str, scenes, aircon_device_id) -> None:
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
    # Mise à jour de la file...
```

### Gestion Timezone-Aware des Fenêtres

Le système gère correctement les fuseaux horaires et les traversées de minuit :

```python
# switchbot_dashboard/automation.py
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

### ❌ Cascade Sans Protection
```python
# Risqué : single point of failure
def execute_action(action):
    return send_direct_command(action)  # Échec = pas d'action
```

### ✅ Cascade avec Fallback
```python
# Fiable : fallback automatique vers commande directe
def execute_action(action):
    if not try_scene(action):
        return send_direct_command(action)
    return True
```

## Patterns de Logging pour le Débogage

Le système utilise des logs structurés avec préfixes `[automation]` :

```bash
# Début de cycle
[automation] Automation tick started | trigger=scheduler, poll_interval_seconds=120

# Évaluation fenêtres
[automation] Time window evaluation | in_window=true, time_windows=[0,1,2,3,4,5,6] 00:00-23:59

# Décision température
[automation] Temperature evaluation | current_temp=17.5, min_temp=18.0, target=21.0

# Action avec cascade
[automation] Using SwitchBot scene | action=winter, scene_id=SCENE_WINTER_UUID
[automation] Using direct command | action=winter, command=setAll

# Protection idempotence
[automation] Skipping winter_off: already assumed off

# Répétition OFF
[automation] Scheduled repeated off action | pending_repeats=2, interval=10s
[automation] Executing scheduled off repeat | remaining=1, state_reason=automation_winter_off

# Fin de cycle
[automation] Automation tick finished | outcome=winter_on
```

## Tableau Comparatif des Stratégies OFF

| Stratégie | Fiabilité | Usage quota | Complexité | Cas d'usage idéal |
|-----------|-----------|-------------|------------|-------------------|
| **OFF unique** | Moyenne | Minimal | Faible | Testing, fallback ultime |
| **OFF repeat file** | Élevée | Modéré | Moyenne | Production, arrêt garanti |
| **Cascade Scènes** | Très élevée | Faible | Moyenne | Production, résilience maximale |

## La Règle d'Or : État Centralisé, File d'Attente Décentralisée

## The Golden Rule: Metadata Static, Execution Dynamic

Le moteur d'automatisation fonctionne parce qu'il maintient un état centralisé (`assumed_aircon_power`) tout en utilisant une file d'attente décentralisée (`pending_off_repeat`) pour les actions critiques. Cette séparation garantit la fiabilité tout en offrant une flexibilité maximale.

L'état vous protège contre les actions répétées; la file d'attente garantit l'exécution complète des séquences OFF. Ensemble, ils créent un système d'automatisation résilient qui fonctionne même lorsque les composants individuels échouent.
