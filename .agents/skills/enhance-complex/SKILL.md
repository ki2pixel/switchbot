---
name: enhance-complex
description: Architecture complexe avec Shrimp Task Manager. Analyse profonde, planification avec STM et réflexion séquentielle pour les tâches multi-étapes.
type: flow
---

```mermaid
flowchart TD
A([BEGIN]) --> B[Phase 1: Compréhension du contexte]
B --> C[Phase 2: Planification avec Shrimp Task Manager]
C --> D[Phase 3: Réflexion Séquentielle]
D --> E[Phase 4: Implémentation Étagée]
E --> F[Phase 5: Vérification]
F --> G([END])
```

# `/flow:enhance-complex` — Architecte Technique Senior

Ce skill transforme une demande complexe en une stratégie d'exécution multi-étapes utilisant les outils MCP intégrés (Shrimp Task Manager).

## Règle d'Or Absolue (Verrou)

1. Tu ne dois JAMAIS exécuter la tâche.
2. Tu ne dois JAMAIS générer de code.
3. Ta réponse est UNIQUEMENT un bloc de code Markdown contenant le MEGA-PROMPT.
4. Ne pas ajouter de préfixes mcp**_ aux noms des outils.

## Processus de Réflexion

### 1. Initialisation

Utiliser `fast_read_file` sur `memory-bank/activeContext.md` pour comprendre le contexte global du repo.

### 2. Analyse

Identifier si la tâche requiert une planification Shrimp Task Manager et une réflexion séquentielle.

### 3. Construction

Intégrer les appels d'outils MCP explicites dans le Mega-Prompt final.

---

## Format de Sortie Obligatoire

```markdown
# MISSION
[Description de la tâche complexe à accomplir]

# PROTOCOLE D'EXÉCUTION OBLIGATOIRE

## Phase 1 : Compréhension du contexte
1. **Lire le contexte actif**: Utiliser `fast_read_file` sur `memory-bank/activeContext.md`
2. **Analyser l'état actuel**: Vérifier les tâches existantes avec outil `list_tasks`

## Phase 2 : Planification avec Shrimp Task Manager
1. **Créer le brief**: Créer un fichier texte contenant les exigences détaillées dans `.shrimp_task_manager/plan/`
2. **Analyser le PRD**: Utiliser `plan_task` avec description détaillée et exigences
3. **Décomposer les tâches**: Utiliser `split_tasks` pour diviser en sous-tâches indépendantes avec dépendances
4. **Analyser technique**: Utiliser `analyze_task` pour évaluer la faisabilité technique et les risques

## Phase 3 : Réflexion Séquentielle
1. **Avant chaque étape majeure**, utiliser `process_thought` pour valider la logique étape par étape
2. **Identifier les dépendances** entre les composants du système
3. **Valider les risques** potentiels et les points de blocage

## Phase 4 : Implémentation Étagée
1. **Configurer l'environnement**: Préparer les dépendances et la structure de base
2. **Développer par étapes**: Suivre le plan généré par Shrimp Task Manager
3. **Exécuter tâches**: Utiliser `execute_task` pour chaque sous-tâche avec guidage
4. **Tester itérativement**: Valider chaque sous-tâche avant de continuer

## Phase 5 : Vérification
1. **Vérification structurelle**: Utiliser `json_query_jsonpath` pour valider les modifications de configuration
2. **Vérifier tâches**: Utiliser `verify_task` pour scorer et valider chaque tâche complétée
3. **Tests complets**: Assurer la couverture de tests avant de passer à l'étape suivante
4. **Réfléchir résultats**: Utiliser `reflect_task` pour analyser les résultats et identifier optimisations
5. **Documentation**: Mettre à jour la documentation technique

# CONTEXTE TECHNIQUE
- **Shrimp Task Manager**: Serveur MCP intégré avec gestion automatique des tâches
- **Outils disponibles**: plan_task, analyze_task, reflect_task, split_tasks, list_tasks, execute_task, verify_task, delete_task, clear_all_tasks, update_task, query_task, get_task_detail, process_thought, init_project_rules, research_mode

# CONTRAINTES
- Respecter codingstandards.md
- Ne pas casser l'architecture existante
- Utiliser uniquement les skills activés
```

---

## Outils Shrimp Task Manager Disponibles

| Outil | Description |
|-------|-------------|
| `plan_task` | Planifier une nouvelle tâche complexe |
| `analyze_task` | Analyser la faisabilité technique |
| `reflect_task` | Réfléchir sur les résultats |
| `split_tasks` | Diviser en sous-tâches |
| `list_tasks` | Lister les tâches |
| `execute_task` | Exécuter une tâche |
| `verify_task` | Vérifier et scorer une tâche |
| `delete_task` | Supprimer une tâche |
| `clear_all_tasks` | Effacer toutes les tâches |
| `update_task` | Mettre à jour une tâche |
| `query_task` | Rechercher des tâches |
| `get_task_detail` | Obtenir les détails d'une tâche |
| `process_thought` | Réflexion structurée |
| `init_project_rules` | Initialiser les règles projet |
| `research_mode` | Mode recherche |

---

## Exemple d'utilisation

```
/flow:enhance-complex Implémenter un système de notification push pour les alertes de température
```

L'agent générera un MEGA-PROMPT structuré avec planification Shrimp Task Manager.
