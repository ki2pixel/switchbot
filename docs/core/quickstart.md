# SwitchBot Dashboard v2 - Démarrage Rapide

**TL;DR** : Clonez, configurez `.env` avec vos tokens SwitchBot, installez les dépendances et lancez `python app.py`. PostgreSQL recommandé mais filesystem fonctionne pour le développement.

---

## Le Problème : Pourquoi Vous en Avez Besoin

Vous gérez des appareils SwitchBot à travers les saisons. Votre climatiseur fonctionne trop longtemps, les températures fluctuent de manière imprévisible, et le contrôle manuel devient fastidieux. Vous avez besoin d'une automatisation qui respecte vos horaires, gère les problèmes réseau avec élégance, et n'épuise pas votre quota API.

Le SwitchBot Dashboard résout ce problème avec une automatisation basée sur des scènes, un suivi des quotas, et une cascade de fallback robuste qui garantit que vos appareils répondent même lorsque la méthode principale échoue.

## La Solution : Aperçu de l'Architecture

Le dashboard implémente une cascade d'automatisation à trois niveaux :

1. **Webhooks IFTTT** (zéro consommation de quota) - Déclencheur d'automatisation primaire
2. **Scènes SwitchBot** (basées API) - Fallback fiable avec configurations prédéfinies  
3. **Commandes Directes** (au niveau device) - Dernier recours quand les scènes échouent

Cette cascade s'exécute sur un scheduler qui respecte les fenêtres horaires, implémente des commandes OFF idempotentes, et traite chaque appel API contre votre quota quotidien. Le système stocke l'état dans PostgreSQL (recommandé) avec fallback filesystem pour la résilience.

## Implémentation : Configuration et Mise en Place

### Prérequis

- **Python 3.8+** - Environnement d'exécution
- **SwitchBot Cloud Service** - Compte actif avec appareils configurés
- **Token API v1.1** - Identifiants développeur SwitchBot valides
- **PostgreSQL** - Neon recommandé (free tier suffisant)

### Configuration de l'Environnement

### ❌ Installation Manuelle / ✅ Setup Automatisé

❌ **Approche manuelle** : Installation dépend par dépendance, configuration `.env` oubliée, erreurs de Python version, conflits venv. Vous passez 30 minutes à déboguer pourquoi `pip install` échoue.

✅ **Setup guidé** : Script unique qui vérifie les prérequis, crée le venv, installe les dépendances, configure `.env.example`, et valide l'installation avec `/healthz`. 5 minutes de A à Z.

```bash
# Clone et préparation
git clone https://github.com/votre-utilisateur/switchbot-dashboard.git
cd switchbot-dashboard
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration Critique

Copiez le modèle d'environnement et configurez vos identifiants :

```bash
cp .env.example .env
```

Éditez `.env` avec ces variables essentielles :

```bash
# Obligatoire : Identifiants API SwitchBot
SWITCHBOT_TOKEN=votre_token_ici
SWITCHBOT_SECRET=votre_secret_ici

# Recommandé : Backend PostgreSQL (fallback filesystem disponible)
STORE_BACKEND=postgres
POSTGRES_URL=votre_url_neon

# Réglages performance
SWITCHBOT_POLL_INTERVAL_SECONDS=60
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10

# Sécurité (obligatoire en production)
FLASK_SECRET_KEY=change_me
LOG_LEVEL=info
```

**Note de sécurité** : Ne commitez jamais `.env` dans le version control. Les tokens ne sont jamais stockés dans les fichiers de configuration JSON.

### Tableau Comparatif des Environnements

| Environnement | Backend | Avantages | Inconvénients |
|---------------|---------|-----------|---------------|
| **Développement local** | JSON fichiers | Zero config, immédiat | Pas de persistance entre redeploys |
| **Développement avancé** | PostgreSQL Neon | Persistance, monitoring | Configuration URL requise |
| **Production** | PostgreSQL Neon | Backup automatique, PITR 6h | Dépendance externe |

### Configuration des Appareils

Configurez vos appareils via l'interface web à `http://127.0.0.1:5000/settings` ou éditez directement `config/settings.json` :

