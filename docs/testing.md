# Tests et Validation

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Ce guide décrit les tests manuels recommandés pour valider le bon fonctionnement du SwitchBot Dashboard. Les tests couvrent l'installation, la configuration, l'interface utilisateur et les scénarios d'erreur.

> 📝 **Décisions connexes** : Les patterns de tests sont documentés dans `memory-bank/systemPatterns.md` et `memory-bank/decisionLog.md`. Voir notamment les décisions du 2026-01-14 sur la validation PostgreSQL et du 2026-01-18 sur les tests frontend.

## Tests d'installation

### 1. Environnement virtuel

```bash
# Vérifier que le venv est activé et les dépendances installées
/mnt/venv_ext4/venv_switchbot/bin/python -c "import flask, requests, apscheduler; print('OK')"
```

### 2. Démarrage du serveur

```bash
/mnt/venv_ext4/venv_switchbot/bin/python app.py
# Vérifier : http://127.0.0.1:5000/ s'affiche sans erreur
```

### 3. Suite Pytest (obligatoire)

```bash
# Toujours exécuter la suite avec l'interpréteur du projet pour éviter les divergences d'environnement
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest

# Alternative avec environnement local
source venv/bin/activate
python -m pytest
```

**Objectifs de couverture** :
- Maintenir ≥85% de couverture (voir `.windsurf/rules/codingstandards.md`)
- Prioriser les tests unitaires pour les conversions/validateurs
- Couvrir les scénarios d'intégration automation → DB → UI
- Inclure les tests de régression pour les hotspots identifiés par `radon` (voir `docs/complexity_report.txt`)

### 3. Configuration initiale

```bash
# Vérifier que .env existe et contient les tokens
test -f .env && grep -q "SWITCHBOT_TOKEN\|SWITCHBOT_SECRET" .env
```

## Tests de configuration

### 1. IDs de devices invalides

**Scénario** : `settings.json` avec `meter_device_id` ou `aircon_device_id` vide/incorrect

**Attendu** :
- Message d'erreur dans le dashboard
- Pas de crash du serveur
- `state.json` contient l'erreur

**Validation** :
```bash
# Mettre un ID incorrect dans settings.json
# Ouvrir http://127.0.0.1:5000/
# Vérifier l'affichage d'erreur
```

### 2. Paramètres hors limites

**Scénarios** :
- `poll_interval_seconds` < 15 ou > 3600
- `min_temperature` > `max_temperature`
- `hysteresis_celsius` > 5

**Attendu** :
- Flash message d'erreur
- `settings.json` non modifié
- Formulaire réinitialisé aux valeurs valides

### 3. Fenêtre horaire invalide

**Scénario** : Jours cochés mais heures non définies (ou inverse)

**Attendu** :
- Message "Invalid time window..."
- Aucune écriture dans `settings.json`

## Tests du point de terminaison de santé

### 1. Endpoint `/healthz` - Cas nominal

**Prérequis :**
- Application démarrée avec une configuration valide
- Store fonctionnel (Redis ou JSON)
- Scheduler en cours d'exécution

**Scénarios de test :**
1. **Requête de base**
   ```bash
   curl -v http://localhost:8000/healthz
   ```
   - Vérifier le code de statut `200 OK`
   - Vérifier le contenu de la réponse :
     ```json
     {
       "status": "ok",
       "scheduler_running": true,
       "automation_enabled": true,
       "last_tick": "2024-01-10T14:30:00Z",
       "api_requests_total": 42,
       "api_requests_remaining": 958,
       "api_quota_day": "2024-01-10",
       "version": "1.0.0"
     }
     ```
   - Vérifier que `last_tick` est récent (< 5 minutes)
   - Vérifier que `api_requests_remaining` est cohérent avec le quota quotidien

