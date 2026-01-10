# SwitchBot Flask Dashboard (local)

Documentation structurée du projet avec guides thématiques.

## 📚 Guides

- **[Installation et Démarrage](setup.md)** - Prérequis, installation venv, configuration initiale
- **[Configuration](configuration.md)** - `.env`, `settings.json`, workflow `/devices`, validation, quotas API
- **[Guide UI](ui-guide.md)** - Interface utilisateur, bandeau quota, interactions mobile/desktop, accessibilité  
- **[Theming](theming.md)** - Thème sombre, variables CSS, personnalisation, contrast WCAG
- **[Tests et Validation](testing.md)** - Scénarios de test manuel (quota, automation, sécurité)
- **[Déploiement Render/GitHub](deployment.md)** - Docker, CI/CD GHCR, secrets, déclenchement Render

## 🎯 Objectif

Dashboard Flask local qui orchestre la lecture de capteurs SwitchBot et pilote un climatiseur IR virtuel avec résilience locale.

### Fonctionnalités clés

- **Automatisation intelligente** : Boucle de contrôle avec hystérésis et fenêtres horaires
- **Interface mobile-first** : Thème sombre immersif, responsive, accessible
- **Inventaire devices** : Page `/devices` avec copie d'ID et métadonnées
- **Sécurité** : Tokens dans `.env` uniquement, validation systématique
- **Résilience** : Retry automatique, cooldown, gestion d'erreurs

## 🏗️ Architecture

- **`app.py`** : Bootstrap Flask minimal
- **`switchbot_dashboard/`** : Logique métier (services, routes, automation)
- **`config/`** : `settings.json` (paramètres) + `state.json` (télémétrie)
- **`static/css/`** : Thème sombre partagé (`theme.css`) + feuilles spécifiques
- **`docs/`** : Documentation thématique (ce fichier)

## 🚀 Démarrage rapide

```bash
# Installation
/mnt/venv_ext4/venv_switchbot/bin/python -m pip install -r requirements.txt

# Configuration
cp .env.example .env
# Éditer .env avec vos tokens SwitchBot

# Lancement
/mnt/venv_ext4/venv_switchbot/bin/python app.py
# Ouvrir http://127.0.0.1:5000/
```

## 📖 Références

- **API SwitchBot** : `docs/switchbot/README.md` (v1.1) et `docs/switchbot/README-v1.0.md`
- **Standards de développement** : `.windsurf/rules/codingstandards.md`
- **Memory Bank** : `memory-bank/` (décisions, progression, patterns)

---

*Pour la configuration détaillée, voir [Configuration](configuration.md). Pour l'utilisation quotidienne, voir [Guide UI](ui-guide.md). Pour héberger sur Render via GHCR, voir [Déploiement](deployment.md).*
