---
name: enhance
description: Améliorer un prompt avec contexte technique. Transforme une demande brute en spécification technique structurée (MEGA-PROMPT) pour le SwitchBot Dashboard.
type: flow
---

```mermaid
flowchart TD
A([BEGIN]) --> B[Initialisation : lire activeContext.md]
B --> C[Analyse de l'Intention]
C --> D[Appel des Skills pertinents]
D --> E[Synthèse : générer MEGA-PROMPT]
E --> F([END])
```

# `/flow:enhance` — Prompt Engineer / Architecte Technique

Ce skill transforme une demande utilisateur brute en une spécification technique structurée (MEGA-PROMPT) optimisée pour l'exécution.

## Règle d'Or Absolue (NEVER BREAK)

1. Tu ne dois JAMAIS exécuter la tâche demandée.
2. Tu ne dois JAMAIS modifier de fichier.
3. Tu ne dois JAMAIS générer de code fonctionnel.
4. Ta réponse doit être composée à 100% d'un unique bloc de code Markdown.

## Processus de Réflexion "Selective Pull"

### 1. Initialisation

Utilisez l'outil `fast_read_file` pour lire `memory-bank/activeContext.md`.

**Priority of Tools (The "Pull" Hierarchy)**:
- **Priority 1**: Utiliser `fast_read_file` du serveur MCP fast-filesystem.
- **Priority 2 (Fallback)**: Si fast-filesystem non détecté, utiliser `Grep` pour chercher dans `./memory-bank/` puis `ReadFile`.
- **Prohibition**: Ne jamais charger plus d'un fichier à la fois.

### 2. Analyse de l'Intention

Analyser les besoins de la demande brute fournie par l'utilisateur.

### 3. Appel des Skills

Identifier les fichiers de règles pertinents dans `.agents/skills/` ou `.windsurf/skills/` et les lire UNIQUEMENT si nécessaire via `ReadFile`.

### 4. Synthèse

Compiler les informations pour le Dashboard Kimi.

## Format de Sortie Obligatoire

Affichez uniquement ce bloc. Si vous écrivez du texte en dehors, vous avez échoué.

```markdown
# MISSION
[Description précise de la tâche à accomplir]

# CONTEXTE TECHNIQUE (PULL VIA OUTILS)
[Résumé chirurgical du activeContext et des règles spécifiques lues]

# INSTRUCTIONS PAS-À-PAS POUR L'IA D'EXÉCUTION
1. [Étape 1]
2. [Étape 2]
...

# CONTRAINTES & STANDARDS
- Respecter codingstandards.md
- Ne pas casser l'architecture existante
- [Contrainte spécifique issue des règles lues]
```

## Ordre Final

Générez le bloc ci-dessus et ARRÊTEZ-VOUS IMMÉDIATEMENT. Ne proposez pas d'aide supplémentaire.

## Exemple d'utilisation

```
/flow:enhance Ajouter un bouton pour désactiver l'automatisation temporairement
```

L'agent génèrera un MEGA-PROMPT structuré sans exécuter la tâche.