2. **Vérification des métriques**
   - Exécuter plusieurs actions via l'API/UI
   - Vérifier que `api_requests_total` est incrémenté
   - Vérifier que `api_requests_remaining` est décrémenté en conséquence
   - Vérifier que `api_quota_day` correspond à la date du jour (UTC)

### 2. Tests d'erreur

1. **Store indisponible**
   - Démarrer l'application avec `STORE_BACKEND=invalid`
   - Vérifier que `/healthz` retourne `503 Service Unavailable`
   - Vérifier que `status` est `error` dans la réponse

2. **Scheduler arrêté**
   - Arrêter le scheduler via l'API/UI
   - Vérifier que `scheduler_running` est `false`
   - Vérifier que `status` est `warning`

3. **Quota épuisé**
   - Simuler un quota épuisé en modifiant le store
   - Vérifier que `api_requests_remaining` est `0`
   - Vérifier que `status` est `warning`

### 3. Surveillance continue

**Configuration recommandée :**
- **Fréquence** : Toutes les 5 minutes
- **Seuils d'alerte :**
  - `status != "ok"` → Critique
  - `scheduler_running == false` → Avertissement
  - `last_tick` > 10 minutes → Critique
  - `api_requests_remaining` < 100 → Avertissement
  - `api_requests_remaining` < 50 → Critique

**Outils recommandés :**
- **Uptime Kuma** : Surveillance de la disponibilité
- **Prometheus** : Collecte des métriques
- **Grafana** : Tableaux de bord de surveillance
- **AlertManager** : Gestion des alertes

### 4. Tests d'intégration

1. **Redémarrage de l'application**
   - Vérifier que les compteurs de quota sont conservés
   - Vérifier que le statut du scheduler est rétabli

2. **Changement de jour**
   - Simuler un changement de jour (minuit UTC)
   - Vérifier que les compteurs sont réinitialisés
   - Vérifier que `api_quota_day` est mis à jour

3. **Chargement élevé**
   - Simuler un nombre élevé de requêtes concurrentes
   - Vérifier que l'endpoint reste réactif
   - Surveiller l'utilisation mémoire/CPU

**Validation** :
- Simuler une panne (arrêter le planificateur, couper l'accès à l'API SwitchBot)
- Vérifier que les alertes se déclenchent correctement
- Vérifier que les alertes se résolvent lorsque le problème est corrigé

## Tests de l'automatisation

### 1. Priorité des scènes SwitchBot

**Scénario** : Vérifier que le service d'automatisation utilise d'abord les scènes configurées avant de recourir aux commandes bas niveau.

**Étapes :**
1. Configurer une scène `winter` valide
2. Simuler une température en dessous du seuil minimum
3. Vérifier que la scène `winter` est déclenchée
4. Vérifier que les commandes `setAll`/`turnOff` ne sont pas utilisées

**Assertions :**
- La scène est déclenchée exactement une fois
- Le log indique l'utilisation de la scène
- L'état du climatiseur est correctement mis à jour

### 2. Fallback sur les commandes bas niveau

**Scénario** : Vérifier le comportement lorsqu'une scène n'est pas configurée.

**Étapes :**
1. Supprimer la configuration de la scène `winter`
2. Simuler une température en dessous du seuil minimum
3. Vérifier que la commande `setAll` est utilisée avec les paramètres du profil hiver
4. Vérifier qu'un avertissement est enregistré dans les logs

**Assertions :**
- La commande `setAll` est appelée avec les bons paramètres
- Un avertissement est enregistré dans les logs
- L'interface utilisateur affiche un indicateur pour la scène manquante

### 3. Gestion des erreurs de scène

**Scénario** : Vérifier le comportement lorsqu'une scène échoue.

**Étapes :**
1. Configurer une scène avec un UUID invalide
2. Simuler une température en dessous du seuil minimum
3. Vérifier que le système bascule sur les commandes bas niveau
4. Vérifier qu'une erreur est enregistrée dans les logs

