# Gestion des Quotas API SwitchBot

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Le SwitchBot Dashboard implémente un système complet de suivi des quotas API pour éviter la saturation des appels vers l'API SwitchBot (limitée à 10 000 requêtes par jour par défaut).

> 📝 **Décisions connexes** : Les patterns de gestion des quotas sont documentés dans `memory-bank/systemPatterns.md`. Voir notamment les décisions du 2026-01-10 sur l'implémentation du suivi local.

## Architecture

### Composants principaux

- **`ApiQuotaTracker`** : Service central de suivi des quotas
- **`SwitchBotClient`** : Intégration transparente du suivi dans chaque appel API
- **Interface utilisateur** : Bandeau d'alerte et page `/quota` dédiée
- **Stockage** : Persistance dans `state.json` via `state_store`

### Flux de données

1. **Appel API** → `SwitchBotClient._request()` 
2. **Capture quota** → `SwitchBotClient._capture_quota_metadata()`
3. **Mise à jour** → `ApiQuotaTracker.record_call()`
4. **Persistance** → `state_store.write()` (atomique)
5. **Alerte UI** → Bandeau si `api_requests_remaining` ≤ `api_quota_warning_threshold`

## ApiQuotaTracker - Architecture Complète

### Implémentation
Le tracker utilise un double mécanisme :
1. **Comptage local** : `record_call()` incrémente `state["api_requests_today"]`
2. **Snapshot headers** : `record_from_headers()` capture `X-RateLimit-*`

### Gestion des limites
- Limite par défaut : 10,000 requêtes/jour
- Ajustement dynamique via headers API SwitchBot
- Réinitialisation à minuit UTC avec `api_quota_day`

### Code Source Référence
```python
# switchbot_dashboard/quota.py - Lignes 45-67
def record_call(self, context: str = "unknown") -> None:
    """Enregistre un appel API et met à jour les compteurs."""
    self._ensure_quota_initialized()
    
    # Incrémentation du compteur local
    self._state["api_requests_today"] += 1
    
    # Calcul des requêtes restantes
    remaining = self._state["api_requests_limit"] - self._state["api_requests_today"]
    self._state["api_requests_remaining"] = max(0, remaining)
    
    # Persistance atomique
    self._state_store.write(self._state)
```

## Mécanismes de Suivi

### Comptage Local

```python
# Dans ApiQuotaTracker.record_call()
def record_call(self, context: str = "unknown") -> None:
    """Enregistre un appel API et met à jour les compteurs."""
    self._ensure_quota_initialized()
    
    # Incrémentation du compteur local
    self._state["api_requests_today"] += 1
    
    # Calcul des requêtes restantes
    remaining = self._state["api_requests_limit"] - self._state["api_requests_today"]
    self._state["api_requests_remaining"] = max(0, remaining)
    
    # Persistance atomique
    self._state_store.write(self._state)
```

### Capture des Headers SwitchBot

```python
# Dans SwitchBotClient._capture_quota_metadata()
def _capture_quota_metadata(self, response: requests.Response) -> None:
    """Extrait les métadonnées de quota des headers HTTP."""
    if "X-RateLimit-Limit" in response.headers:
        limit = int(response.headers["X-RateLimit-Limit"])
        if limit != self._quota_tracker.get_limit():
            self._quota_tracker.set_limit(limit)
    
    if "X-RateLimit-Remaining" in response.headers:
        remaining = int(response.headers["X-RateLimit-Remaining"])
        # Synchronisation avec le compteur local si nécessaire
        self._quota_tracker.sync_with_header(remaining)
```

### Réinitialisation Automatique

```python
# Dans ApiQuotaTracker._ensure_quota_initialized()
def _ensure_quota_initialized(self) -> None:
    """Initialise ou réinitialise le quota quotidien."""
    current_day = datetime.utcnow().date().isoformat()
    
    if self._state.get("api_quota_day") != current_day:
        # Réinitialisation à minuit UTC
        self._state.update({
            "api_quota_day": current_day,
            "api_requests_today": 0,
            "api_requests_remaining": self._state.get("api_requests_limit", 10000),
            "api_quota_reset_at": _utc_now_iso()
        })
```

## Configuration

### Paramètres dans `settings.json`

```json
{
  "api_quota_warning_threshold": 250,
  "api_requests_limit": 10000
}
```

### Variables d'environnement

```bash
# .env
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10
LOG_LEVEL=info
```

## Interface Utilisateur

### Bandeau d'Alerte

