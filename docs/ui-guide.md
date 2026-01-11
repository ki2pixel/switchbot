# Guide d'Utilisation et Interface

## Vue d'ensemble

Le tableau de bord propose une interface mobile-first avec thème sombre immersif, entièrement traduite en français. L'interface est organisée autour de quatre pages principales :

- **Page d'accueil (`/`)** : Statut temps réel, actions rapides et scènes
- **Page Réglages (`/reglages`)** : Configuration complète (fenêtres horaires, profils saisonniers, scènes, quotas…)
- **Page Quota (`/quota`)** : Suivi de la consommation de l'API SwitchBot
- **Page Appareils (`/devices`)** : Inventaire et configuration des équipements

## Messages d'alerte et notifications

### Messages flash

Les messages flash informent l'utilisateur du résultat des actions :

- **Durée d'affichage** : 6 secondes avant disparition automatique
- **Types de messages** :
  - `success` (vert) : Action réussie
  - `danger` (rouge) : Erreur critique
  - `warning` (jaune) : Avertissement
  - `info` (bleu) : Information générale

### Accessibilité

- **Contraste** : Respect des normes WCAG AA pour une bonne lisibilité
- **Fermeture** : Bouton de fermeture clairement visible (×)
- **Focus** : Gestion du focus pour la navigation au clavier
- **ARIA** : Attributs ARIA pour les lecteurs d'écran
- **Thème sombre** : Adaptation des couleurs pour une lecture confortable

### Personnalisation

Les messages utilisent des variables CSS personnalisées pour une cohérence visuelle :

```css
:root {
  --alert-success-bg: #d4edda;
  --alert-success-text: #155724;
  --alert-danger-bg: #f8d7da;
  --alert-danger-text: #721c24;
  --alert-warning-bg: #fff3cd;
  --alert-warning-text: #856404;
  --alert-info-bg: #d1ecf1;
  --alert-info-text: #0c5460;
}

/* Thème sombre */
[data-bs-theme="dark"] {
  --alert-success-bg: rgba(25, 135, 84, 0.2);
  --alert-success-text: #75b798;
  /* ... autres couleurs ... */
}
```

## Alerte de quota API

Une bannière d'alerte s'affiche automatiquement lorsque le nombre de requêtes API restantes tombe en dessous du seuil configuré (250 par défaut).

### Comportement

- **Affichage** : Bannière fixe en haut de l'écran
- **Couleur** : Jaune (avertissement) ou rouge (critique)
- **Contenu** :
  - Nombre de requêtes restantes
  - Heure de réinitialisation (minuit UTC)
  - Bouton pour accéder à la page de quota

### Configuration

- **Seuil d'alerte** : Modifiable dans les paramètres avancés
- **Valeur par défaut** : 250 requêtes (10% de la limite quotidienne de 2500 appels)
- **Réinitialisation** : Automatique à minuit UTC

### Bonnes pratiques

- Surveillez régulièrement la consommation d'API
- Augmentez le seuil d'alerte si nécessaire
- Évitez les actions manuelles répétitives qui consomment des crédits

## Page d'accueil (`/`)

### En-tête

- **Titre** : "Tableau de bord SwitchBot"
- **Boutons d'accès rapide** :
  - **Réglages** : Accès aux paramètres complets
  - **Quota API** : Consommation et limites
  - **Appareils** : Gestion des équipements

### Vignette Quota API

Affiche en temps réel :

- **Requêtes restantes** : Nombre d'appels disponibles
- **Utilisation** : Barre de progression visuelle
- **Réinitialisation** : Compte à rebours avant minuit UTC

### Statut actuel

- **Température/Humidité** : Dernière lecture
- **Climatisation** : État supposé (ON/OFF)
- **Dernière action** : Commande exécutée
- **Erreurs** : Dernier message d'erreur

### Actions rapides

Les boutons du dashboard utilisent automatiquement les webhooks IFTTT avec système de fallback :

- **Bouton "Hiver"** → webhook winter → scène SwitchBot "Hiver" → commande `setAll` (fallback)
- **Bouton "Été"** → webhook summer → scène SwitchBot "Été" → commande `setAll` (fallback)
- **Bouton "Ventilateur"** → webhook fan → scène SwitchBot "Fan" → commande `setAll` (fallback)
- **Bouton "Quick OFF"** → webhook off → scène SwitchBot "Arrêt" → commande `turnOff` (fallback)

### Indicateurs visuels de configuration

Les boutons affichent des états visuels selon la configuration :

- **Bouton vert** : Webhook IFTTT configuré et valide
- **Bouton orange** : Webhook manquant mais scène SwitchBot configurée (fallback)
- **Bouton rouge** : Aucun webhook ni scène configuré
- **Icône ⚠️** : Avertissement de configuration manquante

