# Guide UI et Navigation - SwitchBot Dashboard

**TL;DR** : Le tableau de bord propose une interface mobile-first avec navigation basse intuitive, thème sombre immersif, et six pages principales organisées pour une utilisation quotidienne efficace.

## Le Problème : Pourquoi une nouvelle approche UI ?

Vous utilisez votre SwitchBot quotidiennement, mais l'interface existante vous force à naviguer entre plusieurs écrans, stretch votre pouce pour atteindre les boutons critiques, et perd des informations importantes dans le fouillis visuel. Sur mobile, chaque action supplémentaire coûte précieux temps et attention.

Les tableaux de bord traditionnels conçus pour desktop transposent mal sur mobile : les boutons d'action sont placés en haut, les informations critiques sont dispersées, et la navigation nécessite souvent deux mains pour être efficace.

## La Solution : L'architecture mobile-first

Le SwitchBot Dashboard adopte une approche mobile-first centrée sur la **zone du pouce** (thumb zone) et une **navigation basse** intuitive. L'architecture repose sur six pages spécialisées avec une hiérarchie claire de l'information.

### Structure des pages

- **Page d'accueil (`/`)** : Vue d'ensemble avec statut temps réel et accès rapide
- **Page Réglages (`/reglages`)** : Configuration complète de l'automatisation
- **Page Actions (`/actions`)** : Six actions manuelles regroupées avec états visuels
- **Page Quota (`/quota`)** : Suivi détaillé de la consommation API
- **Page Historique (`/history`)** : Dashboard Chart.js temps réel
- **Page Appareils (`/devices`)** : Inventaire et configuration des équipements

## L'Implémentation : Le code et la configuration

### Variables d'environnement essentielles

```bash
# Configuration principale
SWITCHBOT_TOKEN=votre_token_api
SWITCHBOT_SECRET=votre_secret_api

# Base de données (PostgreSQL prioritaire)
DATABASE_URL=postgresql://user:pass@localhost:5432/switchbot
JSON_STORE_PATH=config/state.json

# Fuseau horaire pour les fenêtres horaires
TZ=Europe/Paris
```

### Configuration JSON (`config/settings.json`)

```json
{
  "automation_enabled": true,
  "current_mode": "winter",
  "poll_interval_seconds": 300,
  "command_delay_seconds": 2,
  "timezone": "Europe/Paris",
  "aircon_device_id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  "meter_device_id": "YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY",
  "ifttt_webhooks": {
    "winter_on": "https://maker.ifttt.com/trigger/winter_on/with/key/...",
    "summer_on": "https://maker.ifttt.com/trigger/summer_on/with/key/...",
    "fan_on": "https://maker.ifttt.com/trigger/fan_on/with/key/...",
    "off": "https://maker.ifttt.com/trigger/off/with/key/..."
  },
  "scenes": {
    "winter": "UUID_SCENE_WINTER",
    "summer": "UUID_SCENE_SUMMER", 
    "fan": "UUID_SCENE_FAN",
    "off": "UUID_SCENE_OFF"
  },
  "api_quota_warning_threshold": 250,
  "hysteresis_celsius": 0.5,
  "off_repeat_count": 2,
  "off_repeat_interval_seconds": 10
}
```

### Navigation basse - Structure HTML

```html
<!-- Bottom navigation (mobile-first) -->
<nav class="bottom-nav" role="navigation" aria-label="Navigation principale">
  <a href="/" class="nav-item active" aria-current="page">
    <i class="fas fa-home"></i>
    <span>Accueil</span>
  </a>
  <a href="/actions" class="nav-item">
    <i class="fas fa-bolt"></i>
    <span>Actions</span>
  </a>
  <a href="/reglages" class="nav-item">
    <i class="fas fa-cog"></i>
    <span>Réglages</span>
  </a>
  <a href="/devices" class="nav-item">
    <i class="fas fa-tv"></i>
    <span>Appareils</span>
  </a>
  <a href="/history" class="nav-item">
    <i class="fas fa-chart-line"></i>
    <span>Historique</span>
  </a>
  <a href="/quota" class="nav-item">
    <i class="fas fa-chart-pie"></i>
    <span>Quota</span>
  </a>
</nav>
```

### CSS Glassmorphism - Tokens de design

