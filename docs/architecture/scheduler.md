# Scheduler Service - Architecture APScheduler

**TL;DR**: Le SchedulerService utilise APScheduler avec 1 worker Gunicorn pour exécuter les ticks d'automatisation toutes les 15 secondes en production, avec gestion adaptative de l'intervalle et protection contre les erreurs.

## Le Problème : Multi-Worker et Fiabilité

Vous déployez en production avec Gunicorn. Soudain, vous voyez des ticks d'automatisation dupliqués et des quotas API qui s'envolent. Le problème ? Chaque worker Gunicorn démarre son propre APScheduler, créant des exécutions concurrentes.

La solution classique serait un cron externe, mais ça ajoute de la latence (1 minute minimum), des dépendances externes et des logs dispersés.

## La Solution : APScheduler Intégré + 1 Worker

L'architecture actuelle combine APScheduler intégré avec une configuration Gunicorn optimisée :

```python
# gunicorn.conf.py
workers = 1           # Un seul worker pour APScheduler
threads = 2           # Concurrence via threads  
worker_class = "sync"
```

Le scheduler s'adapte dynamiquement selon les fenêtres horaires avec `adaptive_polling_enabled` :
- **In-window** : intervalle normal (`poll_interval_seconds`)
- **Warmup** : intervalle normal pendant `poll_warmup_minutes` avant fenêtre
- **Idle** : intervalle rallongé (`idle_poll_interval_seconds`) hors fenêtre
- **Pending off-repeat** : maintien intervalle normal pour exécuter les répétitions
- **Fixed** : désactive l'adaptation si `adaptive_polling_enabled=false`

## L'Implémentation : Code et Configuration

### Variables d'environnement critiques

```bash
SCHEDULER_ENABLED=true      # Active/désactive APScheduler
WEB_CONCURRENCY=1           # Force 1 worker Gunicorn
```

**Attention** : Ne jamais augmenter `WEB_CONCURRENCY` si `SCHEDULER_ENABLED=true`.

### Configuration JSON (`settings.json`)

```json
{
  "poll_interval_seconds": 15,
  "idle_poll_interval_seconds": 300,
  "poll_warmup_minutes": 10,
  "adaptive_polling_enabled": true,
  "timezone": "Europe/Paris"
}
```

### Démarrage Production

```bash
gunicorn 'switchbot_dashboard:create_app()' --config gunicorn.conf.py
```

Logs attendus :
```
[scheduler] BackgroundScheduler started successfully
[scheduler] Job scheduled with interval=15 seconds
[scheduler] Triggering immediate first tick
```

### Wrappers de résilience

```python
# SchedulerService._run_tick_safe()
try:
    automation_service.run_once(trigger='scheduler')
except Exception as e:
    logger.error(f"[scheduler] Tick failed (will retry next interval)", exc_info=True)
```

Chaque tick est protégé par un wrapper try/except. En cas d'erreur, le scheduler continue et planifie le prochain tick.

### Cache timezone

```python
# AutomationService
_cached_timezone_key = None
_cached_timezone_value = None
```

Le fuseau horaire est mis en cache pour éviter les résolutions répétées lors des ticks fréquents.

### Implémentation Adaptive Polling

```python
# switchbot_dashboard/scheduler.py - Lignes 113-172
def _get_effective_interval_seconds(self, *, now_utc: dt.datetime | None = None) -> tuple[int, str]:
    """Calcule l'intervalle effectif selon le mode adaptatif."""
    settings = self._settings_store.read()
    
    base_interval = self._as_int(settings.get("poll_interval_seconds", 120), default=120)
    adaptive_enabled = bool(settings.get("adaptive_polling_enabled", True))
    
    if not adaptive_enabled:
        return base_interval, "fixed"
    
    # Logique des modes : in_window, warmup, idle, pending_off_repeat
    # ...
```

### Auto-reschedule Intelligent

```python
# switchbot_dashboard/scheduler.py - Lignes 178-194
def _maybe_reschedule_after_tick(self) -> None:
    """Reprogramme automatiquement si l'intervalle change."""
    desired_interval, mode = self._get_effective_interval_seconds()
    if self._current_interval_seconds == desired_interval:
        return
    
    self._logger.info(
        "[scheduler] Adaptive polling reschedule: %s -> %s seconds (mode=%s)",
        previous, desired_interval, mode
    )
    self._schedule_or_reschedule_locked()
```

Le scheduler se reprogramme automatiquement lors des changements de mode (idle→warmup→in-window).

## Les Pièges : Erreurs Communes

### ❌ Multi-workers Gunicorn

**Symptôme** : Ticks dupliqués, quotas doublés

