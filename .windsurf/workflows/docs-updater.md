---
description: Docs Updater (Context-Aware with Code Verification)
---

# Workflow: Docs Updater (Context-Aware with Code Verification)

## Étape 0 · Préambule
- Se conformer aux règles globales (Memory Bank, coding standards, test strategy) avant toute action.
- N'utiliser que les outils autorisés : `read_file`, `find_by_name`, `list_dir`, `code_search`, `grep_search`, `apply_patch`, `write_to_file`, etc. Éviter `run_command` lorsqu'un outil spécialisé existe.

## Étape 1 · Acquisition du Contexte (Pourquoi ?)
1. Utiliser `read_file` pour charger **progress.md**, **decisionLog.md**, **productContext.md**, **systemPatterns.md**.
2. Synthétiser mentalement les décisions et fonctionnalités récentes.

## Étape 2 · Cartographie de la Documentation (Qu'est déjà documenté ?)
1. Inventorier la structure de `docs/` via `find_by_name` (ex. `find_by_name docs --pattern "**/*.md"`) ou, pour une vision hiérarchique rapide, `list_dir` sur les sous-dossiers pertinents.
2. Identifier les fichiers candidats à la mise à jour.

## Étape 3 · Inspection du Code Source (Quoi ?)
1. À partir des informations de l'Étape 1, cibler les modules/fichiers impactés.
2. Utiliser `code_search` pour localiser les portions pertinentes, puis `read_file` pour les analyser précisément. Compléter avec `grep_search` si nécessaire.
3. Vérifier signatures, docstrings, logique métier, et comparer avec l'état de la documentation.

## Étape 4 · Triangulation
Sans outils, croiser :
- **Pourquoi** (Memory Bank)
- **Quoi** (code source inspecté)
- **Existant** (structure docs)

Questions clés :
- La doc reflète-t-elle encore les comportements actuels ?
- Des signatures ou paramètres ont-ils changé ?
- Des patterns récents (systemPatterns) manquent-ils dans les guides ?

## Étape 5 · Rapport final / Plan de mise à jour
Rédiger (Markdown) :

```
## 📚 Assistant de Documentation (Analyse Triangulée)

### 1. Diagnostic des Changements
[Résumé]

### 2. Preuves du Code (Code Evidence)
- `@chemin#Lx-Ly` : divergence constatée

### 3. Plan de Mise à Jour
#### 📄 Fichier : docs/xxx.md
- **Problème identifié** : ...
- **Suggestion précise** :
  ```markdown
  [Texte ou diff conceptuel]
  ```
```

Conclure en demandant confirmation avant toute modification (`apply_patch` ou `write_to_file`).