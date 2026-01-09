# SwitchBot Flask Dashboard (local)

## Prérequis

- Python 3.10+
- Un compte SwitchBot avec Cloud Service activé
- Un `token` et un `secret` SwitchBot (API v1.1)

## Installation (venv demandé)

Tu as demandé d'utiliser le venv situé dans `/mnt/venv_ext4/venv_switchbot`.

Dans un terminal:

```bash
/mnt/venv_ext4/venv_switchbot/bin/python -m pip install -r requirements.txt
```

## Configuration

1. Copier le fichier d'exemple:

```bash
cp .env.example .env
```

2. Remplir dans `.env`:

- `SWITCHBOT_TOKEN`
- `SWITCHBOT_SECRET`

Optionnel (recommandé si Wi‑Fi instable):

- `SWITCHBOT_RETRY_ATTEMPTS` (par défaut `2` = 1 retry)
- `SWITCHBOT_RETRY_DELAY_SECONDS` (par défaut `10`)

3. Ouvrir `config/settings.json` et renseigner:

- `meter_device_id`: l'ID du capteur (deviceType: `Meter`)
- `aircon_device_id`: l'ID de la télécommande IR virtuelle (remoteType: `Air Conditioner`)

#### Inventaire `/devices`

1. Ouvre la page `/devices` (bouton **Devices** dans la barre supérieure).
2. Repère la carte “Inventory snapshot” : elle compte séparément les devices physiques (`deviceList`) et les télécommandes IR (`infraredRemoteList`), ce qui confirme immédiatement que ton compte est bien synchronisé.
3. Utilise les cartes individuelles :
   - Bouton **Copier l'ID** pour coller directement `meter_device_id` ou `aircon_device_id` dans `config/settings.json`.
   - Badges “Hub/Standalone” ou “Hub XXX” pour vérifier la topologie SwitchBot.
   - Les métadonnées (firmware, statut cloud, batterie) aident à diagnostiquer un device injoignable avant même de modifier la configuration.
4. Si tu dois inspecter le payload complet fourni par l'API (court‑circuiter un bug, vérifier un `virtualModel`, etc.), ouvre les blocs `<details>` “Afficher le JSON brut deviceList/infraredRemoteList`. Ils restent disponibles sans surcharger l'UI principale.

> 💡 Ce workflow évite les copier/coller depuis l'app mobile : l'intégralité des identifiants nécessaires est accessible depuis le navigateur, validée par les listes officielles SwitchBot.

### Paramétrage dans l'UI

Une fois les identifiants saisis, l'écran principal (`/`) permet d'ajuster tous les réglages via une carte **Settings** orientée mobile :

