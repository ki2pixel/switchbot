---
description: Docs Updater (Context-Aware with Code Verification)
---

---
description: Docs Updater (Standard Tools: Cloc/Radon + Quality Context)
---

# Workflow: Docs Updater — Standardized & Metric-Driven

> Ce workflow harmonise la documentation en utilisant l'analyse statique standard (`cloc`, `radon`, `tree`) pour la précision technique et les modèles de référence pour la qualité éditoriale.

## 🚨 Protocoles Critiques
1.  **Outils autorisés** : L'usage de `run_command` est **strictement limité** aux commandes d'audit : `tree`, `cloc`, `radon`, `ls`.
2.  **Contexte** : Charger la Memory Bank (`productContext.md`, `systemPatterns.md`, `activeContext`, `progress.md`) via `read_file` avant toute action.
3.  **Source de Vérité** : Le Code (analysé par outils) > La Documentation existante > La Mémoire.

## Étape 1 — Audit Structurel et Métrique
Lancer les commandes suivantes configurées pour **ignorer le template HTML massif** (`sticky_mobile_template`) et se concentrer sur l'automatisation Python.

1.  **Cartographie (Filtre Template UI)** :
    - `run_command "tree -L 2 -I '__pycache__|venv|node_modules|.git|sticky_mobile_template|debug|docs|memory-bank'"`
    - *But* : Visualiser clairement l'app Flask (`switchbot_dashboard`) et les scripts de migration DB sans voir les 400 fichiers HTML du thème.
2.  **Volumétrie (Code Métier)** :
    - `run_command "cloc . --exclude-dir=sticky_mobile_template,tests,docs,venv,debug,memory-bank --exclude-ext=json,sql --md"`
    - *But* : Quantifier le backend Python.
3.  **Complexité Cyclomatique (IoT Core)** :
    - `run_command "radon cc switchbot_dashboard app.py scripts -a -nc"`
    - *But* : Identifier les points de fragilité.
    - **Cibles probables** : `switchbot_dashboard/automation.py` et `switchbot_api.py` (gestion des retries/quotas API) sont souvent complexes.

## Étape 2 — Diagnostic Triangulé
Comparer les sources pour détecter les incohérences :

| Source | Rôle | Outil |
| :--- | :--- | :--- |
| **Intention** | Le "Pourquoi" | `read_file` (Memory Bank) |
| **Réalité** | Le "Quoi" & "Comment" | `radon` (complexité), `cloc` (volume), `code_search` |
| **Existant** | L'état actuel | `find_by_name` (sur `docs/core` ou `docs/guides`), `read_file` |

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
```

## Étape 5 — Application et Finalisation
1.  **Exécution** : Après validation, utiliser `apply_patch`.
2.  **Mode Rédaction — documentation/SKILL.md** :
    - Charger immédiatement `.sixthskills/documentation/SKILL.md`.
    - Appliquer les checkpoints obligatoires du skill (TL;DR, ouverture orientée problème, comparaison ❌/✅, tableau de trade-offs si pertinent, Golden Rule, vérification ponctuation) avant toute rédaction.
    - Tracer la conformité dans vos commits/PR : `Guidé par documentation/SKILL.md — sections: TLDR, Problem-first, Comparaison, Trade-offs, Golden Rule`.
3.  **Mise à jour Memory Bank** :
    - Si des règles métier cachées (hardcoded) sont trouvées dans `automation.py`, les extraire ou les documenter dans `systemPatterns.md`.
