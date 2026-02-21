---
name: docs-updater
description: Docs Updater (Context-Aware with Code Verification)
invokable: true
---

# Workflow: Docs Updater — Standardized & Metric-Driven

> Ce workflow harmonise la documentation en utilisant l'analyse statique standard (`cloc`, `radon`, `tree`) pour la précision technique et les modèles de référence pour la qualité éditoriale.

## 🚨 Protocoles Critiques
1.  **Outils autorisés** : L'usage de `run_command` est **strictement limité** aux commandes d'audit : `tree`, `cloc`, `radon`, `ls`.
2.  **Contexte** : Initialiser le contexte en appelant l'outil `fast_read_file` du serveur fast-filesystem pour lire UNIQUEMENT `activeContext.md`. Ne lire les autres fichiers de la Memory Bank que si une divergence majeure est détectée lors du diagnostic.
3.  **Source de Vérité** : Le Code (analysé par outils) > La Documentation existante > La Mémoire.
4.  **Interdiction formelle d'utiliser les outils `filesystem` (read_text_file) pour accéder au dossier `memory-bank/`. Passez toujours par le serveur MCP dédié pour garantir le tracking des tokens dans le Dashboard Kimi.**

## Étape 1 — Audit Structurel et Métrique
Lancer les commandes suivantes configurées pour **ignorer le template HTML massif** (`sticky_mobile_template`) et se concentrer sur l'automatisation Python, avec extension pour couvrir les parties plus larges et répertoires potentiellement manqués.

1.  **Cartographie (Filtre Template UI)** :
    - `run_command "tree -L 3 -I '__pycache__|venv|node_modules|.git|sticky_mobile_template|debug|docs|memory-bank'"`
    - *But* : Visualiser clairement l'app Flask (`switchbot_dashboard`) et les scripts de migration DB sans voir les 400 fichiers HTML du thème, avec profondeur accrue pour détecter les sous-répertoires.
2.  **Volumétrie Étendue (Scripts et Configurations)** :
    - `run_command "cloc . --exclude-dir=sticky_mobile_template,tests,docs,venv,debug,memory-bank,.continue,.windsurf --include-ext=py,sh,sql --md"`
    - *But* : Quantifier le backend Python, scripts shell et SQL, en incluant les répertoires de configuration potentiellement manqués.
3.  **Complexité Cyclomatique (IoT Core)** :
    - `run_command "radon cc switchbot_dashboard app.py scripts -a -nc"`
    - *But* : Identifier les points de fragilité dans les modules principaux.
    - **Cibles probables** : `switchbot_dashboard/automation.py` et `switchbot_api.py` (gestion des retries/quotas API) sont souvent complexes.
4.  **Analyse de Dépendances et Imports** :
    - `run_command "grep -r '^import|^from' --include='*.py' . --exclude-dir=venv,__pycache__,node_modules,.git,sticky_mobile_template,tests,docs,memory-bank | head -50"`
    - *But* : Détecter les scripts isolés ou manqués via leurs imports, focalisant sur les modules non couverts par l'audit initial.
5.  **Complexité Cyclomatique Élargie** :
    - `run_command "radon cc . --exclude-dir=venv,__pycache__,node_modules,.git,sticky_mobile_template,tests,docs,memory-bank,.continue,.windsurf -a -nc"`
    - *But* : Scanner tous les répertoires Python pour identifier les points de fragilité dans les scripts de déploiement, configuration ou automation manqués.

## Étape 2 — Diagnostic Triangulé
Comparer les sources pour détecter les incohérences :

| Source | Rôle | Outil |
| :--- | :--- | :--- |
| **Intention** | Le "Pourquoi" | `fast_read_file (via fast-filesystem)` |
| **Réalité** | Le "Quoi" & "Comment" | `radon` (complexité), `cloc` (volume), `search` |
| **Existant** | L'état actuel | `fast_search_files` (sur `docs/core` ou `docs/guides`), `fast_read_text_file` |

**Action** : Identifier les divergences. Ex: "Le script `migrate_to_postgres.py` existe, mais la doc `docs/core/deployment.md` le marque comme 'à faire'."

## Étape 3 — Sélection du Standard de Rédaction
Choisir le modèle approprié selon la nature du module (Hardware vs Web) :

- **IoT & Intégration** (`switchbot_dashboard/`, `switchbot_api.py`) :
  - **Quotas & Limites** : Documenter les limites API (ex: 100 req/jour).
  - **Gestion d'erreur** : Que se passe-t-il si le device est hors ligne ?
- **Automation & Scheduling** (`scheduler.py`, `automation.py`) :
  - **Logique d'État** : Comment `state.json` est-il mis à jour ?
  - **Triggers** : Conditions de déclenchement (Température > X).
- **Database & Ops** (`scripts/`, `config/`) :
  - **Migration** : Étapes SQL (`schema.sql`).
  - **Secrets** : Liste des clés requises dans `settings.json`.

## Étape 4 — Proposition de Mise à Jour
Générer un plan de modification avant d'appliquer :

```markdown
## 📝 Plan de Mise à Jour Documentation
### Audit Métrique
- **Cible** : `switchbot_dashboard/quota.py`
- **Analyse** : Gestion critique des limites API, non documentée.

### Modifications Proposées
#### 📄 docs/architecture/quota-management.md
- **Type** : [IoT Integration]
- **Ajout** : Tableau des limites API officielles vs implémentées.
- **Correction** :
  ```markdown
  [Explication du mécanisme de backoff exponentiel]
```

## Étape 5 — Application et Finalisation
1.  **Exécution** : Après validation, utiliser `edit` ou `multi_edit`.
2.  **Mode Rédaction — documentation/SKILL.md** :
    - Charger immédiatement `.continue/rules/documentation.md`.
    - Appliquer les checkpoints obligatoires du skill (TL;DR, ouverture orientée problème, comparaison ❌/✅, tableau de trade-offs si pertinent, Golden Rule, vérification ponctuation) avant toute rédaction.
    - Tracer la conformité dans vos commits/PR : `Guidé par documentation.md — sections: TLDR, Problem-first, Comparaison, Trade-offs, Golden Rule`.
3.  **Mise à jour Memory Bank** :
    - Mettre à jour la Memory Bank en utilisant EXCLUSIVEMENT l'outil `fast_edit_block` du serveur fast-filesystem. Utilisez des chemins absolus.
    - Si des règles métier cachées (hardcoded) sont trouvées dans `automation.py`, les extraire ou les documenter dans `systemPatterns.md`.
    - Employer `edit`/`multi_edit` ou `write_to_file` selon le besoin pour consigner :  
      - Nouvelles entrées dans `progress.md` (section "Terminé" + remise à "Aucune tâche active").  
      - Ajustements dans `activeContext.md` (retour à l'état neutre).  
      - Toute décision ou information pertinente dans les autres fichiers de la Memory Bank.  
    - Utiliser `advanced-search` si nécessaire pour vérifier la présence d'anciennes entrées et éviter les doublons.