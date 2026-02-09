# Guide de Dépannage SwitchBot Dashboard v2

**TL;DR** : Le Dashboard utilise une architecture à 3 niveaux de fallback (IFTTT → scène → commande directe) avec retry automatique, monitoring structuré et bascule PostgreSQL → fichier pour garantir la résilience en production.

## Le Problème : Pourquoi la Gestion d'Erreurs est Critique

Vous déployez un dashboard de domotique qui contrôle votre climatisation. Soudain, l'API SwitchBot rate limite à 429, votre webhook IFTTT timeout, et PostgreSQL refuse la connexion. Votre climatisation reste en mode "on" alors qu'il fait 35°C. C'est exactement le scénario que la gestion d'erreurs multicouche du Dashboard v2 empêche.

## La Solution : Architecture de Résilience

### Cascade de Fallback à 3 Niveaux

Le Dashboard n'a jamais un seul point de défaillance. Chaque action climatisation suit une cascade déterministe :

1. **IFTTT Webhook** (priorité) → déclenche applet IFTTT personnalisée
2. **Scène SwitchBot** (fallback 1) → appelle API SwitchBot avec scène prédéfinie  
3. **Commande directe** (fallback 2) → `setAll`/`turnOff` sur l'appareil

```python
# switchbot_dashboard/automation.py
def _trigger_aircon_action(self, action_key: str, state_reason: str) -> bool:
    """Déclenche une action avec cascade à 3 niveaux."""
    
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

### Fallback Store Automatique

La persistance suit le même principe de résilience :

```python
# switchbot_dashboard/__init__.py
def create_app() -> Flask:
    """Crée l'application avec gestion des bascules de store."""
    
    # Tentative PostgreSQL (recommandé)
    if STORE_BACKEND == "postgres":
        try:
            postgres_store = PostgresStore(postgres_url, ssl_mode)
            app.extensions["settings_store"] = postgres_store
            app.extensions["state_store"] = postgres_store
            _logger.info("[store] PostgreSQL backend initialized")
            return app
        except PostgresStoreError as e:
            _logger.error(f"[store] PostgreSQL failed, falling back to filesystem: {e}")
    
    # Fallback JsonStore (toujours disponible)
    json_store = JsonStore()
    app.extensions["settings_store"] = json_store
    app.extensions["state_store"] = json_store
    _logger.warning("[store] Fallback to filesystem backend")
    return app
```

## L'Implémentation : Patterns Techniques

### 1. Retry avec Backoff Exponentiel

Les requêtes API survivent aux rate limits et timeouts réseau :

```python
# switchbot_dashboard/switchbot_api.py
def _request(self, method: str, endpoint: str, **kwargs) -> dict:
    """Requête HTTP avec retry automatique et backoff exponentiel."""
    max_attempts = int(os.getenv("SWITCHBOT_RETRY_ATTEMPTS", "2"))
    base_delay = int(os.getenv("SWITCHBOT_RETRY_DELAY_SECONDS", "10"))
    
    for attempt in range(max_attempts + 1):
        try:
            response = requests.request(method, self._base_url + endpoint, **kwargs)
            response.raise_for_status()
            
            # Capture des métadonnées de quota
            self._capture_quota_metadata(response)
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Rate limit
                if attempt < max_attempts:
                    delay = base_delay * (2 ** attempt)  # Backoff exponentiel
                    self._logger.warning(f"Rate limit reached, retrying in {delay}s")
                    time.sleep(delay)
                    continue
            raise SwitchBotApiError(f"HTTP {response.status_code}: {e}", 
                                  status_code=response.status_code)
                                  
        except requests.exceptions.RequestException as e:
            if attempt < max_attempts:
                delay = base_delay * (2 ** attempt)
                self._logger.warning(f"Network error, retrying in {delay}s: {e}")
                time.sleep(delay)
                continue
            raise SwitchBotApiError(f"Network error: {e}")
```

### 2. Wrapper Global SchedulerService

Le scheduler ne crash jamais, même en cas d'exception critique :

```python
# switchbot_dashboard/scheduler.py
def _run_tick_safe(self) -> None:
    """Wrapper global pour catcher toutes les exceptions du scheduler."""
    try:
        self._tick_callable()
    except Exception as exc:  # pragma: no cover - exercised via tests
        self._logger.error(
            "[scheduler] Automation tick raised exception: %s",
            exc,
            exc_info=True,  # Stack trace complet
        )
        # Ne pas crasher le scheduler, continuer les ticks suivants
