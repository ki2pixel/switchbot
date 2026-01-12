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
[2026-01-10 13:35:00] - Aircon presets configurables et tests associés
[2026-01-10 16:40:00] - Scène OFF SwitchBot + documentation/tests
[2026-01-10 20:30:00] - Amélioration des flash messages (auto-dismiss et contraste)
[2026-01-10 20:40:00] - Harmonisation totale des templates UI en français (index.html, devices.html, quota.html) : traductions des labels, boutons, badges et métadonnées selon la terminologie UI.
[2026-01-10 20:42:00] - Traduction complète des messages flash/alertes en français dans routes.py pour cohérence avec l'interface.
[2026-01-10 20:50:00] - Session question température redeploy et implémentation flag stale

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

[2026-01-10 13:35:00] - Session presets Aircon configurables
- Ajout de `DEFAULT_AIRCON_PRESETS`, `_extract_aircon_presets` et `_send_manual_aircon_setall` pour séparer les actions Aircon ON hiver/été et respecter les valeurs documentées.
- Section UI dédiée “Manual Aircon presets” avec alertes si les réglages divergent des recommandations.
- Persistance des presets via `settings["aircon_presets"]`, mise à jour des docs (`configuration.md`, `ui-guide.md`) et des tests (`test_aircon_presets.py`, `test_dashboard_routes.py`).
- Conseils fournis sur la persistance Redis (modifier via l’UI plutôt que `config/settings.json`).

[2026-01-10 15:30:00] - Migration des presets vers des scènes SwitchBot
- Suppression complète de la logique `aircon_presets` (constantes, helpers, routes) au profit de `aircon_scenes`
- Mise à jour de l'interface utilisateur pour ne conserver que la configuration des scènes
- Mise à jour de la documentation pour refléter ces changements
- Nettoyage des références aux presets dans les tests

[2026-01-10 16:40:00] - Scène OFF SwitchBot et validations associées
- Ajout de la clé `off` aux scènes SwitchBot (stockage, validation, interface et boutons rapides).
- Routes `/actions/aircon_off` et `/actions/quick_off` désormais pilotées par la scène OFF avec repli `turnOff`.
- Documentation (`docs/configuration.md`) mise à jour, nouvelles assertions dans `tests/test_dashboard_routes.py` et nettoyage de `tests/test_aircon_presets.py`.
- Exécution complète de la suite Pytest via `/mnt/venv_ext4/venv_switchbot/bin/python -m pytest`.

[2026-01-10 17:30:00] - Implémentation du point de terminaison de santé (/healthz)
- Ajout de la méthode `is_running()` à `SchedulerService` pour vérifier l'état du planificateur
- Mise à jour de `AutomationService.run_once()` pour enregistrer l'horodatage du dernier tick
- Implémentation du point de terminaison `/healthz` dans `routes.py` avec gestion robuste des erreurs
- Ajout de tests unitaires complets dans `test_dashboard_routes.py`
- Mise à jour de la documentation de déploiement pour inclure des informations sur le point de terminaison de santé
- Tous les tests passent avec succès
- Documentation mise à jour dans `docs/deployment.md`
- Memory Bank synchronisée (decisionLog, progress, activeContext)

[2026-01-10 17:56:00] - Automatisation pilotée par scènes SwitchBot + couverture de tests
- `AutomationService` consomme désormais `aircon_scenes` (helper dédié, fallback `setAll`/`turnOff` si scènes ou `aircon_device_id` manquants).
- Ajout de `tests/test_automation_service.py` pour valider l’utilisation des scènes, les replis et la mise à jour des quotas.
- Documentation mise à jour (`docs/configuration.md`, `docs/ui-guide.md`) pour préciser la dépendance à ces scènes.
- Memory Bank synchronisée (decisionLog, activeContext mis à jour).

[2026-01-10 19:18:00] - Suppression des actions rapides quick_winter et quick_summer
- Supprimé les actions rapides "Chauffage (Hiver)" et "Clim (Été)" du tableau de bord
- Mis à jour l'interface utilisateur dans `index.html` pour une expérience plus propre
- Mise à jour de la documentation dans `ui-guide.md` pour refléter les changements
- Conservation de la fonctionnalité `quick_off` pour désactiver l'automatisation
- Tous les tests unitaires passent avec succès après les modifications

