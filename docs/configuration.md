# Configuration du Dashboard

## Fichiers de configuration

### 1. Identifiants SwitchBot (`.env`)

Les identifiants API sont stockés dans `.env` et jamais sérialisés dans les fichiers JSON :

```bash
SWITCHBOT_TOKEN=votre_token_ici
SWITCHBOT_SECRET=votre_secret_ici
SWITCHBOT_RETRY_ATTEMPTS=2
SWITCHBOT_RETRY_DELAY_SECONDS=10
```

> ⚠️ **Sécurité** : Ne jamais commiter `.env`. Utiliser `.env.example` comme modèle.

### 2. Paramètres applicatifs (`config/settings.json`)

Ce fichier contient les réglages métier persistés :

```json
{
  "meter_device_id": "C271111EC0AB",
  "aircon_device_id": "02-202008110034-13",
  "poll_interval_seconds": 60,
  "command_cooldown_seconds": 30,
  "hysteresis_celsius": 0.5,
  "automation_enabled": true,
  "mode": "summer",
  "time_windows": {
    "monday": {"enabled": true, "start": "08:00", "end": "22:00"},
    "tuesday": {"enabled": true, "start": "08:00", "end": "22:00"}
  },
  "summer_profile": {
    "min_temperature": 22.0,
    "max_temperature": 26.0,
    "target_temperature": 24.0,
    "ac_mode": 2,
    "fan_speed": 1
  },
  "winter_profile": {
    "min_temperature": 18.0,
    "max_temperature": 22.0,
    "target_temperature": 20.0,
    "ac_mode": 5,
    "fan_speed": 1
  }
}
```

## Inventaire des devices (`/devices`)

### Workflow de récupération des IDs

1. Ouvrir la page `/devices` (bouton **Devices** dans la barre supérieure)
2. La carte "Inventory snapshot" affiche :
   - Nombre de devices physiques (`deviceList`)
   - Nombre de télécommandes IR (`infraredRemoteList`)
3. Utiliser les cartes individuelles :
   - Bouton **Copier l'ID** pour coller directement dans `settings.json`
   - Badges "Hub/Standalone" pour vérifier la topologie
   - Métadonnées (firmware, statut, batterie) pour diagnostic
4. Pour debug : ouvrir les blocs `<details>` "Afficher le JSON brut"

> 💡 Ce workflow évite les erreurs de copie depuis l'app mobile et garantit l'utilisation des IDs officiels SwitchBot.

### Types de devices requis

- **Capteur de température** : `deviceType: "Meter"` → `meter_device_id`
- **Télécommande IR climatisation** : `remoteType: "Air Conditioner"` → `aircon_device_id`

## Validation et constantes

La validation des formulaires utilise des constantes partagées dans `routes.py` :

```python
# @switchbot_dashboard/routes.py#15-207
DAY_CHOICES = [...]
TIME_CHOICES = [...]
TEMP_CHOICES = [...]
AC_MODE_CHOICES = [...]
FAN_SPEED_CHOICES = [...]
```

### Règles de validation

- `poll_interval_seconds` : 15‑3600 s
- `command_cooldown_seconds` : 0‑3600 s  
- `hysteresis_celsius` : 0‑5 °C
- Températures : 14‑32 °C par pas de 0,5 °C
- Modes AC : 1 (Auto), 2 (Cool), 3 (Dry), 4 (Fan), 5 (Heat)
- Vitesses : 1 (Auto), 2 (Low), 3 (Medium), 4 (High)

> 📝 Les helpers `_as_bool`, `_as_int`, `_as_float` garantissent la cohérence entre UI et stockage JSON. Décision documentée dans `memory-bank/decisionLog.md` (2026-01-09 16:21).

## État opérationnel (`config/state.json`)

Ce fichier journalise l'état courant pour l'affichage UI :

```json
{
  "last_temperature": 23.5,
  "last_humidity": 55,
  "last_action": "setAll",
  "last_action_at": "2026-01-09T17:30:00Z",
  "assumed_aircon_state": "on",
  "last_error": null
}
```

## Sécurité et bonnes pratiques

- **Principe du moindre privilège** : n'exposer que les données nécessaires
- **Accès atomique** : `JsonStore` utilise `threading.Lock` et écriture via fichier temporaire
- **Validation systématique** : jamais de consommation directe de `request.form`
- **Logs sécurisés** : jamais de secrets dans les logs, utilisation de `current_app.logger`

---

*Voir aussi [Guide UI](ui-guide.md) pour l'interaction avec les formulaires, [Tests](testing.md) pour la validation, et `memory-bank/systemPatterns.md` pour les patterns architecturaux.*