**Assertions :**
- Le système tente d'abord d'exécuter la scène
- En cas d'échec, il bascule sur les commandes bas niveau
- Une erreur est enregistrée dans les logs
- L'interface utilisateur affiche l'état d'erreur

### 4. Tests de performance

**Scénario** : Vérifier que le système peut gérer un grand nombre de scènes et de commandes.

**Étapes :**
1. Configurer plusieurs scènes avec des paramètres différents
2. Simuler des changements de température rapides
3. Surveiller les temps de réponse et l'utilisation des ressources

**Assertions :**
- Les temps de réponse restent acceptables (< 500ms)
- Aucune fuite de mémoire n'est détectée
- Les commandes sont exécutées dans le bon ordre

### 5. Tests d'intégration

**Scénario** : Vérifier l'intégration entre les différents composants.

**Étapes :**
1. Configurer des scènes pour différents modes (hiver, été, ventilation)
2. Simuler des changements de température et des plages horaires
3. Vérifier que les scènes appropriées sont déclenchées
4. Vérifier que le quota API est correctement mis à jour

**Assertions :**
- Les scènes sont déclenchées en fonction des conditions
- Le quota API est correctement mis à jour
- Les logs reflètent les actions entreprises
- L'interface utilisateur est mise à jour en temps réel

## Tests de l'interface utilisateur

### 1. Gestion du quota API

**Scénario** : Vérifier que l'interface affiche correctement les informations de quota.

**Étapes :**
1. Configurer un seuil d'alerte bas (ex: 100)
2. Simuler une consommation de quota
3. Vérifier que l'alerte s'affiche lorsque le seuil est atteint
4. Vérifier que le compteur de quota est mis à jour en temps réel

**Assertions :**
- L'alerte de quota s'affiche au bon moment
- Le compteur est mis à jour après chaque action
- Le lien vers la configuration du quota fonctionne

### 2. Configuration des scènes

**Scénario** : Vérifier que l'interface permet de configurer les scènes.

**Étapes :**
1. Accéder à la page de configuration
2. Ajouter/modifier une scène
3. Vérifier que les changements sont enregistrés
4. Tester la scène directement depuis l'interface

**Assertions :**
- Les champs de formulaire sont correctement validés
- Les erreurs sont affichées de manière claire
- Les scènes sont exécutées comme prévu

### 3. Navigation

- **Pages** : Vérifier que toutes les pages sont accessibles
- **Liens** : Vérifier que tous les liens fonctionnent correctement
- **Responsive** : Tester l'affichage sur différentes tailles d'écran
- **Accessibilité** : Vérifier la navigation au clavier et le contraste des couleurs

### 4. Formulaire de configuration

- **Validation** : Tester la validation des champs (températures, heures, etc.)
- **Soumission** : Vérifier que les modifications sont correctement enregistrées
- **Retour d'erreur** : Vérifier que les messages d'erreur sont clairs et pertinents
- **Confirmation** : Vérifier que les actions critiques nécessitent une confirmation

## Tests de thème et styles

### 1. Contraste WCAG

**Éléments à vérifier** :
- Texte normal sur fond de carte : ratio ≥ 4.5:1
- Texte secondaire : ratio ≥ 4.5:1
- Boutons primaires : ratio ≥ 4.5:1

**Outils** :
- Extension Chrome "Contrast Checker"
- WebAIM Contrast Checker

### 2. Cohérence visuelle

**Points de contrôle** :
- Toutes les cartes utilisent les mêmes variables CSS
- Les boutons ont des états hover/focus cohérents
- Les couleurs d'erreur/succès sont uniformes

### 3. Performance

**Validation** :
- Pas de styles inline dans les templates
- Utilisation des variables CSS
- Transitions fluides (60fps)

## Logs et debugging

### Préfixes de logs structurés

Le système utilise des préfixes pour faciliter le diagnostic des problèmes :

