# Guide de Dépannage SwitchBot Dashboard v2

**TL;DR** : Le Dashboard utilise une architecture à 2 niveaux de fallback (Scène favorite → Commande directe) avec retry automatique, monitoring structuré et résilience PostgreSQL via `ResilientStore` (alerte + `503` en production, fallback JSON hors production).

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
def healthz() -> Any:
    """Endpoint de monitoring pour les systèmes externes."""
    # Lecture des stores, health check PostgreSQL, état scheduler...
    payload = {
        "status": status,  # ok / degraded / error
        "scheduler_running": scheduler_running,
        "automation_enabled": automation_enabled,
        "last_tick": last_tick,
        "last_scheduler_tick": last_scheduler_tick,
        "average_tick_duration_seconds": round(average_tick_duration, 4),
        "postgres_connected": postgres_connected,
        "store_degraded": store_degraded,
        "active_store_backend": getattr(settings_store, "active_backend", "unknown"),
        "store_fallback_enabled": bool(getattr(settings_store, "fallback_enabled", False)),
        "timestamp_utc": timestamp,
    }
    return app.response_class(json.dumps(payload) + "\n", mimetype="application/json", status=status_code)
```

Le endpoint renvoie `503` si PostgreSQL est configuré mais injoignable, si le store est dégradé, ou si le scheduler est activé mais arrêté. Les compteurs de quota ne font pas partie de la réponse.

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

```bash
# Retry API et capture quota
python -m pytest tests/test_switchbot_api.py -v

# Cascade scène → commande directe, idempotence OFF, timezone
python -m pytest tests/test_automation_service.py -v

# Wrapper du scheduler et gestion d'exception
python -m pytest tests/test_scheduler_service.py -v

# Bascule PostgreSQL → filesystem
python -m pytest tests/test_config_store_failover.py tests/test_postgres_store.py -v
```

## Checklist Production

### Symptômes d'un `FLASK_DEBUG` oublié en production

- Le cookie de session n'a **pas** l'attribut `Secure` (visible dans `Set-Cookie`).
- L'en-tête `Strict-Transport-Security` est absent des réponses.
- Le log de démarrage affiche `[store] Runtime filesystem fallback configured …`
  alors que `STORE_RUNTIME_FALLBACK` n'est pas activé.
- `/healthz` renvoie `"store_fallback_enabled": true` sans opt-in explicite.

Cause : `FLASK_DEBUG=1` traîné depuis le `.env` local. Depuis la remédiation V2,
`create_app()` force `app.debug=False` dès qu'un serveur WSGI est détecté
(gunicorn dans `sys.modules`, `RENDER=true` ou `SERVER_SOFTWARE`), mais la
variable doit tout de même être retirée du dashboard d'hébergement.

### Avant Déploiement

- [ ] `LOG_LEVEL=info` (pas `debug` en production)
- [ ] `FLASK_DEBUG` absent ou `0`
- [ ] `STORE_RUNTIME_FALLBACK` absent ou `false`
- [ ] Health check `/healthz` accessible depuis monitoring
- [ ] Variables d'environnement `.env` configurées
- [ ] Configuration `config/settings.json` validée
- [ ] Backup `state.json`/`settings.json`
- [ ] PostgreSQL connection pool configuré si utilisé

## La Règle d'Or : Fallback Contrôlé, Intervention Minimale

**La Règle d'Or** : Chaque composant critique doit avoir un fallback explicite ou une alerte. En production, le store privilégie l'alerte + `503` pour éviter un split-brain ; hors production, le fallback JSON est automatique.
