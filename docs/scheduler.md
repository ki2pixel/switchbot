# Scheduler - APScheduler intégré

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Le dashboard utilise **APScheduler** (BackgroundScheduler) pour déclencher automatiquement les ticks d'automatisation toutes les 15 secondes (configurable via `poll_interval_seconds`).
- Les fenêtres horaires sont évaluées dans le fuseau horaire configuré (`timezone` dans `settings.json`, valeur par défaut `Europe/Paris`). En cas de valeur invalide, le backend retombe sur UTC pour continuer à appliquer les plages.

> 📝 **Décisions connexes** : Les patterns de scheduler sont documentés dans `memory-bank/systemPatterns.md` et `memory-bank/decisionLog.md`. Voir notamment les décisions du 2026-01-11 sur la configuration APScheduler et du 2026-01-12 sur la gestion timezone.

## Configuration Production (Gunicorn)

### Problème résolu : Multi-worker conflicts

Avec Gunicorn multi-worker, chaque worker démarrerait son propre APScheduler, causant des ticks dupliqués et des conflits de cooldown.

**Solution** : Utiliser **1 worker** avec **threads** pour gérer la concurrence.

### Configuration actuelle

`gunicorn.conf.py` :
```python
workers = 1           # Un seul worker pour APScheduler
threads = 2           # Concurrence via threads
worker_class = "sync"
```

### Variables d'environnement

- **`SCHEDULER_ENABLED`** : `true` (défaut) | `false`
  - Contrôle le démarrage d'APScheduler
  - Mettre à `false` si utilisation d'un cron externe

- **`WEB_CONCURRENCY`** : `1` (défaut)
  - Nombre de workers Gunicorn
  - **Ne pas augmenter** si APScheduler est activé

## Démarrage en production

### Render / Docker

Le scheduler démarre **automatiquement** au lancement de l'application :

```bash
gunicorn 'switchbot_dashboard:create_app()' --config gunicorn.conf.py
```

Logs attendus :
```
[scheduler] BackgroundScheduler started successfully
[scheduler] Job scheduled with interval=15 seconds
[scheduler] Triggering immediate first tick
```

### Désactiver APScheduler (cron externe)

Si utilisation d'un cron job externe :

```bash
export SCHEDULER_ENABLED=false
```

**Note** : Depuis la résolution du problème multi-worker, **l'utilisation d'un cron externe n'est plus recommandée**. APScheduler intégré est plus fiable.

## Vérification du fonctionnement

### Logs à surveiller

**Démarrage correct** :
```
[scheduler] APScheduler enabled and started
[automation] Automation tick started | trigger='scheduler'
```

**Tick régulier** (toutes les 15s) :
```
[automation] Automation tick started | trigger='scheduler'
[automation] Polling SwitchBot meter | meter_device_id='XXX'
[automation] Meter reading stored | temperature=XX.X | humidity=XX
```

### Si APScheduler ne démarre pas

1. **Vérifier les logs** :
   ```
   [scheduler] APScheduler disabled via SCHEDULER_ENABLED=false
   ```
   → Variable d'environnement mal configurée

2. **Vérifier workers Gunicorn** :
   ```bash
   ps aux | grep gunicorn
   ```
   → Doit montrer **1 worker** principal + master process

3. **Vérifier trigger source** :
   - `trigger='scheduler'` → APScheduler OK ✅
   - `trigger='http:dashboard.run_once'` → Cron externe (ancien système)

## Migration depuis cron-job.org

Si vous utilisez actuellement un cron job externe (cron-job.org, Render Cron, etc.) :

### Étapes

1. **Déployer** la nouvelle version avec APScheduler
2. **Surveiller les logs** : vérifier `trigger='scheduler'`
3. **Désactiver** le cron job externe
4. **Supprimer** le cron job externe après 24h de stabilité

### Avantages APScheduler intégré

✅ **Fiabilité** : Pas de dépendance externe  
✅ **Latence** : Ticks toutes les 15s (vs 1 min pour cron)  
✅ **Logs centralisés** : Même flux que l'application  
✅ **Gratuit** : Pas de quota externe  
✅ **Cohérence** : Même environnement (variables, stores)

## Troubleshooting

### Ticks dupliqués

**Symptôme** : Plusieurs ticks en même temps, quotas API doublés

**Cause** : Plusieurs workers Gunicorn

**Solution** :
```bash
export WEB_CONCURRENCY=1
```

### Arrêt brutal du scheduler

**Symptôme** : Plus de ticks après démarrage

