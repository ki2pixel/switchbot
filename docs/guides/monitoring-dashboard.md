# Guide de Monitoring du Dashboard

**TL;DR** : Le History Monitoring transforme vos données brutes SwitchBot en visualisations temps réel avec une rétention de 6 heures, le tout via PostgreSQL et Chart.js sans dépendances externes.

## Le Problème : Pourquoi du Monitoring ?

Vous gérez vos appareils SwitchBot depuis l'interface web, mais vous ne voyez jamais les tendances. La climatisation s'alligne-t-elle avec les pics de température ? L'humidité dépasse-t-elle les seuils critiques pendant la nuit ? Les logs accumulent des données, mais elles restent inertes.

Pire encore, chaque dashboard que vous construisez tombe dans les pièges classiques : dépendances CDN qui cassent l'offline-first, graphiques qui rament sur mobile, ou données qui s'accumulent indéfiniment jusqu'à saturer votre base.

## La Solution : L'Architecture du Monitoring

### Le Pattern "State History Service"

Au lieu de laisser les données s'accumuler passivement, nous enregistrons un snapshot après chaque tick d'automation. C'est le pattern "Event Sourcing" appliqué à l'IoT : chaque état devient un fait immuable, query-able et visualisable.

```python
# Dans automation.py, après chaque tick
if history_service:
    history_service.record_state({
        'temperature': current_temp,
        'humidity': current_humidity,
        'assumed_aircon_power': assumed_state,
        'last_action': last_action,
        'api_requests_today': api_quota_tracker.get_today_count(),
        'error_count': error_count
    })
```

### La Découpe Temporelle Intelligente

Ne stockez pas tout éternellement. 6 heures = la fenêtre PITR de Neon PostgreSQL. Au-delà, cleanup automatique. C'est suffisant pour voir les tendances journalières sans exploser vos coûts de stockage.

### L'Architecture en Couches

```
AutomationService → HistoryService → PostgreSQL → REST API → Frontend Chart.js
```

Chaque couche a une responsabilité unique. Pas de fuites d'abstraction, pas de couplage fort.

## L'Implémentation : Le Code et la Configuration

### Structure de la Table PostgreSQL

```sql
CREATE TABLE state_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    temperature DECIMAL(4,1),
    humidity DECIMAL(4,1),
    assumed_aircon_power VARCHAR(10),
    last_action VARCHAR(50),
    api_requests_today INTEGER DEFAULT 0,
    error_count INTEGER DEFAULT 0,
    last_temperature_stale BOOLEAN DEFAULT FALSE,
    timezone VARCHAR(50) DEFAULT 'UTC',
    metadata JSONB DEFAULT '{}'
);
```

Les types sont optimisés : `DECIMAL(4,1)` pour la température (pas de FLOAT inutile), `JSONB` pour les métadonnées flexibles, indexes automatiques sur `timestamp`.

### Injection du Service

Dans `switchbot_dashboard/__init__.py` :

```python
from .history_service import HistoryService

# Après setup du PostgresStore
if isinstance(settings_store, PostgresStore):
    history_service = HistoryService(
        connection_pool=settings_store._pool,
        logger=app.logger,
        retention_hours=6,
    )
    app.extensions["history_service"] = history_service
    
    # Injection dans AutomationService
    automation_service = AutomationService(
        settings_store=settings_store,
        state_store=state_store,
        switchbot_client=switchbot_client,
        ifttt_client=ifttt_client,
        history_service=history_service,  # ← Le passage clé
        logger=app.logger,
    )
```

### Variables d'Environnement

Aucune variable supplémentaire. Le service réutilise `POSTGRES_URL` existant. C'est le principe DRY : pas de configuration dupliquée.

### API REST : Trois Endpoints Simples

```python
# /history/api/data - Données filtrées avec granularité
@app.route('/history/api/data')
def get_history_data():
    start = request.args.get('start', (datetime.now() - timedelta(hours=6)).isoformat())
    end = request.args.get('end', datetime.now().isoformat())
    granularity = request.args.get('granularity', 'minute')
    metrics = request.args.getlist('metrics')
    
    return history_service.get_data(start, end, granularity, metrics)

# /history/api/aggregates - Statistiques agrégées  
@app.route('/history/api/aggregates')
def get_aggregates():
    period_hours = int(request.args.get('period_hours', 6))
    return history_service.get_aggregates(period_hours)

# /history/api/latest - Derniers enregistrements
@app.route('/history/api/latest')
def get_latest():
    limit = int(request.args.get('limit', 10))
    return history_service.get_latest(limit)
```

### Frontend : Chart.js Offline-First

```javascript
// static/js/history.js - Le cœur du dashboard
function initCharts() {
    const tempCtx = document.getElementById('tempChart').getContext('2d');
    tempChart = new Chart(tempCtx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Température',
                data: [],
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        displayFormats: {
                            minute: 'HH:mm'
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: true
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            }
        }
    });
}
```

### Le Filtre Temporel Interactif

```javascript
// Filtrage sans rechargement de page
function applyFilters() {
    const start = document.getElementById('start-time').value;
    const end = document.getElementById('end-time').value;
    const granularity = document.getElementById('granularity').value;
    
    const params = new URLSearchParams({
        start: start,
        end: end,
        granularity: granularity
    });
    
    // Ajout des métriques sélectionnées
    document.querySelectorAll('input[name="metrics"]:checked').forEach(checkbox => {
        params.append('metrics', checkbox.value);
    });
    
    fetch(`/history/api/data?${params}`)
        .then(response => response.json())
        .then(data => updateCharts(data));
}
```

