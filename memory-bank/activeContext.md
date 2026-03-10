# Mise à jour du contexte actif

# Contexte Actif - Conformité Skills

## Objectifs
- ✅ **Passe de conformité des skills terminée** : Audit et mise à jour de 13 SKILL.md dans `.agents/skills/` et `.windsurf/skills/`.

## Décisions Clés
- **Polling adaptatif implémenté** : SchedulerService calcule intervalles effectifs (idle/warmup/in-window) avec auto-reschedule et garantie réveil warmup. Tests unitaires OK (12 passed). Plan d'action UI/Postgres créé dans `docs/adaptive-polling-settings-plan.md`.
- **Intégration UI/Postgres des réglages de polling adaptatif terminée** : Toggle + champs idle/warmup ajoutés dans settings.html, validation backend via `_as_bool/_as_int`, documentation complète (configuration.md + scheduler.md), tests couvrant persistance UI et mode fixe. 33 tests passants.
- **Skills synchronisés (2026-03-09)** : Les SKILL.md ont été mis à jour pour refléter le polling adaptatif et les patterns actuels. Les scripts/references manquants ont été synchronisés depuis `.windsurf/skills/` vers `.agents/skills/`.

## Modifications Skills Effectuées
| Skill | Action |
|-------|--------|
| `scheduler-ops` | Ajouté polling adaptatif, corrigé signature `reschedule()` |
| `automation-diagnostics` | Ajouté `assumed_aircon_mode` |
| `quota-alerting` | Ajouté tests polling adaptatif |
| `postgres-ops-manager` | Corrigé tables SQL (`state_history`, `history_entries`) |
| `render-postgres-integration` | Ajouté avertissement scripts placeholder |
| `render-service-manager` | Ajouté avertissement scripts placeholder |
| Tous les skills | Synchronisé scripts/references depuis `.windsurf/skills/` |

## Questions/Problèmes Ouverts
- Aucun problème ouvert.

## Prochaines Étapes
- En attente d'une nouvelle tâche utilisateur.