> ℹ️ **Fonctionnement de l'automatisation** :
> - L'automatisation utilise d'abord les webhooks IFTTT (pas de consommation quota)
> - Si le webhook échoue ou est absent, elle bascule sur les scènes SwitchBot
> - En dernier recours, elle utilise les commandes `setAll`/`turnOff` (nécessite `aircon_device_id`)
> - Vérifiez les messages d'état pour les erreurs de configuration

## Page Réglages (`/reglages`)

### 1. Automatisation

- **Activer/désactiver** : Active ou désactive l'automatisation
- **Mode** : Bascule entre hiver et été
- **Intervalle** : Fréquence de vérification (15-3600 secondes)
- **Délai entre commandes** : Protection contre les déclenchements trop rapprochés

### 2. Fenêtres horaires

Définissez les plages d'activation :

- **Jours** : Sélection multiple (lun-dim)
- **Heure de début/fin** : Format 24h
- **Bouton +** : Ajoute une nouvelle plage

### 3. Profils saisonniers

#### Hiver
- Température minimale : 14-30°C
- Température maximale : 16-32°C
- Température cible : 18-28°C
- Mode : Auto/Froid/Sécheur/Ventilation/Chauffage
- Vitesse : Auto/Faible/Moyenne/Forte

#### Été
- Mêmes paramètres que l'hiver
- Configuration indépendante

### 4. Webhooks IFTTT

Configuration des webhooks IFTTT (priorité sur les scènes) :

1. **Hiver** : URL du webhook IFTTT pour le chauffage
2. **Été** : URL du webhook IFTTT pour la climatisation  
3. **Ventilation** : URL du webhook IFTTT pour la ventilation
4. **Arrêt** : URL du webhook IFTTT pour l'arrêt

> ⚠️ **Sécurité** : Les URLs doivent commencer par `https://` (HTTP non autorisé). Ne partagez jamais vos clés webhooks publiquement.