```

### 3. Variables d'Environnement Critiques

```bash
# .env - Configuration de résilience
LOG_LEVEL=INFO                    # DEBUG, INFO, WARNING, ERROR, CRITICAL
SWITCHBOT_RETRY_ATTEMPTS=2         # Nombre de tentatives API
SWITCHBOT_RETRY_DELAY_SECONDS=10  # Délai base pour backoff exponentiel
STORE_BACKEND=postgres             # postgres ou json
POSTGRES_URL=postgresql://...      # Connection string PostgreSQL
POSTGRES_SSL_MODE=require          # SSL PostgreSQL (disable/require/verify-ca)
SCHEDULER_ENABLED=true             # Active/désactive le scheduler
```

### 4. Configuration JSON

```json
// config/settings.json - Configuration des fallbacks
{
  "ifttt_webhooks": {
    "aircon_cool": "https://maker.ifttt.com/trigger/aircon_cool/with/key/...",
    "aircon_heat": "https://maker.ifttt.com/trigger/aircon_heat/with/key/..."
  },
  "aircon_scenes": {
    "aircon_cool": "scene_id_cool_mode",
    "aircon_heat": "scene_id_heat_mode"
  },
  "aircon_device_id": "device_id_here",
  "automation_enabled": true
}
```

## Monitoring et Observabilité

### Logging Structuré par Composant

```python
# Préfixes standards pour faciliter le filtering
[api]       # Appels API SwitchBot, quotas, retries
[automation] # Logique métier, décisions, actions
[scheduler] # Ticks, erreurs globales, health
[store]     # Opérations stockage, bascules, erreurs
[history]   # Service d'historique, batch insert
[ifttt]     # Webhooks IFTTT, timeouts, fallbacks
```

### Health Check `/healthz`

```python
# switchbot_dashboard/routes.py
@dashboard_bp.get("/healthz")
def health_check() -> Response:
    """Endpoint de monitoring pour les systèmes externes."""
    try:
        scheduler_service = current_app.extensions["scheduler_service"]
        quota_tracker = current_app.extensions["quota_tracker"]
        state_store = current_app.extensions["state_store"]
        
        status = "ok"
        details = {
            "status": status,
            "scheduler_running": scheduler_service.is_running(),
            "automation_enabled": bool(state_store.read().get("automation_enabled")),
            "last_tick": state_store.read().get("last_tick"),
            "api_requests_total": quota_tracker.get_total_calls(),
            "api_requests_remaining": quota_tracker.get_remaining_calls(),
            "api_quota_day": quota_tracker.get_quota_day(),
            "version": "2.0.0"
        }
        
        # Détection automatique des problèmes
        if not scheduler_service.is_running():
            status = "error"
            details["error"] = "Scheduler not running"
            
        if quota_tracker.get_remaining_calls() < 50:
            status = "warning"
            details["warning"] = "API quota low"
            
        return jsonify(details), 200 if status == "ok" else 503
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e),
            "timestamp": _utc_now_iso()
        }), 503
```

## Les Pièges : Erreurs Communes à Éviter

### ❌ Ignorer les Fallbacks

```python
# mauvais : pas de fallback
if not self._execute_ifttt_webhook(url):
    logger.error("IFTTT failed, nothing else to do")
    return False
```

### ✅ Cascade Complète

```python
# bon : cascade à 3 niveaux
if not self._execute_ifttt_webhook(url):
    logger.warning("IFTTT failed, trying scene")
    if not self._execute_aircon_scene(scene_id):
        logger.error("Scene failed, trying direct command")
        return self._execute_direct_command(device_id, action)
```

### ❌ Logs Non Structurés

```python
# mauvais : pas de contexte
logger.error("API failed")
```

### ✅ Logs Structurés

```python
# bon : contexte complet
self._error(
    "SwitchBot API request failed",
    status_code=response.status_code,
    endpoint=endpoint,
    attempt=attempt,
    max_attempts=max_attempts,
    trigger="automation_tick"
)
```

### ❌ Crash du Scheduler

```python
# mauvais : exception non catchée
def tick(self):
    # Si ça lève une exception, le scheduler s'arrête
    result = some_operation_that_can_fail()
