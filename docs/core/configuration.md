# Configuration du SwitchBot Dashboard v2

**TL;DR** : Le Dashboard utilise PostgreSQL par défaut avec fallback automatique vers JSON, implémente une cascade IFTTT→Scènes→Commandes directes pour la résilience, et suit les quotas API SwitchBot avec alertes configurables. Toute la configuration persiste dans `settings.json` sauf les secrets qui restent en `.env`.

## Le problème : Pourquoi une configuration complexe ?

Vous déployez un dashboard de climatisation qui doit tourner 24/7. Entre les redéploy Render qui réinitialisent les fichiers, les quotas SwitchBot qui limitent les appels, et les webhooks IFTTT qui parfois tombent, vous vous retrouvez avec un système qui perd son état à chaque restart.

La configuration devient un casse-tête : les IDs de devices changent, les scènes SwitchBug ne s'exécutent pas, et vous perdez le suivi du quota API au milieu de la journée. Pire encore, le scheduler continue de tourner avec des paramètres obsolètes.

## La solution : Une architecture à trois couches

Le Dashboard v2 sépare les préoccupations en trois couches indépendantes :

1. **Secrets (`.env`)** : Tokens API qui ne doivent jamais être persistés côté serveur
2. **Configuration métier (`settings.json`)** : Paramètres utilisateur qui survivent aux redeploys
3. **État opérationnel (`state.json`)** : Données volatiles pour l'UI et le diagnostic

Cette architecture permet au scheduler de continuer son travail même pendant un redeploy, et garantit que vos réglages métier (fenêtres horaires, seuils de température) ne sont jamais perdus.

## L'implémentation : Le code et la configuration

### 1. Secrets dans `.env`

Les identifiants sensibles restent dans les variables d'environnement :

```bash
SWITCHBOT_TOKEN=votre_token_ici
SWITCHBOT_SECRET=votre_secret_ici
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10
SWITCHBOT_POLL_INTERVAL_SECONDS=60
LOG_LEVEL=info
FLASK_SECRET_KEY=change_me
SCHEDULER_ENABLED=true
```

**Override du poll interval** : Quand `SWITCHBOT_POLL_INTERVAL_SECONDS` est défini, `create_app()` force immédiatement cette valeur dans `settings.json` au démarrage. Mettre à jour `.env` suffit donc pour modifier durablement l'intervalle.

### 2. Configuration métier dans `settings.json`

Ce fichier contient tous les réglages qui survivent aux redeploys :

### Tableau Comparatif des Approches de Configuration

| Approche | Persistance | Sécurité | Flexibilité | Cas d'usage idéal |
|----------|-------------|----------|-------------|-------------------|
| **Variables ENV** | Volatile | Élevée | Faible | Secrets, overrides temporaires |
| **Settings JSON** | Persistente | Moyenne | Élevée | Configuration métier durable |
| **Overlay UI** | Persistente | Moyenne | Très élevée | Modifications utilisateur |

```json
{
  "automation_enabled": true,
  "mode": "summer",
  "poll_interval_seconds": 60,
  "adaptive_polling_enabled": true,
  "idle_poll_interval_seconds": 600,
  "poll_warmup_minutes": 15,
  "command_cooldown_seconds": 60,
  "action_on_cooldown_seconds": 300,
  "action_off_cooldown_seconds": 60,
  "hysteresis_celsius": 0.5,
  "meter_device_id": "C271111EC0AB",
  "aircon_device_id": "02-202008110034-13",
  "time_windows": [
    {
      "days": [0, 1, 2, 3, 4, 5, 6],
      "start": "08:00",
      "end": "22:00"
    }
  ],
  "winter": {
    "min_temp": 18.0,
    "max_temp": 22.0,
    "target_temp": 20.0,
    "ac_mode": 5,
    "fan_speed": 3
  },
  "summer": {
    "min_temp": 22.0,
    "max_temp": 26.0,
    "target_temp": 24.0,
    "ac_mode": 2,
    "fan_speed": 2
  },
  "api_quota_warning_threshold": 250,
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
  "off_repeat_count": 2,
  "off_repeat_interval_seconds": 10,
  "timezone": "Europe/Paris",
  "turn_off_outside_windows": true
}
```

### 3. Cascade de résilience IFTTT → Scènes → Commandes

Le système implémente trois niveaux de fallback pour garantir l'exécution :

```python
# 1. Webhook IFTTT (priorité)
if webhooks.get(action):
    response = requests.post(webhook_url, timeout=10)
    
# 2. Scène SwitchBot (fallback 1)
elif scenes.get(action):
    response = switchbot_client.execute_scene(scene_id)
    
# 3. Commande directe (fallback 2)
elif action == "off":
    response = switchbot_client.turn_off(device_id)
else:
    response = switchbot_client.set_all(device_id, params)
```

**Validation des URLs IFTTT** : Les URLs doivent commencer par `https://`, validation automatique dans `ifttt.py:17-27`.

### 4. Stockage PostgreSQL avec fallback

```bash
# Production (Recommandé)
STORE_BACKEND=postgres
POSTGRES_URL=postgresql://user:password@ep-xxx.aws.neon.tech/dbname?sslmode=require

# Développement (Fallback)
STORE_BACKEND=filesystem
SWITCHBOT_SETTINGS_PATH=config/settings.json
SWITCHBOT_STATE_PATH=config/state.json
```

**Performances PostgreSQL** : Connection pooling via `psycopg_pool.ConnectionPool` (1-10 connexions), batch insert HistoryService pour -50% latence.

### 5. État opérationnel dans `state.json`

