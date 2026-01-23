---
trigger: always_on
description: 
globs: 
---

# Standards de développement – SwitchBot Dashboard v2 (23/01/2026)

## 1. Principes & Organisation
1.  **Lisibilité & Nommage** : Code explicite (`meter_device_id`, pas `mdid`). Commentaires sur l'intention uniquement. Pas de code mort.
2.  **Architecture** : Logique dans `switchbot_dashboard/`, config dans `BaseStore`, secrets dans `.env`.
3.  **Docs** : Règles dans `docs/`, liées au README.
4.  **Imports** : Ordre PEP 8 (stdlib, deps, local).
5.  **Dépendances Frontend (Offline-first)** : **Interdiction stricte des CDNs**. Bootstrap, Chart.js, FontAwesome et polices (Space Grotesk) doivent être servis depuis `static/vendor/`.

## 2. Backend (Flask) & Stockage

### Code & Validation
- **Typage** : `from __future__ import annotations` + typage strict.
- **Validation** : Helpers obligatoires (`_as_bool`, etc.). Jamais de `request.form` brut.

### Stockage (`BaseStore`)
- **Priorité** : `PostgresStore` (Neon) > `JsonStore` (Fallback).
- **Accès** : Via `current_app.extensions["settings_store"|"state_store"]`. Ne jamais utiliser `open()` directement.
- **Résilience** : `create_app()` gère le basculement automatique sur `PostgresStoreError`. Logs avec préfixe `[store]`.
- **Connexion** : Utiliser le pool `psycopg_pool` existant.

### SwitchBot & Services
- **Client** : Utiliser `SwitchBotClient` (instance unique avec `ApiQuotaTracker`).
- **Logique** : Webhooks IFTTT > Scènes (`winter`/`summer`/`off`) > Commandes directes.
- **OFF** : Utiliser `off_repeat_count/interval`. Vérifier l'idempotence (pas de OFF si déjà `assumed_aircon_power == "off"`).
- **Quick Actions** : Bouton "Quick off" = Scène `off` (fallback `turnOff` si nécessaire).
- **IFTTT** : `IFTTTWebhookClient` avec validation HTTPS stricte.
- **Historique** : `HistoryService` avec buffer batch thread-safe et cleanup auto (6h).

## 3. Frontend & Templates

- **Structure** : HTML/Jinja séparé du CSS (`static/css/`). Pas de styles inline.
- **Thème** : Variables CSS (`theme.css`) uniquement. Thème sombre par défaut.
- **Navigation** : Bottom nav (mobile) / Label (desktop). Page `actions.html` instrumentée.

### Performance & UX (Critique)
- **Loaders** : `loaders.js` obligatoire sur POST/Actions. **Failsafe 15s** requis (timeout auto).
- **Chart.js** : **Décimation LTTB** client-side obligatoire. Profil mobile forcé (hauteur 180px, granularité réduite).
- **Vitesse** : LCP < 1.8s. Timeouts : Form 5s, Action 3s. CSS critique inliné.
- **Feedback** : Retour immédiat (overlay/spinner) sur toute action.

## 4. Config, Logs & Monitoring

- **Env** : `POSTGRES_URL` et `POSTGRES_SSL_MODE` requis. Redis déprécié (warning).
- **Logs** : `current_app.logger` avec préfixe `[scheduler]`, `[api]`, `[history]`. Pas de secrets.
- **Santé** : `/healthz` reflète l'état du store (503 si erreur).
- **Quotas** : Affichage UI obligatoire (calcul local, reset minuit UTC). Alerte visuelle si dépassement.

## 5. Tests & Qualité

- **Commande** : `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest`.
- **Couverture** : Min 85%. Unitaires (conversion) + Intégration (Flux complet IFTTT->DB->UI).
- **Scénarios Clés** :
    1. Bascule Postgres -> JsonStore (vérifier logs `[store]`).
    2. API Quotas (Simulation 429 -> Alerte UI).
    3. IFTTT (Validation HTTPS, Timeouts).
    4. Historique (Batch flush, Chart.js rendering).

## 6. Process de Contribution
1. Branche `feature/*` ou `fix/*`.
2. PR avec capture d'écran (mobile/dark mode) et validation quotas.
3. Mise à jour doc si nécessaire.

## 7. Références Documentation
- **Migration DB** : `docs/postgresql-migration.md`, `scripts/migrate_to_postgres.py`
- **History** : `docs/history-monitoring.md`, `scripts/create_history_table.sql`
- **IFTTT** : `docs/ifttt-integration.md`
- **Performance** : `docs/frontend-performance.md`, `static/js/loaders.js`
- **Décisions** : `memory-bank/decisionLog.md`