```bash
# Logs IFTTT
[ifttt] IFTTT webhook triggered successfully | status_code=200, url=https://maker.ifttt.com/trigger/...
[ifttt] IFTTT webhook failed | action_key=winter, error=timeout

# Logs d'automatisation
[automation] Automation tick started | trigger=scheduler, interval=60s
[automation] Using SwitchBot scene (webhook unavailable) | action_key=winter, scene_id=scene-w
[automation] Scheduled repeated off action | pending_repeats=1, interval_seconds=10

# Logs de santé
[health] Health check completed | status=ok, scheduler_running=true
```

### Commandes de recherche dans les logs

```bash
# Filtrer les logs IFTTT
grep "\[ifttt\]" /var/log/switchbot_dashboard.log

# Rechercher les fallbacks
grep "fallback" /var/log/switchbot_dashboard.log

# Surveiller les erreurs
grep -i "error\|failed" /var/log/switchbot_dashboard.log

# Logs de répétition OFF
grep "off repeat" /var/log/switchbot_dashboard.log

# Logs de quota API
grep "quota" /var/log/switchbot_dashboard.log
```

### Niveaux de log recommandés

- **DEBUG** : Développement et diagnostic détaillé
- **INFO** : Production normale (par défaut)
- **WARNING** : Production stable (réduit le bruit)
- **ERROR** : Problèmes critiques uniquement

**Activation du mode debug :**
```bash
export LOG_LEVEL=debug
python app.py
# ou dans Render : définir LOG_LEVEL=debug dans les variables d'environnement
```

## Tests d'automatisation

### 1. Logique d'hystérésis

**Scénario** : Température exactement à la limite ± hystérésis

**Exemple** :
- Min = 22°C, Max = 26°C, Hystérésis = 0.5°C
- Température = 22.5°C : pas de changement
- Température = 22.4°C : activation clim

**Validation** :
- Modifier `state.json` manuellement
- Déclencher `Run once`
- Vérifier la décision prise

### 2. Cooldown des commandes

**Scénario** : Actions rapides successives

**Attendu** :
- Respect du `command_cooldown_seconds`
- Pas de commandes en double
- `state.json` trace les tentatives

### 3. Fenêtres horaires

**Validation** :
- Configurer une fenêtre horaire spécifique
- Tester dedans/dehors des heures
- Vérifier que l'automatisation respecte les horaires

### 4. Système de quotas API

**Validation** :
1. **Compteur normal + fallback local**
   - Déclencher plusieurs actions manuelles (`Run once`, `Aircon ON/OFF`) et vérifier que `api_requests_total` dans `state.json` s'incrémente après chaque appel API réussi, même en l'absence d'headers (`AutomationService._record_local_quota_fallback` s'exécute alors automatiquement).
   - Forcer l'absence d'headers (ex : couper temporairement Internet ou invalider les tokens) et confirmer que le compteur continue d'augmenter grâce au fallback local.
2. **Réinitialisation à minuit UTC**
   - Modifier `api_quota_day` dans `state.json` pour une date passée, redémarrer le serveur et déclencher un appel API. Vérifier que `api_requests_total` repart de 1 et que `api_quota_day` se met à jour avec la date du jour (UTC).
3. **Affichage UI**
   - Ouvrir l'UI juste après un appel API pour constater la mise à jour du bandeau "Quota API quotidien" (restantes/utilisées).
   - Vérifier l'état "N/A" si aucune requête n'a encore été effectuée depuis le démarrage, puis constater la transition vers des chiffres réels après un appel.
4. **Seuil d’alerte opérateur**
   - Enchaîner des actions jusqu'à descendre sous 200 requêtes restantes (simulation possible via la modification de `api_requests_remaining`). La vignette doit refléter ce niveau bas, incitant à ralentir les actions manuelles ou à augmenter `poll_interval_seconds`.

### 5. Backend de stockage (filesystem vs Redis)

**Scénario** : S'assurer que les réglages persistent après redémarrage/redeploy.