- **Affichage conditionnel** : Uniquement si `api_requests_remaining` ≤ `api_quota_warning_threshold`
- **Style** : Alert Bootstrap `warning` avec icône FontAwesome
- **Informations** : Requêtes restantes, jour suivi, heure de réinitialisation
- **Action** : Lien vers page `/quota` pour détails

### Page `/quota`

```python
# Route : GET /quota
@dashboard_bp.get("/quota")
def quota_page() -> str:
    """Page de monitoring des quotas API."""
    quota_tracker = current_app.extensions["quota_tracker"]
    quota_state = quota_tracker.get_state()
    
    return render_template("quota.html", quota=quota_state)
```

**Contenu de la page :**
- Carte "Quota API quotidien" avec compteur visuel
- Encadré "Fonctionnement du suivi"
- Conseils d'exploitation
- Bouton "Rafraîchir le quota" (POST `/quota/refresh`)

## Patterns d'Utilisation

### Types d'Appels Suivis

1. **Lecture Meter** : `poll_meter()` dans `AutomationService`
2. **Exécution Scènes** : `SwitchBotClient.execute_scene()`
3. **Commandes Directes** : `SwitchBotClient.set_all()`, `turn_off()`
4. **Inventory Devices** : Page `/devices`
5. **Actions Manuelles** : Routes `/actions/*`

### Exemples de Logs

```bash
# Comptage standard
[api] Quota snapshot updated | context=poll_meter, used=42, remaining=958, limit=10000

# Synchronisation header
[api] Syncing with header quota | header_remaining=950, local_used=50

# Réinitialisation quotidienne
[api] Daily quota reset | day=2026-01-26, new_limit=10000
```

## Bonnes Pratiques

### Surveillance

1. **Monitoring régulier** : Consulter `/quota` quotidiennement
2. **Alerte proactive** : Ajuster `api_quota_warning_threshold` selon usage
3. **Tendance** : Observer la consommation par type d'action

### Optimisation

1. **Intervalles de poll** : Augmenter `poll_interval_seconds` si quota proche
2. **Actions manuelles** : Réduire les clics manuels en période critique
3. **Webhooks IFTTT** : Privilégier les webhooks (pas de quota SwitchBot)

### Dépannage

```bash
# Forcer la réinitialisation du quota
curl -X POST http://localhost:5000/quota/refresh

# Vérifier l'état courant
curl http://localhost:5000/healthz | jq '.api_requests_*'

# Logs de quota
grep "\[api\]" logs/app.log | tail -20
```

## Intégration Monitoring Externe

### Health Check `/healthz

```json
{
  "api_requests_total": 842,
  "api_requests_remaining": 158,
  "api_quota_day": "2026-01-26",
  "api_quota_reset_at": "2026-01-27T00:00:00Z"
}
```

### Métriques Prometheus (exemple)

```yaml
# monitoring.yml
groups:
  - name: switchbot_dashboard
    rules:
      - alert: SwitchBotQuotaLow
        expr: switchbot_api_requests_remaining < 100
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "SwitchBot API quota low"
          description: "Only {{ $value }} requests remaining"
```

## Cas d'Usage Avancés

### Gestion Multi-Environnement

```python
# Développement : limite réduite
if os.getenv("FLASK_ENV") == "development":
    quota_tracker.set_limit(1000)  # Limite dev

# Production : limite complète
else:
    quota_tracker.set_limit(10000)  # Limite prod
```

### Personnalisation du Seuil d'Alerte

```python
# Selon le jour de la semaine (plus usage weekday)
if datetime.now().weekday() < 5:  # Lundi-Vendredi
    settings["api_quota_warning_threshold"] = 500
else:  # Week-end
    settings["api_quota_warning_threshold"] = 200
```

## Tests et Validation

### Tests Unitaires

```python
# tests/test_api_quota_tracker.py
def test_quota_daily_reset():
    """Test la réinitialisation quotidienne du quota."""
    
def test_quota_warning_threshold():
    """Test le déclenchement de l'alerte."""
    
def test_quota_sync_with_headers():
    """Test la synchronisation avec les headers SwitchBot."""
```

### Tests Manuels

1. **Simulation de quota** : Modifier `state.json` manuellement
2. **Validation UI** : Vérifier l'affichage du bandeau
3. **Test réinitialisation** : Attendre minuit UTC ou forcer via `/quota/refresh`

---

*Pour le monitoring avancé et l'intégration avec les systèmes externes, consultez [Gestion des Erreurs](error-handling.md) et [Optimisations Performance](performance-optimizations.md).*
