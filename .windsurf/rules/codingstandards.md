---
trigger: always_on
description: 
globs: 
---

# Standards de développement – SwitchBot Dashboard v2 (MàJ Janvier 2026)

Ce document décrit les règles obligatoires pour tout nouveau code ou refactorisation, intégrant les évolutions majeures récentes (PostgreSQL, History Monitoring, IFTTT, Performance Frontend).

## 1. Philosophie générale

1. **Lisibilité avant concision** : privilégier des blocs simples, explicites et aisés à relire.
2. **Nommage descriptif** : bannir les abréviations opaques (`meter_device_id`, pas `mdid`).
3. **Commentaires ciblés** : documenter uniquement les raisons d'un choix non trivial.
4. **Principe du moindre privilège** : n'exposer que les données/permissions nécessaires.
5. **Sécurité dès la conception** : valider toutes les entrées utilisateur ou externes.
6. **DRY & modularité** : factoriser dès que deux blocs partagent une intention commune.

## 2. Organisation du code

- **Python** : Logique métier dans `switchbot_dashboard/`. Éviter d'ajouter du code dans `app.py`.
- **Configuration** : Valeurs persistées dans le store (`BaseStore`). Secrets dans `.env`.
- **Docs** : Toute règle doit résider dans `docs/` et être liée depuis le README.
- **Imports** : Ordre PEP 8 (stdlib, deps, modules locaux).
- **Thématisation** : Styles dans `static/css/`. `<style>` inline proscrit dans les templates Jinja.

## 3. Backend Python (Flask) & Stockage

- **Clean Code** : Pas de code mort commenté (supprimer directement). Commentaires : Expliquer le "Pourquoi" (intention métier), pas le "Comment" (syntaxe évidente).

### Typage et Validation
- **Typage** : Activer `from __future__ import annotations` et typer toutes les signatures publiques.
- **Validation** : Centraliser la validation via les helpers (`_as_bool`, `_as_int`, etc.). Ne jamais consommer `request.form` directement.

### Gestion du Stockage (`BaseStore`)
- **Architecture PostgreSQL** : Utiliser `PostgresStore` comme backend principal (Neon recommandé). `JsonStore` comme fallback.
- **Accès** : Accéder aux stores uniquement via `current_app.extensions["settings_store"]` ou `current_app.extensions["state_store"]`.
- **Interdiction** : Ne jamais ouvrir les fichiers JSON directement via `open()`.
- **Résilience** : En cas de `PostgresStoreError` ou `StoreError`, laisser `create_app()` gérer le fallback automatique. Le composant doit simplement journaliser l'erreur avec le préfixe `[store]`.
- **Connection pooling** : Utiliser le pool `psycopg_pool.ConnectionPool` existant, pas de connexions directes.

### Services et API SwitchBot
- **Encapsulation** : Utiliser `SwitchBotClient`. Pas de requêtes HTTP directes dans les vues.
- **Quotas** : Utiliser l'instance unique d'`ApiQuotaTracker` branchée dans `SwitchBotClient`. Tout nouveau service doit réutiliser ce client pour garantir la cohérence des compteurs.
- **Cascade d'actions** : Priorité aux webhooks IFTTT → scènes SwitchBot (`winter`, `summer`, `off`) → commandes directes (`setAll`/`turnOff`).
- **Off-repeat** : Utiliser les paramètres `off_repeat_count` et `off_repeat_interval_seconds` pour répéter les actions OFF selon la configuration.
- **Idempotence OFF** : Empêcher les déclenchements répétés d'actions OFF si `assumed_aircon_power == "off"`.
- **Quick actions** : Le bouton "Quick off" doit déclencher la scène `off` (avec repli `turnOff` uniquement si `aircon_device_id` est présent).

### Services Spécialisés
- **IFTTTWebhookClient** : Pour les déclenchements via webhooks IFTTT avec validation HTTPS obligatoire.
- **HistoryService** : Pour la collecte et récupération des données historiques dans PostgreSQL. Utiliser le connection pool existant.
- **PostgresStore** : Implémentation PostgreSQL respectant `BaseStore` avec schéma JSONB et indexes optimisés.