1. Démarrer localement avec `STORE_BACKEND=filesystem`. Modifier un réglage via l'UI et vérifier la mise à jour du fichier `config/settings.json`.
2. Exporter `config/settings.json` / `config/state.json`, définir `STORE_BACKEND=redis`, `REDIS_URL` (ex. instance Redis Docker locale) et redémarrer.
3. Vérifier que l'UI affiche les réglages existants. Modifier de nouveaux paramètres, puis arrêter/redémarrer l'application : les valeurs doivent être conservées.
4. Simuler une indisponibilité Redis (arrêt du conteneur) : confirmer que des logs d'erreur apparaissent et que l'application retombe en mode filesystem.

### 6. Scènes SwitchBot (aircon_scenes)

**Objectif** : Vérifier que la configuration des scènes favorites (four slots : hiver, été, mode neutre, OFF) et les boutons rapides associés fonctionnent de bout en bout.

1. **Configuration UI**
   - Renseigner les champs “Aircon ON – Hiver/Été/Mode neutre” et “Aircon OFF (scène)” avec des `sceneId` valides via la carte “Scènes favorites SwitchBot”.
   - Cliquer sur “Save settings” et vérifier dans `config/settings.json` (ou Redis) que `aircon_scenes.winter/summer/fan/off` contiennent bien les IDs saisis.
2. **État des boutons rapides**
   - Rafraîchir `/` : les badges “Prêt” doivent apparaître et les quatre boutons correspondants doivent être actifs.
   - Supprimer un ID pour confirmer que le bouton est désactivé et affiche “Scene ID manquant”.
3. **Exécution et traçabilité**
   - Cliquer sur chaque bouton (`Aircon ON – Hiver`, `Aircon ON – Été`, `Aircon ON – Mode neutre`, `Aircon OFF (scène)`) et vérifier que :
     - Les flash messages confirment l’exécution.
     - `config/state.json` met à jour `last_action` avec `scene(<sceneId>)` et réinitialise les paramètres supposés (mode, power). Pour la scène OFF, vérifier que `assumed_aircon_power` passe à `"off"` et que les routes `/actions/aircon_off` et `/actions/quick_off` utilisent bien la scène configurée.
4. **Tests automatisés**
   - Exécuter `pytest tests/test_dashboard_routes.py::test_update_settings_persists_aircon_scenes tests/test_dashboard_routes.py::test_aircon_on_winter_runs_scene_and_updates_state tests/test_dashboard_routes.py::test_aircon_off_runs_off_scene_when_configured tests/test_dashboard_routes.py::test_quick_off_prefers_scene_and_disables_automation` pour couvrir la persistance, les actions ON et OFF via scènes.

### Tests IFTTT Webhooks - [2026-01-11] - Mise à jour complète

**Objectif** : Vérifier l'intégration complète des webhooks IFTTT avec le système de fallback cascade.

#### 1. Configuration des webhooks
- Configurer des URLs IFTTT valides (format `https://maker.ifttt.com/trigger/.../with/key/...`)
- Tester les URLs directement avec `curl` pour valider l'accessibilité
- Vérifier la validation HTTPS (HTTP doit être rejeté)

#### 2. Exécution des webhooks
- Cliquer sur les boutons de scènes (Hiver, Été, Ventilation, Arrêt)
- Vérifier dans les logs que le webhook est déclenché en premier
- Confirmer que les appels IFTTT ne consomment pas le quota API SwitchBot

#### 3. Fallback automatique
- Configurer une URL IFTTT invalide et une scène SwitchBot valide
- Déclencher une action et vérifier le fallback vers la scène SwitchBot
- Supprimer la scène et vérifier le fallback vers les commandes directes