- **Automatisation & mode** : interrupteur principal et menu `winter/summer`.
- **Fenêtre horaire** : cases à cocher par jour (lundi→dimanche) et dropdowns 24 h pour `start/end`. Les options proviennent des constantes backend `DAY_CHOICES` et `_build_time_choices()` (@switchbot_dashboard/routes.py#15-207), garantissant que la validation et l'UI restent synchrones.
- **Profils Winter/Summer** : chaque profil dispose de dropdowns bornés pour `min/max/target` (0,5 °C de pas), `ac_mode` (Auto/Cool/Dry/Fan/Heat) et `fan_speed` (Auto/Low/Medium/High). Les menus sont alimentés par `TEMP_CHOICES`, `AC_MODE_CHOICES` et `FAN_SPEED_CHOICES`, ce qui évite toute valeur non supportée.

> 💡 Sur mobile, les badges “mobile friendly” et la mise en page responsive (cards, boutons pill) permettent de cocher rapidement les jours puis de sélectionner l’heure via des sélecteurs, sans saisie libre.

### Thème sombre par défaut

Les templates `index.html` et `devices.html` utilisent désormais un thème sombre immersif :

- Palette centralisée via des variables CSS (`--sb-bg`, `--sb-card`, `--sb-text`, `--sb-accent`, etc.) pour garantir une cohérence de contraste et faciliter les futurs thèmes. Les variables sont déclarées dans `switchbot_dashboard/static/css/theme.css` et consommées par les feuilles spécifiques `index.css` et `devices.css`.
- Cartes vitrées avec blur et bordures légères, ombres prononcées et boutons pill pour une lecture confortable sur desktop comme sur mobile.
- Alertes, formulaires et badges consomment les mêmes variables afin d'assurer lisibilité (WCAG) et maintenance rapide lorsque la palette évolue.

> ℹ️ Toute personnalisation visuelle doit passer par l'extension de ces variables, pas par des couleurs inline. Étendre `theme.css` en priorité, puis ajouter (si besoin) des règles ciblées dans `index.css` ou `devices.css` pour conserver la séparation des responsabilités conformément aux décisions du 2026‑01‑09 16:47 documentées dans la Memory Bank.

#### Organisation des feuilles de style

- `switchbot_dashboard/static/css/theme.css` : palette sombre, composants globaux (cartes, formulaires, badges, alertes) et typographie. Ajoute toute nouvelle variable ici pour garder la documentation et le code synchronisés.
- `switchbot_dashboard/static/css/index.css` : règles propres à la carte **Settings** et aux interactions de l'écran principal (chips des jours, carte “Time window”, badges “mobile friendly”, etc.). Ne pas réintroduire de styles inline dans `index.html`.
- `switchbot_dashboard/static/css/devices.css` : mise en forme de la page `/devices` (grille responsive, boutons “Copier l’ID”, badges Hub/Standalone, blocs JSON). Réutilise les variables déclarées dans `theme.css` afin d'éviter des écarts de contraste.

> 💡 Pour toute nouvelle page, commence par vérifier si un composant existe déjà dans `theme.css`. Étends-le ensuite via la feuille dédiée à la page plutôt que d’ajouter des couleurs ou ombres non référencées.

### UI & accessibilité

- Conserve la hiérarchie actuelle (Space Grotesk + composants arrondis) lorsque tu ajoutes des pages : cela garantit l'homogénéité du thème sombre et évite les contrastes incohérents.
- Les boutons critiques (Run once, profils hiver/été, copie d'ID) exposent des labels explicites et des attributs `aria-label` pour les lecteurs d'écran ; reproduis ce modèle sur toute nouvelle action.
- Les messages flash et alertes héritent des couleurs `--sb-warning/--sb-success/--sb-danger` : si tu ajoutes un nouveau statut, pense à étendre la palette et à documenter la variable correspondante ici.

### Règles de validation

Le formulaire `/settings` s’appuie sur les helpers `_as_bool`, `_as_int`, `_as_float` (@switchbot_dashboard/routes.py#75-244). Concrètement :

1. Les champs numériques sont bornés : `poll_interval_seconds` (15‑3600 s), `command_cooldown_seconds` (0‑3600 s), `hysteresis_celsius` (0‑5 °C).
2. Toute tentative de créer une fenêtre horaire partielle (jours sans heure ou inversement) déclenche un `flash("Invalid time window...", "error")` et n’écrit rien dans `settings.json`.
3. Les profils saisonniers sont forcés via les dropdowns : impossible de sortir du domaine supporté par SwitchBot (modes 1‑5, vitesses 1‑4, températures 14‑32 °C par pas de 0,5).

Documente systématiquement les futures extensions en mettant à jour les constantes dans `routes.py` afin de conserver la parité UI/validation (cf. décision du 2026‑01‑09 16:21 dans la Memory Bank).

## Lancement

```bash
/mnt/venv_ext4/venv_switchbot/bin/python app.py
```

Puis ouvre:

- http://127.0.0.1:5000/

## Fonctionnement

- Le serveur lit la température via `GET /v1.1/devices/{deviceId}/status` (capteur Meter)
- Le contrôle clim utilise la télécommande IR virtuelle via:
  - `turnOff`
  - `setAll` avec paramètre: `{temperature},{mode},{fan_speed},{power_state}`

### Actions rapides & journalisation

La carte **Current status** affiche la dernière lecture, les erreurs, ainsi que des boutons:

- `Run once` : déclenche manuellement la boucle `AutomationService.run_once`.
- `Chauffage (Hiver)` / `Clim (Été)` / `Off` : basculent `settings["mode"]`, réactivent l’automatisation et envoient immédiatement `setAll` ou `turnOff`.
- `Aircon ON (setAll)` / `Aircon OFF` : commandes directes, même hors automation.

Chaque action met à jour `state.json` (`assumed_aircon_*`, `last_action`, `last_action_at`) pour que l’UI reste cohérente (@switchbot_dashboard/routes.py#351-476). Pense à vérifier ces champs si tu testes des scénarios manuels.

Références modes (SwitchBot doc):

- mode: 2=cool, 5=heat
- fan_speed: 1=auto, 2=low, 3=medium, 4=high

## Retry (anti-échecs réseau)

Le client SwitchBot relance automatiquement une action si un échec transitoire survient:

- erreurs réseau / timeout
- HTTP 429
- HTTP 5xx
- `statusCode` SwitchBot `190`

Le comportement est configurable via `.env`.

## Tests à prévoir (suggestions)

- Vérifier qu'une configuration invalide (IDs vides, min>max, JSON windows invalide) n'entraîne pas de crash et remonte une erreur dans le dashboard
- Vérifier que le `cooldown` empêche le spam de commandes
- Vérifier les transitions de seuil avec hysteresis (cas limite à +/- hysteresis)
- Tester la page `/devices` en mobile et desktop : cartes visibles, badges lisibles, retour visuel “Copié ✓” après clic sur **Copier l'ID**.
- Confirmer que les blocs `<details>` s'ouvrent correctement et qu'ils reflètent fidèlement les payloads SwitchBot (utile pour diagnostiquer un ID manquant ou un `remoteDeviceType` inattendu).
- Vérifier que la palette sombre reste cohérente après l'ajout d'un composant (contrastes WCAG AA sur les titres, boutons et alertes).
- Sur `/devices`, vérifier que l’événement clipboard renvoie bien “Copié ✓” puis revient à l’état normal après 1,8 s, et qu’une erreur `navigator.clipboard` est loguée proprement en console.
- Si de nouvelles couleurs sont introduites dans `theme.css`, mesurer leur ratio de contraste (WCAG AA/AAA) avant de les exposer aux composants critiques (titres, badges d’état, boutons primaires).
