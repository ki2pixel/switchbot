# Guide d'Utilisation et Interface

## Vue d'ensemble

Le tableau de bord propose une interface mobile-first avec thème sombre immersif, entièrement traduite en français. La navigation basse regroupe désormais six pages principales :

- **Page d'accueil (`/`)** : Statut temps réel et accès aux CTA principaux.
- **Page Réglages (`/reglages`)** : Configuration complète (fenêtres horaires, profils saisonniers, scènes, quotas…).
- **Page Actions (`/actions`)** : Les six actions manuelles (Hiver, Été, Ventilateur, Quick OFF, Exécuter une fois, Arrêt rapide) regroupées avec indicateurs d’état.
- **Page Quota (`/quota`)** : Suivi détaillé de la consommation de l’API SwitchBot.
- **Page Historique (`/history`)** : Dashboard Chart.js temps réel (température, humidité, état clim).
- **Page Appareils (`/devices`)** : Inventaire et configuration des équipements.

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
- **Valeur par défaut** : 250 requêtes (≈2,5 % de la limite quotidienne de **10 000** appels suivie par `ApiQuotaTracker`)
- **Réinitialisation** : Automatique à minuit UTC

### Bonnes pratiques

- Surveillez régulièrement la consommation d'API
- Augmentez le seuil d'alerte si nécessaire
- Évitez les actions manuelles répétitives qui consomment des crédits

## Page d'accueil (`/`) - [2026-01-12]

### En-tête

- **Titre** : "Tableau de bord SwitchBot"
- **Boutons d'accès rapide** :
  - **Réglages** : Accès aux paramètres complets
  - **Quota API** : Consommation et limites
  - **Appareils** : Gestion des équipements

### Bandeau d'alerte quota - [2026-01-12]

Un bandeau d'alerte s'affiche automatiquement en haut de la page d'accueil lorsque le quota API est faible :

- **Déclenchement** : Quand `api_requests_remaining` ≤ `api_quota_warning_threshold`
- **Affichage** : Bannière fixe avec couleur d'avertissement (jaune/rouge)
- **Contenu** : Nombre de requêtes restantes, lien vers la page quota
- **Styles** : Responsive avec thème sombre, contraste WCAG AA

### Vignette Quota API

Affiche en temps réel :

- **Requêtes restantes** : Nombre d'appels disponibles
- **Utilisation** : Barre de progression visuelle
- **Réinitialisation** : Compte à rebours avant minuit UTC

### Statut actuel - Grille mobile - [2026-01-12]

Refactorisé en grille CSS (`status-grid`) pour améliorer la scannabilité mobile :

- **Structure** : Grille responsive avec items (`status-item`)
- **Contenu** : Température/Humidité, État climatisation, Dernière action, Quota
- **Responsive** : Auto-ajustable pour écrans de différentes tailles
- **Accessibilité** : Attributs ARIA pour lecteurs d'écran

### Grille pour les cartes de statut
- Remplace la liste verticale par une grille CSS (`status-grid`)
- Meilleure lisibilité sur petits écrans
- Espacement et alignement cohérents

### Accès aux actions manuelles

- La page d’accueil affiche désormais un bouton CTA « Actions » menant à `/actions`. Les quatre boutons historiques ne sont plus présents directement sur l’accueil afin d’éviter l’overlay mobile.
- Les messages flash continuent d’informer du résultat d’une action (succès/fallback/erreur) et rappellent d’aller sur `/actions` si une configuration est manquante.
- Les états visuels (webhook/scène manquante) sont décrits dans la section dédiée ci-dessous.

## Page Actions (`/actions`) - [2026-01-18]

### Objectif

Regrouper les six actions manuelles dans une page dédiée, responsive, afin d’éviter la surcharge de la page d’accueil tout en offrant une vue claire sur l’état de configuration (webhooks/scènes).

- **Template** : `switchbot_dashboard/templates/actions.html`
- **Styles** : `switchbot_dashboard/static/css/actions.css` (glassmorphism, grille responsive 1→2 colonnes, badges de statut)
- **Route** : `routes.py::actions_page` (injection du contexte settings/state pour chaque action)

