---
name: switchbot-api-dev
description: Guide pour ajouter de nouvelles commandes ou endpoints à l'API SwitchBot (v1.1) en respectant l'authentification HMAC et les quotas.
---

# Développement API SwitchBot

Utilisez ce skill lorsque vous devez ajouter de nouvelles méthodes dans `switchbot_api.py` ou déboguer des problèmes d'authentification.

## Authentification HMAC (Obligatoire)
L'API utilise un header `sign` généré via HMAC-SHA256.
Voir `SwitchBotClient._build_headers` dans `switchbot_dashboard/switchbot_api.py`.

```python
# Modèle de signature obligatoire
string_to_sign = f"{token}{t}{nonce}"
sign = base64.b64encode(
    hmac.new(secret_bytes, msg=string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
).decode("utf-8")
```

## Gestion des Quotas et Erreurs
Toute nouvelle méthode API doit :
1. Être enveloppée dans le mécanisme de retry (`_request`)
2. Mettre à jour le `quota_tracker` si les headers X-RateLimit sont présents
3. Lever `SwitchBotApiError` en cas d'échec avec logs structurés
4. Utiliser `current_app.logger` avec préfixe `[api]`

## Pattern d'injection et accès
Le client est injecté dans `create_app()` et accessible via :
```python
client = current_app.extensions["switchbot_client"]
```

## Ajouter une nouvelle commande
Pour ajouter une commande (ex: humidifier, aspirateur) :
1. Ajouter la méthode dans `SwitchBotClient`
2. Utiliser `self._request("POST", ...)` ou `self._request("GET", ...)`
3. Pour les commandes POST, le body JSON doit inclure `command`, `parameter`, et `commandType`

## Exemple de méthode conforme
```python
def control_device(self, device_id: str, action: str) -> Any:
    try:
        result = self._request(
            "POST", 
            f"/v1.1/devices/{device_id}/commands",
            json_body={"command": action, "parameter": "default", "commandType": "command"}
        )
        current_app.logger.info(f"[api] Device {device_id} controlled: {action}")
        return result
    except Exception as e:
        current_app.logger.error(f"[api] Device control failed: {e}")
        raise SwitchBotApiError(f"Control failed: {e}")
```

## Standards critiques
- **Typage strict** : `from __future__ import annotations`
- **Logs structurés** : Préfixes `[api]` obligatoires
- **Gestion quotas** : Intégration `quota_tracker` automatique
- **Tests** : Simulation 429 -> Alerte UI dans scénarios de test