```json
{
  "devices": {
    "meter_device_id": "VOTRE_ID_DEVICE_METRE",
    "aircon_device_id": "VOTRE_ID_DEVICE_CLIMATISEUR"
  },
  "ifttt_webhooks": {
    "winter": "https://maker.ifttt.com/trigger/switchbot_winter/with/key/VOTRE_CLE",
    "summer": "https://maker.ifttt.com/trigger/switchbot_summer/with/key/VOTRE_CLE",
    "fan": "https://maker.ifttt.com/trigger/switchbot_fan/with/key/VOTRE_CLE",
    "off": "https://maker.ifttt.com/trigger/switchbot_off/with/key/VOTRE_CLE"
  },
  "aircon_scenes": {
    "winter": "1234567890abcdef1234567890abcdef",
    "summer": "abcdef1234567890abcdef1234567890",
    "fan": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
    "off": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
  }
}
```

### Lancement de l'Application

```bash
python app.py
```

Accédez au dashboard à `http://127.0.0.1:5000/`

### Checklist de Vérification

- Le serveur démarre sans erreurs
- L'interface charge à `http://127.0.0.1:5000/`
- Les logs du scheduler montrent les entrées `[scheduler]`
- La suite de tests passe : `python -m pytest`
- L'endpoint de santé répond : `curl http://127.0.0.1:5000/healthz`

## Pièges Courants et Solutions

### Problèmes d'Installation

**Problème** : `ImportError` ou dépendances manquantes
**Solution** : Assurez-vous que l'environnement virtuel est activé et les dépendances installées
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Échecs d'Authentification

**Problème** : Erreurs de token invalide ou échecs d'authentification API
**Solution** : Vérifiez que les identifiants SwitchBot dans `.env` correspondent à votre compte développeur
```bash
# Testez vos tokens
curl -H "Authorization: VOTRE_TOKEN" https://api.switchbot.jp/v1.0/devices
```

### Problèmes de Connexion Base de Données

**Problème** : Échecs de connexion PostgreSQL
**Solution** : Soit configurez `POSTGRES_URL` correctement, soit utilisez le fallback filesystem :
```bash
# Fallback pour développement
STORE_BACKEND=filesystem
```

### Épuisement du Quota API

**Problème** : Quota API quotidien épuisé prématurément
**Solution** : Implémentez les webhooks IFTTT comme déclencheurs primaires (zéro consommation de quota) et surveillez l'utilisation via la bannière de quota du dashboard.

### Scheduler Non Démarré

**Problème** : L'automatisation ne se déclenche pas
**Solution** : Vérifiez les logs pour les entrées `[scheduler]` et confirmez `SCHEDULER_ENABLED=true` (par défaut). Le scheduler évite automatiquement de s'exécuter sous le reloader Flask.

### Incohérences de Fuseau Horaire

**Problème** : L'automatisation se déclenche aux mauvais moments
**Solution** : Configurez votre fuseau horaire dans les paramètres. Le système utilise le format IANA avec Europe/Paris par défaut.

## Déploiement en Production

Pour le déploiement en production, assurez-vous de ces mesures de sécurité :

```bash
# Paramètres obligatoires en production
FLASK_SECRET_KEY=generez_secret_robuste_ici
STORE_BACKEND=postgres
POSTGRES_URL=votre_url_neon_production
LOG_LEVEL=warning
```

Utilisez Gunicorn pour le service en production :

```bash
gunicorn -c gunicorn.conf.py app:app
```

Surveillez la santé via l'endpoint `/healthz` et configurez des alertes pour la consommation de quota.

## La Règle d'Or : Validez /healthz Avant de Considérer le Déploiement Réussi

Toujours tester l'endpoint `/healthz` après chaque déploiement ou changement de configuration - c'est votre canari dans la mine pour détecter les problèmes avant que les utilisateurs ne les remarquent.

## Prochaines Étapes

Une fois en fonctionnement :

1. **Configurez les fenêtres horaires** dans l'interface des paramètres pour les périodes de contrôle automatisé
2. **Testez la cascade** en déclenchant les webhooks IFTTT et en vérifiant le comportement de fallback
3. **Surveillez les quotas** via le suivi temps réel du dashboard
4. **Consultez l'historique** via le dashboard de monitoring Chart.js
5. **Personnalisez les thèmes** si le glassmorphism sombre par défaut nécessite des ajustements

---

Le dashboard privilégie la fiabilité plutôt que les fonctionnalités. Chaque automatisation inclut des sauvegardes idempotentes, un suivi des quotas, et une dégradation élégante. Quand la méthode principale échoue, le système bascule automatiquement vers la prochaine option fiable sans intervention manuelle.
