# Tableau de bord SwitchBot

Tableau de bord Flask pour la gestion des appareils SwitchBot avec automatisation intelligente et surveillance du quota API.

## 📚 Documentation

- **[Installation et Démarrage](setup.md)** - Prérequis, installation, configuration initiale
- **[Guide de Configuration](configuration.md)** - Paramètres, scènes SwitchBot, seuils d'alerte
- **[Guide Utilisateur](ui-guide.md)** - Interface, gestion du quota, configuration des scènes
- **[Déploiement](deployment.md)** - Docker, CI/CD, surveillance avec l'endpoint `/healthz`
- **[Tests](testing.md)** - Scénarios de test, validation des fonctionnalités
- **[Thème](theming.md)** - Personnalisation de l'interface utilisateur

## 🎯 Objectif

Dashboard Flask local qui orchestre la lecture de capteurs SwitchBot et pilote un climatiseur IR virtuel avec résilience locale.

### Fonctionnalités clés

- **Automatisation intelligente** : Contrôle basé sur des scènes SwitchBot avec fallback sur les commandes bas niveau
- **Gestion du quota API** : Surveillance en temps réel avec alertes configurables
- **Scènes personnalisables** : Configuration facile des scènes hiver/été/ventilation/arrêt
- **Surveillance de santé** : Endpoint `/healthz` pour le monitoring
- **Interface utilisateur moderne** : Thème sombre, responsive et accessible
- **Inventaire des appareils** : Page `/devices` avec gestion des IDs et métadonnées
- **Sécurité renforcée** : Gestion sécurisée des tokens et validation des entrées
- **Haute disponibilité** : Résilience aux pannes, reprise sur erreur, basculement automatique

## 🏗️ Architecture

- **`app.py`** : Point d'entrée de l'application Flask
- **`switchbot_dashboard/`** : 
  - `routes.py` : Gestion des routes et requêtes HTTP
  - `automation.py` : Service d'automatisation avec gestion des scènes
  - `quota.py` : Suivi et gestion du quota API
  - `aircon.py` : Définition des scènes et commandes climatiseur
- **`config/`** : 
  - `settings.json` : Configuration utilisateur (scènes, seuils, etc.)
  - `state.json` : État de l'application et télémétrie
- **`static/`** : 
  - `css/theme.css` : Thème sombre et styles partagés
  - `js/` : Scripts côté client
- **`templates/`** : Vues Jinja2 pour l'interface utilisateur
- **`docs/`** : Documentation complète du projet

## 🚀 Démarrage rapide

### Prérequis
- Python 3.8+
- Compte SwitchBot avec token API valide
- (Optionnel) Redis pour la persistance des données

### Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/switchbot-dashboard.git
cd switchbot-dashboard

# 2. Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer l'application
cp .env.example .env
# Éditer .env avec vos tokens SwitchBot et paramètres

# 5. Démarrer l'application
python app.py

# L'application est disponible à l'adresse : http://127.0.0.1:5000/
```

### Démarrage avec Docker

```bash
# Construire l'image
docker build -t switchbot-dashboard .

# Démarrer le conteneur
docker run -d -p 8000:8000 --env-file .env --name switchbot switchbot-dashboard
```

## 📊 Monitoring et surveillance

L'application expose un endpoint de santé pour le monitoring :

```
GET /healthz
```

**Réponse exemple :**
```json
{
  "status": "ok",
  "scheduler_running": true,
  "automation_enabled": true,
  "last_tick": "2024-01-10T14:30:00Z",
  "api_requests_total": 42,
  "api_requests_remaining": 958,
  "api_quota_day": "2024-01-10",
  "version": "1.0.0"
}
```

## 🔧 Configuration avancée

### Variables d'environnement

| Variable | Description | Valeur par défaut |
|----------|-------------|-------------------|
| `SWITCHBOT_TOKEN` | Token d'API SwitchBot (requis) | - |
| `SWITCHBOT_SECRET` | Clé secrète SwitchBot (requis) | - |
| `SWITCHBOT_POLL_INTERVAL_SECONDS` | Intervalle de rafraîchissement (secondes) | 60 |
| `LOG_LEVEL` | Niveau de journalisation (DEBUG, INFO, WARNING, ERROR) | INFO |
| `STORE_BACKEND` | Backend de stockage (redis, filesystem) | filesystem |
| `REDIS_URL` | URL de connexion à Redis (si STORE_BACKEND=redis) | - |

## 📖 Références

- **API SwitchBot** : `docs/switchbot/README.md` (v1.1)
- **Documentation détaillée** : Consultez les guides dans le dossier `docs/`
- **Standards de développement** : `.windsurf/rules/codingstandards.md`

---

*Pour commencer, consultez le [Guide de configuration](configuration.md) et le [Guide utilisateur](ui-guide.md). Pour le déploiement en production, reportez-vous au [Guide de déploiement](deployment.md).*
