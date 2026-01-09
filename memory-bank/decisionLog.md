[2026-01-09 16:23:00] - Baseline documenté
- productContext.md décrit désormais la vision globale, les composants clés et le flux d’automatisation.
- systemPatterns.md recense les patterns techniques (services injectés, stockage JSON atomique, APScheduler, validations).
- Prochaine étape : enrichir les entrées au fil des évolutions produit/fonctionnelles.

[2026-01-09 16:21:00] - Standardisation des contrôles UI/Backend
- Décision : introduire des constantes partagées (`DAY_CHOICES`, `TIME_CHOICES`, `TEMP_CHOICES`, etc.) dans `routes.py` et refondre les formulaires (fenêtres horaires, profils hiver/été) autour de dropdowns/checkboxes mobiles.
- Motivation : réduire les erreurs de saisie sur mobile et garantir que seules des valeurs supportées sont persistées dans `config/settings.json`.
- Implication : toute extension future (nouveaux pas de température, nouveaux modes) passera par l’actualisation des constantes backend pour conserver la parité UI/validation.

[2026-01-09 16:22:00] - Session UI mobile & synchronisation Memory Bank
- Étendu `routes.py` pour exposer des constantes partagées (jours, horaires 24 h, températures, modes, vitesses) et sécuriser la validation des formulaires.
- Refait le template `index.html` côté mobile (checkbox jours, dropdowns horaires, profils hiver/été entièrement guidés, styles responsive).
- Mis à jour productContext, systemPatterns et decisionLog pour refléter ces choix; progress synchronisé et aucun travail actif restant.

[2026-01-09 16:47:00] - Implémentation du thème sombre par défaut
- Décision : appliquer un thème sombre immersif par défaut sur les templates `index.html` et `devices.html`, avec palette CSS centralisée (variables), cartes vitrées, composants recolorisés pour lisibilité.
- Motivation : améliorer l'expérience visuelle en respectant les standards de lisibilité, nommage et accessibilité du projet (codingstandards.md).
- Implication : tous les éléments (cartes, boutons, formulaires, tableaux, alertes) utilisent désormais les variables CSS pour faciliter les futures extensions thématiques.

[2026-01-09 17:00:00] - Vue Devices enrichie et exploitable
- Décision : transformer `/devices` en inventaire structuré (cartes par device/remote, compteur synthèse, boutons de copie d’ID, accordéons JSON) pour éviter l’affichage de blobs JSON bruts.
- Motivation : améliorer la lisibilité mobile/desktop et guider explicitement la récupération des identifiants `meter_device_id` / `aircon_device_id` avant modification de `config/settings.json`.
- Implication : la page fournit désormais des métadonnées clés (statut, firmware, batterie) et conserve les payloads pour debug via `<details>`, réduisant les erreurs de configuration manuelle.

[2026-01-09 17:20:00] - Externalisation des styles et palette partagée
- Décision : supprimer tous les styles inline des templates `index.html` et `devices.html` pour les regrouper dans `static/css/theme.css` (variables et composants globaux) et des feuilles dédiées (`index.css`, `devices.css`).
- Motivation : garantir la cohérence du thème sombre, simplifier les évolutions futures (nouvelles pages, variantes de palette) et respecter les standards DRY/documentation.
- Implication : toute personnalisation s’effectue via ces feuilles CSS; la documentation (`docs/README.md`) décrit désormais le workflow d’extension et les tests (contraste, retour clipboard).

[2026-01-09 17:40:00] - Restructuration de la documentation
- Décision : diviser `docs/README.md` en guides thématiques (setup.md, configuration.md, ui-guide.md, theming.md, testing.md) pour améliorer la lisibilité et la maintenance.
- Motivation : l'ancien README était volumineux et monolithique; la nouvelle structure permet une navigation modulaire et respecte les principes DRY et d'organisation.
- Implication : `docs/README.md` devient une page d'index concise; chaque guide référence les autres et la Memory Bank pour tracer les décisions architecturales.

[2026-01-09 22:05:00] - Chaîne de déploiement containerisée (Docker → GHCR → Render)
- Décision : standardiser l’exécution via un Dockerfile Gunicorn (logs stdout/stderr, utilisateur non-root) et publier l’image sur GitHub Container Registry avec un workflow GitHub Actions doté d’un fallback API Render.
- Motivation : éviter les limites de build Render, disposer d’un pipeline reproductible et contrôlé depuis GitHub, garantir le déclenchement via webhook puis API si besoin.
- Implication : tous les déploiements passent par `.github/workflows/build-and-push.yml`, les secrets `RENDER_DEPLOY_WEBHOOK_URL`, `RENDER_API_KEY`, `RENDER_SERVICE_ID` sont requis sur GitHub, Render consomme l’image GHCR (plan Free).
