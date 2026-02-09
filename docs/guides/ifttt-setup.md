# Guide IFTTT pour SwitchBot Dashboard v2

**TL;DR**: Configurez IFTTT pour déclencher vos scènes SwitchBot via webhooks et bénéficiez d'une cascade de fallback automatique (IFTTT → scène → commande directe) avec une économie de quota API et une fiabilité maximale.

## Le Problème : Pourquoi IFTTT ?

Vous utilisez l'API SwitchBot directement et vous faites face à plusieurs frustrations :

- **Quota limité** : 10 000 requêtes par jour qui s'épuisent vite
- **Bugs d'API** : l'exécution des scènes via `/scenes/{id}/execute` est souvent instable
- **Manque de flexibilité** : impossible d'ajouter des notifications ou des logs complexes
- **Point unique de défaillance** : si l'API SwitchBot est indisponible, tout s'arrête

J'ai rencontré ces problèmes lors de l'automatisation hivernale 2026. Après plusieurs échecs de scènes qui ne se déclenchaient pas, j'ai implémenté une solution de cascade qui résout tous ces problèmes.

## La Solution : Architecture de Cascade à 3 Niveaux

Le système implémente une **cascade de fallback** intelligente :

```
IFTTT Webhook (priorité) → Scène SwitchBot (fallback 1) → Commande directe (fallback 2)
```

### Pourquoi cette architecture fonctionne

- **Économie** : Les webhooks IFTTT ne consomment pas votre quota SwitchBot
- **Résilience** : Si un niveau échoue, le suivant prend automatiquement le relais
- **Flexibilité** : Créez des applets IFTTT complexes (notifications, multi-actions)
- **Traçabilité** : Chaque niveau génère des logs structurés pour le debugging

### L'analogie du restaurant

Pensez à cette cascade comme commander au restaurant :
1. **IFTTT** = Le serveur prioritaire (rapide, gratuit, ne vous coûte rien)
2. **Scène** = Le chef directement (un peu plus lent, mais fiable)
3. **Commande** = La cuisine en mode dégradé (dernier recours, limité)

## L'Implémentation : Configuration Complète

### Étape 1 : Préparer IFTTT