#### 4. Tests automatisés
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_ifttt.py
```
- Tests de validation d'URL (HTTPS obligatoire)
- Tests de déclenchement avec mock
- Tests de timeout et gestion d'erreurs

#### 5. Tests de logs structurés
- Vérifier la présence des préfixes `[ifttt]` dans les logs
- Confirmer que les fallbacks sont correctement journalisés
- Valider la structure des logs avec métadonnées

#### 6. Tests de timeout et gestion erreurs
- Simuler un timeout IFTTT (URL lente ou inaccessible)
- Vérifier le fallback automatique vers les scènes
- Tester les erreurs HTTP 4xx/5xx
- Valider les logs d'erreur structurés

### Tests de répétition OFF - [2026-01-11] - Mise à jour complète

**Objectif** : Valider le fonctionnement de la répétition paramétrable des commandes OFF.

#### 1. Configuration de la répétition
- Configurer `off_repeat_count: 2` et `off_repeat_interval_seconds: 10`
- Vérifier la persistance dans `settings.json`
- Tester les bornes de validation (1-10, 1-600s)

#### 2. Exécution de la répétition
- Déclencher une action OFF (automatique ou manuelle)
- Observer dans les logs : `[automation] Executing scheduled off repeat`
- Vérifier l'état dans `state.json` sous `pending_off_repeat`

#### 3. Annulation des répétitions
- Déclencher une action ON pendant des répétitions OFF en attente
- Vérifier que les répétitions sont annulées
- Confirmer que `pending_off_repeat` est vidé

#### 4. Tests automatisés
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_automation_service.py::test_off_repeat_parameter
```
- Tests de planification des répétitions
- Tests d'annulation lors d'actions ON
- Tests de validation des paramètres (bornes 1-10, 1-600s)

#### 5. Tests d'idempotence - [2026-01-12]
- Configurer une température élevée (> seuil max + hysteresis)
- Déclencher une action OFF (vérifier `assumed_aircon_power="off"`)
- Tenter de redéclencher OFF : doit être ignoré avec log `Skipping winter_off: already assumed off`
- Déclencher ON : doit réinitialiser `assumed_aircon_power="on"`
- Vérifier que les logs sont cohérents

### Tests de gestion timezone - [2026-01-12] - Mise à jour complète

**Objectif** : Valider le fonctionnement timezone-aware des fenêtres horaires.

#### 1. Configuration du fuseau
- Configurer `timezone: "Europe/Paris"` (défaut)
- Tester avec `timezone: "UTC"` et `timezone: "Europe/London"`
- Configurer un fuseau invalide et vérifier le fallback UTC

#### 2. Tests de conversion horaire
- Configurer une fenêtre 10:00-01:00 (jour suivant)
- Vérifier que l'automatisation fonctionne correctement à 00:30 UTC (01:30 Paris)
- Tester les transitions horaires (été/hiver)

#### 3. Tests automatisés
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_automation_service.py::test_timezone_handling
```
- Tests de validation IANA
- Tests de conversion UTC→local
- Tests des fenêtres horaires timezone-aware

### Tests UI mobile et bandeau quota - [2026-01-12] - Mise à jour complète

**Objectif** : Valider les améliorations UI/UX mobile et l'affichage du bandeau quota.

#### 1. Tests du bandeau d'alerte quota
- Configurer `api_quota_warning_threshold: 100`
- Simuler une consommation proche du seuil
- Vérifier l'affichage du bandeau sur la page d'accueil
- Tester la responsivité du bandeau sur mobile

#### 2. Tests de la grille status-grid
- Tester l'affichage sur desktop (multi-colonnes)
- Tester sur mobile (single colonne)
- Vérifier les attributs ARIA pour accessibilité

#### 3. Tests du feedback dynamique des jours
- Sélectionner des jours dans le formulaire des fenêtres horaires
- Vérifier le compteur live des jours sélectionnés
- Tester `aria-live` pour lecteurs d'écran

#### 4. Tests des détails pliables (/devices)
- Ouvrir/fermer les sections `<details>` sur mobile
- Vérifier que l'ID reste toujours visible
- Tester le bouton de copie d'ID

#### 5. Tests automatisés avec BeautifulSoup
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_dashboard_routes.py::test_quota_warning_display
```
- Tests d'affichage conditionnel du bandeau
- Tests de présence des classes CSS mobile
- Tests des attributs ARIA

