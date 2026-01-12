---
trigger: always_on
description: 
globs: 
---

# Standards de développement – SwitchBot Dashboard (MàJ Janvier 2026)

Ce document décrit les règles obligatoires pour tout nouveau code ou refactorisation.

## 1. Philosophie générale

1. **Lisibilité avant concision** : privilégier des blocs simples, explicites et aisés à relire.
2. **Nommage descriptif** : bannir les abréviations opaques (`meter_device_id`, pas `mdid`).
3. **Commentaires ciblés** : documenter uniquement les raisons d’un choix non trivial.
4. **Principe du moindre privilège** : n’exposer que les données/permissions nécessaires.
5. **Sécurité dès la conception** : valider toutes les entrées utilisateur ou externes.
6. **DRY & modularité** : factoriser dès que deux blocs partagent une intention commune.

## 2. Organisation du code

- **Python** : Logique métier dans `switchbot_dashboard/`. Éviter d’ajouter du code dans `app.py`.
- **Configuration** : Valeurs persistées dans le store (`BaseStore`). Secrets dans `.env`.
- **Docs** : Toute règle doit résider dans `docs/` et être liée depuis le README.
- **Imports** : Ordre PEP 8 (stdlib, deps, modules locaux).
- **Thématisation** : Styles dans `static/css/`. `<style>` inline proscrit dans les templates Jinja.

## 3. Backend Python (Flask) & Stockage

### Typage et Validation
- **Typage** : Activer `from __future__ import annotations` et typer toutes les signatures publiques.
- **Validation** : Centraliser la validation via les helpers (`_as_bool`, `_as_int`, etc.). Ne jamais consommer `request.form` directement.

### Gestion du Stockage (`BaseStore`)
- **Accès** : Accéder aux stores uniquement via `current_app.extensions["settings_store"]` ou `current_app.extensions["state_store"]`.
- **Interdiction** : Ne jamais ouvrir les fichiers JSON directement via `open()`.
- **Résilience** : En cas de `StoreError`, laisser `create_app()` gérer le fallback (ex: Redis → Filesystem). Le composant doit simplement journaliser l'erreur avec le préfixe `[store]`.

### Services et API SwitchBot
- **Encapsulation** : Utiliser `SwitchBotClient`. Pas de requêtes HTTP directes dans les vues.
- **Quotas** : Utiliser l'instance unique d'`ApiQuotaTracker` branchée dans `SwitchBotClient`. Tout nouveau service doit réutiliser ce client pour garantir la cohérence des compteurs.
- **Actions prioritaires** : Priorité aux webhooks IFTTT pour les actions automatiques et manuelles, avec fallback vers scènes SwitchBot (`winter`, `summer`, `off`) puis commandes directes (`setAll`/`turnOff`).
- **Off-repeat** : Utiliser les paramètres `off_repeat_count` et `off_repeat_interval_seconds` pour répéter les actions OFF selon la configuration.
- **Idempotence OFF** : Empêcher les déclenchements répétés d'actions OFF si `assumed_aircon_power == "off"`.
- **Quick actions** : Le bouton "Quick off" doit déclencher la scène `off` (avec repli `turnOff` uniquement si `aircon_device_id` est présent).

## 4. Frontend & Templates Jinja

- **Structure** : Séparer strictement HTML et CSS. Styles spécifiques dans `static/css/devices.css`, etc.
- **Thème Sombre** : Utiliser exclusivement les variables CSS de `theme.css`. Pas de codes couleur "magiques" (#FFF).
- **Accessibilité** : Respecter WCAG (labels, `aria-*`, contrastes).
- **UI & Quotas** : L'affichage des quotas et l'alerte de seuil (`api_quota_warning_threshold`) sont obligatoires.
- **Messages** : Traduire les `SwitchBotApiError` en messages utilisateur via `flash`.

## 5. Configuration, secrets et environnement

- **.env** : Aucune valeur sensible commitée. Fournir un `.env.example` à jour.
- **Variables Redis** : Toute variable (`STORE_BACKEND`, `REDIS_URL`, `REDIS_PREFIX`, `REDIS_TTL_SECONDS`) doit être documentée dans `docs/configuration.md` et validée (trim, types) dans `create_app`.
- **Validation** : Vérifier les schémas des données persistées et loguer les champs inconnus.

## 6. Journalisation & Observabilité

- **Logger** : Utiliser `current_app.logger`. Préfixer par contexte : `[scheduler]`, `[api]`, `[store]`, `[auth]`.
- **Santé** : Le endpoint `/healthz` est le contrat de monitoring. Il doit refléter l'état des stores (503 si `StoreError`).
- **Scheduler** : Gérer gracieusement les appels `reschedule()` si non démarré, utiliser `SERVER_SOFTWARE` pour détecter le mode production et éviter les skippings erronés.
- **Quotas** : L'interface doit afficher les quotas calculés localement (reset à minuit UTC) et alerter en cas de dépassement imminent.
- **Sécurité** : Ne jamais loguer de secrets, jetons ou données personnelles.

## 7. Tests & Assurance Qualité

### Scénarios obligatoires
- **Cas nominaux** : Température stable, commandes SwitchBot OK.
- **Cas limites** : Seuils avec hystérésis (±0.1°C), JSON corrompu.
- **Résilience stockage** : Simuler l'indisponibilité de Redis pour vérifier le basculement transparent vers le stockage local (`JsonStore`) et la journalisation.
- **Scènes manquantes** : Vérifier que `AutomationService` gère le fallback proprement.
- **API SwitchBot** : Simuler les erreurs 429 et 5xx. Vérifier l'apparition du bandeau d'alerte quota en UI via BeautifulSoup.
- **Endpoint santé** : Tester `/healthz` (succès, StoreError, erreurs inattendues).

### Automatisation
- Tests unitaires pour toute logique de conversion.
- Utiliser `caplog` (pytest) pour valider les niveaux de log (surtout lors des bascules de stockage).
- **Exécution Pytest** : Lancer systématiquement la suite via l’environnement projet `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest`.

## 8. Process de contribution

1. **Branche** : `feature/nom-descriptif` ou `fix/nom-descriptif`.
2. **Documentation** : Mettre à jour `docs/` (configuration, thèmes, tests) simultanément.
3. **PR (Pull Request)** :
   - Description claire.
   - Capture d'écran si impact UI (vérification thème sombre/mobile).
   - Validation du fallback storage et de la gestion des quotas.
4. **Revue** : Vérifier l'absence de styles inline et le passage systématique par `BaseStore`.

## 9. Décisions et traçabilité

- Toute décision architecturale majeure (ex: suppression des anciennes actions rapides) doit être consignée dans `memory-bank/decisionLog.md` avec horodatage.
- Ce standard est complété par les guides spécifiques : `docs/configuration.md`, `docs/testing.md`, `docs/theming.md`.

---
*Dernière mise à jour : 12 Janvier 2026*