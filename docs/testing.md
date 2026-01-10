# Tests et Validation

## Vue d'ensemble

Ce guide décrit les tests manuels recommandés pour valider le bon fonctionnement du SwitchBot Dashboard. Les tests couvrent l'installation, la configuration, l'interface utilisateur et les scénarios d'erreur.

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

## Tests de l'interface utilisateur

### 1. Page d'accueil responsive

**Desktop (> 768px)** :
- Cartes en grille multi-colonnes
- Hover states fonctionnels
- Espacements optimaux pour souris

**Mobile (< 768px)** :
- Cartes pleine largeur
- Contrôles tactiles espacés
- Scrolling vertical fluide

**Validation** :
- Ouvrir devtools, tester différentes tailles d'écran
- Vérifier que tous les éléments restent cliquables

### 2. Formulaire Settings

**Fonctionnalités** :
- Switchs automatisation/mode
- Dropdowns temporels (jours/heures)
- Profils saisonniers bornés

**Validation** :
- Changer chaque paramètre individuellement
- Vérifier la sauvegarde dans `settings.json`
- Tester les valeurs limites (min/max)

### 3. Actions rapides

**Boutons à tester** :
- `Run once` : Vérifier exécution et mise à jour `state.json`
- `Chauffage/Clim/Off` : Changement de mode et commande immédiate
- `Aircon ON/OFF` : Commandes directes

**Validation** :
- Cliquer chaque bouton
- Vérifier `state.json` mis à jour
- Confirmer comportement attendu

## Tests page `/devices`

### 1. Inventaire et copie d'ID

**Workflow** :
1. Ouvrir `/devices`
2. Vérifier compteur devices/remotes
3. Cliquer "Copier l'ID" sur un device Meter
4. Coller dans un éditeur pour validation
5. Répéter pour une remote Air Conditioner

**Attendu** :
- Retour visuel "Copié ✓" pendant 1,8 s
- ID valide dans le presse-papiers
- Pas d'erreur console

### 2. Accordion JSON

**Test** :
- Cliquer "Afficher le JSON brut deviceList"
- Vérifier que le payload s'affiche
- Refermer et vérifier la fermeture

### 3. Mobile responsiveness

**Validation** :
- Tester sur mobile réel ou devtools mobile
- Vérifier que les cartes restent lisibles
- Confirmer que les boutons sont accessibles

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

## Tests d'erreur et résilience

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
