---
name: fast-filesystem-ops
description: Expert en édition chirurgicale. Obligation d'utiliser edit_file pour préserver les tokens. Recherche globale via grep_search.
---

# Fast Filesystem Operations

> **Expertise** : Édition chirurgicale de fichiers, optimisation token, recherche textuelle efficace, manipulation précise de codebase via MCP.

## Quick Start

### Mental Model

Fast Filesystem Ops optimise chaque opération de fichier pour minimiser l'usage de tokens :
- Recherche textuelle ciblée avec `grep_search` (outil d'API standard) pour localiser le code.
- Recherche de fichiers par nom avec `fast_search_files` (substring match sur le nom du fichier).
- Lecture ciblée via `view_file` (ou `fast_read_file` pour la Memory Bank).
- Édition chirurgicale et fine avec `edit_file` du serveur `filesystem-agent` pour éviter les réécritures complètes.

### Workflow obligatoire

1. **Localisation textuelle** : Utiliser `grep_search` pour trouver le code cible précis.
2. **Recherche de structure** : `fast_search_files` si vous cherchez simplement un fichier par son nom.
3. **Lecture chirurgicale** : `view_file` (ou `fast_read_multiple_files` si plusieurs fichiers sont nécessaires) pour lire uniquement les sections indispensables.
4. **Édition ciblée** : `edit_file` avec des blocs d'édition précis (`oldText`/`newText`).
5. **Validation** : Vérifier que les modifications préservent la validité syntaxique.

### Patterns d'utilisation Réels (MCP JSON)

#### 1. Localisation et lecture d'une fonction spécifique

Pour localiser et éditer une fonction `calculate_total` :

```json
// Étape 1 : Localiser précisément la fonction dans le codebase
default_api:grep_search({
  "Query": "def calculate_total",
  "SearchPath": "/home/kidpixel/SwitchBot"
})

// Étape 2 : Lire la section de code identifiée
default_api:view_file({
  "AbsolutePath": "/home/kidpixel/SwitchBot/src/calculations.py",
  "StartLine": 45,
  "EndLine": 67
})

// Étape 3 : Éditer précisément
mcp:filesystem-agent/edit_file({
  "path": "/home/kidpixel/SwitchBot/src/calculations.py",
  "edits": [
    {
      "oldText": "def calculate_total(a, b):\n    return a + b",
      "newText": "def calculate_total(a, b):\n    # Utilise un typage précis\n    return float(a + b)"
    }
  ]
})
```

## Token optimization strategies

### Éviter les chargements massifs de fichiers

Ne chargez pas un fichier de plus de 1000 lignes avec `read_file` ou `view_file` sans cibler les lignes :

❌ **Incorrect** :
```json
default_api:view_file({
  "AbsolutePath": "/home/kidpixel/SwitchBot/large_file.py"
}) // Plus de 5000 lignes lues d'un coup = gaspillage de tokens !
```

✅ **Correct** :
```json
default_api:view_file({
  "AbsolutePath": "/home/kidpixel/SwitchBot/large_file.py",
  "StartLine": 120,
  "EndLine": 150
})
```

## API Reference (Vrais Outils MCP & Standard API)

### Outils de Recherche
- **`default_api:grep_search`** : Recherche textuelle précise par pattern (regex ou literal) dans un répertoire/fichier.
  - `Query` (string) : Texte à chercher.
  - `SearchPath` (string) : Chemin absolu.
- **`mcp:fast-filesystem/fast_search_files`** : Recherche simple de fichiers par substring match sur le nom du fichier.
  - `directory` (string) : Répertoire de recherche.
  - `pattern` (string) : Nom du fichier ou partie du nom.

### Outils de Lecture
- **`default_api:view_file`** : Outil standard hautement optimisé pour visualiser le contenu d'un fichier (supporte `StartLine` et `EndLine`).
- **`mcp:fast-filesystem/fast_read_multiple_files`** : Lecture simultanée de plusieurs fichiers.
  - `paths` (array de strings) : Liste des chemins de fichiers.
- **`mcp:fast-filesystem/fast_read_file`** : Lecture ciblée (particulièrement recommandé pour la Memory Bank).
  - `path` (string) : Chemin absolu.

### Outils d'Écriture et Modification
- **`mcp:filesystem-agent/edit_file`** : Édition chirurgicale ligne par ligne.
  - `path` (string) : Chemin absolu du fichier.
  - `edits` (array) : `{ "oldText": "...", "newText": "..." }`.
  - `dryRun` (boolean) : Pour prévisualiser les changements.
- **`default_api:replace_file_content`** / **`default_api:multi_replace_file_content`** : Outils par défaut hautement performants pour les remplacements de blocs de code contigus ou non.

## When to use this skill

- **Fichiers volumineux** : Quand les fichiers dépassent 1000 lignes.
- **Modifications ciblées** : Pour modifier des fonctions spécifiques sans toucher au reste.
- **Optimisation de tokens** : Pour garder la fenêtre de contexte propre et réactive.
- **Opérations sur la Memory Bank** : Pour manipuler chirurgicalement `activeContext.md` et `progress.md`.

## Integration patterns

### Avec Sequential Thinking
Valider la logique de l'édition avec `sequentialthinking_tools` avant d'appliquer `edit_file`.

### Avec JSON Query
Utiliser `json_query_query_json` pour inspecter et interroger un fichier JSON complexe avant de modifier ses clés avec `edit_file`.