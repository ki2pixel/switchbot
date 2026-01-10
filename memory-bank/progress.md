[2026-01-09 16:01:00] - Baseline documenté
- productContext.md décrit désormais la vision globale, les composants clés et le flux d’automatisation.
- systemPatterns.md recense les patterns techniques (services injectés, stockage JSON atomique, APScheduler, validations).
- Prochaine étape : enrichir les entrées au fil des évolutions produit/fonctionnelles.

[2026-01-09 16:22:00] - Session UI mobile & synchronisation Memory Bank
- Étendu `routes.py` pour exposer des constantes partagées (jours, horaires 24 h, températures, modes, vitesses) et sécuriser la validation des formulaires.
- Refait le template `index.html` côté mobile (checkbox jours, dropdowns horaires, profils hiver/été entièrement guidés, styles responsive).
- Mis à jour productContext, systemPatterns et decisionLog pour refléter ces choix; progress synchronisé et aucun travail actif restant.

[2026-01-09 16:47:00] - Session thème sombre par défaut
- Implémenté un thème sombre immersif sur `index.html` et `devices.html` : palette CSS centralisée, cartes vitrées, composants recolorisés (boutons, formulaires, alertes, pre).
- Respecté les standards de codingstandards.md (lisibilité, nommage, accessibilité).
- Tests manuels suggérés : rendu desktop/mobile, lisibilité, contraste, cohérence.
- Synchronisé Memory Bank (decisionLog, activeContext, progress); session terminée.

[2026-01-09 17:00:00] - Session inventaire Devices
- Refonte de `switchbot_dashboard/templates/devices.html` : compteur synthèse, cartes responsives (devices et IR), boutons de copie d’ID, accordéons JSON conservés pour le debug.
- Renforcé le contraste du résumé et des titres afin d’assurer la lisibilité sur le thème sombre.
- Tests recommandés : vérification copier-coller ID, affichage mobile, ouverture/fermeture des `<details>`.

[2026-01-09 17:20:00] - Session externalisation CSS
- Extraction des styles inline de `index.html` et `devices.html` vers `static/css/theme.css`, `index.css`, `devices.css` tout en conservant la palette sombre partagée.
- Mise à jour des templates pour référencer les nouvelles feuilles via `url_for` et suppression des blocs `<style>`.
- Documentation `docs/README.md` enrichie (workflow palette, consignes DRY, tests contraste/clipboard).
- Memory Bank synchronisée (decisionLog, systemPatterns, progress, activeContext).

[2026-01-09 17:40:00] - Session restructuration documentation
- Analyse de la structure existante (README.md, switchbot/README.md, switchbot/README-v1.0.md).
- Proposition d'arborescence thématique (setup.md, configuration.md, ui-guide.md, theming.md, testing.md).
- Création de docs/setup.md (prérequis, installation, lancement).
- Création de docs/configuration.md (.env, settings.json, workflow /devices, validation routes.py).
- Création de docs/ui-guide.md (interactions / et /devices, UX mobile, clipboard).
- Création de docs/theming.md (thème sombre, variables CSS, réutilisation des feuilles).
- Création de docs/testing.md (tests recommandés, validation manuelle).
- Mise à jour de docs/README.md comme page d'index concise.
- Ajout de renvois croisés entre fichiers et références Memory Bank.
- Validation de cohérence (orthographe, liens, TOC).
- Memory Bank synchronisée (decisionLog, productContext, systemPatterns, progress).

[2026-01-09 22:05:00] - Session déploiement Render & CI/CD
- Création du `Dockerfile` (Gunicorn, logs stdout/stderr, utilisateur non-root) et `.dockerignore`.
- Ajout de `gunicorn` dans `requirements.txt`.
- Ajout du workflow GitHub Actions `build-and-push.yml` (build/push GHCR, webhook Render + fallback API).
- Documentation du déploiement (`docs/deployment.md`) et mise à jour de `docs/README.md`.
- Initialisation Git locale, connexion au repo GitHub, premier commit/push « Initial deployment setup ».
- Création du `.gitignore` aligné projet.
- Assistance à la configuration Render (variables, récupération `RENDER_SERVICE_ID` via API) et validation du déploiement live.
- Memory Bank synchronisée (decisionLog enrichi; progress, activeContext mis à jour).

[2026-01-09 23:11:00] - Session documentation configuration & déploiement
- Ajouté la description de l'override `SWITCHBOT_POLL_INTERVAL_SECONDS`, des valeurs de secours `SWITCHBOT_RETRY_*` et de l'exigence `FLASK_SECRET_KEY` dans `docs/configuration.md`.
- Clarifié dans `docs/deployment.md` l'échec anticipé du workflow si les secrets Render sont incomplets et détaillé la matrice des secrets GHCR/Render.
- Vérifié la cohérence avec `switchbot_dashboard/__init__.py` et les fichiers CI/CD avant validation.
- Memory Bank synchronisée (progress mis à jour).

## Terminé
[2026-01-09 16:47:00] - Implémentation du thème sombre par défaut sur les templates index.html et devices.html.
[2026-01-09 17:00:00] - Refonte de la page Devices : cartes lisibles, synthèse, copie d'ID et JSON repliables.
[2026-01-09 17:20:00] - Externalisation complète des styles (theme.css + feuilles spécifiques) et documentation associée.
[2026-01-09 17:40:00] - Restructuration de la documentation en guides thématiques avec index et renvois croisés.
[2026-01-09 22:05:00] - Chaîne de déploiement containerisée (Dockerfile, GHCR workflow, doc déploiement) livrée et premier déploiement Render validé.
[2026-01-10 02:20:00] - Implémentation d'un système de suivi local des quotas API SwitchBot
  - Ajout d'un compteur journalier local dans `automation.py` pour suivre l'utilisation de l'API (10 000 requêtes/jour)
  - Configuration de `LOG_LEVEL` pour Gunicorn via la variable d'environnement
  - Vérification de l'absence de headers de quota dans les réponses de l'API SwitchBot
  - Mise à jour de l'interface utilisateur pour afficher les quotas calculés localement
  - Documentation des décisions techniques dans la Memory Bank

## En cours
Aucune tâche active.
