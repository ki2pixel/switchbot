---
name: enhance
description: Améliorer un Prompt avec le Contexte du Projet, Techniques Avancées et Skills Spécialisés
invokable: true
---

### `/enhance` — Optimisation Avancée de Prompt
1. **Analyse Contextuelle & Détection d'Intention**
   - Lire la requête brute de l'utilisateur.
   - Charger le contexte global via `mcp0_read_text_file` sur les fichiers de la Memory Bank (`activeContext.md`, `progress.md`, `systemPatterns.md`, etc.).
   - **Détection de Skill** : Analyser la nature de la tâche :
     - Si **Debugging** (bug, crash, erreur, performance) : Charger immédiatement `.continue/rules/debugging-strategies.md`.
     - Si **Architecture** : Identifier le sous-domaine concerné et charger les SKILL workspace pertinents (`.continue/rules/scheduler-ops.md` pour SchedulerService, `.continue/rules/postgres-store-maintenance.md` pour les stores/DB, `.continue/rules/switchbot-api-dev.md` pour l'API/HMAC, `.continue/rules/performance-audit-runbook.md` pour les architectures performance). Mentionner explicitement les SKILL consultés dans le prompt.
     - Si **Feature** : Charger `.continue/rules/add-feature.md` puis compléter avec les SKILL métier associés (ex. `history-dashboard-updater`, `quota-alerting`, `loader-patterns`, `ifttt-cascade`, `automation-diagnostics`) selon la fonctionnalité visée. Lister ces SKILL dans le prompt final.

2. **Recherche Active de Documentation**
   - Identifier les règles spécifiques au projet via `code_search` dans `docs/` et `.continue/rules/codingstandards.md`.
   - Utiliser `mcp0_read_text_file` sur les documents pertinents trouvés.
   - Si mode **Debugging** activé : Vérifier via `mcp1_advanced-search` si les outils mentionnés dans le Skill (ex: configurations de log, profileurs) sont déjà présents dans le code source pour les inclure dans le contexte.

3. **Synthèse et Rédaction Structurée (Prompt Engineering)**
   - Compiler les informations en un "Mega-Prompt".
   - **Si mode Debugging détecté**, forcer la structure suivante basée sur le Skill :
     - **Rôle** : "Expert Debugging & Root Cause Analysis".
     - **Méthodologie** : Imposer les phases du Skill (1. Reproduire, 2. Collecter, 3. Hypothèse, 4. Test).
     - **Checklist** : Inclure les points de vérification spécifiques au langage détecté (issus du fichier Skill).
   - **Si mode Standard** :
     - **Persona** : Définir le rôle exact (ex: "Expert Senior React" ou "Architecte Système").
     - **Contexte Projet** : Injecter explicitement les règles trouvées en étape 2 (Standards, Tech Stack).
     - **Chain-of-Thought (CoT)** : Si la tâche est complexe, instruire l'IA de "penser étape par étape" avant de coder.
     - **Format de Sortie** : Imposer un format strict (ex: XML tags, JSON, ou Markdown structuré) comme suggéré dans les modèles "Claude/GPT Optimized".
     - **Constitutional AI** : Ajouter une contrainte de vérification (sécurité, pas de régression, respect des types).
   
   - **Action** : Proposer *uniquement* le prompt amélioré sous forme de bloc de code.

4. **Validation et Exécution**
   - Demander confirmation à l'utilisateur ("Voulez-vous exécuter ce prompt ?").
   - Une fois validé :
     - Exécuter le prompt.
     - Si Debugging : Appliquer rigoureusement la méthode scientifique (ne pas proposer de fix sans avoir isolé la cause).
     - Utiliser systématiquement les outils (`mcp0_read_text_file`, `edit`/`multi_edit`, `run_command`) pour réaliser la tâche.
     - Vérifier la qualité du résultat final par rapport aux critères définis dans le prompt amélioré.