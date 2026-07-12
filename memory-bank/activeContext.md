# Contexte Actif

## Objectifs
- [x] Résolution des vulnérabilités de sécurité P0 et P1 (mot de passe en clair DASHBOARD_PASSWORD, session authentifiée avec CSRF, page login glassmorphic, retrait du jeton de l'URL pour Bearer token).
- [x] Durcissement du stockage et SSL (sslmode explicite via kwargs, blocage de démarrage sans fallback JSON en production).
- [x] Optimisation des verrous et de la concurrence (appel API hors transaction PostgreSQL, verrou d'état distribué de 2 minutes pour éviter les conflits d'automatisation et d'UI).
- [x] Fiabilité des quotas et rate-limiting (correction de la métrique history_service.py vers api_requests_total, rafraîchissement réel des quotas via get_devices, rate-limiting global configurable).
- [x] Campagne d'intégration de tests unitaires et de non-régression complétée (164 tests passed, 0 failed).
- [x] Remédiation des défauts, vulnérabilités et ergonomie frontend de l'audit complétée (Navigation SPA, CTA mobile, A11y loaders et graphiques, sémantique HTML, allègement optimiseurs, local fonts et CSS critique).
- [x] Intégration complète de la configuration et des règles de l'écosystème Codex (Starlark, instructions AGENTS.md hiérarchiques, compatibilité de skills, guide de configuration).

## Décisions Clés
- Utilisation de règles Starlark déclaratives dans `.codex/rules/development.rules` pour autoriser les commandes de développement (pytest, git, activation venv) sans invites interactives.
- Découpage hiérarchique de `AGENTS.md` (racine) et `tests/AGENTS.md` (tests) pour rester sous le budget de 32 KiB imposé par Codex tout en conservant toutes les règles de développement.
- Standardisation des compétences (`.agents/skills/`) avec spécification Open Agent Skills et support de configuration via `agents/openai.yaml`.
- Correction du test `test_quota_refresh_route_makes_api_call` qui échouait à cause d'une session non authentifiée, rétablissant le statut 100% vert de la suite de tests (164/164).

## Prochaines Étapes
- En attente de nouveaux retours de l'utilisateur ou de démarrage d'une nouvelle tâche de développement.
