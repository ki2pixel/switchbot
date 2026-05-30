---
description: Generate Repomix bundle for LLM analysis
---

# /repomix-bundle — Générer le bundle Repomix

## Objectif
Créer un bundle optimisé du codebase pour analyse par LLMs externes (Claude, ChatGPT, etc.) en utilisant Repomix avec la configuration existante.

## Étapes

1. **Vérification de la configuration**
   - Confirmer que `repomix.config.json` existe et est à jour
   - Vérifier les patterns d'inclusion/exclusion

2. **Génération du bundle**
   // turbo
   ```bash
   npx repomix --config repomix.config.json
   ```

3. **Vérification du résultat**
   - Contrôler que `repomix-output.md` a été généré
   - Vérifier la taille et le compte de tokens
   - Valider que les fichiers critiques sont inclus

---

## Priority of Tools (The "Pull" Hierarchy)
- **Priority 1**: Use `fast_read_file` from fast-filesystem MCP server.
- **Priority 2 (Fallback)**: If fast-filesystem server not detected, use `ripgrep` to search in `./memory-bank/` and `filesystem` to read found files.
- **Prohibition**: Never load more than one file at a time.

## Technical Lockdown
- Utilisez les outils fast-filesystem (fast_*) pour accéder aux fichiers memory-bank avec des chemins absolus.
- Windsurf is now in 'Token-Saver' mode. Minimize context usage by using tools instead of pre-loading.