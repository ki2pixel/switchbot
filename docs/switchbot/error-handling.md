# Gestion des Erreurs SwitchBot Dashboard

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Le SwitchBot Dashboard implémente une architecture de gestion d'erreurs multicouche avec fallback automatique, retry intelligent et monitoring complet pour garantir la résilience en production.

> 📝 **Décisions connexes** : Les patterns de gestion d'erreurs sont documentés dans `memory-bank/systemPatterns.md`. Voir notamment les décisions du 2026-01-18 sur le wrapper global SchedulerService.

## Hiérarchie des Exceptions

### Exceptions Métier

```python
# switchbot_dashboard/switchbot_api.py
class SwitchBotApiError(Exception):
    """Erreur générique de l'API SwitchBot."""
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

# switchbot_dashboard/ifttt.py  
class IFTTTWebhookError(Exception):
    """Erreur lors de l'appel webhook IFTTT."""
    pass

# switchbot_dashboard/postgres_store.py
class PostgresStoreError(Exception):
    """Erreur de connexion ou opération PostgreSQL."""
    pass

# switchbot_dashboard/config_store.py
class StoreError(Exception):
    """Erreur générique de stockage (base ou fichier)."""
    pass
```

### Exceptions Système

- **`psycopg.OperationalError`** : Erreur de connexion PostgreSQL
- **`requests.exceptions.RequestException`** : Erreur réseau HTTP
- **`json.JSONDecodeError`** : Erreur parsing JSON
- **`threading.TimeoutError`** : Timeout d'opération

## Cascade de Fallback

### Architecture à 3 Niveaux
1. **IFTTT Webhook** (priorité) → déclenche applet IFTTT
2. **Scène SwitchBot** (fallback 1) → appelle API SwitchBot
3. **Commande directe** (fallback 2) → `setAll`/`turnOff`

### Code Source Référence
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

## Patterns de Gestion

### 1. Retry avec Backoff Exponentiel

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

### 2. Fallback Cascade à 3 Niveaux

```python
# switchbot_dashboard/automation.py
def _trigger_aircon_action(self, action_key: str, settings: dict, trigger: str) -> bool:
    """Déclenche une action avec cascade IFTTT → scène → commande directe."""
    
    # Niveau 1: Webhook IFTTT (priorité)
    webhooks = extract_ifttt_webhooks(settings)
    if action_key in webhooks:
        try:
            if self._execute_webhook(webhooks[action_key], trigger):
                self._info(f"IFTTT webhook triggered successfully", 
                          action_key=action_key, trigger=trigger)
                return True
        except IFTTTWebhookError as e:
            self._warning(f"IFTTT webhook failed, falling back to scene", 
                         error=str(e), action_key=action_key)
    
    # Niveau 2: Scène SwitchBot (fallback 1)
    scenes = extract_aircon_scenes(settings)
    if action_key in scenes:
        try:
            if self._execute_aircon_scene(scenes[action_key], trigger):
                self._info(f"SwitchBot scene executed successfully", 
                          action_key=action_key, trigger=trigger)
                return True
        except SwitchBotApiError as e:
            self._warning(f"SwitchBot scene failed, falling back to direct command", 
                         error=str(e), action_key=action_key)
    
    # Niveau 3: Commande directe (fallback 2)
    aircon_id = str(settings.get("aircon_device_id", "")).strip()
    if aircon_id:
        try:
            if self._execute_direct_command(action_key, aircon_id, trigger):
                self._info(f"Direct command executed successfully", 
                          action_key=action_key, trigger=trigger)
                return True
        except SwitchBotApiError as e:
            self._error(f"All fallbacks failed for aircon action", 
                       error=str(e), action_key=action_key, trigger=trigger)
    
    return False
```

### 3. Wrapper Global SchedulerService

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

### 4. Fallback Store Automatique

```python
# switchbot_dashboard/__init__.py
def create_app() -> Flask:
    """Crée l'application Flask avec gestion des bascules de store."""
    
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

## Logging Structuré

### Préfixes de Logs

```python
# Standards de préfixes pour faciliter le filtering
[api]       # Appels API SwitchBot, quotas, retries
[automation] # Logique métier, décisions, actions
[scheduler] # Ticks, erreurs globales, health
[store]     # Opérations stockage, bascules, erreurs
[history]   # Service d'historique, batch insert
[ifttt]     # Webhooks IFTTT, timeouts, fallbacks
```

### Niveaux de Log

```python
# Configuration via LOG_LEVEL (.env)
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Exemples d'utilisation
self._debug("Detailed execution info", ...)      # Développement
self._info("Normal operation", ...)             # Production
self._warning("Fallback activated", ...)         # Attention
self._error("Operation failed", ...)            # Erreur
self._critical("System failure", ...)           # Critique
```

### Format des Logs

```python
# Structure standardisée
self._info(
    "Message human readable",
    field1=value1,           # Contexte structuré
    field2=value2,
    trigger="scheduler",   # Source du déclenchement
    exc_info=True          # Stack trace si exception
)

