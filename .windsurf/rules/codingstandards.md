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
3. **Commentaires ciblés** : documenter uniquement les raisons d’un choix non trivial (pas l’évidence).
4. **Principe du moindre privilège** : n’exposer que les données/permissions nécessaires.
5. **Sécurité dès la conception** : valider toutes les entrées utilisateur ou externes avant usage.
6. **DRY & modularité** : factoriser dès que deux blocs partagent une intention commune.

## 2. Organisation du code

- **Python** : regrouper la logique métier dans `switchbot_dashboard/` (services, API, tâches). Éviter d’ajouter du code dans `app.py` hors bootstrap.
- **Configuration** : seules les valeurs persistées vont dans le store configuré (Redis ou JSON). Les secrets restent dans `.env`.
- **Docs** : toute règle ou procédure doit résider dans `docs/` et être liée depuis le README si critique.
- **Imports** : ordre PEP 8 (stdlib, deps, modules locaux) avec lignes vides entre groupes.
- **Thématisation** : Tous les styles doivent résider dans `static/css/`. L'usage de `<style>` inline dans les templates Jinja est proscrit.

## 3. Backend Python (Flask) & Stockage

### Typage et Validation
- **Typage** : activer `from __future__ import annotations` dans les nouveaux modules et typer toutes les signatures publiques.
- **Validation** : centraliser la conversion/validation des paramètres (cf. helpers `_as_bool`, `_as_int`, `_as_float`). Ne jamais consommer directement `request.form` hors de ces fonctions.

### Sélection dynamique du stockage (`BaseStore`)
- Toute lecture/écriture de `settings` ou `state` doit passer par un objet `BaseStore` obtenu via `current_app.extensions`. **Interdiction d'ouvrir les fichiers JSON directement.**
- Le système supporte Redis (`RedisJsonStore`) avec un fallback automatique vers le système de fichiers (`JsonStore`).
- Lorsqu'un code manipule un store, il doit traiter `StoreError` et laisser `create_app()` gérer la logique de bascule (ne pas dupliquer la logique de fallback).

### Services et API
- **Services** : encapsuler les appels SwitchBot dans des classes dédiées (ex: `SwitchBotClient`). Pas de requêtes HTTP dans les vues.
- **Quotas API** : Chaque appel au `SwitchBotClient` doit enregistrer le quota via l'API fournie par `AutomationService`. L'accès direct à `state.json` pour incrémenter les compteurs est interdit.
- **Erreurs** : lever des exceptions spécifiques (`SwitchBotApiError`) et les traduire en messages utilisateur via `flash`.

## 4. Frontend & templates Jinja

- **Structure** : séparer le HTML des styles. Importer la palette via `theme.css` et placer les styles spécifiques dans un fichier dédié sous `static/css/` (ex: `devices.css`).
- **Thème Sombre** : Utiliser exclusivement les variables CSS définies dans `theme.css`. Éviter les codes couleur "magiques" (#FFF, etc.) dans les templates.
- **Accessibilité** : respecter la checklist WCAG (labels explicites, attributs `aria-*`, contrastes suffisants). Tester systématiquement le focus et le survol (hover).
- **Comportement** : tout script JS manipulant l’état doit vérifier les valeurs renvoyées par le backend; gérer les erreurs via `try/catch`.

## 5. Configuration, secrets et environnement

- **.env** : aucune valeur sensible ne doit être commitée. Fournir une version dans `.env.example`.
- **Variables dynamiques** : Toute nouvelle variable (ex: `REDIS_URL`, `LOG_LEVEL`, `STORE_BACKEND`) doit être documentée dans `docs/configuration.md` avec des valeurs par défaut explicites et validées (trim, types) dans `create_app`.
- **Validation** : lors du chargement de données persistées, vérifier les schémas attendus et loguer les champs inconnus.

## 6. Journalisation & Observabilité

- **Logger** : Utiliser `current_app.logger` ou un logger enfant. Ne jamais utiliser `logging.basicConfig` ou `print`.
- **Configuration** : Le niveau de log doit respecter la variable d'environnement `LOG_LEVEL`.
- **Contexte** : Préfixer les messages par le contexte entre crochets : `[scheduler]`, `[api]`, `[store]`, etc.
- **Sécurité** : Ne jamais loguer de secrets, de jetons API ou de payloads contenant des données personnelles sensibles.
- **Quotas** : L'interface doit afficher les quotas calculés localement (reset à minuit UTC) et alerter l'utilisateur en cas de dépassement imminent.

## 7. Tests & assurance qualité

### Scénarios obligatoires
- **Cas nominaux** : température stable, réglages valides, commandes SwitchBot OK.
- **Cas limites** : seuils avec hystérésis (limite ±0.1°C), JSON corrompu, credentials manquants.
- **Résilience stockage** : simuler l'indisponibilité de Redis pour vérifier le basculement transparent vers le stockage local.
- **API SwitchBot** : simuler les erreurs 429 (Too Many Requests) et 5xx pour vérifier le comportement des compteurs de quota et des retries.

### Automatisation
- Ajouter des tests unitaires pour toute logique de conversion/validation.
- Utiliser `caplog` (pytest) pour vérifier que les logs de bascule de stockage ou d'erreurs API sont correctement émis au niveau attendu.

## 8. Process de contribution

1. **Branche** : Créer une branche descriptive (`feature/redis-backend`).
2. **Documentation** : Mettre à jour `docs/` (configuration, thèmes, tests) en même temps que le code.
3. **PR (Pull Request)** :
   - Description claire des changements.
   - Capture d'écran si impact UI (vérification thème sombre/mobile).
   - Checklist des tests manuels effectués (notamment le fallback storage).
4. **Revue** :
   - Vérifier l'absence de styles inline.
   - Vérifier que l'accès au stockage passe par `BaseStore`.
   - Confirmer la gestion des quotas API.

## 9. Décisions et traçabilité

- Toute décision architecturale majeure doit être consignée dans `memory-bank/decisionLog.md` avec horodatage.
- Les progrès et tâches restantes sont suivis dans `memory-bank/progress.md`.
- Ce standard est complété par les guides spécifiques : `docs/configuration.md`, `docs/testing.md`, `docs/theming.md`.

---
*Dernière mise à jour : 10 Janvier 2026*