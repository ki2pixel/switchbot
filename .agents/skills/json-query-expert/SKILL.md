---
name: json-query-expert
description: Expert en manipulation de données JSON massives via le pattern "Sniper". Stratégie : Ne jamais charger un fichier > 1000 lignes. Inspection via json_query_query_json. Édition via edit_file.
---

# JSON Query Expert

> **Expertise** : Manipulation chirurgicale de JSON massifs, extraction précise de clés et valeurs, optimisation token pour fichiers de configuration.

## Quick Start

### Mental Model

JSON Query Expert utilise le pattern "Sniper" pour les fichiers JSON :
- Jamais de chargement complet de fichiers JSON volumineux (> 1000 lignes).
- Lecture ciblée du fichier, puis interrogation via les outils du serveur MCP `json-query` en passant le contenu JSON dans `json_data`.
- Localisation précise avant édition.
- Modification chirurgicale avec `edit_file` du serveur `filesystem-agent` ou les outils de remplacement d'API stricts.

### Workflow obligatoire

1. **Lecture sélective** : Lire le fichier JSON à l'aide de `view_file` (ou `fast_read_file`).
2. **Requête JSON** : Utiliser `json_query_query_json` en transmettant le JSON parsé pour inspecter les clés ou les valeurs cibles.
3. **Localisation** : Trouver la clé ou le bloc à éditer.
4. **Édition** : Appliquer les modifications avec `edit_file` de `filesystem-agent`.
5. **Validation** : Vérifier la conformité syntaxique du JSON après modification.

### Patterns d'utilisation Réels (MCP JSON)

#### 1. Inspection et modification de configuration

Pour interroger et modifier un paramètre dans un fichier `settings.json` :

```json
// Étape 1 : Lire le contenu de settings.json (si petit) ou une section identifiée
default_api:view_file({
  "AbsolutePath": "/home/kidpixel/SwitchBot/settings.json"
})

// Étape 2 : Interroger la configuration via le serveur MCP json-query
mcp:json-query/json_query_query_json({
  "json_data": {
    "scheduler": {
      "poll_interval_seconds": 30,
      "idle_timeout": 600
    },
    "automation": {
      "hysteresis": 1.5
    }
  },
  "query": "scheduler"
})

// Étape 3 : Éditer précisément la ligne avec edit_file
mcp:filesystem-agent/edit_file({
  "path": "/home/kidpixel/SwitchBot/settings.json",
  "edits": [
    {
      "oldText": "\"poll_interval_seconds\": 30,",
      "newText": "\"poll_interval_seconds\": 60,"
    }
  ]
})
```

## Token optimization strategies

### Pattern "Sniper" pour fichiers massifs

Ne jamais charger un gros fichier JSON entièrement dans le contexte de l'agent.

❌ **Incorrect** :
```json
default_api:view_file({
  "AbsolutePath": "/home/kidpixel/SwitchBot/massive_manifest.json"
}) // +10000 lignes chargées = explosion du contexte !
```

✅ **Correct** :
Utiliser des outils d'API ou de recherche ciblés, ou charger des segments si possible, pour inspecter les parties critiques. Si le fichier est structuré, on peut le lire en plusieurs fois par plages de lignes, ou charger les variables d'environnement de configuration pour les petites interrogations.

## API Reference (Vrais Outils MCP de json-query)

Le serveur MCP `json-query` dispose de trois outils clés opérant sur des structures JSON en mémoire :

### 1. `json_query_query_json`
Effectue une requête simple par clé sur un objet JSON.
- **Paramètres** :
  - `json_data` (object) : L'objet JSON à interroger.
  - `query` (string) : La clé ou le chemin simple de clé à extraire.

### 2. `json_query_search_keys`
Extrait et liste toutes les clés présentes dans un objet JSON.
- **Paramètres** :
  - `json_data` (object) : L'objet JSON dont on veut extraire les clés.

### 3. `json_query_search_values`
Recherche toutes les valeurs correspondant à une clé donnée dans un objet JSON.
- **Paramètres** :
  - `json_data` (object) : L'objet JSON dans lequel chercher.
  - `key` (string) : La clé dont on veut récupérer les valeurs.

## When to use this skill

- **Fichiers de configuration** : settings.json, ifttt_webhooks.json, state.json.
- **Fichiers de traduction (i18n)** : Fichiers JSON contenant des chaînes de traduction.
- **Diagnostics complexes** : Dumps, mock de données ou fixtures d'API au format JSON.

## Integration patterns

### Avec Fast Filesystem
Utiliser `fast_read_file` pour récupérer le contenu de la configuration puis le passer à `json_query_query_json`.

### Avec Sequential Thinking
Valider la logique de restructuration JSON avec `sequentialthinking_tools` avant d'appliquer les éditions complexes.