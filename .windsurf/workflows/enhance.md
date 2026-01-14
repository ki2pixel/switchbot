---
description: Améliorer un Prompt avec le Contexte du Projet
---

## Workflow `/enhance`

1. **Initialisation mémoire**  
   - Utiliser `read_file` pour charger l'intégralité des fichiers obligatoires de la Memory Bank (`productContext.md`, `activeContext.md`, `systemPatterns.md`, `decisionLog.md`, `progress.md`).
2. **Analyse du prompt brut**  
   - Examiner la requête utilisateur directement (aucun outil requis) et identifier les besoins implicites.
3. **Collecte de contexte stratégique**  
   - Si des compléments sont nécessaires au-delà de la Memory Bank, employer `code_search` pour localiser les modules ou services pertinents.  
   - Utiliser `read_file` pour consulter les fichiers identifiés et `grep_search` pour confirmer la présence de symboles spécifiques.
4. **Collecte de contexte tactique (documentation)**  
   - Prioriser les fichiers de `docs/` liés au sujet en utilisant `find_by_name` si besoin, puis `read_file` pour les parcourir.  
   - Limiter la lecture aux sections pertinentes (offset/limit) afin de respecter la contrainte de portée.
5. **Synthèse et rédaction du prompt amélioré**  
   - Structurer un prompt unique en incorporant les chemins de fichiers et standards applicables.  
   - Présenter uniquement : `"Voici une version améliorée... Dois-je l'exécuter ? (oui/non)"`.
6. **Attente de confirmation**  
   - Suspendre toute action jusqu'à validation explicite.
7. **Exécution après confirmation**  
   - Rejouer le prompt amélioré comme une nouvelle demande.  
   - Pour toute lecture/écriture additionnelle, continuer d'utiliser `read_file`, `edit`/`multi_edit`, `grep_search` et `code_search` conformément aux règles.