# Exemple réel
[automation] Winter mode triggered | current_temp=17.5, min_temp=18.0, hysteresis=0.5, trigger=scheduler
```

## Monitoring et Observabilité

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
        
        # Vérification de la santé des composants
        status = "ok"
        details = {
            "status": status,
            "scheduler_running": scheduler_service.is_running(),
            "automation_enabled": bool(state_store.read().get("automation_enabled")),
            "last_tick": state_store.read().get("last_tick"),
            "api_requests_total": quota_tracker.get_total_calls(),
            "api_requests_remaining": quota_tracker.get_remaining_calls(),
            "api_quota_day": quota_tracker.get_quota_day(),
            "version": "1.0.0"
        }
        
        # Détecter les problèmes
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

### Métriques d'Erreur

```python
# Dans state.json - tracking des erreurs
{
  "error_count": 3,
  "last_error": {
    "timestamp": "2026-01-26T14:30:00Z",
    "message": "SwitchBot API timeout",
    "context": "poll_meter",
    "severity": "warning"
  },
  "error_history": [
    {
      "timestamp": "2026-01-26T14:25:00Z",
      "type": "api_timeout",
      "context": "execute_scene",
      "resolved": true
    }
  ]
}
```

## Patterns de Dépannage

### 1. Diagnostic d'Automatisation

```bash
# Activer les logs détaillés
export LOG_LEVEL=debug

# Forcer un tick et observer
curl -X POST http://localhost:5000/actions/run_once

# Observer les logs avec préfixes
tail -f logs/app.log | grep "\[automation\]"
```

### 2. Diagnostic API

```bash
# Logs API avec retries
grep "\[api\]" logs/app.log | grep "retry\|fallback"

# Vérifier l'état du quota
curl http://localhost:5000/healthz | jq '.api_requests_*'

# Test direct de l'API
curl -H "Authorization: Bearer $TOKEN" \
     https://api.switchbot.com/v1/devices
```

### 3. Diagnostic Store

```bash
# Logs de bascule de store
grep "\[store\]" logs/app.log

# Vérifier la connectivité PostgreSQL
python -c "import psycopg; print('PostgreSQL OK')" 2>/dev/null || echo "PostgreSQL KO"

# Validation des fichiers JSON
python -c "import json; print('Settings OK')" < config/settings.json
```

## Intégration Monitoring Externe

### Prometheus (exemple)

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'switchbot-dashboard'
    static_configs:
      - targets: ['localhost:5000']
    metrics_path: '/healthz'
    scrape_interval: 30s
```

### Grafana Dashboard

```json
{
  "dashboard": {
    "panels": [
      {
        "title": "API Quota Usage",
        "type": "stat",
        "targets": [
          {
            "expr": "switchbot_api_requests_remaining",
            "legendFormat": "Remaining"
          }
        ]
      },
      {
        "title": "Automation Errors",
        "type": "graph",
        "targets": [
          {
            "expr": "increase(switchbot_automation_errors[5m])",
            "legendFormat": "Errors/min"
          }
        ]
      }
    ]
  }
}
```

### Alertmanager

```yaml
# alertmanager.yml
routes:
  - receiver: 'switchbot-alerts'
    group_by: ['alertname']
    group_wait: 10s
    repeat_interval: 1h

receivers:
  - name: 'switchbot-alerts'
    slack_configs:
      - api_url: 'https://hooks.slack.com/...'
        channel: '#alerts'
        title: 'SwitchBot Dashboard Alert'
```

## Tests et Validation

### Tests Unitaires

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

### Tests de Charge

```bash
# Simulation de charge API
python scripts/load_test_api.py --requests=1000 --concurrent=10

# Test de résilience du scheduler
python scripts/stress_test_automation.py --duration=3600
```

## Checklist Production

### Avant Déploiement

- [ ] `LOG_LEVEL=info` (pas `debug` en production)
- [ ] Health check `/healthz` accessible
- [ ] Monitoring externe configuré
- [ ] Alertes quota et erreurs actives
- [ ] Backup `state.json`/`settings.json`
- [ ] PostgreSQL connection pool configuré

### Monitoring Continu

- [ ] Taux d'erreurs API < 1%
- [ ] Quota API > 100 requêtes restantes
- [ ] Scheduler running = true
- [ ] Latence par tick < 100ms
- [ ] Disponibilité > 99.9%

### Incident Response

1. **Détection** : Alertes monitoring ou logs ERROR
2. **Diagnostic** : Logs structurés avec préfixes
3. **Isolation** : Vérifier composant affecté (API/store/scheduler)
4. **Résolution** : Fallback automatique ou intervention manuelle
5. **Post-mortem** : Documenter cause et prévention

---

*Pour les optimisations de performance et le monitoring avancé, consultez [Optimisations Performance](performance-optimizations.md) et [Gestion des Quotas API](api-quotas.md).*
