---
name: end
description: Terminer la Session et Synchroniser la Memory Bank
invokable: true
---

## Workflow `/end`

1. **Arrêt du travail en cours**  
   - Annoncer l'activation du mode `UMB` et stopper toute autre tâche.
2. **Chargement de la Memory Bank**  
   - Utiliser `mcp0_read_text_file` pour relire systématiquement `productContext.md`, `activeContext.md`, `systemPatterns.md`, `decisionLog.md` et `progress.md` avant toute mise à jour.
3. **Analyse de la session**  
   - Passer en revue l'historique de la conversation (mémoire interne) et dresser la liste des décisions/progrès à synchroniser.
4. **Mise à jour des fichiers**  
   - Employer `edit`/`multi_edit` (via `apply_patch`) ou `write_to_file` selon le besoin pour consigner :  
     - Nouvelles entrées dans `progress.md` (section "Terminé" + remise à "Aucune tâche active").  
     - Ajustements dans `activeContext.md` (retour à l'état neutre).  
     - Toute décision ou information pertinente dans les autres fichiers de la Memory Bank.  
   - Utiliser `mcp1_advanced-search` si nécessaire pour vérifier la présence d'anciennes entrées et éviter les doublons.
5. **Résumé final**  
   - Synthétiser les tâches accomplies en se basant sur `progress.md` mis à jour.  
   - Confirmer à l'utilisateur que la Memory Bank est synchronisée et prête pour la prochaine session.