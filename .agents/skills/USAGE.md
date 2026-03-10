# Guide d'Utilisation des Skills Kimi Code CLI

Ce guide explique comment utiliser les skills du projet SwitchBot Dashboard dans Kimi Code CLI.

## Principe de Base

Les skills sont automatiquement découverts par Kimi Code CLI au démarrage. L'agent IA décide de lire le `SKILL.md` approprié en fonction du contexte de la conversation.

## Invocation Manuelle

Vous pouvez forcer le chargement d'un skill avec la commande slash :

```bash
/skill:end              # Terminer une session
/skill:enhance          # Améliorer un prompt
/skill:docs-updater     # Mettre à jour la documentation
/skill:enhance-complex  # Planifier une tâche complexe
/skill:commit-push      # Committer et pusher
/skill:documentation    # Standards de rédaction
```

Vous pouvez ajouter du contexte après la commande :

```bash
/skill:enhance Ajouter un bouton de désactivation temporaire de l'automatisation
/skill:commit-push fix: correct temperature threshold calculation
```

## Cas d'Usage par Skill

### `/skill:end` — Fin de Session

**Quand l'utiliser :**
- À la fin d'une session de travail
- Avant de fermer Kimi Code CLI
- Pour sauvegarder le contexte et les décisions

**Exemple :**
```
/skill:end
```

**Résultat :**
- `activeContext.md` mis à jour
- `progress.md` synchronisé
- État neutre vérifié

---

### `/skill:enhance` — Amélioration de Prompt

**Quand l'utiliser :**
- Pour transformer une idée en spécification technique
- Avant de démarrer une nouvelle fonctionnalité
- Pour obtenir un plan structuré sans exécution

**Exemple :**
```
/skill:enhance Implémenter un système de notification par email pour les alertes de température
```

**Résultat :**
```markdown
# MISSION
Implémenter un système de notification par email...

# CONTEXTE TECHNIQUE
[Résumé du activeContext et règles]

# INSTRUCTIONS PAS-À-PAS
1. [Étape 1]
2. [Étape 2]
...

# CONTRAINTES & STANDARDS
- Respecter codingstandards.md
- ...
```

---

### `/skill:docs-updater` — Mise à Jour Documentation

**Quand l'utiliser :**
- Après des changements significatifs dans le code
- Pour harmoniser la documentation avec le code réel
- Quand la documentation est dépassée

**Exemple :**
```
/skill:docs-updater
```

**Résultat :**
- Audit avec `cloc`, `radon`, `tree`
- Identification des divergences code/docs
- Propositions de mise à jour

---

### `/skill:enhance-complex` — Tâches Complexes

**Quand l'utiliser :**
- Pour les fonctionnalités multi-étapes
- Quand une planification détaillée est nécessaire
- Pour utiliser Shrimp Task Manager

**Exemple :**
```
/skill:enhance-complex Refactoriser le système d'automatisation pour supporter plusieurs types de devices
```

**Résultat :**
- Plan complet avec 5 phases
- Intégration Shrimp Task Manager
- Outils MCP identifiés

---

### `/skill:commit-push` — Commit et Push

**Quand l'utiliser :**
- Après avoir terminé des changements
- Pour commit avec format Conventional Commits
- Pour pousser vers le remote

**Exemple :**
```
/skill:commit-push feat: add email notification for temperature alerts
```

**Résultat :**
- Staging des changements
- Commit avec message formaté
- Push vers `origin <current-branch>`

---

### `/skill:documentation` — Standards de Rédaction

**Quand l'utiliser :**
- Pour écrire de la documentation technique
- Pour éviter le style "AI-generated"
- Pour structurer un README

**Exemple :**
```
/skill:documentation
```

**Checkpoints appliqués :**
- TL;DR en premier
- Ouverture orientée problème
- Comparaisons ❌/✅
- Tableau de trade-offs
- Golden Rule

---

## Bonnes Pratiques

### 1. Laissez l'IA choisir

Pour les conversations normales, l'IA décidera automatiquement de lire le skill approprié :

```
"Je veux améliorer la documentation du module quota"
```

L'IA lira automatiquement `docs-updater/SKILL.md` et `documentation/SKILL.md`.

### 2. Soyez explicite pour les workflows

Pour les workflows spécifiques, utilisez les commandes slash :

```
/skill:end
```

### 3. Combinez les skills

Vous pouvez enchaîner les skills :

```
/skill:enhance <votre demande>
# ... après review du MEGA-PROMPT ...
/skill:enhance-complex <demande détaillée>
# ... après planification ...
# implémentation ...
/skill:commit-push feat: implement <feature>
/skill:end
```

### 4. Ajoutez du contexte

Les commandes slash acceptent du texte additionnel :

```
/skill:enhance --focus=security Ajouter l'authentification 2FA
```

---

## Différences avec Windsurf

| Aspect | Windsurf | Kimi Code CLI |
|--------|----------|---------------|
| Chemin | `.windsurf/workflows/` | `.agents/skills/` |
| Fichier | `<name>.md` | `<name>/SKILL.md` |
| Format | YAML + Markdown | YAML frontmatter + Markdown |
| Invocation | Automatique | `/skill:<name>` |
| Outils | `run_command` | `Shell` |

---

## Dépannage

### Le skill n'est pas détecté

Vérifiez que :
1. Le répertoire est `.agents/skills/`
2. Le fichier est nommé `SKILL.md`
3. Le YAML frontmatter est valide

### L'outil `run_command` n'existe pas

Les workflows Windsurf utilisaient `run_command`. Dans Kimi Code CLI, utilisez l'outil `Shell` :

```markdown
# Windsurf
`run_command "tree -L 3"`

# Kimi Code CLI
Utiliser l'outil `Shell` avec la commande `tree -L 3`
```

---

## Références

- [Kimi Code CLI Skills Documentation](../docs/docs-kimi-code_extension/customization/skills.md)
- [Agent Skills Specification](https://agentskills.io/)
- [AGENTS.md](../../AGENTS.md) — Contexte projet