### Tests d'erreur et résilience

### 1. API SwitchBot injoignable

**Simulation** :
- Couper Wi-Fi ou mettre des tokens invalides
- Déclencher une action

**Attendu** :
- Message d'erreur dans l'UI
- `state.json` contient l'erreur
- Pas de crash du serveur

### 2. HTTP 429 (rate limit)

**Scénario** : Appels API très rapides

**Attendu** :
- Retry automatique avec délai
- Message informatif si échec final
- Respect des `SWITCHBOT_RETRY_*`

### 3. Corruption JSON

**Test** :
- Corrompre manuellement `settings.json`
- Redémarrer le serveur

**Attendu** :
- Message d'erreur clair
- Fichier non écrasé
- Possibilité de correction manuelle

## Tests de sécurité

### 1. Secrets non exposés

**Vérifications** :
- Aucun token dans `settings.json` ou `state.json`
- Pas de secrets dans les logs
- `.env` bien dans `.gitignore`

### 2. Validation des entrées

**Points de contrôle** :
- Helpers `_as_bool/_as_int/_as_float` utilisés
- Pas de consommation directe de `request.form`
- Bornes respectées sur tous les champs

## Tests unitaires (nouvelles fonctionnalités)

### Tests IFTTT Webhooks (`tests/test_ifttt.py`)

**Fichier de test** : `tests/test_ifttt.py` (16 tests)

**Scénarios couverts** :
1. **Validation des URLs** :
   - URLs HTTPS valides acceptées
   - URLs HTTP et invalides rejetées
   - URLs vides et nulles gérées

2. **Client IFTTT** :
   - Trigger webhook réussi (status 200)
   - Gestion des timeouts (10s par défaut)
   - Erreurs HTTP et réseau
   - Validation des payloads JSON

3. **Extraction des webhooks** :
   - Normalisation des configurations
   - Clés manquantes (winter, summer, fan, off)
   - Types de données invalides

**Exécution** :
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_ifttt.py -v
```

### Tests de répétition OFF (`tests/test_automation_service.py`)

**Nouveaux tests ajoutés** :
1. **Planification des répétitions** :
   - `_schedule_off_repeat_task()` crée les tâches correctement
   - Validation des bornes (count: 1-10, interval: 1-600s)
   - État `pending_off_repeat` mis à jour dans `state.json`

2. **Exécution différée** :
   - `_process_off_repeat_task()` exécute les répétitions
   - Décrémentation correcte du compteur
   - Logs appropriés pour chaque exécution

3. **Purge automatique** :
   - `_clear_off_repeat_task()` nettoie l'état
   - Annulation sur nouvelle action ON
   - Gestion des cas où aucune répétition n'est en cours

**Scénarios de test** :
```python
# Test de la planification
def test_schedule_off_repeat_task():
    # Vérifie création de pending_off_repeat avec count=2, interval=10
    
# Test de l'exécution
def test_process_off_repeat_task():
    # Vérifie décrémentation et exécution
    
# Test de l'idempotence
def test_off_idempotence_when_already_off():
    # Vérifie qu'aucun nouvel OFF n'est envoyé si assumed_aircon_power="off"
```

### Tests de robustesse du scheduler

**Nouveaux comportements testés** :
1. **Démarrage conditionnel** :
   - `SCHEDULER_ENABLED=false` : scheduler ne démarre pas
   - `FLASK_DEBUG=1` avec Gunicorn : scheduler démarre
   - `flask run` : scheduler ne démarre pas

2. **Logging amélioré** :
   - `reschedule()` loggue en DEBUG pas WARNING
   - Messages informatifs pour les états normaux

**Exécution ciblée** :
```bash
# Tests spécifiques au scheduler
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_automation_service.py::test_scheduler_* -v