## 4. Frontend & Templates Jinja

- **Clean Code** : Pas de code mort commenté (supprimer directement). Commentaires : Expliquer le "Pourquoi" (intention métier), pas le "Comment" (syntaxe évidente).
- **Structure** : Séparer strictement HTML et CSS. Styles spécifiques dans `static/css/devices.css`, etc.
- **Thème Sombre** : Utiliser exclusivement les variables CSS de `theme.css`. Pas de codes couleur "magiques" (#FFF).
- **Accessibilité** : Respecter WCAG (labels, `aria-*`, contrastes).
- **UI & Quotas** : L'affichage des quotas et l'alerte de seuil (`api_quota_warning_threshold`) sont obligatoires.
- **Messages** : Traduire les `SwitchBotApiError` en messages utilisateur via `flash`.

### Performance et UX
- **Loaders non bloquants** : Utiliser le système `loaders.js` pour tous les formulaires POST et actions utilisateur.
- **Animations GPU** : Privilégier `transform` et `opacity` pour les animations CSS.
- **Feedback visuel** : Fournir un retour immédiat lors des clics et soumissions (overlay, spinner).
- **Temps réponse** : Timeouts de sécurité : 5s formulaires, 3s actions, 2s navigation.

### Dashboard Monitoring
- **Chart.js** : Utiliser Chart.js pour les visualisations de données historiques.
- **Filtres interactifs** : Implémenter des filtres temps réel sans rechargement de page.
- **Mise à jour automatique** : Polling pour les données temps réel (30s recommandé).
- **Responsive** : Adapter les graphiques pour mobile et desktop.

## 5. Configuration, secrets et environnement

- **.env** : Aucune valeur sensible commitée. Fournir un `.env.example` à jour.
- **Variables PostgreSQL** : `POSTGRES_URL`, `POSTGRES_SSL_MODE` obligatoires pour backend PostgreSQL. Documentées dans `docs/configuration.md`.
- **Variables Redis** : Dépréciées mais supportées avec warning. `REDIS_URL`, `REDIS_PREFIX`, `REDIS_TTL_SECONDS`.
- **Validation** : Vérifier les schémas des données persistées et loguer les champs inconnus.

## 6. Journalisation & Observabilité

- **Logger** : Utiliser `current_app.logger`. Préfixer par contexte : `[scheduler]`, `[api]`, `[store]`, `[auth]`, `[history]`.
- **Santé** : Le endpoint `/healthz` est le contrat de monitoring. Il doit refléter l'état des stores (503 si `PostgresStoreError` ou `StoreError`).
- **Scheduler** : Gérer gracieusement les appels `reschedule()` si non démarré, utiliser `SERVER_SOFTWARE` pour détecter le mode production.
- **Quotas** : L'interface doit afficher les quotas calculés localement (reset à minuit UTC) et alerter en cas de dépassement imminent.
- **Historique** : `HistoryService` journalise les erreurs de collecte avec préfixe `[history]`.
- **Sécurité** : Ne jamais loguer de secrets, jetons ou données personnelles.

## 7. Tests & Assurance Qualité

### Scénarios obligatoires
- **Cas nominaux** : Température stable, commandes SwitchBot OK.
- **Cas limites** : Seuils avec hystérésis (±0.1°C), JSON corrompu.
- **Résilience stockage** : Simuler l'indisponibilité de PostgreSQL pour vérifier le basculement transparent vers `JsonStore` et la journalisation.
- **Scènes manquantes** : Vérifier que `AutomationService` gère le fallback IFTTT → scènes → commandes proprement.
- **API SwitchBot** : Simuler les erreurs 429 et 5xx. Vérifier l'apparition du bandeau d'alerte quota en UI via BeautifulSoup.
- **Endpoint santé** : Tester `/healthz` (succès, PostgresStoreError, erreurs inattendues).
- **History Monitoring** : Tests CRUD, agrégations, erreurs, intégration PostgreSQL.
- **IFTTT Webhooks** : Validation HTTPS, timeouts, gestion d'erreurs.

### Automatisation
- Tests unitaires pour toute logique de conversion.
- Utiliser `caplog` (pytest) pour valider les niveaux de log (surtout lors des bascules de stockage).
- **Exécution Pytest** : Lancer systématiquement la suite via l'environnement virtuel dédié :
  ```bash
  /mnt/venv_ext4/venv_switchbot/bin/python -m pytest
  ```
- **Fixtures PostgreSQL** : Utiliser des mocks pour les tests unitaires, connexion réelle pour les tests d'intégration.

### Couverture et Qualité
- **Coverage cible** : 85% minimum pour les modules critiques.
- **Tests d'intégration** : Valider les flux complets (IFTTT → PostgreSQL → UI).
- **Tests frontend** : Validation des loaders, Chart.js, filtres interactifs.

## 8. Architecture et Patterns

### Patterns de Stockage
- **PostgreSQL primaire** : `PostgresStore` avec connection pooling, JSONB, indexes.
- **Fallback filesystem** : `JsonStore` pour résilience locale.
- **Redis déprécié** : Support maintenu avec warning mais non recommandé.

### Patterns d'Automatisation
- **Cascade IFTTT** : Webhooks IFTTT → Scènes SwitchBot → Commandes directes.
- **Idempotence** : Protection contre les actions répétées (OFF, ON).
- **Timezone-aware** : Utiliser `zoneinfo` pour les fenêtres horaires.

### Patterns de Monitoring
- **Historique temps réel** : Collecte automatique dans `AutomationService.run_once()`.
- **API REST** : Endpoints `/history/api/*` pour données filtrées et agrégées.
- **Dashboard responsive** : Chart.js avec filtres interactifs et thème sombre.

## 9. Process de contribution

1. **Branche** : `feature/nom-descriptif` ou `fix/nom-descriptif`.
2. **Documentation** : Mettre à jour `docs/` (configuration, monitoring, IFTTT, performance) simultanément.
3. **PR (Pull Request)** :
   - Description claire.
   - Capture d'écran si impact UI (vérification thème sombre/mobile).
   - Validation du fallback PostgreSQL et de la gestion des quotas.
   - Tests exécutés dans l'environnement virtuel `/mnt/venv_ext4/venv_switchbot`.
4. **Revue** : Vérifier l'absence de styles inline, le passage par `BaseStore` et l'intégration des nouveaux services.

## 10. Décisions et traçabilité

- Toute décision architecturale majeure (ex: migration PostgreSQL, ajout IFTTT) doit être consignée dans `memory-bank/decisionLog.md` avec horodatage.
- Ce standard est complété par les guides spécialisés : `docs/configuration.md`, `docs/testing.md`, `docs/theming.md`, `docs/postgresql-migration.md`, `docs/history-monitoring.md`, `docs/ifttt-integration.md`, `docs/frontend-performance.md`.

## 11. Références aux Nouvelles Fonctionnalités

### PostgreSQL Migration
- Guide complet : `docs/postgresql-migration.md`
- Script migration : `scripts/migrate_to_postgres.py`
- Schéma SQL : `scripts/schema.sql`

### History Monitoring
- Guide utilisateur : `docs/history-monitoring.md`
- Service : `switchbot_dashboard/history_service.py`
- Table SQL : `scripts/create_history_table.sql`

### IFTTT Integration
- Guide complet : `docs/ifttt-integration.md`
- Client : `switchbot_dashboard/ifttt.py`
- API référence : `docs/IFTTT/api_reference.md`

### Performance Frontend
- Guide optimisations : `docs/frontend-performance.md`
- Loaders : `static/js/loaders.js`
- Styles theme : `static/css/theme.css`

---
*Dernière mise à jour : 14 Janvier 2026*