**Cause** : Exception non catchée dans le tick

**Solution** : Consulter `[scheduler]` logs pour l'exception

### Comportement de logging (mis à jour)

#### Changement de niveau de log pour reschedule()

**Ancien comportement** :
```
[WARNING] Cannot schedule job: scheduler is None
```

**Nouveau comportement** (depuis Jan 2026) :
```
[DEBUG] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)
```

**Raison** : Éviter les faux positifs dans les logs quand `SCHEDULER_ENABLED=false` ou en mode debug. Le message est maintenant informatif plutôt qu'alarmant.

#### Détection améliorée du mode debug

**Ancien comportement** : Le scheduler était désactivé si `FLASK_DEBUG=1`

**Nouveau comportement** : Détection précise du mode de fonctionnement :
- **Flask dev reloader** (`flask run`) : Scheduler désactivé
- **Gunicorn avec `FLASK_DEBUG=1`** : Scheduler activé

**Logs attendus** :
```bash
# Développement local (flask run)
[scheduler] Flask development mode detected, skipping scheduler start

# Production Render (Gunicorn)
[scheduler] BackgroundScheduler started successfully
[scheduler] Job scheduled with interval=15 seconds
```

#### Messages de logs à surveiller

**Démarrage normal** :
```
[scheduler] BackgroundScheduler started successfully
[scheduler] Job scheduled with interval=15 seconds
[scheduler] Triggering immediate first tick
```

**Reschedule après changement de configuration** :
```
[scheduler] Reschedule called but scheduler not started (normal if SCHEDULER_ENABLED=false)
# ou
[scheduler] Rescheduling automation job
[scheduler] Job scheduled with interval=30 seconds
```

**Scheduler désactivé intentionnellement** :
```
[scheduler] APScheduler disabled via SCHEDULER_ENABLED=false
[scheduler] Flask development mode detected, skipping scheduler start
```

### Performance avec 1 worker

Le worker unique avec threads suffit pour :
- ✅ Dashboard web (requêtes légères)
- ✅ API SwitchBot (I/O bound)
- ✅ Background scheduler (non bloquant)

Si charge élevée :
1. Monitorer CPU/mémoire
2. Augmenter `threads` avant `workers`
3. Considérer Redis pour stores partagés

## Résilience post-audit (Janvier 2026)

### Wrapper `_run_tick_safe()`
- Chaque tick est exécuté via `SchedulerService._run_tick_safe()`, qui enveloppe l'appel automation dans un `try/except`.
- En cas d'exception :
  - Le log `[scheduler] Tick failed (will retry next interval)` est émis avec `exc_info=True`.
  - Le scheduler reste actif et planifie le tick suivant (plus de blocage permanent).
- Ce wrapper est utilisé :
  - Lors du tick immédiat déclenché au démarrage.
  - Lors de la planification périodique (intervalle configuré).

### Cache timezone AutomationService
- `AutomationService` conserve en mémoire le fuseau résolu (`_cached_timezone_key/_cached_timezone_value`).
- Lorsqu'un POST `/reglages` modifie `timezone`, le cache est invalidé (nouvelle résolution `ZoneInfo` au tick suivant).
- Avantages :
  - Moins d'allocations lors des ticks fréquents (>=15 s).
  - Logs plus lisibles (la résolution du fuseau n'apparaît qu'en cas de changement réel).

### Conséquences opérationnelles
- Un bug ponctuel dans `run_once()` n'arrête plus l'automatisation (protection automatique).
- Les logs `[scheduler]` fournissent diagnostics explicites sans polluer (`DEBUG` au lieu de `WARNING` pour les cas attendus).
- Aucun paramètre supplémentaire n'est requis : ces protections sont activées tant que `SCHEDULER_ENABLED=true`.

---

## Références croisées

### Documentation technique
- [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) – Standards de développement obligatoires
- [DOCUMENTATION.md](DOCUMENTATION.md) – Architecture et métriques
- [setup.md](setup.md) – Installation et configuration initiale

### Guides spécialisés
- [Configuration](configuration.md) – Variables d'environnement et paramètres
- [Deployment](deployment.md) – Configuration Gunicorn et production
- [Testing](testing.md) – Tests et validation du scheduler

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions de configuration APScheduler (workers, timezone)
- `memory-bank/systemPatterns.md` – Patterns de scheduler et logging
- `memory-bank/progress.md` – Historique des améliorations scheduler

---

**Dernière mise à jour** : 25 janvier 2026
