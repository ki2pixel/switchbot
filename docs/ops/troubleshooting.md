# Guide de Dépannage SwitchBot Dashboard v2

**TL;DR** : Le Dashboard utilise une architecture à 2 niveaux de fallback (Scène favorite → Commande directe) avec retry automatique, monitoring structuré et bascule PostgreSQL → fichier pour garantir la résilience en production.

## Le Problème : Pourquoi la Gestion d'Erreurs est Critique

Vous déployez un dashboard de domotique qui contrôle votre climatisation. Soudain, l'API SwitchBot rate limite à 429, PostgreSQL refuse la connexion, et vos commandes directes échouent. Votre climatisation reste en mode "on" alors qu'il fait 35°C. C'est exactement le scénario que la gestion d'erreurs multicouche du Dashboard v2 empêche.

## La Solution : Architecture de Résilience

### Cascade de Fallback à 2 Niveaux

Le Dashboard n'a jamais un seul point de défaillance. Chaque action climatisation suit une cascade déterministe :

1. **Scène SwitchBot** (priorité) → appelle API SwitchBot avec scène favorite prédéfinie
2. **Commande directe** (fallback) → `setAll`/`turnOff` sur l'appareil

```python
# switchbot_dashboard/automation.py
def _trigger_aircon_action(self, action_key: str, state_reason: str) -> bool:
    """Déclenche une action avec cascade à 2 niveaux."""
    
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
  "aircon_scenes": {
    "winter": "scene_id_winter_mode",
    "summer": "scene_id_summer_mode",
    "fan": "scene_id_fan_mode",
    "off": "scene_id_off_mode"
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
if not self._execute_aircon_scene(scene_id):
    logger.error("Scene failed, nothing else to do")
    return False
```

### ✅ Cascade Complète

```python
# bon : cascade à 2 niveaux
if not self._execute_aircon_scene(scene_id):
    logger.warning("Scene failed, trying direct command")
    return self._execute_direct_command(device_id, action)
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
```

## Tests de Validation

### Tests Unitaires Essentiels

```python
# tests/test_error_handling.py
def test_switchbot_api_retry():
    """Test le retry avec backoff exponentiel."""
    
def test_scene_execution_fallback():
    """Test le fallback scène → commande."""
    
def test_scheduler_exception_handling():
    """Test le wrapper global du scheduler."""
    
def test_postgres_store_fallback():
    """Test la bascule PostgreSQL → filesystem."""
```

## Checklist Production

### Avant Déploiement

- [ ] `LOG_LEVEL=info` (pas `debug` en production)
- [ ] Health check `/healthz` accessible depuis monitoring
- [ ] Variables d'environnement `.env` configurées
- [ ] Configuration `config/settings.json` validée
- [ ] Backup `state.json`/`settings.json`
- [ ] PostgreSQL connection pool configuré si utilisé

## La Règle d'Or : Fallback Automatique, Intervention Minimale

**La Règle d'Or** : Chaque composant critique doit avoir un fallback automatique. Le Dashboard ne doit jamais laisser l'utilisateur dans un état non contrôlé à cause d'une défaillance technique.
