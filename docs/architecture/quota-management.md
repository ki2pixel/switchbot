# Gestion des Quotas API SwitchBot

**TL;DR** : Le Dashboard SwitchBot implémente un suivi local des quotas API avec `ApiQuotaTracker` pour éviter la saturation des 10 000 requêtes/jour autorisées par SwitchBot, via un double mécanisme de comptage local et capture des headers HTTP.

## Le Problème : Pourquoi un Suivi Local ?

Vous développez un dashboard qui interroge continuellement les devices SwitchBot. L'API est limitée à 10 000 requêtes par jour, mais vous n'avez aucun moyen de savoir combien il vous reste jusqu'à recevoir une erreur 429. Pire, si vous déployez en production avec plusieurs utilisateurs, vous pourriez épuiser votre quota sans même vous en rendre compte.

C'est le problème classique du "compteur externe invisible" : vous consommez une ressource limitée sans visibilité sur votre consommation réelle.

## La Solution : Architecture Double Track

Le Dashboard SwitchBot résout ce problème avec une architecture à deux voies :

### 1. Comptage Local Prédictif
Chaque appel API est immédiatement compté localement avant même d'être envoyé. Ça vous donne une vision en temps réel de votre consommation.

### 2. Synchronisation Headers SwitchBot
Les réponses API contiennent des headers `X-RateLimit-*` qui révèlent le quota réel. On synchronise notre compteur local avec cette source de vérité.

### Le Flux Complet

```
Appel API → SwitchBotClient._request()
    ↓
Capture quota → _capture_quota_metadata()
    ↓
Mise à jour → ApiQuotaTracker.record_call()
    ↓
Persistance → state_store.write() (atomique)
    ↓
Alerte UI → Bandeau si api_requests_remaining ≤ api_quota_warning_threshold
```

## L'Implémentation : Le Code et la Configuration

### ApiQuotaTracker - Le Cœur du Système

```python
# switchbot_dashboard/quota.py
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

### Réinitialisation Quotidienne Automatique

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

### Configuration Essentielle

#### `settings.json`
```json
{
  "api_quota_warning_threshold": 250,
  "api_requests_limit": 10000
}
```

#### `.env`
```bash
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10
LOG_LEVEL=info
```

### Interface Utilisateur Intégrée

#### Bandeau d'Alerte Automatique
Le bandeau apparaît uniquement quand `api_requests_remaining` ≤ `api_quota_warning_threshold`. Il affiche les requêtes restantes, le jour suivi et l'heure de réinitialisation avec un lien vers la page détaillée.

#### Page `/quota` de Monitoring
```python
@dashboard_bp.get("/quota")
def quota_page() -> str:
    """Page de monitoring des quotas API."""
    quota_tracker = current_app.extensions["quota_tracker"]
    quota_state = quota_tracker.get_state()
    
    return render_template("quota.html", quota=quota_state)
```

## Les Pièges à Éviter

### ❌ Ignorer la Synchronisation Headers
```python
# Mauvais : seulement compter localement
def record_call(self):
    self._state["api_requests_today"] += 1
    # Jamais synchroniser avec les headers SwitchBot
```

### ✅ Double Track Complet
```python
# Bon : comptage local + synchronisation headers
def record_call(self, context: str = "unknown") -> None:
    self._ensure_quota_initialized()
    self._state["api_requests_today"] += 1
    
    # Synchronisation avec les headers si disponibles
    if self._header_remaining:
        self._sync_with_header(self._header_remaining)
```

### ❌ Réinitialisation Manuelle Oubliée
```python
# Mauvais : pas de réinitialisation automatique
def record_call(self):
    if not self._state.get("api_quota_day"):
        self._state["api_quota_day"] = datetime.now().isoformat()
```

### ✅ Réinitialisation UTC Fiable
```python
# Bon : réinitialisation automatique à minuit UTC
def _ensure_quota_initialized(self) -> None:
    current_day = datetime.utcnow().date().isoformat()
    if self._state.get("api_quota_day") != current_day:
        # Reset complet du quota