```css
:root {
  /* Tokens glassmorphism */
  --sb-glass-bg: rgba(255, 255, 255, 0.05);
  --sb-glass-border: rgba(255, 255, 255, 0.1);
  --sb-glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  --sb-glass-bg-hover: rgba(255, 255, 255, 0.08);
  --sb-glass-border-hover: rgba(255, 255, 255, 0.15);
  
  /* Espacements mobile-first */
  --sb-spacing-xs: 0.25rem;
  --sb-spacing-sm: 0.5rem;
  --sb-spacing-md: 1rem;
  --sb-spacing-lg: 1.5rem;
  --sb-spacing-xl: 2rem;
  
  /* Breakpoints */
  --sb-breakpoint-sm: 576px;
  --sb-breakpoint-md: 768px;
  --sb-breakpoint-lg: 992px;
}

.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: var(--sb-glass-bg);
  backdrop-filter: blur(20px);
  border-top: 1px solid var(--sb-glass-border);
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 1000;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem;
  min-width: 44px;
  min-height: 44px;
  color: var(--sb-text-secondary);
  text-decoration: none;
  transition: all 0.2s ease;
}

.nav-item.active {
  color: var(--sb-primary);
}
```

### Actions manuelles avec états visuels

```python
# routes.py - Construction du contexte actions
@app.route('/actions')
def actions_page():
    settings = current_app.extensions['settings_store'].load()
    state = current_app.extensions['state_store'].load()
    
    actions_context = {}
    for action in ['winter_on', 'summer_on', 'fan_on', 'off']:
        webhook_url = settings.get('ifttt_webhooks', {}).get(action, '')
        scene_uuid = settings.get('scenes', {}).get(action.replace('_on', ''), '')
        
        if webhook_url and webhook_url.startswith('https://'):
            status = 'webhook'
            badge = 'badge-success'
            text = 'Webhook configuré'
        elif scene_uuid:
            status = 'scene'
            badge = 'badge-warning'
            text = 'Scène uniquement'
        else:
            status = 'missing'
            badge = 'badge-danger'
            text = 'Configuration manquante'
            
        actions_context[action] = {
            'status': status,
            'badge': badge,
            'text': text
        }
    
    return render_template('actions.html', 
                         actions_context=actions_context,
                         settings=settings, 
                         state=state)
```

### Alertes quota avec monitoring temps réel

```python
# api_quota_tracker.py - Suivi des quotas API
class ApiQuotaTracker:
    def __init__(self, settings_store):
        self.settings_store = settings_store
        self.state_store = current_app.extensions['state_store']
    
    def update_quota(self, response_headers):
        """Met à jour le quota depuis les headers API"""
        remaining = int(response_headers.get('X-Rate-Limit-Remaining', 0))
        limit = int(response_headers.get('X-Rate-Limit-Limit', 10000))
        
        state = self.state_store.load()
        state['api_requests_remaining'] = remaining
        state['api_requests_limit'] = limit
        state['api_quota_day'] = datetime.utcnow().strftime('%Y-%m-%d')
        
        self.state_store.save(state)
        
        # Vérification du seuil d'alerte
        settings = self.settings_store.load()
        threshold = settings.get('api_quota_warning_threshold', 250)
        
        if remaining <= threshold:
            self._trigger_quota_alert(remaining, limit)
    
    def _trigger_quota_alert(self, remaining, limit):
        """Déclenche une alerte quota"""
        percentage = (remaining / limit) * 100
        alert_level = 'danger' if percentage < 5 else 'warning'
        
        flash(f'⚠️ Quota API faible : {remaining}/{limit} requêtes restantes', 
              alert_level)
```

### Optimisations mobile - CSS responsive

```css
/* Thumb zone optimization */
@media (max-width: 768px) {
  .scene-actions-wrapper {
    position: sticky;
    bottom: 1rem;
    background: var(--sb-glass-bg);
    backdrop-filter: blur(20px);
    border-radius: 1.25rem;
    padding: 1rem;
    margin: 1rem -1rem -1rem;
    box-shadow: var(--sb-glass-shadow);
  }
  
  .scene-action {
    min-height: 56px;
    padding: 1rem;
  }
}

/* Status grid mobile fix */
@media (max-width: 480px) {
  .status-grid {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }
  .status-item {
    padding: 1rem;
  }
}

/* Chart.js responsive */
@media (max-width: 576px) {
  .chart-container { 
    height: 250px;
    margin-bottom: 1rem;
  }
}
```

## Les Pièges : Éviter les erreurs courantes

### ❌ Ne pas négliger la zone du pouce

Placer les boutons d'action critiques en haut de l'écran sur mobile force l'utilisateur à étirer son pouce, créant une friction importante.

```css
/* ❌ Éviter : boutons en haut sur mobile */
.header-actions {
  position: fixed;
  top: 0; /* Inaccessible au pouce */
}

/* ✅ Préférer : zone basse accessible */
.bottom-actions {
  position: sticky;
  bottom: 1rem; /* Zone naturelle du pouce */
}
```

### ❌ Ignorer les états visuels des actions

Ne pas montrer si une action utilisera un webhook IFTTT, une scène SwitchBot, ou une commande directe crée de l'incertité pour l'utilisateur.

```python
# ❌ Éviter : bouton sans contexte
<button onclick="execute_action('winter_on')">Hiver</button>

# ✅ Préférer : bouton avec état visuel
<div class="action-card">
  <span class="badge badge-success">Webhook configuré</span>
  <button data-loader="card" onclick="execute_action('winter_on')">
    <i class="fas fa-snowflake"></i> Hiver
  </button>
</div>
```

