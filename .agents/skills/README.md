# SwitchBot Dashboard — Agent Skills

Ce répertoire contient les skills Kimi Code CLI pour le projet SwitchBot Dashboard, convertis depuis les workflows Windsurf.

## Structure

```
.agents/skills/
├── README.md           # Ce fichier
├── USAGE.md            # Guide d'utilisation détaillé
├── commit-push/        # Commit et push automatisé
├── documentation/      # Standards de rédaction documentation
├── docs-updater/       # Mise à jour documentation métrique
├── end/                # Terminer la session et synchroniser Memory Bank
├── enhance/            # Améliorer un prompt avec contexte technique
└── enhance-complex/    # Architecture complexe avec Shrimp Task Manager
```

## Skills Disponibles

| Skill | Commande | Description |
|-------|----------|-------------|
| **end** | `/skill:end` | Terminer la session et synchroniser la Memory Bank |
| **enhance** | `/skill:enhance` | Transformer une demande en spécification technique structurée |
| **docs-updater** | `/skill:docs-updater` | Mise à jour documentation avec analyse statique (`cloc`, `radon`, `tree`) |
| **enhance-complex** | `/skill:enhance-complex` | Planification de tâches complexes avec Shrimp Task Manager |
| **commit-push** | `/skill:commit-push` | Commit et push automatisé vers le remote |
| **documentation** | `/skill:documentation` | Standards de rédaction documentation et README |

## Détails des Skills

### `/skill:end`

Fermeture propre d'une session de travail avec synchronisation complète de la Memory Bank :
- Charge le contexte minimal (`activeContext.md`, `progress.md`)
- Exécute le protocole Memory Bank
- Met à jour les fichiers avec les décisions et progrès
- Vérifie l'état neutre final

### `/skill:enhance`

Prompt Engineer pour transformer une demande brute en MEGA-PROMPT structuré :
- Analyse l'intention sans exécuter
- Charge les skills techniques pertinents
- Génère un bloc Markdown avec MISSION, CONTEXTE, INSTRUCTIONS, CONTRAINTES

### `/skill:docs-updater`

Workflow d'harmonisation de la documentation avec métriques :
- Audit structurel (`tree`, `cloc`, `radon`)
- Diagnostic triangulé (Intention vs Réalité vs Existant)
- Application des standards de rédaction

### `/skill:enhance-complex`

Architecture pour tâches multi-étapes avec outils MCP :
- Planification Shrimp Task Manager
- Réflexion séquentielle
- Vérification et documentation

### `/skill:commit-push`

Workflow de commit et push automatisé :
- Format Conventional Commits
- Vérifications de qualité optionnelles
- Push vers la branche courante

### `/skill:documentation`

Standards de rédaction pour documentation technique :
- Structure TL;DR First
- Comparaisons ❌/✅
- Éviter le style "AI-generated"
- Guidelines README

## Migration depuis Windsurf

Ces skills ont été convertis depuis `.windsurf/workflows/` :

| Workflow Windsurf | Skill Kimi Code CLI |
|-------------------|---------------------|
| `end.md` | `end/SKILL.md` |
| `enhance.md` | `enhance/SKILL.md` |
| `docs-updater.md` | `docs-updater/SKILL.md` |
| `enhance_complex.md` | `enhance-complex/SKILL.md` |
| `commit-push.md` | `commit-push/SKILL.md` |
| `.windsurf/skills/documentation/` | `documentation/SKILL.md` |

## Voir aussi

- [USAGE.md](./USAGE.md) — Guide d'utilisation détaillé
- [AGENTS.md](../../AGENTS.md) — Contexte projet pour agents IA
- `.clinerules/` — Règles de codage et protocoles
