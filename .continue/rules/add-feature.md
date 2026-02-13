---
description: Workflow complet pour ajouter une nouvelle fonctionnalité (Backend + Frontend) au Dashboard SwitchBot.
globs: 
  - "**/*.{py,js,md}"
alwaysApply: true
---

# Ajouter une fonctionnalité au Dashboard SwitchBot

Ce workflow assure la cohérence entre le backend Flask, le stockage PostgreSQL et le frontend optimisé.

## Checklist d'implémentation

> Ressource détaillée : consulter `.windsurf/skills/add-feature/references/feature_playbook.md` pour matrices Backend/Frontend, snippets et validations complètes.

### 1. Backend (Service Layer)
- Si logique métier complexe : Ajouter dans `automation.py` ou créer un nouveau service
- Si persistance nécessaire : Utiliser `PostgresStore` (priorité) avec `BaseStore` interface
- Enregistrer le service dans `create_app` (`__init__.py`) via `app.extensions`
- Utiliser `current_app.extensions["settings_store"|"state_store"]` pour l'accès aux données

### 2. Backend (Routes)
- Ajouter la route dans `routes.py` avec le blueprint `dashboard_bp`
- Utiliser `current_app.extensions[...]` pour récupérer les services injectés
- Validation obligatoire avec helpers `_as_bool`, `_as_int`, `_as_float`
- Retourner `render_template` ou JSON (pour AJAX)

### 3. Frontend (Template)
- Créer/Modifier le fichier `.html` dans `templates/`
- Étendre le layout de base ou inclure `_footer_nav.html`
- Utiliser les classes CSS existantes (`sb-card`, `btn-primary`, `status-value`)
- **Thème sombre obligatoire** : utiliser les variables CSS (`var(--sb-bg)`, etc.)

### 4. Frontend (Assets)
- CSS : **Interdiction stricte des styles inline**. Si critique (above the fold), placer dans `switchbot_dashboard/static/css/critical.css`. Sinon dans fichier CSS dédié dans `switchbot_dashboard/static/css/`.
- JS : **Loaders.js obligatoire** pour les boutons d'action (`data-loader`)
- Performance : `loading="lazy"` pour les images sauf LCP
- **CDNs interdits** : Bootstrap, Chart.js, FontAwesome et polices (Space Grotesk) doivent être servis depuis `switchbot_dashboard/static/vendor/`

## Ressources complémentaires
- `.windsurf/skills/add-feature/references/feature_playbook.md` : playbook backend/routes/UI, matrices de tests, snippets de service.

## Exemple de Route conforme
```python
@dashboard_bp.route("/ma-fonction", methods=["POST"])
def ma_fonction():
    service = current_app.extensions["mon_service"]
    result = service.do_something()
    flash("Action effectuée", "success")
    return redirect(url_for("dashboard.index"))
```

## Standards critiques à respecter
- **Stockage** : `PostgresStore` (Neon) > `JsonStore` (fallback)
- **Performance** : Loaders.js sur tous les POST/Actions avec failsafe 15s
- **Logs** : `current_app.logger` avec préfixes `[service]`
- **Tests** : Couverture 85% minimum avec `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest`