# Tableau de bord SwitchBot

Tableau de bord de surveillance et d'automatisation pour les appareils SwitchBot, spécialement conçu pour la gestion des climatiseurs et capteurs de température avec une approche orientée scènes.

## 🚀 Fonctionnalités clés

### Automatisation intelligente
- **Gestion des scènes** : Exécution de scènes SwitchBot préconfigurées
- **Profils saisonniers** : Paramètres distincts pour l'hiver et l'été
- **Fenêtres horaires** : Planification précise des plages d'activation
- **Détection de présence** : Basée sur les plages horaires configurées

### Surveillance et contrôle
- **Tableau de bord temps réel** : Vue d'ensemble de l'état du système
- **Gestion des quotas API** : Suivi et alertes de consommation
- **Indicateur de fraîcheur** : Détection des données de température obsolètes
- **Journalisation complète** : Historique des actions et erreurs

### Architecture moderne
- **Injection de dépendances** : Services modulaires et testables
- **Multi-backend de stockage** : Redis ou système de fichiers
- **Estimation locale des quotas** : Même sans en-têtes de taux
- **Gestion robuste des erreurs** : Repli élégant en cas d'indisponibilité

## ⚙️ Prérequis

- **Python** : 3.8 ou supérieur
- **Compte SwitchBot** : Avec appareils configurés
- **Token d'API** : Jeton d'API SwitchBot valide
- **Stockage** : Redis recommandé pour la production

## 🛠 Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/switchbot-dashboard.git
   cd switchbot-dashboard
   ```

2. **Configurer l'environnement** :
   ```bash
   cp .env.example .env
   # Éditer .env avec vos identifiants SwitchBot
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application** :
   ```bash
   python app.py
   ```

## 🏗 Architecture

### Composants principaux

- **`AutomationService`** : Cœur de l'automatisation, gère la logique métier
- **`SwitchBotClient`** : Client API avec suivi des quotas intégré
- **`BaseStore`** : Interface de stockage abstraite
  - `RedisJsonStore` : Stockage Redis haute performance
  - `JsonStore` : Stockage basé sur des fichiers JSON
- **`ApiQuotaTracker`** : Suivi précis des quotas d'API

### Flux de données

1. **Collecte** : Récupération des données des capteurs via `poll_meter()`
2. **Analyse** : Vérification des seuils et des fenêtres horaires
3. **Action** : Exécution des scènes SwitchBot appropriées
4. **Persistance** : Sauvegarde de l'état et des paramètres

## 📚 Documentation complète

- [Guide d'installation](setup.md) - Configuration détaillée
- [Guide de l'utilisateur](ui-guide.md) - Utilisation de l'interface
- [Référence de configuration](configuration.md) - Options avancées
- [Intégration IFTTT](ifttt-integration.md) - Configuration des webhooks IFTTT
- [Guide de déploiement](deployment.md) - Mise en production

## 🚦 Statut du projet

### Fonctionnalités implémentées

- [x] Support des scènes SwitchBot
- [x] Gestion des quotas API
- [x] Stockage Redis et système de fichiers
- [x] Interface utilisateur réactive
- [x] Documentation complète

### Prochaines étapes

- [ ] Support multi-utilisateurs
- [ ] Tableau de bord d'administration
- [ ] Notifications push
- [ ] Intégration avec d'autres écosystèmes domotiques

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une [issue](https://github.com/votre-utilisateur/switchbot-dashboard/issues).

## 🙏 Remerciements

- À l'équipe SwitchBot pour leur API
- Aux contributeurs du projet
- À la communauté open source

---

*Dernière mise à jour : 10 janvier 2025*

## 🔍 Aperçu technique

### Gestion des scènes

Le tableau de bord utilise les scènes SwitchBot pour une configuration flexible. Voici un exemple de configuration :

```python
# Exemple de configuration de scène
{
  "winter_scene": "1234567890abcdef1234567890abcdef",
  "summer_scene": "abcdef1234567890abcdef1234567890",
  "fan_scene": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
  "off_scene": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
}
```

### Surveillance de la santé

L'application expose un endpoint de monitoring à `/healthz` qui fournit des informations détaillées sur l'état du système, y compris les indicateurs de fraîcheur des données et l'utilisation de l'API.

## 🚀 Démarrage rapide

### Prérequis
- **Python** : 3.8 ou supérieur
- **Compte SwitchBot** : Avec appareils configurés
- **Token d'API** : Jeton d'API SwitchBot valide
- **Stockage** : Redis recommandé pour la production

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