# Tests IFTTT complets
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_ifttt.py -v

# Tests de répétition OFF
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_automation_service.py::test_off_repeat -v
```

### Tests d'intégration avec BeautifulSoup

**Tests UI avec quota** :
- Vérification de l'affichage de l'alerte quota
- Test du seuil `api_quota_warning_threshold`
- Validation des métadonnées (jour, reset_at)

**Exécution** :
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest tests/test_dashboard_routes.py::test_quota_warning -v
```

### Couverture de tests complète

**Statut actuel** : 53 tests passants (au 12 Jan 2026)

**Répartition** :
- `test_app_init.py` : Initialisation et santé
- `test_dashboard_routes.py` : Routes et interface
- `test_automation_service.py` : Logique métier et répétitions
- `test_ifttt.py` : Webhooks et fallbacks
- `test_adaptive_cooldown.py` : Cooldown adaptatif
- `test_aircon_presets.py` : Extraction et validation des scènes (`_extract_aircon_scenes`) + migrations legacy

**Commande complète** :
```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pytest --tb=short -q
```

## Checklist finale

- [ ] Installation et démarrage OK
- [ ] Configuration tokens/IDs fonctionnelle
- [ ] Interface responsive desktop/mobile
- [ ] Actions manuelles fonctionnent
- [ ] Automatisation respecte les seuils
- [ ] Page `/devices` permet la copie d'ID
- [ ] Thème sombre respecte WCAG AA
- [ ] Erreurs API gérées proprement
- [ ] Sécurité des tokens respectée
- [ ] Performance acceptable

---

*Voir aussi [Configuration](configuration.md) pour les paramètres, [Guide UI](ui-guide.md) pour les interactions, et `memory-bank/progress.md` pour l'historique des tests.*

### Bandeau d'alerte de quota
- Tests dans `test_dashboard_routes.py` couvrent :
  - Affichage quand quota ≤ seuil
  - Masquage quand quota > seuil
  - Cas limites (seuil = 0)

```
### Conversion de Timezone
- `test_dashboard_routes.py` inclut :
  - Gestion des timezones valides (Europe/Paris)
  - Fallback pour timezone invalide (UTC)
  - Formats de timestamp (naïf, suffixe Z)
```
### Conversion de Timezone
- `test_dashboard_routes.py` inclut :
  - Gestion des timezones valides (Europe/Paris)
  - Fallback pour timezone invalide (UTC)
  - Formats de timestamp (naïf, suffixe Z)

```

### Répétition OFF
- `test_automation_service.py` teste :
  - Logique de planification
  - Vérifications d'idempotence
  - Annulation par les actions ON

```

### Chemins de fallback IFTTT
- `test_ifttt.py` vérifie :
  - Cascade webhook → scène → commande
  - Récupération d'erreur à chaque niveau
  - Complétude des logs

---

## Références croisées

### Documentation technique
- [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) – Standards de développement obligatoires
- [DOCUMENTATION.md](DOCUMENTATION.md) – Architecture et métriques
- [setup.md](setup.md) – Installation et configuration initiale
- [configuration.md](configuration.md) – Paramètres applicatifs

### Guides spécialisés
- [Intégration IFTTT](ifttt-integration.md) – Tests webhooks et cascade
- [Migration PostgreSQL](postgresql-migration.md) – Tests de stockage
- [Guide du scheduler](scheduler.md) – Tests APScheduler

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions de tests (PostgreSQL, frontend, backend)
- `memory-bank/systemPatterns.md` – Patterns de tests et validation
- `memory-bank/progress.md` – Historique des validations

---

*Ce document fait partie de la documentation structurée du SwitchBot Dashboard. Retour au [README principal](README.md).*