### ❌ Oublier l'accessibilité

Les attributs ARIA et les contrastes WCAG sont obligatoires pour une interface professionnelle.

```html
<!-- ❌ Éviter : navigation sans accessibilité -->
<nav>
  <a href="/">Accueil</a>
  <a href="/actions">Actions</a>
</nav>

<!-- ✅ Préférer : navigation accessible -->
<nav role="navigation" aria-label="Navigation principale">
  <a href="/" class="nav-item active" aria-current="page">
    <i class="fas fa-home" aria-hidden="true"></i>
    <span>Accueil</span>
  </a>
</nav>
```

### ❌ Négliger les performances mobile

Les animations CSS doivent être GPU-optimisées pour éviter la latence sur mobile.

```css
/* ❌ Éviter : animations non optimisées */
.card {
  transition: left 0.3s ease; /* Reflow coûteux */
}

/* ✅ Préférer : animations GPU */
.card {
  transform: translateZ(0);
  will-change: transform;
  transition: transform 0.3s ease; /* GPU-acceléré */
}
```

### ❌ Configurer les webhooks HTTP

Les webhooks IFTTT doivent impérativement utiliser HTTPS pour la sécurité.

```json
// ❌ Éviter : webhook HTTP non sécurisé
{
  "ifttt_webhooks": {
    "winter_on": "http://maker.ifttt.com/trigger/..."
  }
}

// ✅ Préférer : webhook HTTPS sécurisé
{
  "ifttt_webhooks": {
    "winter_on": "https://maker.ifttt.com/trigger/..."
  }
}
```

## Monitoring et maintenance

### Scripts SQL pour la maintenance

```sql
-- Nettoyage des entrées historique (>6h)
DELETE FROM history 
WHERE created_at < NOW() - INTERVAL '6 hours'
AND meter_temperature IS NOT NULL;

-- Vérification des quotas par jour
SELECT 
  DATE(created_at) as day,
  COUNT(*) as api_calls,
  MIN(api_requests_remaining) as min_remaining
FROM history 
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY DATE(created_at)
ORDER BY day DESC;
```

### Commandes Python pour le débogage

```python
# Vérification de l'état courant
python -c "
from switchbot_dashboard import create_app
app = create_app()
with app.app_context():
    settings = app.extensions['settings_store'].load()
    state = app.extensions['state_store'].load()
    print('API remaining:', state.get('api_requests_remaining', 'Unknown'))
    print('Automation enabled:', settings.get('automation_enabled', False))
"

# Test des webhooks IFTTT
curl -X POST "https://maker.ifttt.com/trigger/winter_on/with/key/VOTRE_KEY" \
     -H "Content-Type: application/json" \
     -d '{"value1":"Test depuis dashboard"}'
```

### Surveillance des performances

```javascript
// Monitoring Core Web Vitals
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.entryType === 'largest-contentful-paint') {
      console.log('LCP:', entry.startTime);
    }
    if (entry.entryType === 'first-input') {
      console.log('FID:', entry.processingStart - entry.startTime);
    }
    if (entry.entryType === 'layout-shift') {
      console.log('CLS:', entry.value);
    }
  }
});

observer.observe({entryTypes: ['largest-contentful-paint', 'first-input', 'layout-shift']});
```

### ❌ Desktop-First / ✅ Mobile-First

❌ **Desktop-first** : Interface conçue pour grand écran, puis adaptée pour mobile. Résultat : navigation complexe sur petit écran, boutons trop petits, scroll horizontal, expérience frustrante.

✅ **Mobile-first** : Interface conçue pour mobile d'abord, puis enrichie pour desktop. Résultat : navigation intuitive partout, composants adaptatifs, performance optimale sur tous les appareils.

### Tableau Comparatif des Approches UI

| Approche | Accessibilité | Performance | Maintenance | Utilisateurs |
|----------|---------------|--------------|-------------|-------------|
| **Desktop-first** | Moyenne | Moyenne | Élevée | Desktop majoritairement |
| **Mobile-first** | Élevée | Élevée | Moyenne | Tous appareils |
| **Responsive only** | Faible | Faible | Faible | Fragmenté |

## La Règle d'Or : Mobile-First, Accessibilité Maximale

Concevez d'abord pour l'écran le plus contraignant, puis enrichissez pour les écrans plus grands. Cette approche garantit une expérience optimale pour tous les utilisateurs, quel que soit leur appareil.

---

Cette architecture UI mobile-first garantit une expérience utilisateur optimale sur tous les appareils, avec une navigation intuitive, des performances de pointe, et une maintenance simplifiée. Le design system cohérent et les patterns glassmorphism assurent une interface moderne et professionnelle.
