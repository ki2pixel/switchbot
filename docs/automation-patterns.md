# Patterns d'Automatisation SwitchBot

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Ce document décrit les patterns architecturaux implémentés dans le système d'automatisation du SwitchBot Dashboard, notamment la cascade IFTTT, l'idempotence des actions, et la gestion des répétitions OFF.

> 📝 **Décisions connexes** : Les patterns d'automatisation sont documentés dans `memory-bank/systemPatterns.md`. Voir notamment les décisions du 2026-01-11 sur les webhooks IFTTT et du 2026-01-12 sur l'idempotence.

## Cascade IFTTT → Scènes → Commandes

### Architecture

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

### Avantages de la Cascade

1. **Fiabilité accrue** : Contourne les bugs de l'API SwitchBot native
2. **Flexibilité** : Applets IFTTT complexes (notifications, logs)
3. **Pas de quota** : Les webhooks IFTTT ne consomment pas le quota SwitchBot
4. **Fallback automatique** : Bascule transparente entre niveaux

### Configuration

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
  "aircon_device_id": "02-202008110034-13"
}
```

## Idempotence des Actions OFF

### Principe

Pour éviter les déclenchements excessifs, le système implémente une protection basée sur l'état supposé du climatiseur :

```python
# switchbot_dashboard/automation.py - Lignes 320-340
def _should_trigger_off_action(self, action_key: str) -> bool:
    """Vérifie si une action OFF doit être déclenchée (idempotence)."""
    
    # Protection contre les déclenchements multiples
    if self._state.get("assumed_aircon_power") == "off":
        logger.info(f"[automation] Skipping {action_key}: already assumed off")
        return False
    
    return True
```

### Cycle de Vie

1. **Premier déclenchement OFF** → `assumed_aircon_power = "off"`
2. **Température reste dans zone** → **Aucun nouveau déclenchement**
3. **Action ON** → `assumed_aircon_power = "on"`
4. **Redémarrage application** → `assumed_aircon_power = "unknown"`

### Logs Caractéristiques

```bash
# Protection activée
[automation] Skipping winter_off: already assumed off

# Action ON réinitialise
[automation] Winter mode triggered | current_temp=17.5, assumed_power=on
```

## Répétition OFF Paramétrable

### File d'Attente

```python
# switchbot_dashboard/automation.py - Lignes 430-450
def _schedule_off_repeat_task(self, state_reason: str) -> None:
    """Planifie des commandes OFF répétées avec intervalle configurable."""
    
    off_repeat_count = self._settings.get("off_repeat_count", 1)
    off_repeat_interval = self._settings.get("off_repeat_interval_seconds", 10)
    
    if off_repeat_count <= 1:
        return
    
    # Création de la file d'attente
    self._state["pending_off_repeat"] = {
        "remaining": off_repeat_count - 1,
        "interval_seconds": off_repeat_interval,
        "next_run_at": _utc_now_iso(seconds=off_repeat_interval),
        "state_reason": state_reason
    }
```

### Structure d'État

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

### Exécution

```python
# switchbot_dashboard/automation.py - Lignes 460-480
def _process_off_repeat_task(self) -> bool:
    """Exécute la prochaine commande OFF de la file."""
    
    pending = self._state.get("pending_off_repeat")
    if not pending:
        return False
    
    # Vérification du timing
    next_run = datetime.fromisoformat(pending["next_run_at"])
    if datetime.utcnow() < next_run:
        return False
    
    # Exécution de l'action OFF
    success = self._trigger_aircon_action("off", pending["state_reason"])
    
    if success and pending["remaining"] > 1:
        # Planification de la prochaine répétition
        pending["remaining"] -= 1
        pending["next_run_at"] = _utc_now(seconds=pending["interval_seconds"])
    else:
        # Fin de la file d'attente
        self._clear_off_repeat_task()
    
    return success
```

## Gestion des Fenêtres Horaires

### Évaluation Timezone-Aware

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

### Cache Timezone

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

## Arrêt Hors Fenêtres

### Logique

```python
# switchbot_dashboard/automation.py - Lignes 200-220
def _handle_outside_window_behavior(self) -> Optional[str]:
    """Gère l'arrêt automatique en dehors des fenêtres horaires."""
    
    if not self._settings.get("turn_off_outside_windows", False):
        return None
    
    # Vérification de l'état actuel
    if self._state.get("assumed_aircon_power") == "off":
        logger.info("[automation] Already off outside window")
        return None
    
    # Action OFF avec raison spécifique
    if self._trigger_aircon_action("off", "automation_off_outside_window"):
        self._schedule_off_repeat_task("automation_off_outside_window")
        return "turned_off_outside_window"
    
    return "outside_window_no_action"
```

## Patterns de Logging

### Logs Structurés

```python
# switchbot_dashboard/automation.py - Lignes 650-700
def _log_automation_outcome(self, outcome: str, context: dict) -> None:
    """Journalise le résultat d'un cycle d'automatisation."""
    
    logger.info(f"[automation] Automation tick finished | outcome={outcome}", **context)
```

### Messages Types

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

# Répétition OFF
[automation] Scheduled repeated off action | pending_repeats=2, interval=10s
[automation] Executing scheduled off repeat | remaining=1, state_reason=automation_winter_off

# Fin de cycle
[automation] Automation tick finished | outcome=winter_on, duration=1.2s
```

## Bonnes Pratiques

### Développement

1. **Tests unitaires** : Couvrir tous les niveaux de la cascade
2. **Mocks IFTTT** : Simuler les timeouts et erreurs HTTP
3. **Validation état** : Vérifier `assumed_aircon_power` après chaque action
4. **Logs structurés** : Utiliser les préfixes `[automation]` systématiquement

### Exploitation

1. **Monitoring** : Surveiller les logs `[automation]` pour les fallbacks
2. **Performance** : Optimiser `poll_interval_seconds` selon usage
3. **Quota** : Privilégier les webhooks IFTTT pour économiser le quota
4. **Dépannage** : Utiliser `Run once` pour tester les configurations

---

*Pour la configuration détaillée des scènes et webhooks, consultez [Intégration IFTTT](ifttt-integration.md) et [Référence Configuration](configuration.md).*