1. Créez un compte gratuit sur [ifttt.com](https://ifttt.com)
2. Connectez le service **SwitchBot** dans IFTTT
3. Créez vos scènes dans l'application SwitchBot mobile

### Étape 2 : Créer les Applets

Pour chaque action (winter, summer, fan, off) :

#### Applet "Hiver" - Configuration complète

**Trigger** : Webhooks → "Receive a web request"
- Event Name : `switchbot_winter`

**Action** : SwitchBot → "Execute scene"
- Sélectionnez votre scène "Hiver 21°C"

#### Récupérer l'URL du webhook

Allez dans IFTTT → Services → Webhooks → Documentation. Votre URL ressemble à :
```
https://maker.ifttt.com/trigger/switchbot_winter/with/key/VOTRE_CLÉ
```

### Étape 3 : Configurer le Dashboard

Accédez à **Réglages** (`/reglages`) et configurez les URLs :

```json
{
  "ifttt_webhooks": {
    "winter": "https://maker.ifttt.com/trigger/switchbot_winter/with/key/VOTRE_CLÉ",
    "summer": "https://maker.ifttt.com/trigger/switchbot_summer/with/key/VOTRE_CLÉ",
    "fan": "https://maker.ifttt.com/trigger/switchbot_fan/with/key/VOTRE_CLÉ",
    "off": "https://maker.ifttt.com/trigger/switchbot_off/with/key/VOTRE_CLÉ"
  }
}
```

### Configuration fallback optionnelle

```json
{
  "aircon_scenes": {
    "winter": "scene-winter-id",
    "summer": "scene-summer-id", 
    "fan": "scene-fan-id",
    "off": "scene-off-id"
  },
  "aircon_device_id": "votre-device-id-ir"
}
```

## Les Pièges : Ce que j'ai appris

### ❌ Ne pas configurer de fallback

J'ai fait cette erreur au début. Si IFTTT est down, tout s'arrête.

```json
// MAUVAIS : Uniquement IFTTT
{
  "ifttt_webhooks": {
    "winter": "https://maker.ifttt.com/trigger/winter/with/key/abc"
  }
  // Pas de scenes, pas de device_id
}
```

### ✅ Configurer la cascade complète

```json
// BON : Cascade complète
{
  "ifttt_webhooks": { ... },
  "aircon_scenes": { ... },
  "aircon_device_id": "device-123"
}
```

### ❌ URLs HTTP non sécurisées

Le système rejette automatiquement les URLs `http://` pour des raisons de sécurité.

### ✅ Toujours utiliser HTTPS

```bash
# Test de validation
curl -X POST https://maker.ifttt.com/trigger/test/with/key/YOUR_KEY \
  -H "Content-Type: application/json" \
  -d '{"action":"test","timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}'
```

### ❌ Ignorer les logs de fallback

Les logs sont votre meilleur ami pour diagnostiquer les problèmes :

```bash
# Webhook réussi
[ifttt] IFTTT webhook triggered successfully | status_code=200

# Fallback automatique
[automation] IFTTT webhook failed | action_key=winter, error=timeout
[automation] Using SwitchBot scene (webhook unavailable) | action_key=winter
```

## Patterns de Payload JSON

Les webhooks IFTTT peuvent recevoir des données structurées :

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

Ces données enrichissent vos applets IFTTT pour des notifications personnalisées.

## Guide de Dépannage Rapide

### Le webhook ne se déclenche pas

1. **Vérifiez l'URL** : doit commencer par `https://`
2. **Testez avec curl** : voir commande ci-dessus
3. **Consultez les logs** : `grep "\[ifttt\]" /var/log/switchbot_dashboard.log`

### L'applet se déclenche mais la scène ne s'exécute pas

1. **Vérifiez la connexion SwitchBot** dans IFTTT
2. **Testez la scène manuellement** dans l'application SwitchBot
3. **Consultez l'historique** de l'applet dans IFTTT

### Messages d'erreur courants

- `"Invalid webhook URL"` : URL doit être HTTPS
- `"Webhook request timeout"` : IFTTT ne répond pas (10s max)
- `"IFTTT webhook failed"` : Le système basculera automatiquement sur la scène

## Sécurité et Bonnes Pratiques

🔒 **Protégez votre clé webhook** :
- Ne la partagez jamais publiquement
- Stockez-la dans `.env` si possible
- Régénérez-la si compromise

🛡️ **Validation HTTPS stricte** :
- Toutes les URLs sont validées via regex
- HTTP est automatiquement rejeté
- Logs tronqués pour éviter les fuites

📊 **Monitoring** :
- Surveillez `[ifttt]` et `[automation]` dans les logs
- Utilisez `grep "fallback"` pour identifier les basculements
- Configurez des alertes sur les erreurs répétées

### Tableau Comparatif des Approches d'Action

| Approche | Coût quota | Fiabilité | Complexité | Cas d'usage idéal |
|----------|------------|-----------|------------|-------------------|
| **IFTTT webhooks** | Aucun | Élevée | Moyenne | Production, notifications |
| **Scènes SwitchBot** | Moyen | Élevée | Faible | Configurations natives |
| **Commandes directes** | Élevé | Moyenne | Faible | Testing, fallback |

## La Règle d'Or : Webhook d'abord, Fallback Ensuite

Configurez toujours IFTTT en premier, puis ajoutez les fallbacks. Les webhooks sont gratuits et rapides ; les fallbacks assurent la résilience.

---

*[Guide basé sur l'expérience réelle d'automatisation hivernale 2026 et les patterns documentés dans memory-bank/]*