> 💡 **Avantages** : Les webhooks IFTTT ne consomment pas le quota API SwitchBot et permettent des applets complexes (notifications, logs, chaînes d'actions).

### 5. Scènes SwitchBot

Configuration des scènes (fallback si webhooks échouent) :

1. **Hiver** : UUID de la scène de chauffage
2. **Été** : UUID de la scène de climatisation
3. **Ventilation** : UUID de la scène de ventilation
4. **Arrêt** : UUID de la scène d'arrêt

> ℹ️ Les scènes doivent être créées au préalable dans l'application SwitchBot.

### 6. Répétition OFF

Configuration de la répétition des commandes OFF :

- **Nombre de répétitions** : 1-10 (défaut : 1)
- **Intervalle** : 1-600 secondes (défaut : 10)
- **Comportement** : La première commande est envoyée immédiatement, les suivantes sont planifiées

> 💡 **Usage typique** : `2 répétitions` avec `10 secondes` d'intervalle reproduit le comportement de l'application SwitchBot.

> 📊 **Monitoring** : L'état des répétitions en cours est visible dans `state.json` sous `pending_off_repeat`.

### 7. Paramètres avancés

- **Seuil d'alerte API** : Nombre de requêtes restantes avant alerte
- **Hystérésis** : Marge pour éviter les déclenchements intempestifs
- **ID des appareils** : Configuration manuelle si nécessaire

### Guide de configuration des scènes

### 1. Création des scènes

Dans l'application SwitchBot :

1. **Hiver** :
   - Température : 20°C
   - Mode : Chauffage
   - Vitesse : Moyenne

2. **Été** :
   - Température : 24°C
   - Mode : Froid
   - Vitesse : Auto

3. **Ventilation** :
   - Mode : Ventilateur
   - Vitesse : Faible

4. **Arrêt** :
   - Commande : Éteindre

### 2. Récupération des UUID

#### Méthode 1 : Application mobile
1. Allez dans **Paramètres**
2. Sélectionnez **Aide**
3. Appuyez sur **À propos**
4. Choisissez **Détails de l'API**
5. Notez les UUID des scènes

#### Méthode 2 : API SwitchBot

```bash
curl -X GET "https://api.switch-bot.com/v1.1/scenes" \
     -H "Authorization: VOTRE_TOKEN" \
     -H "Content-Type: application/json"
```

### 3. Configuration dans le tableau de bord

1. Allez dans **Réglages** > **Scènes SwitchBot**
2. Pour chaque scène :
   - Cliquez sur le champ correspondant
   - Collez l'UUID
   - Validez avec la touche Entrée
3. Sauvegardez les paramètres

### Vérification

- **Succès** : Le bouton devient vert
- **Erreur** : Message d'erreur explicite
- **Test** : Utilisez les boutons de la page d'accueil

## Gestion des erreurs

### Messages d'erreur courants

#### Scène non configurée
- **Cause** : L'UUID de la scène est manquant ou invalide
- **Solution** : Vérifiez la configuration dans **Réglages** > **Scènes**

#### Erreur API
- **Cause** : Problème de connexion avec SwitchBot
- **Solution** : Vérifiez votre connexion Internet et les identifiants API

#### Données obsolètes
- **Cause** : Pas de mise à jour récente
- **Solution** : Vérifiez l'intervalle de sondage et la connexion

### Journalisation

Les erreurs sont enregistrées dans :

- **Fichiers de log** : `logs/switchbot.log`
- **Niveaux** : DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Rotation** : 10 Mo max, 5 fichiers de sauvegarde

Pour le débogage, activez le mode verbose :

```bash
LOG_LEVEL=debug python app.py
```

## FAQ

### Comment ajouter un nouvel appareil ?

1. Allez dans **Appareils**
2. Notez l'ID de l'appareil
3. Ajoutez-le dans **Réglages** > **Paramètres avancés**

### Pourquoi ma scène ne s'exécute-t-elle pas ?

Vérifiez :
- Que l'UUID est correct
- Que l'appareil est en ligne
- Que le mode correspond à la saison

### Comment réduire la consommation d'API ?

- Augmentez l'intervalle de sondage
- Désactivez l'automatisation si non nécessaire
- Évitez les actions manuelles répétitives

## Support

Pour toute question, consultez :

- [Documentation SwitchBot](https://github.com/OpenWonderLabs/SwitchBotAPI)
- [Forum communautaire](https://community.switch-bot.com/)
- Support technique : support@example.com

---

*Dernière mise à jour : 10 janvier 2025*
- Bouton grisé : scène désactivée (configuration manquante ou erreur de chargement)
- Animation : scène en cours d'exécution

> 💡 **Conseil** : Pour une expérience optimale, configurez toujours la scène `off` pour assurer un arrêt propre du climatiseur.

#### Indicateurs visuels

- **Bouton vert** : Scène configurée et prête à l'emploi
- **Bouton rouge** : Scène non configurée (cliquer pour configurer)
- **Icône ⚠️** : Avertissement de configuration manquante

> ℹ️ **Fonctionnement de l'automatisation** :
> - L'automatisation utilise d'abord les scènes configurées (`winter`/`summer`/`off`)
> - Si une scène n'est pas configurée, elle utilise les commandes `setAll`/`turnOff` (nécessite `aircon_device_id`)
> - Vérifiez les messages d'état pour les erreurs de configuration

### Surveillance du quota API

La jauge de quota en haut à droite de l'interface affiche en temps réel :
- Le nombre de requêtes restantes (sur 2500 par jour par défaut)
- Un indicateur visuel (vert/orange/rouge) selon le niveau de consommation
- Un lien vers la page de configuration du quota

**Bonnes pratiques :**
- Surveillez régulièrement le quota pour éviter les coupures
- Augmentez le seuil d'alerte si nécessaire dans les paramètres
- Contactez le support SwitchBot pour augmenter votre quota si nécessaire

### Dépannage des scènes

Si une scène ne s'exécute pas correctement :
1. Vérifiez que l'UUID est correct dans les paramètres
2. Testez la scène directement depuis l'application SwitchBot
3. Vérifiez que le device est en ligne et accessible
4. Consultez les logs de l'application pour les erreurs (niveau `debug` si nécessaire)
5. Vérifiez que le quota API n'est pas épuisé

### Bonnes pratiques

- **Sécurité** : Ne partagez jamais vos tokens API ou UUID de scènes
- **Sauvegardes** : Exportez régulièrement vos configurations
- **Mises à jour** : Vérifiez les mises à jour de l'application pour les nouvelles fonctionnalités
- **Support** : En cas de problème, consultez les logs et préparez les informations de débogage avant de contacter le support

## Surveillance de l'état

### Carte Current Status

Affiche en temps réel :

- **Dernière lecture** : Température et humidité actuelles
- **État du climatiseur** : Allumé/éteint (basé sur `assumed_aircon_power`)
- **Dernière action** : Détail de la dernière commande envoyée
- **Quota API** : Nombre de requêtes restantes (limite quotidienne)
- **Messages d'état** : Erreurs ou avertissements importants

> ℹ️ **Note** : L'état affiché est une estimation basée sur la dernière commande envoyée. Pour une mise à jour en temps réel, utilisez le bouton "Run once".

## Gestion des appareils (`/devices`)

### Vue d'ensemble

La page des appareils fournit une vue complète de votre écosystème SwitchBot :

- **Appareils physiques** : Compteur et détails des appareils connectés
- **Télécommandes IR** : Gestion des appareils infrarouges contrôlés
- **État de synchronisation** : Dernière mise à jour et statut du compte

### Inventaire

- **Dernière mise à jour** : Horodatage de la dernière synchronisation
- **Appareils** : Nombre total d'appareils physiques détectés
- **Télécommandes** : Nombre de périphériques infrarouges configurés

### Fiche appareil

Chaque appareil est représenté par une carte interactive :

#### En-tête
- **Icône** : Représentation visuelle du type d'appareil
- **Nom** : Identifiant personnalisable
- **Badge** : Type de connexion (Hub, Bluetooth, etc.)

#### Détails techniques
- **Modèle** : Référence du matériel
- **Version** : Numéro de firmware
- **Batterie** : Niveau actuel (si applicable)
- **Statut** : Connecté/déconnecté
- **Dernière activité** : Horodatage de la dernière interaction

#### Actions
- **Copier l'ID** : Copie l'identifiant unique de l'appareil
- **Voir les détails** : Affiche les métadonnées techniques complètes
- **Rafraîchir** : Met à jour les informations de l'appareil

> 💡 **Astuce** : Maintenez la touche `Maj` enfoncée lors du clic sur "Copier l'ID" pour ouvrir un menu contextuel avec plus d'options.

### Workflow de configuration

1. Repérer le device Meter → Copier l'ID → `meter_device_id`
2. Repérer la remote Air Conditioner → Copier l'ID → `aircon_device_id`
3. Coller dans `config/settings.json`
4. Rafraîchir la page d'accueil pour validation

## Interactions et accessibilité

### Contrôles tactiles

- **Switchs** : Interrupteurs pour automatisation/mode
- **Dropdowns** : Sélection guidée sans saisie libre
- **Boutons pill** : Actions primaires avec coins arrondis
- **Cards** : Zones tactibles avec ombres portées

### Labels et attributs ARIA

- Boutons critiques avec `aria-label` explicites
- Messages flash avec rôles appropriés
- Navigation au clavier fonctionnelle

### Messages utilisateur

Le tableau de bord utilise des messages flash pour informer l'utilisateur du résultat des actions. Ces messages s'affichent en haut de la page et se ferment automatiquement après 6 secondes.

**Messages spécifiques aux webhooks IFTTT :**
- **Success** : "Webhook IFTTT déclenché avec succès"
- **Warning** : "Webhook IFTTT échoué, utilisation de la scène SwitchBot"
- **Info** : "Action exécutée via commande directe (fallback ultime)"

> **Note technique** : L'auto-fermeture des messages est gérée par le script `static/js/alerts.js` qui ajoute une animation de fondu et supprime le message du DOM après un délai de 600ms, pour éviter d'encombrer l'interface tout en laissant le temps de lire le message.

- **Badges d'état** : Information contextuelle sur les devices
- **Retours clipboard** : Confirmation visuelle temporaire

## Responsive design

### Mobile (< 768px)

- Cartes pleine largeur
- Contrôles tactiles espacés
- Typography adaptée
- Scrolling vertical optimisé

### Desktop (> 768px)

- Grille multi-colonnes
- Hover states sur boutons
- Espacements optimisés pour souris
- Fenêtres modales si nécessaire

## Raccourcis clavier

- `Tab` : Navigation entre éléments interactifs
- `Enter/Space` : Validation des boutons/switchs
- `Escape` : Fermeture des modales (si présentes)
- `F5` : Rafraîchir la page (met à jour l'état des appareils)
- `Ctrl+Enter` : Soumettre le formulaire actif

## Dépannage courant

### Scènes non détectées
1. Vérifiez que les scènes sont bien créées dans l'application SwitchBot
2. Vérifiez que l'UUID est correctement copié (sans espaces avant/après)
3. Vérifiez les logs pour les erreurs d'authentification

### Problèmes d'automatisation
1. Vérifiez que `automation_enabled` est activé
2. Vérifiez que les plages horaires sont correctement configurées
3. Vérifiez les seuils de température dans les profils hiver/été

### Problèmes de connexion
1. Vérifiez que le token API est valide
2. Vérifiez que les appareils sont en ligne dans l'application SwitchBot
3. Vérifiez les logs pour les erreurs de connexion

---

*Voir aussi [Configuration](configuration.md) pour les paramètres, [Theming](theming.md) pour la personnalisation visuelle, et `memory-bank/decisionLog.md` pour les décisions UX.*
