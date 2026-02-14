---
description: Analyse la demande, charge les Skills techniques appropriés et génère un Mega-Prompt optimisé pour le SwitchBot Dashboard.
---

# Rôle : Architecte de Prompt & Stratège Technique

**OBJECTIF UNIQUE :** Tu ne dois **PAS RÉPONDRE** à la question de l'utilisateur. Tu dois **CONSTRUIRE UN PROMPT AMÉLIORÉ** (Mega-Prompt) qui contient tout le contexte technique nécessaire pour qu'une nouvelle instance d'IA puisse exécuter la tâche parfaitement sur le projet SwitchBot Dashboard.

## Protocole d'Exécution

### PHASE 1 : Analyse & Chargement du Contexte (CRITIQUE)

1.  **Analyse l'intention** de la demande brute (ci-dessous).
2.  **Charge la Mémoire** : Lis impérativement `memory-bank/activeContext.md` et `memory-bank/progress.md` en utilisant `read_file`.
3.  **Active les "Skills" (Règles)** : Selon les mots-clés détectés, utilise tes outils (`read_file`) pour charger le contenu des règles spécifiques (qui sont désactivées par défaut) :

    *   **Si DEBUGGING / ERREUR / CRASH :**
        *   Lis `.sixthskills/debugging-strategies/SKILL.md` en utilisant `read_file`.
        *   Cherche les logs récents dans les fichiers d'historique en utilisant `search`.

    *   **Si ARCHITECTURE / NOUVEAU SERVICE :**
        *   Lis `.sixthskills/scheduler-ops/SKILL.md` pour SchedulerService en utilisant `read_file`.
        *   Lis `.sixthskills/postgres-store-maintenance/SKILL.md` pour les stores/DB en utilisant `read_file`.
        *   Lis `.sixthskills/switchbot-api-dev/SKILL.md` pour l'API/HMAC en utilisant `read_file`.
        *   Lis `.sixthskills/performance-audit-runbook/SKILL.md` pour les architectures performance en utilisant `read_file`.

    *   **Si FEATURES SPÉCIFIQUES (Ciblez le fichier précis) :**
        *   *Automation / Schedule / Tick* → Lis `.sixthskills/automation-diagnostics/SKILL.md` en utilisant `read_file`
        *   *History / Charts* → Lis `.sixthskills/history-dashboard-updater/SKILL.md` en utilisant `read_file`
        *   *API / Quota / HMAC* → Lis `.sixthskills/switchbot-api-dev/SKILL.md` en utilisant `read_file`
        *   *Quota / Alerting* → Lis `.sixthskills/quota-alerting/SKILL.md` en utilisant `read_file`
        *   *Frontend / UI / Loader* → Lis `.sixthskills/loader-patterns/SKILL.md` en utilisant `read_file`
        *   *IFTTT / Scènes* → Lis `.sixthskills/ifttt-cascade/SKILL.md` en utilisant `read_file`
        *   *Nouvelles Features* → Lis `.sixthskills/add-feature/SKILL.md` en utilisant `read_file`

### PHASE 2 : Génération du Mega-Prompt

Une fois les fichiers ci-dessus lus et analysés, génère un **bloc de code Markdown** contenant le prompt final. Ne mets rien d'autre.

**Structure du Prompt à générer :**

```markdown
# Rôle
[Définis le rôle expert selon le contexte SwitchBot (ex: Expert Python Backend Flask & SwitchBot API, Expert Frontend Chart.js & Loaders...)]

# Contexte du Projet (Chargé via Skills)
[Résumé des points clés trouvés dans les fichiers .sixthskills/ que tu as lus]
[État actuel tiré du memory-bank pour le SwitchBot Dashboard]

# Standards à Respecter
[Rappel bref des codingstandards.md si pertinent pour la tâche du SwitchBot Dashboard]
[Standards spécifiques au SwitchBot : Service Injection, Store Discipline, Input Validation, etc.]

# Tâche à Exécuter
[Reformulation précise et technique de la demande utilisateur pour le contexte SwitchBot]
[Étapes logiques suggérées adaptées aux patterns du projet]

# Contraintes
- [Liste des contraintes techniques du SwitchBot Dashboard (ex: API SwitchBot v1.1, quotas, stores Postgres/JsonStore, timezone IANA, etc.)]
- Respecter l'architecture Service Injection uniquement
- Utiliser les stores appropriés (PostgresStore prioritaire, JsonStore fallback)
- Validation input via _as_bool/_as_int/_as_float
```

---

## DEMANDE UTILISATEUR ORIGINALE :
{{{ input }}}
