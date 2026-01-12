# Intégration IFTTT pour SwitchBot Dashboard

## Vue d'ensemble

Ce dashboard permet désormais de déclencher vos scènes de climatisation via des **webhooks IFTTT** au lieu d'utiliser directement l'API SwitchBot. Cette approche offre plusieurs avantages :

- **Fiabilité accrue** : les webhooks IFTTT déclenchent les scènes SwitchBot via le cloud IFTTT
- **Flexibilité** : vous pouvez créer des applets IFTTT complexes (notifications, logs, chaînes d'actions)
- **Compatibilité** : contourne les limitations de l'API SwitchBot native pour le déclenchement de scènes

## Architecture de fallback

Le système implémente une **cascade de fallback** à trois niveaux pour garantir une fiabilité maximale :

1. **Webhook IFTTT** (priorité) → déclenche l'applet IFTTT qui exécute une scène SwitchBot
2. **Scène SwitchBot** (fallback 1) → appelle directement l'API SwitchBot `/scenes/{id}/execute`
3. **Commande directe** (fallback 2) → utilise `turnOff` ou `setAll` sur le device IR

### Ordre de priorité

- **IFTTT** : Toujours essayé en premier (pas de consommation quota API)
- **Scène** : Utilisée si le webhook échoue ou est absent
- **Commande** : Dernier recours (nécessite `aircon_device_id`, uniquement pour "off")

### Avantages de cette architecture

- ✅ **Résilience** : Si un niveau échoue, le système bascule automatiquement au suivant
- ✅ **Économie** : Les webhooks IFTTT ne consomment pas le quota SwitchBot (10 000/jour)
- ✅ **Flexibilité** : Possibilité de créer des applets IFTTT complexes (notifications, logs, multi-actions)
- ✅ **Compatibilité** : Contourne les bugs de l'API SwitchBot native pour l'exécution de scènes

### Exemples de payloads JSON

Les webhooks IFTTT peuvent recevoir des données structurées pour enrichir les applets :

```json
{
  "action": "winter",
  "temperature": 18.5,
  "mode": "heating",
  "source": "automation",
  "timestamp": "2026-01-11T20:30:00Z"
}
```

```json
{
  "action": "off",
  "reason": "quick_off",
  "source": "manual",
  "timestamp": "2026-01-11T21:15:00Z"
}
```

### Logs structurés pour le debugging

Le système génère des logs détaillés avec préfixes pour faciliter le diagnostic :

```bash
# Webhook IFTTT déclenché avec succès
[ifttt] IFTTT webhook triggered successfully | status_code=200, url=https://maker.ifttt.com/trigger/...

# Fallback vers scène SwitchBot
[automation] IFTTT webhook failed | action_key=winter, error=timeout
[automation] Using SwitchBot scene (webhook unavailable) | action_key=winter, scene_id=scene-w

# Fallback vers commande directe
[automation] Scene execution failed | action_key=off, scene_id=scene-off, error=invalid_scene
[automation] Falling back to direct command | action_key=off, device_id=aircon-1
```

## Configuration

### Étape 1 : Connecter IFTTT à SwitchBot

1. Créez un compte IFTTT gratuit sur [ifttt.com](https://ifttt.com)
2. Connectez le service **SwitchBot** dans IFTTT :
   - Allez dans "Services" → recherchez "SwitchBot"
   - Autorisez IFTTT à accéder à votre compte SwitchBot
3. Créez vos scènes dans l'application SwitchBot mobile (ex: "Hiver 21°C", "Été 24°C", "Arrêt clim")

### Étape 2 : Créer des Applets IFTTT

Pour chaque action (winter, summer, fan, off), créez un applet IFTTT :

#### Exemple : Applet "Hiver"

1. **Trigger** : Webhooks → "Receive a web request"
   - Event Name : `switchbot_winter` (choisissez un nom unique)
2. **Action** : SwitchBot → "Execute scene"
   - Sélectionnez votre scène "Hiver 21°C"
3. Publiez l'applet

#### Récupérer l'URL du Webhook

1. Allez dans "Services" → Webhooks → "Documentation"
2. Copiez votre clé webhook (format : `https://maker.ifttt.com/trigger/{event}/with/key/{your_key}`)
3. Remplacez `{event}` par votre nom d'événement (ex: `switchbot_winter`)

**Exemple d'URL finale :**
```
https://maker.ifttt.com/trigger/switchbot_winter/with/key/abc123xyz
```

### Étape 3 : Configurer le Dashboard

1. Accédez à **Réglages** (`/reglages`)
2. Dans la section **"Webhooks IFTTT (Priorité)"**, renseignez les URLs pour chaque action :
   - **Hiver** : URL de votre applet winter
   - **Été** : URL de votre applet summer
   - **Ventilateur** : URL de votre applet fan
   - **Arrêt** : URL de votre applet off
3. Sauvegardez les paramètres

### Configuration optionnelle : Scènes SwitchBot (fallback)

Dans la section **"Scènes favorites SwitchBot (Fallback)"**, vous pouvez configurer les IDs de scènes SwitchBot natives pour servir de secours si les webhooks IFTTT échouent.

## Utilisation

### Actions manuelles

Les boutons du dashboard utilisent automatiquement les webhooks IFTTT :
- Bouton **"Hiver"** → webhook winter → scène SwitchBot "Hiver"
- Bouton **"Été"** → webhook summer → scène SwitchBot "Été"
- Bouton **"Ventilateur"** → webhook fan → scène SwitchBot "Fan"
- Bouton **"Quick OFF"** → webhook off → scène SwitchBot "Arrêt"

### Automatisation

L'automatisation (`AutomationService`) suit la même logique :
- Température < seuil min → webhook winter
- Température > seuil max → webhook summer/off selon le mode

## Logique de fallback

```
┌─────────────────────────┐
│  Webhook IFTTT défini ? │
└─────────┬───────────────┘
          │ Oui
          ▼
    ┌─────────────────┐
    │ Trigger Webhook │
    └────┬────────────┘
         │ Succès
         ▼
    ┌─────────┐
    │   FIN   │
    └─────────┘

    ┌──────────────────────┐
    │ Webhook échoue/absent│
    └─────────┬────────────┘
              │
              ▼
    ┌──────────────────────┐
    │  Scène SwitchBot ?   │
    └─────────┬────────────┘
              │ Oui
              ▼
        ┌─────────────┐
        │  run_scene  │
        └─────┬───────┘
              │ Succès
              ▼
        ┌─────────┐
        │   FIN   │
        └─────────┘

        ┌──────────────────────┐
        │ Scène échoue/absente │
        └─────────┬────────────┘
                  │
                  ▼
        ┌────────────────────────┐
        │ aircon_device_id défini?│
        └─────────┬──────────────┘
                  │ Oui (uniquement pour "off")
                  ▼
            ┌──────────┐
            │ turnOff  │
            └─────┬────┘
                  │
                  ▼
            ┌─────────┐
            │   FIN   │
            └─────────┘
```

## Avantages et limitations

### Avantages

✅ **Fiabilité maximale** : cascade de fallback à 3 niveaux (IFTTT → scène → commande)  
✅ **Économie de quota** : les appels IFTTT ne consomment pas le quota d'API SwitchBot (10 000/jour)  
✅ **Flexibilité** : créez des applets IFTTT complexes (notifications, logs, intégrations tierces)  
✅ **Résilience** : contournement automatique des bugs de l'API SwitchBot native  
✅ **Traçabilité** : logs détaillés pour chaque niveau de fallback  

### Limitations

⚠️ **Latence** : les webhooks IFTTT peuvent avoir un délai de quelques secondes  
⚠️ **Dépendance externe** : nécessite une connexion Internet et le service IFTTT opérationnel  
⚠️ **Configuration initiale** : nécessite de créer 4 applets IFTTT et récupérer les URLs  
⚠️ **Complexité** : plus de composants à maintenir (IFTTT + scènes + device IDs)

## Guide de dépannage

### Le webhook ne se déclenche pas

1. Vérifiez que l'URL est correcte (format `https://maker.ifttt.com/trigger/.../with/key/...`)
2. Testez l'URL directement dans votre navigateur ou avec `curl`
3. Consultez les logs du dashboard : recherchez les messages préfixés `[ifttt]`
4. Vérifiez l'historique de l'applet dans IFTTT

**Test avec curl :**
```bash
curl -X POST https://maker.ifttt.com/trigger/switchbot_winter/with/key/YOUR_KEY \
  -H "Content-Type: application/json" \
  -d '{"action":"test","timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}'
```

### L'applet IFTTT se déclenche mais la scène ne s'exécute pas

1. Vérifiez que la scène existe dans l'application SwitchBot
2. Vérifiez que le service SwitchBot est bien connecté dans IFTTT
3. Testez manuellement la scène dans l'application SwitchBot
4. Consultez les logs IFTTT pour les erreurs d'exécution

### Messages d'erreur courants

- **"Invalid webhook URL"** : l'URL doit commencer par `https://` (HTTP non autorisé)
- **"Webhook request timeout"** : IFTTT ne répond pas dans le délai imparti (10s par défaut)
- **"Aucun webhook ou scène configuré"** : configurez au moins un webhook ou une scène SwitchBot
- **"IFTTT webhook failed"** : erreur HTTP ou réseau, le système basculera automatiquement sur la scène

### Logs et monitoring

**Préfixes de logs à surveiller :**
- `[ifttt]` : actions liées aux webhooks IFTTT
- `[automation]` : logique d'automatisation et fallbacks
- `[health]` : état du système et endpoint de santé

**Commandes de recherche dans les logs :**
```bash
# Filtrer les logs IFTTT
grep "\[ifttt\]" /var/log/switchbot_dashboard.log

# Rechercher les fallbacks
grep "fallback" /var/log/switchbot_dashboard.log

# Surveiller les erreurs
grep -i "error\|failed" /var/log/switchbot_dashboard.log
```

## Gestion des erreurs et timeouts

### Types d'erreurs gérées

Le système gère automatiquement les erreurs suivantes avec fallback approprié :

- **Timeout HTTP** : Délai d'attente dépassé (10s par défaut)
- **Erreur HTTP 4xx/5xx** : Problèmes de connexion ou de serveur IFTTT
- **URL invalide** : Format incorrect ou protocole non-HTTPS
- **Réseau inaccessible** : Problèmes de connectivité

### Configuration des timeouts

Le timeout des webhooks IFTTT est configurable via le code source :

```python
# Dans switchbot_dashboard/ifttt.py
DEFAULT_TIMEOUT = 10  # secondes
```

**Recommandations** :
- **5-10s** : Pour la plupart des usages (défaut : 10s)
- **15-20s** : Si les applets IFTTT sont complexes avec des actions multiples
- **3-5s** : Pour une réactivité maximale (risque d'échecs plus fréquents)

### Logs détaillés pour le debugging

Le système génère des logs structurés avec préfixes pour faciliter le diagnostic :

```bash
# Succès du webhook
[ifttt] IFTTT webhook triggered successfully | status_code=200, url=https://maker.ifttt.com/trigger/...

# Échec avec fallback
[ifttt] IFTTT webhook failed | action_key=winter, error=timeout
[automation] Using SwitchBot scene (webhook unavailable) | action_key=winter, scene_id=scene-w

# Fallback ultime
[automation] Scene execution failed | action_key=off, scene_id=scene-off, error=invalid_scene
[automation] Falling back to direct command | action_key=off, device_id=aircon-1
```

### Stratégies de retry

**Webhooks IFTTT** : Pas de retry automatique (fallback immédiat vers scène)
- Raison : Les webhooks sont souvent des actions utilisateur immédiates
- Le retry créerait une latence inutile

**Scènes SwitchBot** : Retry via `SwitchBotClient` selon `SWITCHBOT_RETRY_*`
- Gère les erreurs 429 (rate limiting) et 5xx (serveur)
- Délai configurable via `SWITCHBOT_RETRY_DELAY_SECONDS`

### Patterns d'erreurs courants

#### 1. Timeout récurrent
**Cause** : Applet IFTTT trop complexe ou serveur IFTTT surchargé
**Solution** :
- Simplifier l'applet IFTTT
- Augmenter le timeout à 15-20s
- Utiliser directement les scènes SwitchBot

#### 2. HTTP 401/403
**Cause** : Clé webhook invalide ou expirée
**Solution** :
- Régénérer la clé dans IFTTT → Webhooks → Settings
- Mettre à jour l'URL dans le dashboard

#### 3. HTTP 429 depuis IFTTT
**Cause** : Trop de requêtes vers les webhooks IFTTT
**Solution** :
- Augmenter `poll_interval_seconds`
- Réduire les actions manuelles
- IFTTT a généralement des limites plus généreuses que SwitchBot

## Sécurité

⚠️ **Protection de votre clé webhook** :
- Ne partagez jamais votre clé webhook publiquement
- Stockez-la de manière sécurisée (variables d'environnement si possible)
- Si votre clé est compromise, régénérez-la dans IFTTT → Webhooks → Settings

🔒 **Validation HTTPS stricte** :
- Toutes les URLs doivent commencer par `https://`
- Les URLs `http://` sont automatiquement rejetées
- Validation via regex dans `ifttt.py:17-27`

🛡️ **Isolation des données** :
- Les payloads JSON ne contiennent jamais de secrets
- Les logs n'affichent jamais les clés webhook complètes
- Les erreurs sont tronquées pour éviter les fuites d'information

## Ressources

- [Documentation IFTTT Webhooks](https://ifttt.com/maker_webhooks)
- [Service SwitchBot sur IFTTT](https://ifttt.com/switchbot)
- [FAQ IFTTT locale](./IFTTT/faq.md)
- [Guide de configuration](./configuration.md)
- [Guide UI](./ui-guide.md)

---

*[Dernière mise à jour : 12 janvier 2026 - Système de fallback cascade et gestion des erreurs]*
