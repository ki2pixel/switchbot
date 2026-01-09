# Installation et Démarrage

## Prérequis

- Python 3.10+
- Un compte SwitchBot avec Cloud Service activé
- Un `token` et un `secret` SwitchBot (API v1.1)

## Installation

Le projet utilise un environnement virtuel dédié situé dans `/mnt/venv_ext4/venv_switchbot`.

Dans un terminal :

```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pip install -r requirements.txt
```

## Configuration initiale

1. Copier le fichier d'exemple :

```bash
cp .env.example .env
```

2. Remplir dans `.env` :

- `SWITCHBOT_TOKEN`
- `SWITCHBOT_SECRET`

Optionnel (recommandé si Wi‑Fi instable) :

- `SWITCHBOT_RETRY_ATTEMPTS` (par défaut `2` = 1 retry)
- `SWITCHBOT_RETRY_DELAY_SECONDS` (par défaut `10`)

> 💡 **Sécurité** : Les tokens ne sont jamais stockés dans les fichiers JSON. Respect du principe du moindre privilège.

> 📝 **Décision** : Cette approche centralisée respecte les standards définis dans `memory-bank/decisionLog.md` (2026-01-09 16:21) et `codingstandards.md`.

## Lancement

```bash
/mnt/venv_ext4/venv_switchbot/bin/python app.py
```

Puis ouvre :

- http://127.0.0.1:5000/

## Prochaines étapes

Une fois le serveur démarré :

1. Configurez les identifiants des devices dans `config/settings.json` (voir [Configuration](configuration.md))
2. Explorez l'interface utilisateur (voir [Guide UI](ui-guide.md))
3. Personnalisez le thème si nécessaire (voir [Theming](theming.md))

---

*Ce document fait partie de la documentation structurée du SwitchBot Dashboard. Retour au [README principal](README.md). Voir aussi `memory-bank/` pour les décisions architecturales.*