[2026-01-10 20:00:00] - Implémentation du système d'alerte de quota et métadonnées
- Ajout du seuil d'avertissement configurable `api_quota_warning_threshold` dans `config/settings.json` (valeur par défaut : 250)
- Implémentation de l'alerte visuelle dans l'interface utilisateur quand le nombre de requêtes restantes est faible
- Affichage des métadonnées de quota (`api_quota_day` et `api_quota_reset_at`) dans l'interface
- Mise à jour de `quota.py` pour stocker systématiquement l'heure de réinitialisation
- Ajout de tests d'intégration avec BeautifulSoup pour vérifier le comportement de l'alerte
- Mise à jour de la documentation dans `configuration.md` avec les bonnes pratiques de gestion des quotas
- Styles CSS ajoutés pour une intégration visuelle harmonieuse
- Tous les tests passent avec succès après les modifications
- Amélioration des flash messages avec auto-dismiss (6s) et contraste renforcé (fonds sombres, texte blanc) pour tous les types d'alertes (succès, erreur, info, warning)
- Création de `static/js/alerts.js` pour gérer l'auto-fermeture progressive des alertes
- Mise à jour des templates `index.html` et `quota.html` pour ARIA et auto-dismiss
- Renforcement du contraste dans `theme.css` avec nouvelles variables et styles `.alert`

- Analyse du comportement de récupération de température lors d'un redeploy Render (~1 min) avec Redis.
- Implémentation du flag `last_temperature_stale` pour signaler une température potentiellement obsolète.
- Mise à jour de la documentation (`docs/configuration.md`).
- Ajout de test (`tests/test_app_init.py`) et validation pytest (18 tests passed).
[2026-01-11 15:00:00] - Intégration complète des webhooks IFTTT avec fallback cascade
- Création du module IFTTTWebhookClient avec validation HTTPS et gestion erreurs
- Remplacement de la logique scènes par webhooks avec fallback vers scènes puis commandes directes
- Mise à jour de l'interface utilisateur pour configuration des webhooks IFTTT
- Création de 16 tests unitaires complets pour la nouvelle logique IFTTT
- Suite pytest complète passée (36/36 tests)
- Documentation complète (ifttt-integration.md, configuration.md, README.md mis à jour)
[2026-01-11 20:55:00] - Répétition OFF paramétrable et tests associés
- Ajout des paramètres `off_repeat_count` et `off_repeat_interval_seconds` (validation backend + formulaire UI)
- Extension d'`AutomationService` avec état `pending_off_repeat`, planification différée et exécution forcée des OFF répétés
- Ajout de tests unitaires couvrant la file de répétitions et la purge automatique
- Mise à jour de la documentation et vérification via pytest ciblé (`tests/test_automation_service.py`)
[2026-01-11 23:00:00] - Diagnostic et correction des problèmes scheduler
- Diagnostic du warning "Cannot schedule job: scheduler is None" lors des POST /settings
- Implémentation d'un guard dans reschedule() pour gérer gracieusement les appels sur scheduler non démarré
- Diagnostic et correction du scheduler skippé sur Render à cause de FLASK_DEBUG=1 avec Gunicorn
- Amélioration de la détection mode debug pour distinguer Flask dev reloader de Gunicorn
- Tests validés (53/53 passés), correction appliquée sans régression
[2026-01-12 00:55:00] - Correction des déclenchements excessifs `winter_off`
- Diagnostic initial : `winter_off` se déclenchait trop fréquemment après exécution des `off_repeat`, relançant des scènes OFF toutes les ~60 s tant que la température restait élevée.
- Solution implémentée : Ajout d'une vérification d'idempotence (`assumed_aircon_power == "off"`) dans `AutomationService.run_once()` pour bloquer les nouvelles actions OFF si le climatiseur est déjà supposé OFF.
- Modifications : Code `automation.py` (gardes dans winter_off/summer_off/off-outside-window), tests unitaires (`test_automation_service.py`), documentation (`docs/configuration.md`).
- Validation : Logs utilisateur confirment le succès (`Skipping winter_off: already assumed off`), tests pytest passés.
- Memory Bank synchronisée (decisionLog, activeContext, progress mis à jour).
[2026-01-12 10:33:00] - Implémentation de la gestion timezone explicite pour les fenêtres horaires d'automatisation (Europe/Paris par défaut), incluant validation UI, tests et documentation.

## En cours
- Aucune tâche active.