### Le Mode Démo Automatique

Si PostgreSQL n'est pas disponible, le frontend bascule automatiquement en mode démo :

```javascript
function checkServiceAvailability() {
    fetch('/history/api/latest?limit=1')
        .then(response => {
            if (!response.ok) {
                showDemoBanner();
                loadMockData();
            }
        })
        .catch(() => {
            showDemoBanner();
            loadMockData();
        });
}

function showDemoBanner() {
    const banner = document.getElementById('demo-banner');
    if (banner) {
        banner.style.display = 'block';
        banner.innerHTML = `
            <div class="alert alert-warning">
                <strong>Mode Démo</strong> : Service d'historique indisponible. 
                Données simulées affichées.
            </div>
        `;
    }
}
```

## Les Pièges : Ce Qui Fait Échouer le Monitoring

### ❌ La Fausse Bonne Idée du Stockage Infini

```python
# NE SURTOUT PAS FAIRE :
def record_state_forever():
    # Stockage sans limite = explosion des coûts
    db.execute("INSERT INTO state_history (...) VALUES (...)")
```

### ✅ La Rétention Intelligente

```python
# LA BONNE PRATIQUE :
def cleanup_old_records(self):
    # Nettoyage après 6 heures = aligné PITR Neon
    cutoff = datetime.now() - timedelta(hours=self.retention_hours)
    self._pool.execute(
        "DELETE FROM state_history WHERE timestamp < %s",
        (cutoff,)
    )
```

### ❌ La Dépendance CDN qui Tue l'Offline

```html
<!-- NE SURTOUT PAS FAIRE :
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
-->
```

### ✅ Le Vendor Local

```html
<!-- LA BONNE PRATIQUE :
<script src="{{ url_for('static', filename='vendor/chart.min.js') }}"></script>
-->
```

### ❌ Le Requêtage Sans Index

```sql
-- CATASTROPHE EN PRODUCTION :
SELECT * FROM state_history 
WHERE timestamp BETWEEN '2026-01-14' AND '2026-01-15'
ORDER BY timestamp;
-- Full table scan garanti !
```

### ✅ Les Index Temporels

```sql
-- PERFORMANCE GARANTIE :
CREATE INDEX idx_state_history_timestamp ON state_history(timestamp);
CREATE INDEX idx_state_history_date_bucket ON state_history(date_bucket(timestamp));
```

### ❌ L'Anti-Pattern du Frontend Lourd

```javascript
// GROSSE ERREUR :
setInterval(() => {
    fetch('/history/api/data').then(updateCharts);
}, 1000); // Trop fréquent = timeout
```

### ✅ Le Refresh Intelligent

```javascript
// BONNE PRATIQUE :
let refreshInterval;
function startRealTimeUpdates() {
    refreshInterval = setInterval(() => {
        if (document.visibilityState === 'visible') {
            fetch('/history/api/latest').then(updateLatestOnly);
        }
    }, 30000); // 30 secondes = raisonnable
}
```

### ❌ Oublier le Fallback JSON

Quand PostgreSQL est down, tout le dashboard devient inutilisable.

### ✅ La Bascule Automatique

```python
# Dans __init__.py
if isinstance(settings_store, PostgresStore):
    # Mode PostgreSQL complet
    setup_history_service()
else:
    # Mode JSON avec bannière démo
    app.logger.warning("[history] PostgreSQL indisponible, mode démo activé")
```

### ❌ Stockage Infini / ✅ Rétention Intelligente

❌ **Stockage infini** : Table PostgreSQL qui grandit indéfiniment, performances dégradées, coûts explosifs, backup impossibles. Après 6 mois, votre dashboard devient inutilisable.

✅ **Rétention intelligente** : Cleanup automatique après 6 heures, agrégations préservées, performances constantes, PITR Neon efficace. Vous gardez l'essentiel sans la surcharge.

### Tableau Comparatif des Approches de Stockage

| Approche | Coût | Performance | Maintenance | Utilité |
|----------|------|-------------|-------------|---------|
| **Stockage infini** | Élevé | Dégradée | Élevée | Faible |
| **Rétention 6h** | Gratuit | Constante | Automatique | Élevée |
| **Agrégations seules** | Faible | Optimale | Moyenne | Moyenne |

## La Règle d'Or : Snapshots Légers, Visualisations Riches

Enregistrez le minimum nécessaire à chaque tick, mais offrez le maximum en visualisation. Chaque snapshot doit être léger (quelques octets) mais les agrégations peuvent être riches (moyennes, tendances, corrélations).

---

## Références Techniques

### Configuration JSON

```json
// config/settings.json - Pas de variables spécifiques monitoring
{
  "automation": {
    "poll_interval_seconds": 60,
    "history_retention_hours": 6
  }
}
```

### Scripts SQL

```bash
# Migration manuelle (optionnelle)
psql $POSTGRES_URL -f scripts/create_history_table.sql
```

### Tests Automatisés

```bash
# Validation du service
python -m pytest tests/test_history_service.py -v

# Couverture complète
python -m pytest --cov=switchbot_dashboard.history_service tests/
```

### Health Check

```bash
# Vérification service disponible
curl http://localhost:5000/history/api/latest

# État global PostgreSQL  
curl http://localhost:5000/healthz
```

---

*Guide appliquant les standards [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) et les décisions architecturales de `memory-bank/`.*
