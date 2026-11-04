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
def record_call(self, *, increment: int = 1) -> None:
    """Fallback utilisé quand l'API n'expose pas les headers de quota."""
    if increment <= 0:
        return

    with _transaction_context(self._state_store):
        state = self._normalize_state()
        limit = self._extract_limit(state)
        used = self._safe_int(state.get("api_requests_total"), fallback=0)
        used = max(used, 0) + increment
        remaining = max(limit - used, 0)

        state["api_requests_total"] = used
        state["api_requests_remaining"] = remaining
        self._state_store.write(state)
```

### Capture des Headers SwitchBot

```python
# Dans SwitchBotClient._capture_quota_metadata()
def _capture_quota_metadata(self, response: Response) -> bool:
    """Extrait les métadonnées de quota des headers HTTP."""
    header_map = {key.lower(): value for key, value in response.headers.items()}
    limit = self._safe_int(
        header_map.get("x-ratelimit-limit")
        or header_map.get("x-rate-limit-limit")
        or header_map.get("ratelimit-limit")
    )
    remaining = self._safe_int(
        header_map.get("x-ratelimit-remaining")
        or header_map.get("x-rate-limit-remaining")
        or header_map.get("ratelimit-remaining")
    )

    if response.status_code == 429:
        remaining = 0

    if limit is None and remaining is None:
        self._quota_tracker.record_call()
        return True

    return self._quota_tracker.record_from_headers(limit=limit, remaining=remaining)
```

### Réinitialisation Quotidienne Automatique

```python
# Dans ApiQuotaTracker._normalize_state()
def _normalize_state(self) -> dict[str, Any]:
    """Initialise ou réinitialise le quota quotidien."""
    state = self._state_store.read()
    now = dt.datetime.now(dt.timezone.utc)
    today = now.date().isoformat()

    if state.get("api_quota_day") != today:
        # Réinitialisation à minuit UTC
        state["api_quota_day"] = today
        state["api_requests_total"] = 0
        state["api_requests_limit"] = self._default_daily_limit
        state["api_requests_remaining"] = self._default_daily_limit
        state["api_quota_reset_at"] = now.isoformat()
    else:
        state["api_requests_limit"] = self._extract_limit(state)
        state.setdefault("api_quota_reset_at", now.isoformat())

    return state
```

### Configuration Essentielle

#### `settings.json`
```json
{
  "api_quota_warning_threshold": 250
}
```

La limite (`api_requests_limit`) et les compteurs (`api_requests_total`, `api_requests_remaining`) vivent dans le store d'état, pas dans `settings.json`. La limite par défaut est `10 000` et peut être écrasée par les headers SwitchBot.

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
def quota() -> str:
    """Page de monitoring des quotas API."""
    settings_store = current_app.extensions["settings_store"]
    state_store = current_app.extensions["state_store"]

    settings = settings_store.read()
    state = state_store.read()
    quota_context = _build_quota_context(settings, state)

    return render_template("quota.html", **quota_context)
```

Le bouton de rafraîchissement (`POST /quota/refresh`) appelle `get_devices()` pour récupérer des headers frais, puis `quota_tracker.refresh_snapshot()` normalise le jour courant même sans appel API.

## Les Pièges à Éviter

### ❌ Ignorer la Synchronisation Headers
```python
# Mauvais : seulement compter localement
def record_call(self, *, increment: int = 1) -> None:
    state = self._state_store.read()
    state["api_requests_total"] = state.get("api_requests_total", 0) + increment
    # Jamais synchroniser avec les headers SwitchBot
```

### ✅ Double Track Complet
```python
# Bon : comptage local + synchronisation headers
def record_call(self, *, increment: int = 1) -> None:
    """Fallback quand les headers sont absents."""
    with _transaction_context(self._state_store):
        state = self._normalize_state()
        used = max(self._safe_int(state.get("api_requests_total"), fallback=0), 0) + increment
        state["api_requests_total"] = used
        state["api_requests_remaining"] = max(self._extract_limit(state) - used, 0)
        self._state_store.write(state)

def record_from_headers(self, *, limit: int | None, remaining: int | None) -> bool:
    """Écrase le compteur local avec la vérité SwitchBot."""
    if remaining is None:
        return False
    with _transaction_context(self._state_store):
        state = self._normalize_state()
        limit_value = max(int(limit), 1) if limit is not None else self._extract_limit(state)
        if limit is not None:
            state["api_requests_limit"] = limit_value
        remaining_value = max(min(int(remaining), limit_value), 0)
        state["api_requests_total"] = max(limit_value - remaining_value, 0)
        state["api_requests_remaining"] = remaining_value
        self._state_store.write(state)
        return True
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
def _normalize_state(self) -> dict[str, Any]:
    state = self._state_store.read()
    now = dt.datetime.now(dt.timezone.utc)
    today = now.date().isoformat()
    if state.get("api_quota_day") != today:
        state["api_quota_day"] = today
        state["api_requests_total"] = 0
        state["api_requests_remaining"] = self._default_daily_limit
    return state
```

### ❌ Pas de Persistance Atomique
```python
# Mauvais : compteur partiel écrit sans verrou ni transaction
self._state_store.write({"api_requests_total": self._state["api_requests_total"] + 1})
```

### ✅ Persistance Atomique
```python
# Bon : transaction + écriture unique de l'état complet
with _transaction_context(self._state_store):
    state = self._normalize_state()
    state["api_requests_total"] += 1
    state["api_requests_remaining"] = max(self._extract_limit(state) - state["api_requests_total"], 0)
    self._state_store.write(state)
```

## Patterns d'Utilisation par Type d'Action

Le comptage est centralisé dans `SwitchBotClient` : chaque réponse API met à jour le tracker, quel que soit l'appelant.

| Origine | Exemple | Fréquence | Impact Quota |
| ------- | ------- | --------- | ------------ |
| Poll capteur | `get_device_status()` | Toutes les 15-600 s | Élevé |
| Scène | `run_scene()` | Automatisation/manuel | Moyen |
| Commande directe | `set_all()` / `turn_off()` | Manuel/fallback | Faible |
| Inventaire | `/devices` via `get_devices()` | Navigation | Faible |
| Actions manuelles | `/actions/*` | Manuel | Variable |

## Monitoring et Dépannage

### Health Check Intégré
```bash
curl http://localhost:5000/healthz | jq '{status, active_store_backend, store_degraded}'
```

`/healthz` expose l'état du store et du scheduler, pas les compteurs de quota. Pour lire les compteurs, passez par la page `/quota` ou l'endpoint de debug protégé.

### Logs Quota
```bash
# Comptage standard
[quota] fallback increment recorded: used=42 remaining=9958 limit=10000

# Synchronisation header
[api] SwitchBot quota snapshot captured: remaining=950 limit=10000

# Réinitialisation quotidienne (via refresh_snapshot)
[quota] snapshot refreshed: day=2026-11-04 remaining=10000
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
