---
trigger: always_on
description: 
globs: 
---

# Standards de développement – SwitchBot Dashboard

Ce document décrit les règles obligatoires pour tout nouveau code ou refactorisation. Il complète `docs/README.md` (installation) et doit être lu avant toute contribution.

## 1. Philosophie générale

1. **Lisibilité avant concision** : privilégier des blocs simples, explicites et aisés à relire.
2. **Nommage descriptif** : bannir les abréviations opaques (`meter_device_id`, pas `mdid`).
3. **Commentaires ciblés** : documenter uniquement les raisons d’un choix non trivial (pas l’évidence).
4. **Principe du moindre privilège** : n’exposer que les données/permissions nécessaires.
5. **Sécurité dès la conception** : valider toutes les entrées utilisateur ou externes avant usage.
6. **DRY & modularité** : factoriser dès que deux blocs partagent une intention commune.

## 2. Organisation du code

- **Python** : regrouper la logique métier dans `switchbot_dashboard/` (services, API, tâches). Éviter d’ajouter du code dans `app.py` hors bootstrap.
- **Configuration** : seules les valeurs persistées vont dans `config/settings.json` ou `config/state.json` via `JsonStore`. Les secrets restent dans `.env`.
- **Docs** : toute règle ou procédure doit résider dans `docs/` et être liée depuis le README si critique.
- **Imports** : ordre PEP 8 (stdlib, deps, modules locaux) avec lignes vides entre groupes.

## 3. Backend Python (Flask)

- **Typage** : activer `from __future__ import annotations` dans les nouveaux modules et typer toutes les signatures publiques.
- **Validation** : centraliser la conversion/validation des paramètres (cf. helpers `_as_bool`, `_as_int`, `_as_float`). Ne jamais consommer directement `request.form` hors de ces fonctions.
- **Services** : encapsuler les appels SwitchBot dans des classes dédiées (ex: `SwitchBotClient`). Pas de requêtes HTTP dans les vues.
- **Erreurs** : lever des exceptions spécifiques (`SwitchBotApiError`) et les traduire en messages utilisateur via `flash`.
- **Concurrence** : toute écriture disque via `JsonStore` doit être atomique. Éviter les accès concurrents non contrôlés.
- **Performance** : éviter les requêtes API répétées dans une même requête Flask; préférer un cache léger ou le `SchedulerService`.

## 4. Frontend & templates Jinja

- **Structure** : séparer le HTML, le JS inline minimal, et les styles via des blocs `<style>` situés en bas du template ou dans des fichiers statiques si volumineux.
- **Accessibilité** : utiliser des labels explicites, attributs `aria-*` lorsque nécessaire, contrastes suffisants. Tester en mobile (viewport meta).
- **Comportement** : tout script manipulant l’état doit vérifier les valeurs renvoyées par le backend; gérer les erreurs (`fetch` avec `try/catch`, `flash` côté serveur).
- **Design** : respecter les directives Frontend (pas de fonts par défaut, couleurs intentionnelles, animations limitées mais signifiantes). Documenter les palettes dans ce fichier si personnalisées.

## 5. Configuration, secrets et environnement

- **.env** : aucune valeur sensible ne doit être commitée. Fournir une version dans `.env.example`.
- **Variables dynamiques** : lorsqu’une variable d’environnement peut surcharger un paramètre (ex: `SWITCHBOT_POLL_INTERVAL_SECONDS`), synchroniser proprement dans `create_app`.
- **Validation** : lors du chargement de JSON (settings/state), vérifier les schémas attendus et loguer les champs inconnus.

## 6. Journalisation & observabilité

- Utiliser `current_app.logger` pour tout message serveur. N’écrire ni `print` ni logs silencieux.
- Préfixer les logs critiques par le contexte (`[scheduler]`, `[api]`, etc.) pour simplifier le filtrage.
- Ne jamais loguer de secrets ni de payloads contenant des données sensibles.

## 7. Tests & assurance qualité

- **Cas nominaux** : température stable, réglages valides, commandes SwitchBot OK.
- **Cas limites** : seuils avec hysteresis (limite ±0.1°C), JSON corrompu, credentials manquants, API 429/5xx.
- **Cas d’erreur** : IDs vides, réglages impossibles (min > max), timeouts SwitchBot, scheduler stoppé.
- Ajouter des tests unitaires pour toute logique de conversion/validation nouvellement créée. Décrire les scénarios manuels attendus dans `docs/README.md` si non automatisables.

## 8. Process de contribution

1. Créer une branche descriptive (`feature/hysteresis-config`).
2. Tenir `docs/` synchronisé lorsque vous introduisez de nouvelles commandes, paramètres ou flux.
3. Soumettre une PR avec :
   - description claire,
   - captures ou logs pertinents,
   - checklist de tests manuels effectués.
4. Revue :
   - vérifier sécurité (données utilisateurs, appels API),
   - double-check performance (boucles, appels réseau),
   - confirmer que les règles ci-dessus sont respectées.

## 9. Décisions et traçabilité

- Toute décision architecturale majeure doit être ajoutée dans `memory-bank/decisionLog.md` avec horodatage.
- Documenter les tâches en cours/terminées dans `memory-bank/progress.md` pour garder l’historique des efforts.

---