```

### ❌ Pas de Persistance Atomique
```python
# Mauvais : écritures multiples
self._state["api_requests_today"] += 1
self._state_store.write({"api_requests_today": self._state["api_requests_today"]})
```

### ✅ Persistance Atomique
```python
# Bon : écriture unique de l'état complet
self._state_store.write(self._state)
```

## Patterns d'Utilisation par Type d'Action

| Type d'Appel | Context | Fréquence | Impact Quota |
| ------------ | ------- | --------- | ----------- |
| `poll_meter()` | "poll_meter" | Toutes les 30s | Élevé |
| `execute_scene()` | "scene_execution" | Manuel/IFTTT | Moyen |
| `set_all()` | "direct_command" | Manuel | Faible |
| `/devices` | "inventory" | Navigation | Faible |
| `/actions/*` | "manual_action" | Manuel | Variable |

## Monitoring et Dépannage

### Health Check Intégré
```bash
curl http://localhost:5000/healthz | jq '.api_requests_*'
```

Retourne :
```json
{
  "api_requests_total": 842,
  "api_requests_remaining": 158,
  "api_quota_day": "2026-01-26",
  "api_quota_reset_at": "2026-01-27T00:00:00Z"
}
```

### Logs Quota
```bash
# Comptage standard
[api] Quota snapshot updated | context=poll_meter, used=42, remaining=958, limit=10000

# Synchronisation header
[api] Syncing with header quota | header_remaining=950, local_used=50

# Réinitialisation quotidienne
[api] Daily quota reset | day=2026-01-26, new_limit=10000
```

### Actions Manuelles
```bash
# Forcer la réinitialisation du quota
curl -X POST http://localhost:5000/quota/refresh

# Logs de quota récents
grep "\[api\]" logs/app.log | tail -20
```

## Optimisations Avancées

### Adaptation des Seuils
```python
# Selon le jour de la semaine
if datetime.now().weekday() < 5:  # Lundi-Vendredi
    settings["api_quota_warning_threshold"] = 500
else:  # Week-end
    settings["api_quota_warning_threshold"] = 200
```

### Gestion Multi-Environnement
```python
# Développement : limite réduite
if os.getenv("FLASK_ENV") == "development":
    quota_tracker.set_limit(1000)
else:  # Production : limite complète
    quota_tracker.set_limit(10000)
```

### ❌ Headers Seulement / ✅ Double Track Complet

❌ **Headers seulement** : Dépendance totale aux headers SwitchBot, pas de suivi local, impossibilité de détecter les dépassements avant la réponse API. Vous découvrez le quota épuisé quand l'API renvoie 429.

✅ **Double track complet** : Comptage local instantané + synchronisation headers, détection précoce des dépassements, alertes configurables, résilience en cas d'absence de headers.

### Tableau Comparatif des Approches de Tracking

| Approche | Précision | Latence | Complexité | Résilience |
|----------|-----------|---------|------------|------------|
| **Headers API** | Élevée | Moyenne | Faible | Faible |
| **Tracking local** | Moyenne | Immédiate | Moyenne | Élevée |
| **Hybrid** (notre) | Élevée | Immédiate | Élevée | Très élevée |

## La Règle d'Or : Comptage Local, Synchronisation Headers

Le principe fondamental du système de quotas : **compter localement chaque appel, synchroniser avec les headers externes, et réinitialiser automatiquement à minuit UTC.**

Cette approche vous donne le meilleur des deux mondes : visibilité immédiate via le compteur local et exactitude via la synchronisation avec la source de vérité SwitchBot.

---

*Pour l'intégration avec les systèmes de monitoring externes et les patterns de gestion d'erreurs, consultez la documentation sur l'architecture de monitoring et les stratégies de résilience.*
