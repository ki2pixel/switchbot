# Contexte Actif

## Objectifs
- Aucune tâche active.
- [x] Campagne d'archivage de la Memory Bank effectuée : Les entrées antérieures au 2026-04-05 de `decisionLog.md` et `progress.md` ont été déplacées vers `archives/decisionLog_2026Q1.md` et `archives/progress_2026Q1.md`.
- [x] Audit d'alignement des Skills IA avec la base de code (post-SonarCloud et migrations BDD) réalisé et validé.
- [x] Alignement de la documentation technique (v2) avec le code réel, via le workflow `/docs-updater`.

## Décisions Clés
- Mise en place d'une politique d'archivage trimestriel pour réduire la taille des fichiers de la Memory Bank et optimiser l'usage des tokens via le `fast-filesystem`.

## Modifications Skills Effectuées
- Mise à jour de `add-feature/SKILL.md` (SPA Router, CSRF).
- Mise à jour de `postgres-store-maintenance/SKILL.md` (gestion de contextes psycopg_pool).
- Mise à jour de `ifttt-cascade/SKILL.md` (sécurité SSRF et timing attacks).

## Modifications Documentaires Effectuées
- **`docs/README.md`** : Correction de l'information sur le suivi de quota (approche hybride et synchronisation des headers SwitchBot confirmées).
- **`docs/architecture/storage-layer.md`** : Ajout de la gestion du connection pool (`psycopg_pool`) et des transactions avec row-level locking.
- **`docs/guides/ifttt-setup.md`** : Documentation des sécurités SSRF (blocage IPs locales et domaine strict) et contre les Timing Attacks (`hmac.compare_digest`).
- **`docs/guides/ui-navigation.md`** : Explication du cycle de vie des pages SPA (`spa-router.js`) et de la protection CSRF globale.

## Questions/Problèmes Ouverts
- Aucun.

## Prochaines Étapes
- En attente de nouvelles instructions.
