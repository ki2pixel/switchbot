---
last_updated: 2026-01-28
owner: automation
---

# Mini plan — Intégration UI/Postgres des réglages de polling adaptatif

## Contexte rapide
- Le backend supporte déjà `adaptive_polling_enabled`, `idle_poll_interval_seconds`, `poll_warmup_minutes` (persistés via `settings_store`).
- Aucun champ dédié n’existe dans l’UI ni dans la documentation utilisateur.
- Objectif de la prochaine session : rendre ces réglages éditables depuis le dashboard et documentés côté Postgres.

## Objectifs de la session
1. **Surface UI** : ajouter les champs nécessaires dans `templates/settings.html` + validation `routes.py`.
2. **Docs & Postgres** : détailler les paramètres dans `docs/configuration.md` + mentionner le stockage Postgres (clé/valeurs). 
3. **Expérience utilisateur** : clarifier les valeurs conseillées (idle vs warmup) et les cas d’usage.
4. **Tests** : couvrir la sauvegarde UI (tests BeautifulSoup) + un test service vérifiant que la désactivation UI force le mode fixe.

## Étapes proposées
1. **Analyse**
   - Vérifier les clés existantes dans `config/settings.json` et l’état Postgres.
   - Identifier l’emplacement optimal dans le formulaire (section Automatisation).
2. **Backend/UI**
   - Ajouter champs `adaptive_polling_enabled`, `idle_poll_interval_seconds`, `poll_warmup_minutes` dans `settings.html` (switch + inputs) avec helpers `data-loader`.
   - Étendre `routes.update_settings` pour valider et persister ces champs.
3. **Documentation**
   - Mettre à jour `docs/configuration.md` (sous-section Automatisation → Polling adaptatif).
   - Ajouter un encart dans `docs/scheduler.md` décrivant l’algorithme (in-window / idle / warmup).
4. **Tests**
   - Ajouter un test UI (POST `/settings`) vérifiant la persistance.
   - Ajouter un test scheduler/automation assurant que `adaptive_polling_enabled=false` restaure le comportement fixe.
5. **Validation finale**
   - `pytest` ciblé (`test_dashboard_routes.py`, `test_scheduler_service.py`).
   - Capture d’écran/notes UX si nécessaire.

## Notes ouvertes
- Prévoir des valeurs par défaut lisibles (ex: 600s idle, 15 min warmup) dans l’UI.
- Mentionner dans les docs comment surcharger via env var `SWITCHBOT_POLL_INTERVAL_SECONDS` si besoin.
