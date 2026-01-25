# Installation et Démarrage

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Prérequis

- **Python** : 3.8 ou supérieur
- **Compte SwitchBot** : Avec appareils configurés et Cloud Service activé
- **Token d'API** : Jeton d'API SwitchBot valide (v1.1)
- **PostgreSQL** : Neon recommandé pour la production (free tier suffisant)

## Installation

Le projet utilise un environnement virtuel dédié. Pour un environnement local standard :

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/switchbot-dashboard.git
cd switchbot-dashboard

# 2. Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

> **Note** : Le projet dispose également d'un environnement virtuel préconfiguré dans `/mnt/venv_ext4/venv_switchbot`. Utilisez-le si vous travaillez sur l'environnement de développement partagé.

## Configuration initiale

1. **Copier le fichier d'exemple** :
   ```bash
   cp .env.example .env
   ```

2. **Configurer les identifiants SwitchBot** dans `.env` :
   ```bash
   SWITCHBOT_TOKEN=votre_token_ici
   SWITCHBOT_SECRET=votre_secret_ici
   ```

3. **Variables optionnelles recommandées** :
   ```bash
   # Retry en cas de réseau instable
   SWITCHBOT_RETRY_ATTEMPTS=2
   SWITCHBOT_RETRY_DELAY_SECONDS=10
   
   # Intervalle de polling (minimum 15 secondes)
   SWITCHBOT_POLL_INTERVAL_SECONDS=60
   
   # Niveau de log (DEBUG/INFO/WARNING/ERROR)
   LOG_LEVEL=info
   
   # Clé secrète Flask (obligatoire en production)
   FLASK_SECRET_KEY=change_me
   
   # Backend de stockage (postgres recommandé)
   STORE_BACKEND=postgres
   POSTGRES_URL=votre_url_neon
   ```

> ⚠️ **Sécurité** : Ne jamais commiter `.env`. Les tokens ne sont jamais stockés dans les fichiers JSON. Respect du principe du moindre privilège.

> 📝 **Décisions connexes** : Cette approche centralisée respecte les standards définis dans `memory-bank/decisionLog.md` (2026-01-09 16:21) et les patterns de stockage dans `.windsurf/rules/codingstandards.md`.

## Lancement

### Développement local
```bash
python app.py
```

### Avec l'environnement partagé
```bash
/mnt/venv_ext4/venv_switchbot/bin/python app.py
```

L'application est disponible à l'adresse : http://127.0.0.1:5000/

## Vérification post-installation

1. **Vérifier que le serveur démarre** sans erreur dans les logs
2. **Accéder à l'interface** : http://127.0.0.1:5000/
3. **Vérifier l'état du scheduler** : consulter les logs `[scheduler]`
4. **Tester la suite de tests** (recommandé) :
   ```bash
   python -m pytest
   ```

## Prochaines étapes

Une fois le serveur démarré :

1. **Configurez les identifiants des devices** dans l'interface (Réglages) ou via `config/settings.json` (voir [Configuration](configuration.md))
2. **Explorez l'interface utilisateur** (voir [Guide UI](ui-guide.md))
3. **Configurez les scènes et webhooks** si souhaité (voir [Intégration IFTTT](ifttt-integration.md))
4. **Personnalisez le thème** si nécessaire (voir [Theming](theming.md))

## Dépannage

### Erreurs communes

- **ImportError** : Vérifiez que l'environnement virtuel est activé et les dépendances installées
- **Token invalide** : Vérifiez les identifiants SwitchBot dans `.env`
- **Erreur de connexion PostgreSQL** : Configurez `POSTGRES_URL` ou utilisez `STORE_BACKEND=filesystem` pour le développement

### Logs utiles

- `[scheduler]` : État du planificateur APScheduler
- `[automation]` : Ticks d'automatisation et actions
- `[api]` : Appels API SwitchBot et quotas
- `[store]` : Opérations de stockage

---

*Ce document fait partie de la documentation structurée du SwitchBot Dashboard. Retour au [README principal](README.md). Voir aussi `memory-bank/` pour les décisions architecturales.*
