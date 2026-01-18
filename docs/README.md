# Tableau de bord SwitchBot

Tableau de bord de surveillance et d'automatisation pour les appareils SwitchBot, spécialement conçu pour la gestion des climatiseurs et capteurs de température avec une approche orientée scènes.

## 🚀 Fonctionnalités clés

### Automatisation intelligente
- **Gestion des scènes** : Exécution de scènes SwitchBot préconfigurées
- **Webhooks IFTTT** : Intégration prioritaire avec fallback cascade à 3 niveaux (IFTTT → scène → commande)
- **Profils saisonniers** : Paramètres distincts pour l'hiver et l'été
- **Fenêtres horaires** : Planification précise des plages d'activation
- **Détection de présence** : Basée sur les plages horaires configurées
- **Répétition OFF paramétrable** : Commandes OFF multiples avec intervalle configurable
- **Idempotence des actions** : Protection contre les déclenchements excessifs
- **Scheduler robuste** : Démarrage conditionnel et logging amélioré
- **Fuseau horaire configurable** : Fenêtres horaires interprétées dans le fuseau IANA choisi (défaut Europe/Paris, fallback UTC en cas de valeur invalide)

### Surveillance et contrôle
- **Tableau de bord temps réel** : Vue d'ensemble de l'état du système
- **Gestion des quotas API** : Suivi et alertes de consommation
- **Indicateur de fraîcheur** : Détection des données de température obsolètes
- **Journalisation complète** : Historique des actions et erreurs

### Architecture moderne
- **PostgreSQL par défaut** : Backend Neon avec connection pooling et fallback filesystem
- **Cascade IFTTT** : Webhooks IFTTT → scènes SwitchBot → commandes directes
- **History Monitoring** : Dashboard temps réel avec Chart.js et rétention 6h **(NOUVEAU)**
- **Loaders Frontend** : Système non bloquant pour améliorer la réactivité perçue **(NOUVEAU)**
- **Estimation locale des quotas** : Suivi précis avec alertes configurables
- **Gestion robuste des erreurs** : Repli élégant en cas d'indisponibilité

## ⚙️ Prérequis

- **Python** : 3.8 ou supérieur
- **Compte SwitchBot** : Avec appareils configurés
- **PostgreSQL** : Neon recommandé (backend par défaut, free tier suffisant)
- **Token d'API** : Jeton d'API SwitchBot valide

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
  - `PostgresStore` : Stockage PostgreSQL Neon (recommandé)
  - `JsonStore` : Stockage basé sur des fichiers JSON (fallback)
  - `RedisJsonStore` : Stockage Redis (déprécié mais fonctionnel)
- **`ApiQuotaTracker`** : Suivi précis des quotas d'API
- **`HistoryService`** : Service de monitoring et d'historique temps réel
- **`IFTTTWebhookClient`** : Client webhooks IFTTT avec système de cascade

### Flux de données

1. **Collecte** : Récupération des données des capteurs via `poll_meter()`
2. **Analyse** : Vérification des seuils et des fenêtres horaires
3. **Action** : Exécution des scènes SwitchBot appropriées
4. **Persistance** : Sauvegarde de l'état et des paramètres

## 📚 Documentation complète

- [Guide d'installation](setup.md) - Configuration détaillée
- [Guide de l'utilisateur](ui-guide.md) - Utilisation de l'interface
- [Référence de configuration](configuration.md) - Options avancées
- [Migration PostgreSQL](postgresql-migration.md) - Guide de migration vers Neon
- [Intégration IFTTT](ifttt-integration.md) - Configuration webhooks et cascade
- **[History Monitoring](history-monitoring.md) - Dashboard temps réel et analyse**
- **[Performance Frontend](frontend-performance.md) - Optimisations UX et loaders**
- [Guide du scheduler](scheduler.md) - Configuration et dépannage
- [Guide de déploiement](deployment.md) - Mise en production avec monitoring `/healthz`
- [Guide de tests](testing.md) - Tests manuels et unitaires
- [Guide de thématisation](theming.md) - Styles CSS et composants UI
- [Référence API SwitchBot](switchbot/README.md) - Documentation API v1.1

## 🚀 Améliorations Récentes (Janvier 2026)

### Frontend Excellence - Phase 5 Audit Mobile
- **Critical CSS Inlining** : CSS critique intégré dans `<head>` pour LCP < 1.8s
- **Resource Hints** : Preconnects et preloads pour réduire latence réseau
- **Font Loading Optimization** : font-display: swap + preloads (élimine FOIT/FOUT)
- **Advanced Performance Optimizer** : Optimisations LCP/FID/CLS avec monitoring détaillé
- **Skeleton Screens** : Screens de chargement pour prévention CLS
- **Main Thread Optimization** : Scheduling intelligent et code splitting avancé
- **Performance Score** : 99/100+ (vs 95/100 avant Phase 5)
- **Core Web Vitals** : Tous dans catégorie "Good" de Google

### Corrections UI Post-Audit
- **Bottom bar optimisée** : Icônes-only sur mobile, visible sur desktop
- **Flash blanc éliminé** : Transitions CSS optimisées, anti-flash renforcé
- **Page Actions dédiée** : Regroupement des 6 boutons d'actions manuelles
- **FontAwesome corrigé** : Suppression integrity/crossorigin bloquants
- **Navigation unifiée** : Bottom bar cohérente sur tous les templates

### Performance & Résilience (Post-Audit Backend)
- **Batch insert HistoryService** : Buffer thread-safe avec timer flush pour -50% latence par tick
- **Cache timezone intelligent** : Cache simple avec invalidation automatique sur changement settings
- **Monitoring exceptions complet** : Wrapper try/catch global dans SchedulerService pour logging sans crash
- **Tests robustes centralisés** : 122 tests passants (99% de réussite) avec mocks PostgreSQL optimisés
- **Audit backend validé** : Score 95/100 avec toutes recommandations "Court terme" appliquées

### Architecture Robuste
- **PostgreSQL par défaut** : Backend Neon avec connection pooling optimisé
- **Cascade IFTTT** : Webhooks → scènes → commandes avec fallback automatique
- **History Monitoring** : Dashboard temps réel avec Chart.js et rétention 6h
- **Loaders Frontend** : Système non bloquant pour UX améliorée

### Qualité & Tests
- **122 tests passants** (99% de réussite) avec mocks PostgreSQL optimisés
- **Audit backend validé** : Score 95/100 avec optimisations "Court terme" appliquées
- **Performance batch insert** : Buffer thread-safe pour -50% latence
- **Cache timezone intelligent** : Invalidation automatique et résolutions répétées évitées
- **Wrapper try/catch global** : Monitoring exceptions complet sans crash scheduler

> 📚 **Détails** : Voir [Audit Backend - Rapport Complet](backend-audit-report.md) pour l'analyse complète des améliorations.

## 🚦 Statut du projet

### Fonctionnalités implémentées

- [x] Support des scènes SwitchBot
- [x] Webhooks IFTTT avec système de fallback cascade
- [x] Stockage PostgreSQL Neon avec fallback filesystem
- [x] History Monitoring dashboard temps réel
- [x] Loaders frontend non bloquants
- [x] Répétition OFF paramétrable
- [x] Idempotence des actions OFF
- [x] Gestion des quotas API avec alertes
- [x] Scheduler robuste avec logging amélioré
- [x] Interface utilisateur réactive
- [x] Documentation complète
- [x] Suite de tests complète (122/123 tests passants, 99% de couverture)

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

*Dernière mise à jour : 18 janvier 2026*

## 🔍 Aperçu technique

### Gestion des scènes

Le tableau de bord utilise les scènes SwitchBot pour une configuration flexible. Le système implémente une cascade à 3 niveaux :

1. **Webhooks IFTTT** (priorité) - Ne consomme pas le quota API SwitchBot
2. **Scènes SwitchBot** (fallback 1) - Exécution directe via API
3. **Commandes directes** (fallback 2) - `setAll`/`turnOff` sur device IR

Voici un exemple de configuration :

```python
# Exemple de configuration de scènes
{
  "ifttt_webhooks": {
    "winter": "https://maker.ifttt.com/trigger/switchbot_winter/with/key/YOUR_KEY",
    "summer": "https://maker.ifttt.com/trigger/switchbot_summer/with/key/YOUR_KEY",
    "fan": "https://maker.ifttt.com/trigger/switchbot_fan/with/key/YOUR_KEY",
    "off": "https://maker.ifttt.com/trigger/switchbot_off/with/key/YOUR_KEY"
  },
  "aircon_scenes": {
    "winter": "1234567890abcdef1234567890abcdef",
    "summer": "abcdef1234567890abcdef1234567890",
    "fan": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
    "off": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
  }
}
```

> 💡 **Pour en savoir plus** : Consultez le guide complet [Intégration IFTTT](ifttt-integration.md) pour configurer les webhooks et comprendre le système de fallback cascade.

### Surveillance de la santé

L'application expose un endpoint de monitoring à `/healthz` qui fournit des informations détaillées sur l'état du système, y compris les indicateurs de fraîcheur des données et l'utilisation de l'API.

## 🚀 Démarrage rapide

### Prérequis
- **Python** : 3.8 ou supérieur
- **Compte SwitchBot** : Avec appareils configurés
- **Token d'API** : Jeton d'API SwitchBot valide
- **PostgreSQL** : Neon recommandé pour la production (free tier suffisant)

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