### Contenu de la page

| Carte | Action | Description | Bouton |
|-------|--------|-------------|--------|
| Chauffage Hiver | `actions.winter_on` | Envoie `winter_on` (webhook → scène → setAll) | `data-loader="card"` |
| Clim Été | `actions.summer_on` | Envoie `summer_on` | idem |
| Ventilation | `actions.fan_on` | Active le mode ventilation | idem |
| Quick OFF | `actions.quick_off` | Déclenche la scène `off` (fallback turnOff) | idem |
| Exécuter une fois | `actions.run_once` | Forcer un tick d’automatisation | `data-loader="card"` + texte explicatif |
| Arrêt express | `actions.stop_automation` | Coupe l’automatisation + OFF immédiat | bouton danger |

Chaque carte comporte :
- Une icône FontAwesome (configurée dans `_footer_nav.html` + `actions.html`)
- Un badge d’état (voir ci-dessous)
- Un bouton principal avec loader local (`data-loader="card"`) se connectant à `static/js/loaders.js`

### Badges et états visuels

| Badge | Condition | Signification |
|-------|-----------|---------------|
| `badge-success` « Webhook configuré » | URL HTTPS présente dans `ifttt_webhooks[action]` | L’action s’exécutera côté IFTTT sans consommer de quota |
| `badge-warning` « Scène uniquement » | Webhook manquant mais scène renseignée | L’action utilisera directement `SwitchBotClient.execute_scene` |
| `badge-danger` « Configuration manquante » | Aucune scène ni webhook | Bouton reste actif mais l’utilisateur est renvoyé vers `/reglages` |

Les badges se synchronisent avec `actions_context` construit dans `routes.py#771-799`, qui vérifie à la fois les webhooks et la présence d’UUID de scènes.

### Expérience utilisateur

- **Navigation** : accessible via l’onglet « Actions » de la bottom navigation.
- **Feedback** : chaque action déclenche les messages flash standards (succès, fallback scène, fallback commande directe).
- **Accessibilité** : cartes tactiles ≥56 px de haut, `aria-label` explicites, focus visible.
- **Performance** : la grille passe automatiquement de 1 colonne (≤480 px) à 2 colonnes (≥768 px) ; les ombres et blur suivent les tokens glassmorphism (`--sb-glass-*`).

## Améliorations Mobile (Janvier 2026)

### Bandeau d'alerte de quota
- Visible sur la page d'accueil quand `requêtes_restantes ≤ api_quota_warning_threshold`
- Utilise le même contexte que la page dédiée
- Design responsive adapté aux petits écrans

## Page Réglages (`/reglages`) - [2026-01-12]

### 1. Automatisation

- **Activer/désactiver** : Active ou désactive l'automatisation
- **Mode** : Bascule entre hiver et été
- **Intervalle** : Fréquence de vérification (15-3600 secondes)
- **Délai entre commandes** : Protection contre les déclenchements trop rapprochés
- **Fuseau horaire** : champ texte pour saisir un identifiant IANA (ex. `Europe/Paris`, `UTC`). En cas de valeur invalide, l'UI affiche une erreur et le backend retombe sur UTC pour continuer à appliquer les fenêtres horaires.

### 2. Fenêtres horaires - Feedback dynamique - [2026-01-12]

Définissez les plages d'activation avec feedback utilisateur en temps réel :

- **Jours** : Sélection multiple (lun-dim) avec compteur dynamique
- **Heure de début/fin** : Format 24h
- **Bouton +** : Ajoute une nouvelle plage
- **Feedback** : Compteur live des jours sélectionnés avec `aria-live`

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

### 4. Webhooks IFTTT - [2026-01-11]

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

### 6. Répétition OFF - [2026-01-11]

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
- Le nombre de requêtes restantes (sur **10 000** par jour par défaut — valeur ajustée automatiquement si SwitchBot expose un autre `limit`)
- Un indicateur visuel (vert/orange/rouge) selon le niveau de consommation
- Un bouton **« Voir le quota »** qui conduit à la page `/quota`

