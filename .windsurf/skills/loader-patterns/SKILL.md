---
name: loader-patterns
description: Workflow pour garantir l'usage des loaders UI (data-loader, overlay global, ARIA) sur formulaires et actions.
---

# Loaders UI obligatoires

Utiliser ce skill avant d’ajouter ou modifier un bouton/action afin de conserver l’expérience loaders 15 s.

## 1. Rappels techniques
- JS : `static/js/loaders.js` (init automatique, failsafe 15 s, aria-busy).
- CSS : classes `sb-global-loader`, `sb-btn-loader` dans `static/css/theme.css`.
- Templates : attribut `data-loader` requis sur tous les `<form>` POST et liens d’action.
- Référence : `references/loader_audit.md` pour checklist complète (tests manuels + DevTools).

## 2. Workflow d’implémentation
1. **Formulaires** :
   - Ajouter `data-loader="submit"` (ou valeur spécifique) + `data-loader-text` si besoin.
   - Vérifier que le bouton inclut `<span class="loader" aria-hidden="true"></span>` si pattern local.
2. **Liens/Boutons actions** :
   - Utiliser `data-loader="nav"` pour redirections.
   - S’assurer que la cible inclut loader global (ex : boutons sur index.html).
3. **Scripts** :
   - Importer `loaders.js` en bas du template (`<script src="{{ url_for('static', filename='js/loaders.js') }}"></script>`).
   - Vérifier qu’aucun autre script ne bloque avant `DOMContentLoaded`.

## 3. Tests et validation
- Pytest : `tests/test_frontend_loaders.py` (ajouter cas si nouveau template).
- Manuel :
  - Cliquer sur chaque action → loader visible < 100 ms.
  - Failsafe : après 15 s, loader se retire automatiquement.
  - Accessibilité : `aria-busy="true"` appliqué sur root pendant chargement.

## 4. Documentation
- Mettre à jour `docs/frontend-performance.md` quand un pattern change.
- Noter dans Memory Bank si de nouveaux types de loader introduits.