**Cause** : `WEB_CONCURRENCY > 1` avec `SCHEDULER_ENABLED=true`

**Solution** :
```bash
export WEB_CONCURRENCY=1
```

### ❌ Scheduler désactivé en production

**Symptôme** : Plus de ticks après déploiement

**Cause** : `SCHEDULER_ENABLED=false` ou détection incorrecte du mode debug

**Solution** : Vérifier les logs :
```
[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false
```

### ❌ Adaptive polling désactivé par erreur

**Symptôme** : Polling constant même hors fenêtres horaires

**Cause** : `adaptive_polling_enabled=false` dans settings

**Solution** : Activer l'adaptation :
```json
{
  "adaptive_polling_enabled": true,
  "idle_poll_interval_seconds": 600,
  "poll_warmup_minutes": 15
}
```

### ❌ Intervalles mal configurés

**Symptôme** : Trop de requêtes API ou réveil trop tard

**Cause** : `idle_poll_interval_seconds` trop bas ou `poll_warmup_minutes` trop élevé

**Solution** : Ajuster les valeurs :
```json
{
  "idle_poll_interval_seconds": 600,    // 10 min hors fenêtre
  "poll_warmup_minutes": 15             // 15 min avant fenêtre
}
```

### ❌ Timezone invalide

**Symptôme** : Fenêtres horaires non appliquées

**Cause** : Valeur `timezone` invalide dans `settings.json`

**Fallback** : Le système retombe automatiquement sur UTC

### ❌ Exception non gérée

**Symptôme** : Scheduler arrêté brutalement

**Cause** : Exception dans `automation_service.run_once()`

**Protection** : Wrapper `_run_tick_safe()` avec retry automatique

## Patterns de Logging

### Messages normaux

```
[scheduler] BackgroundScheduler started successfully
[scheduler] Job scheduled with interval=15 seconds
[automation] Automation tick started | trigger='scheduler'
```

### Messages de debug (non alarmants)

```
[DEBUG] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)
```

### Messages d'erreur

```
[ERROR] [scheduler] Tick failed (will retry next interval)
```

### Messages Adaptive Polling

```
[scheduler] Adaptive polling reschedule: 600 -> 15 seconds (mode=warmup)
[scheduler] Adaptive polling reschedule: 15 -> 600 seconds (mode=idle)
[scheduler] Adaptive polling reschedule: 600 -> 15 seconds (mode=in_window)
```

## Migration depuis Cron Externe

### ❌ Cron Externe / ✅ APScheduler Intégré

❌ **Cron externe** : Dépendance externe, latence 60s minimum, logs séparés, environnement différent. Chaque appel doit recréer le contexte Python.

✅ **APScheduler intégré** : Latence 15s configurable, logs centralisés, environnement partagé, état persistant. Un seul processus gère tout.

Si vous utilisez actuellement cron-job.org ou Render Cron :

1. **Déployer** avec `SCHEDULER_ENABLED=true`
2. **Vérifier** les logs `trigger='scheduler'`
3. **Désactiver** le cron externe après 24h de stabilité
4. **Supprimer** le cron externe

**Avantages** :
- Latence 15s vs 60s
- Logs centralisés
- Pas de dépendance externe
- Environnement partagé (variables, stores)

- ✅ Background scheduler (non bloquant)

### Tableau Comparatif des Approches Scheduler

| Approche | Latence | Maintenance | Complexité | Fiabilité |
|----------|---------|-------------|------------|------------|
| **Cron externe** | 60s+ | Élevée | Faible | Moyenne |
| **APScheduler intégré** | 15s | Faible | Moyenne | Élevée |
| **Scheduler cloud** | Variable | Moyenne | Élevée | Variable |

## Performance avec 1 Worker

Le worker unique avec threads gère :
- ✅ Dashboard web (requêtes légères)
- ✅ API SwitchBot (I/O bound) 
- ✅ Background scheduler (non bloquant)

En cas de charge élevée :
1. Monitorer CPU/mémoire
2. Augmenter `threads` avant `workers`
3. Considérer Redis pour stores partagés

## La Règle d'Or : Un Worker Unique, Une Source de Vérité

Un seul worker avec `WEB_CONCURRENCY=1` garantit l'absence de ticks dupliqués, tandis que l'APScheduler intégré assure une latence faible et des logs centralisés. Cette simplicité est la clé de la fiabilité en production.

---

**Références** :
- `.windsurf/rules/codingstandards.md` – Standards de développement
- `memory-bank/decisionLog.md` – Décisions architecturales
- `memory-bank/systemPatterns.md` – Patterns de scheduler