```json
{
  "last_temperature": 23.5,
  "last_humidity": 55,
  "last_action": "setAll",
  "last_action_at": "2026-01-09T17:30:00Z",
  "assumed_aircon_power": "on",
  "api_requests_total": 150,
  "api_requests_remaining": 9850,
  "api_quota_day": "2026-01-10",
  "pending_off_repeat": {
    "remaining": 1,
    "interval_seconds": 10,
    "next_run_at": "2026-01-11T21:30:10Z",
    "state_reason": "automation_winter_off"
  },
  "last_temperature_stale": false,
  "last_error": null
}
```

## Les pièges à éviter

### ❌ Ignorer le quota API

L'API SwitchBot est limitée à 10 000 requêtes/jour. Le `ApiQuotaTracker` centralise le suivi :

```python
# Chaque appel SwitchBot incrémente automatiquement
with ApiQuotaTracker() as tracker:
    response = switchbot_client.get_device_list()
    tracker.record_call()  # Met à jour api_requests_total/remaining
```

**Alerte automatique** : Quand `api_requests_remaining` ≤ `api_quota_warning_threshold`, une bannière jaune s'affiche dans l'interface.

### ❌ Sous-estimer les cooldowns adaptatifs

Le système différencie les cooldowns selon le type d'action :

```json
{
  "action_on_cooldown_seconds": 300,  // 5 min après démarrage
  "action_off_cooldown_seconds": 60,   // 1 min après arrêt
  "command_cooldown_seconds": 60       // Valeur par défaut
}
```

**Raison** : La pompe à chaleur met ~5 minutes pour diffuser la chaleur, mais l'arrêt est instantané.

### ❌ Oublier l'idempotence des actions OFF

Le système empêche les déclenchements excessifs :

```python
# Pas de nouvelle action OFF si déjà supposé OFF
if assumed_aircon_power == "off":
    logger.info("Skipping winter_off: already assumed off")
    return
```

**Logs clairs** : `Skipping winter_off: already assumed off` ou `Skipping summer_off: off repeat already pending`.

### ❌ Négliger le polling adaptatif

Le système réduit automatiquement le polling hors fenêtres horaires avec `adaptive_polling_enabled` :

```json
{
  "adaptive_polling_enabled": true,
  "idle_poll_interval_seconds": 600,  // 10 min hors fenêtre
  "poll_warmup_minutes": 15            // 15 min avant fenêtre
}
```

**Comportement** :
- **In-window** : `poll_interval_seconds` normal (ex: 15s)
- **Warmup** : Retour à l'intervalle normal pendant `poll_warmup_minutes` avant fenêtre
- **Idle** : Intervalle rallongé (`idle_poll_interval_seconds`) hors fenêtre
- **Fixed** : Désactive l'adaptation si `adaptive_polling_enabled=false`

**Auto-reschedule** : Le scheduler se reprogramme automatiquement lors des changements de mode, avec logs `[scheduler] Adaptive polling reschedule: 600 -> 15 seconds (mode=warmup)`.

**Validation UI** : Les champs sont disponibles dans `/reglages` avec validation `_as_bool/_as_int` et bornes appropriées (15-86400s pour idle, 0-1440 min pour warmup).

### ❌ Ignorer les fuseaux horaires

Les fenêtres horaires sont évaluées dans le fuseau configuré :

```json
{
  "timezone": "Europe/Paris"  // IANA identifier
}
```

**Fallback** : UTC si le fuseau est invalide, avec log explicite.

## Monitoring et dépannage

### Health check `/healthz`

```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2024-01-10T14:30:00Z",
  "last_read_at": "2024-01-10T14:29:00Z",
  "temperature_stale": false,
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2024-01-10",
  "version": "2.0.0"
}
```

### Logs Adaptive Polling

```bash
# Changements de mode avec auto-reschedule
[scheduler] Adaptive polling reschedule: 600 -> 15 seconds (mode=warmup)
[scheduler] Adaptive polling reschedule: 15 -> 600 seconds (mode=idle)
[scheduler] Adaptive polling reschedule: 600 -> 15 seconds (mode=in_window)

# Mode fixe (adaptation désactivée)
[scheduler] Using fixed interval=120 seconds (adaptive_polling_enabled=false)
```

### Logs structurés

```bash
[automation] Winter mode triggered | current_temp=17.5, min_temp=18.0, trigger=scheduler
[automation] Time window evaluation | windows=[0,1,2] 08:00-22:00, in_window=true
[automation] Cooldown active (ON action) | remaining_time='4m0s'
[automation] Executing scheduled off repeat | trigger=scheduler, remaining_before=1
[ifttt] Triggering IFTTT webhook | action=winter, url=https://maker.ifttt.com/...
[api] Quota snapshot updated | used=150, remaining=9850, limit=10000
```

### Debug endpoint

`GET /debug/state?token=<STATE_DEBUG_TOKEN>` pour diagnostic complet de l'état opérationnel.

### Commandes utiles

```bash
# Migration PostgreSQL
python scripts/migrate_to_postgres.py \
    --postgres-url "postgresql://user:password@ep-xxx.aws.neon.tech/dbname?sslmode=require" \
    --dry-run

# Test de configuration
curl -s https://votre-instance-render.com/healthz | jq '.status == "ok"'

# Logs d'automatisation
tail -f logs/app.log | grep "\[automation\]"
```

## La Règle d'Or : Configuration Persistante, Secrets Volatiles

Les réglages métier survivent aux redeploys, les secrets restent en environnement. Le scheduler continue son travail même pendant un redémarrage, et le système bascule automatiquement vers le fallback si PostgreSQL est indisponible.

---

*Voir aussi [Guide d'intégration IFTTT](../guides/ifttt.md) pour la configuration des webhooks, [Migration PostgreSQL](../ops/postgresql-migration.md) pour le guide de migration, et [Référence des standards](../../../.windsurf/rules/codingstandards.md) pour les patterns de développement.*
