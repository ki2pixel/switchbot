[2026-01-09 16:21:00] - Standardisation des contrôles UI/Backend
- Décision : introduire des constantes partagées (`DAY_CHOICES`, `TIME_CHOICES`, `TEMP_CHOICES`, etc.) dans `routes.py` et refondre les formulaires (fenêtres horaires, profils hiver/été) autour de dropdowns/checkboxes mobiles.
- Motivation : réduire les erreurs de saisie sur mobile et garantir que seules des valeurs supportées sont persistées dans `config/settings.json`.
- Implication : toute extension future (nouveaux pas de température, nouveaux modes) passera par l’actualisation des constantes backend pour conserver la parité UI/validation.

- [2026-01-09 16:22:00] - Session UI mobile & synchronisation Memory Bank
- Étendu `routes.py` pour exposer des constantes partagées (jours, horaires 24 h, températures, modes, vitesses) et sécuriser la validation des formulaires.
- Refait le template `index.html` côté mobile (checkbox jours, dropdowns horaires, profils hiver/été entièrement guidés, styles responsive).
- Mis à jour productContext, systemPatterns et decisionLog pour refléter ces choix; progress synchronisé et aucun travail actif restant.

[2026-01-09 16:23:00] - Baseline documenté
- productContext.md décrit désormais la vision globale, les composants clés et le flux d’automatisation.
- systemPatterns.md recense les patterns techniques (services injectés, stockage JSON atomique, APScheduler, validations).
- Prochaine étape : enrichir les entrées au fil des évolutions produit/fonctionnelles.

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
- Décision : standardiser l'exécution via un Dockerfile Gunicorn (logs stdout/stderr, utilisateur non-root) et publier l'image sur GitHub Container Registry avec un workflow GitHub Actions doté d'un fallback API Render.
- Motivation : éviter les limites de build Render, disposer d'un pipeline reproductible et contrôlé depuis GitHub, garantir le déclenchement via webhook puis API si besoin.
- Implication : tous les déploiements passent par `.github/workflows/build-and-push.yml`, les secrets `RENDER_DEPLOY_WEBHOOK_URL`, `RENDER_API_KEY`, `RENDER_SERVICE_ID` sont requis sur GitHub, Render consomme l'image GHCR (plan Free).

[2026-01-10 02:20:00] - Gestion des quotas API SwitchBot avec fallback local
- Décision : implémenter un compteur local journalier pour suivre l'utilisation de l'API SwitchBot, avec une limite de 10 000 requêtes par jour, en l'absence de headers de quota dans les réponses de l'API.
- Motivation : l'API SwitchBot ne fournit pas systématiquement les en-têtes de quota (X-RateLimit-*), ce qui rendait l'affichage du quota inutilisable (affichant "N/A").
- Implémentation : ajout d'un mécanisme de suivi local dans `automation.py` qui s'incrémente à chaque appel API et se réinitialise quotidiennement. Le compteur est stocké dans `state.json` et synchronisé avec l'interface utilisateur.
- Configuration du niveau de log : modification du `Dockerfile` pour respecter la variable d'environnement `LOG_LEVEL` dans Gunicorn, permettant un débogage plus efficace en production.

[2026-01-10 10:55:00] - Persistance des réglages via backend Redis optionnel
- Décision : introduire `BaseStore` + `RedisJsonStore` et permettre à `create_app()` de sélectionner dynamiquement un backend `filesystem` (par défaut) ou `redis` via les variables `STORE_BACKEND`, `REDIS_URL`, `REDIS_PREFIX`, `REDIS_TTL_SECONDS`.
- Motivation : conserver `config/settings.json` et `config/state.json` après redeploy/scale Render grâce à un stockage externe (ex. Upstash), éviter la perte d'automatisation.
- Implication : dépendance `redis>=5` ajoutée, `.env.example` et documentation (configuration, déploiement, tests) détaillent la migration et la sécurité; le système retombe automatiquement sur le filesystem si Redis est indisponible.