```

### ✅ Wrapper Résilient

```python
# bon : wrapper global qui catch tout
def _run_tick_safe(self) -> None:
    try:
        self._tick_callable()
    except Exception as exc:
        self._logger.error("[scheduler] Exception caught: %s", exc, exc_info=True)
        # Le scheduler continue de fonctionner
```

## Diagnostic Rapide

### 1. Problèmes d'Automatisation

```bash
# Activer les logs détaillés
export LOG_LEVEL=debug

# Forcer un tick et observer
curl -X POST http://localhost:5000/actions/run_once

# Observer les logs avec préfixes
tail -f logs/app.log | grep "\[automation\]"
```

### 2. Problèmes API

```bash
# Logs API avec retries
grep "\[api\]" logs/app.log | grep "retry\|fallback"

# Vérifier l'état du quota
curl http://localhost:5000/healthz | jq '.api_requests_*'

# Test direct de l'API
curl -H "Authorization: Bearer $TOKEN" \
     https://api.switchbot.com/v1/devices
```

### 3. Problèmes de Store

```bash
# Logs de bascule de store
grep "\[store\]" logs/app.log

# Vérifier la connectivité PostgreSQL
python -c "import psycopg; print('PostgreSQL OK')" 2>/dev/null || echo "PostgreSQL KO"

# Validation des fichiers JSON
python -c "import json; print('Settings OK')" < config/settings.json
```

### 4. Validation de Configuration

```bash
# Vérifier les variables d'environnement
env | grep -E "(LOG_LEVEL|SWITCHBOT_|STORE_|POSTGRES_|SCHEDULER_)"

# Valider la configuration JSON
python -c "
import json
with open('config/settings.json') as f:
    config = json.load(f)
    required = ['aircon_device_id', 'automation_enabled']
    missing = [k for k in required if k not in config]
    print(f'Missing keys: {missing}' if missing else 'Config OK')
"
```

## Tests de Validation

### Tests Unitaires Essentiels

```python
# tests/test_error_handling.py
def test_switchbot_api_retry():
    """Test le retry avec backoff exponentiel."""
    
def test_ifttt_webhook_fallback():
    """Test le fallback webhook → scène → commande."""
    
def test_scheduler_exception_handling():
    """Test le wrapper global du scheduler."""
    
def test_postgres_store_fallback():
    """Test la bascule PostgreSQL → filesystem."""
```

### Tests d'Intégration

```python
# tests/integration/test_error_scenarios.py
def test_api_rate_limit_handling():
    """Test la gestion du rate limit 429."""
    
def test_network_timeout_recovery():
    """Test la récupération après timeout réseau."""
    
def test_database_connection_loss():
    """Test la perte de connexion PostgreSQL."""
```

## Checklist Production

### Avant Déploiement

- [ ] `LOG_LEVEL=info` (pas `debug` en production)
- [ ] Health check `/healthz` accessible depuis monitoring
- [ ] Variables d'environnement `.env` configurées
- [ ] Configuration `config/settings.json` validée
- [ ] Backup `state.json`/`settings.json`
- [ ] PostgreSQL connection pool configuré si utilisé

### Monitoring Continu

- [ ] Taux d'erreurs API < 1%
- [ ] Quota API > 100 requêtes restantes
- [ ] Scheduler running = true
- [ ] Latence par tick < 100ms
- [ ] Disponibilité > 99.9%

### Incident Response

1. **Détection** : Alertes monitoring ou logs ERROR
2. **Diagnostic** : Logs structurés avec préfixes `[component]`
3. **Isolation** : Vérifier composant affecté (API/store/scheduler)
4. **Résolution** : Fallback automatique ou intervention manuelle
5. **Post-mortem** : Documenter cause et prévention

### Tableau Comparatif des Approches de Dépannage

| Approche | Vitesse | Précision | Maintenance | Cas d'usage |
|----------|---------|-----------|-------------|-------------|
| **Logs réactifs** | Rapide | Moyenne | Faible | Problèmes simples |
| **Playbooks guidés** | Moyenne | Élevée | Moyenne | Incidents récurrents |
| **Health checks** | Immédiat | Faible | Faible | Monitoring continu |

## La Règle d'Or : Fallback Automatique, Intervention Minimale

**La Règle d'Or** : Chaque composant critique doit avoir un fallback automatique. Le Dashboard ne doit jamais laisser l'utilisateur dans un état non contrôlé à cause d'une défaillance technique.
