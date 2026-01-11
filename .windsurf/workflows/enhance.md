---
description: Améliorer un Prompt avec le Contexte du Projet
---

# Améliorer un Prompt avec le Contexte du Projet (V2)

description: Prend un prompt utilisateur "brut", l'analyse, l'enrichit avec le contexte du Memory Bank ET de la documentation pertinente, et propose une version améliorée pour validation avant exécution.

---

1.  Follow the protocol in your rules to load the full project context from the `memory-bank`.

2.  Act as an expert "Prompt Engineer". Your goal is to improve the user's request that was provided after the `/enhance` command. Be concise in your final output.

3.  First, analyze the user's raw request to understand its core intent.

4.  Perform a two-level contextual analysis:
    a. Level 1 (Strategic Context): Review the `memory-bank` to understand high-level goals, technical standards, and current focus.
    b. Level 2 (Tactical Details): **Search for and prioritize reading documentation files whose names are highly relevant to the user's request.** For example, for an API question, prioritize `api_reference.md`. For a security question, prioritize `security.md`. If no specific documentation is relevant, rely on the code and the memory bank.

5.  Synthesize this information to rewrite the user's request into a single, comprehensive "enhanced prompt". This new prompt must be:
    *   **Spécifique** : Mentionner les fichiers, fonctions ou endpoints pertinents.
    *   **Contextuel** : Faire référence aux standards et à l'architecture du projet.
    *   **Clair** : Reformuler les ambiguïtés en objectifs clairs.
    *   **Actionnable** : Définir clairement la tâche à accomplir.

6.  Present **only** this "enhanced prompt" to me for validation, without explaining your internal thought process. Frame it clearly: "Voici une version améliorée de votre prompt que je propose. Dois-je l'exécuter ? (oui/non)".

7.  Do not proceed without my explicit confirmation ("oui", "yes", "vas-y", etc.).

8.  Once I confirm, execute the enhanced prompt as if I had just submitted it myself.