[2026-01-10 13:35:00] - Presets Aircon configurables + alerte UI
- Décision : introduire la clé `aircon_presets` (stockée dans le backend settings) pour piloter les actions "Aircon ON – Hiver/Été" et exposer une section d’édition dédiée dans `index.html`.
- Motivation : éviter l’édition manuelle de `config/settings.json` lorsque Redis est actif et garantir que les commandes `setAll` reflètent les préférences utilisateur (25 °C heat, 18 °C cool par défaut).
- Implémentation : `_extract_aircon_presets` applique les bornes SwitchBot, `/settings` persiste les variations, `_send_manual_aircon_setall` consomme ces valeurs et l’UI indique via un bandeau lorsque les presets diffèrent des recommandations.
- Tests : `tests/test_aircon_presets.py` (bornes/immutabilité) et `tests/test_dashboard_routes.py` (POST /settings) empêchent les régressions.

[2026-01-10 15:30:00] - Migration des presets Aircon vers des scènes SwitchBot
- Décision : Remplacer complètement le système de `aircon_presets` (qui utilisait des commandes `setAll` manuelles) par des `aircon_scenes` basées sur des identifiants de scènes SwitchBot.
- Motivation : Simplifier la configuration en utilisant directement les scènes préconfigurées de l'application SwitchBot, ce qui améliore la fiabilité et la maintenabilité. Les scènes permettent également une exécution plus rapide et plus fiable des commandes.
- Implication : Suppression de la logique de construction manuelle des commandes `setAll`, simplification de l'interface utilisateur, et mise à jour de la documentation pour refléter ce changement. Les utilisateurs doivent maintenant configurer leurs scènes directement dans l'application SwitchBot et utiliser les identifiants de scène dans la configuration.

[2026-01-10 17:30:00] - Implémentation du point de terminaison de santé (/healthz)
- Décision : Ajout d'un point de terminaison `/healthz` pour surveiller l'état de l'application, y compris le statut du planificateur, l'état de l'automatisation et le dernier tick.
- Motivation : Fournir un moyen standardisé de surveiller l'état de l'application, ce qui est essentiel pour le débogage et l'intégration avec des systèmes de surveillance externes.
- Implication : Le point de terminaison renvoie des réponses JSON structurées avec des codes d'état HTTP appropriés (200 pour le succès, 503 pour les erreurs de service) et gère gracieusement les échecs du magasin de données.

[2026-01-10 18:45:00] - Automatisation pilotée par scènes SwitchBot
- Décision : implémenter un système d'automatisation basé sur les scènes SwitchBot avec mécanisme de fallback.
- Motivation : permettre une configuration plus flexible et puissante via l'application SwitchBot officielle, tout en maintenant une rétrocompatibilité avec l'approche existante basée sur les commandes directes.
- Implémentation :
  - Création du module `aircon.py` pour centraliser la logique liée aux scènes
  - Mise à jour de `AutomationService` pour prioriser les scènes avec fallback sur `setAll`/`turnOff`
  - Ajout d'une configuration optionnelle des scènes (`aircon_scenes` dans settings.json)
  - Mise à jour de la documentation utilisateur et technique
- Avantages :
  - Permet des configurations avancées via l'application SwitchBot (séquences d'actions, délais, etc.)
  - Réduit le nombre d'appels API en combinant plusieurs actions en une seule scène
  - Maintient la compatibilité avec les configurations existantes

[2026-01-10 19:18:00] - Suppression des actions rapides quick_winter et quick_summer
- Décision : Supprimer les actions rapides "Chauffage (Hiver)" et "Clim (Été)" du tableau de bord au profit des scènes SwitchBot.
- Motivation : Simplifier l'interface utilisateur et promouvoir l'utilisation des scènes SwitchBot qui offrent plus de flexibilité et de fonctionnalités. Les scènes permettent des configurations plus avancées via l'application SwitchBot officielle.
- Implémentation :
  - Suppression des routes `quick_winter` et `quick_summer` dans `routes.py`
  - Mise à jour de l'interface utilisateur dans `index.html`
  - Mise à jour de la documentation dans `ui-guide.md`
  - Conservation de la fonctionnalité `quick_off` pour désactiver l'automatisation et éteindre le climatiseur
- Impact : Les utilisateurs doivent maintenant utiliser les scènes SwitchBot pour les modes hiver et été, ce qui offre une meilleure expérience utilisateur et plus de fonctionnalités.