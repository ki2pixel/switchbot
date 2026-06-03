---
name: sequentialthinking-logic
description: Expert en raisonnement décomposé. Force l'usage de sequentialthinking_tools pour valider la logique Background/Content Script des extensions et architectures complexes.
---

# Sequential Thinking Logic

> **Expertise** : Raisonnement décomposé, validation logique, analyse étape par étape, pensée structurée pour architectures complexes via MCP.

## Quick Start

### Mental Model

Sequential Thinking Logic décompose les problèmes complexes en séquences de pensée logiques validées dynamiquement.
L'outil MCP `sequentialthinking_tools` permet d'exécuter un raisonnement par étapes (chaînes de pensées rigoureuses) pour :
- Décomposer une architecture ou un flux de données (ex: Background Script vs Content Script).
- Formuler et tester des hypothèses de manière isolée.
- Anticiper et identifier les points de rupture et cas limites.
- Garantir une progression structurée exempte de dépendances circulaires.

### Workflow obligatoire

1. **Initialisation** : Lancer la première étape de pensée avec `sequentialthinking_tools` en décrivant le `problem`.
2. **Progression séquentielle** : Dérouler les étapes logiques en incrémentant `thought_number`, en détaillant la pensée dans `thought` et en indiquant si une étape suivante est requise (`next_thought_needed`).
3. **Analyse de structure** : Valider séparément les composants (par ex. isoler la logique Background Script de la logique Content Script).
4. **Validation logique** : Conclure la séquence logique lorsque le problème est résolu en fixant `next_thought_needed` à `false`.

### Patterns d'utilisation Réels (MCP JSON)

Voici comment invoquer dynamiquement `sequentialthinking_tools` pour concevoir une architecture d'extension ou analyser un flux d'authentification complexe :

```json
// Étape 1 : Initialiser la pensée en définissant le problème global
mcp:sequential-thinking/sequentialthinking_tools({
  "problem": "Concevoir l'architecture de communication bidirectionnelle sécurisée entre un Background Script et un Content Script d'une extension Chrome.",
  "thought": "1. Décomposer les composants principaux : Le Content Script (côté DOM utilisateur) et le Background Script (contexte privilégié de l'extension). La communication doit se faire via des ports durables chrome.runtime.connect.",
  "thought_number": 1,
  "total_thoughts": 4,
  "next_thought_needed": true
})

// Étape 2 : Analyser la logique de sécurité et d'injection
mcp:sequential-thinking/sequentialthinking_tools({
  "problem": "Concevoir l'architecture de communication bidirectionnelle sécurisée entre un Background Script et un Content Script d'une extension Chrome.",
  "thought": "2. Analyser le Content Script : Il s'exécute dans un contexte isolé du DOM mais partage la même page. Il doit valider strictement les messages reçus de la page web avant de les transférer au Background pour éviter les injections de privilèges.",
  "thought_number": 2,
  "total_thoughts": 4,
  "next_thought_needed": true
})

// Étape 3 : Structurer la gestion d'état et les cas limites
mcp:sequential-thinking/sequentialthinking_tools({
  "problem": "Concevoir l'architecture de communication bidirectionnelle sécurisée entre un Background Script et un Content Script d'une extension Chrome.",
  "thought": "3. Analyser le Background Script : C'est le cœur de l'extension. Il gère l'état global et appelle les API externes. Si le port de communication se déconnecte accidentellement, il doit implémenter un mécanisme de reconnexion automatique (onDisconnectListener).",
  "thought_number": 3,
  "total_thoughts": 4,
  "next_thought_needed": true
})

// Étape 4 : Conclure et formaliser le flux logique validé
mcp:sequential-thinking/sequentialthinking_tools({
  "problem": "Concevoir l'architecture de communication bidirectionnelle sécurisée entre un Background Script et un Content Script d'une extension Chrome.",
  "thought": "4. Synthèse et flux logique validé : [User Action] -> [Content Script (validation)] -> [chrome.runtime Port] -> [Background Script (traitement API)] -> [Retour de réponse avec gestion d'erreurs]. L'architecture est exempte de cycles et isole parfaitement les responsabilités. Prêt pour l'implémentation.",
  "thought_number": 4,
  "total_thoughts": 4,
  "next_thought_needed": false
})
```

## Token optimization strategies

### Clarté et concision des pensées

N'allongez pas inutilement les descriptions textuelles dans l'argument `thought`. Restez ultra-focalisé sur les aspects purement techniques, architecturaux et logiques de l'étape courante.

## API Reference (Vrais Outils MCP de sequential-thinking)

Le serveur MCP `sequential-thinking` fournit un unique outil puissant :

### `sequentialthinking_tools`
Exécute une étape dans une chaîne de raisonnement logique structurée.
- **Paramètres** :
  - `problem` (string) : Description claire et unique du problème global en cours de résolution.
  - `thought` (string) : Le contenu textuel détaillé de la pensée logique courante.
  - `thought_number` (integer) : L'index de l'étape de pensée courante (commence à 1).
  - `total_thoughts` (integer) : Le nombre total estimé d'étapes de pensée requises pour résoudre le problème.
  - `next_thought_needed` (boolean) : Mettre à `true` si d'autres étapes de pensée sont nécessaires pour conclure le raisonnement, ou `false` s'il s'agit de l'étape finale.

## When to use this skill

- **Architectures complexes** : Extensions web (Background vs Content), microservices, communication distribuée.
- **Logiques métier critiques** : Algorithmes de transaction, cascades IFTTT, agrégations PostgreSQL.
- **Résolution de bugs complexes** : Analyse des causes profondes et diagnostic d'anomalies de concurrence ou d'état.

## Integration patterns

### Avec Shrimp Task Manager
Utiliser `sequentialthinking_tools` pour valider la logique de planification d'un backlog complexe généré par `split_tasks`.

### Avec Fast Filesystem
Valider la logique de refactoring à l'aide de `sequentialthinking_tools` avant d'appliquer les éditions via `edit_file`.