#### Bouton « Rafraîchir le quota »
- Disponible sur la page `/quota`, déclenche un POST `/quota/refresh` avec loader local.
- Force `ApiQuotaTracker` à normaliser l’instantané : remise à jour de la date (`api_quota_day`), de la limite et recalcul `remaining`.
- Affiche un flash `success` (“Quota mis à jour.”) quand l’opération se termine.
- Utiliser juste après avoir modifié manuellement `api_requests_limit` ou avant une journée de forte activité pour repartir d’un compteur propre.

**Bonnes pratiques :**
- Surveillez régulièrement le quota pour éviter les coupures.
- Ajustez `api_quota_warning_threshold` si vous souhaitez être alerté plus tôt (ex. 500).
- Réduisez les actions manuelles répétitives ou augmentez `poll_interval_seconds` lorsque le compteur passe sous ~200.

### Dépannage des scènes

Si une scène ne s'exécute pas correctement :
1. Vérifiez que les scènes sont bien créées dans l'application SwitchBot
2. Vérifiez que l'UUID est correctement copié (sans espaces avant/après)
3. Vérifiez les logs pour les erreurs d'authentification

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

## Gestion des appareils (`/devices`) - [2026-01-12]

### Vue d'ensemble

La page des appareils fournit une vue complète de votre écosystème SwitchBot avec une densité réduite pour mobile :

- **Appareils physiques** : Compteur et détails des appareils connectés
- **Télécommandes IR** : Gestion des appareils infrarouges contrôlés
- **État de synchronisation** : Dernière mise à jour et statut du compte

### Inventaire

- **Dernière mise à jour** : Horodatage de la dernière synchronisation
- **Appareils** : Nombre total d'appareils physiques détectés
- **Télécommandes** : Nombre de périphériques infrarouges configurés

### Fiche appareil - Détails pliables - [2026-01-12]

Chaque appareil est représenté par une carte interactive avec détails optimisés pour mobile :

#### En-tête (visible)
- **Icône** : Représentation visuelle du type d'appareil
- **Nom** : Identifiant personnalisable
- **Badge** : Type de connexion (Hub, Bluetooth, etc.)
- **ID** : Bouton de copie direct (toujours visible)

#### Détails techniques (plier/déplier)
- **Modèle** : Référence du matériel
- **Version** : Numéro de firmware
- **Batterie** : Niveau actuel (si applicable)
- **Statut** : Connecté/déconnecté
- **Dernière activité** : Horodatage de la dernière interaction

> 💡 **Optimisation mobile** : Les métadonnées secondaires sont dans des éléments `<details>` pliables pour réduire la densité visuelle tout en gardant l'accès aux informations détaillées.

### Workflow de configuration

1. Repérer le device Meter → Copier l'ID → `meter_device_id`
2. Repérer la remote Air Conditioner → Copier l'ID → `aircon_device_id`
3. Coller dans `config/settings.json`
4. Rafraîchir la page d'accueil pour validation

### Scripts externes - [2026-01-12]

Pour améliorer les performances et la maintenabilité, les scripts JS sont externalisés :

- **devices.js** : Gestion du clipboard et interactions des appareils
- **settings.js** : Feedback dynamique des formulaires
- **alerts.js** : Auto-fermeture des messages flash

> 💡 **Avantages** : Chargement plus rapide, meilleur cache navigateur, code maintenable.

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

## Améliorations d'accessibilité
- Labels ARIA pour les conteneurs de navigation
- Rôles pour les éléments interactifs
- Ratios de contraste améliorés (WCAG AA)

## Optimisation de la page Devices
- Métadonnées secondaires dans des sections `<details>` pliables
- Externalisation du JS clipboard vers `devices.js`
- Réduction de la densité visuelle

## Feedback dynamique
- Compteur live des jours sélectionnés dans les réglages
- Indicateurs visuels pour les contrôles actifs/inactifs
- Régions ARIA live pour les lecteurs d'écran

## Optimisations de performance
- Externalisation des JS (settings.js, devices.js)
- Réduction des ressources bloquant le rendu
- Sélecteurs CSS optimisés
