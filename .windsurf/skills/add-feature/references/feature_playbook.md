# Playbook Implémentation Fonctionnalités

## Pré-requis
- Suite de tests disponible : `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest` (cibler modules impactés).
- Stores accessibles via `current_app.extensions["settings_store"|"state_store"]`.
- Frontend : loaders actifs (voir `loader-patterns`).

## Matrice Backend
| Étape | Fichier(s) | Clés à vérifier |
| --- | --- | --- |
| Injection service | `switchbot_dashboard/__init__.py` | Enregistrer service sous `app.extensions["<nom>"]`, documenter docstring |
| Logique métier | `automation.py` ou nouveau module | Typage strict, logs `[service]`, pas de `request` direct |
| Stores | `config_store.py` | Utiliser `BaseStore` (Postgres prioritaire, Json fallback) |
| Scheduler | `scheduler.py` | Reschedule via `scheduler_service.reschedule()` si intervalle modifié |

### Templates de code
```python
from flask import current_app

service = current_app.extensions["my_service"]
service.run(payload)
```

## Matrice Routes/UI
1. Ajouter route dans `routes.py` (blueprint `dashboard_bp`).
2. Helpers `_as_bool/_as_int/_as_float` obligatoires.
3. Templates : inclure `_footer_nav.html`, `loaders.js`, classes `sb-card` / `sb-section-title`.
4. CSS : mettre à jour `switchbot_dashboard/static/css/<page>.css` ou `switchbot_dashboard/static/css/theme.css` (pas de inline).

## Tests & Documentation
- Ajouter tests ciblés (`tests/test_<feature>.py` + routes via client Flask + BeautifulSoup si UI).
- Mettre à jour `docs/core/configuration.md` ou `docs/guides/ui-navigation.md` selon feature + Memory Bank (decisionLog + progress).
- Vérifier couverture ≥85% après modifications.

## Checkpoints de revue
- Logs sensibles ? (pas de secrets).
- Loaders actifs sur chaque action.
- Bandeaux/quota/animations respectent tokens existants.
- Relecture FR : labels cohérents avec UI actuelle.
