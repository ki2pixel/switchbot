# Guide d'Utilisation et Interface

## Vue d'ensemble

Le dashboard propose une interface mobile-first avec thème sombre immersif, organisée autour de deux pages principales :

- **Page d'accueil (`/`)** : Contrôle de l'automatisation et des réglages
- **Page devices (`/devices`)** : Inventaire et configuration des équipements

## Page d'accueil (`/`)

### En-tête avec quota API

- L'en-tête affiche le titre "SwitchBot Dashboard" et le bouton d'accès à la page "Devices".
- À droite, la vignette "Quota API quotidien" présente :
  - Le nombre de requêtes restantes sur le quota journalier (limite fixe : 10 000 par compte).
  - Le nombre de requêtes utilisées, avec la limite totale affichée.
  - L'état "N/A" tant qu'aucune requête n'a encore été effectuée depuis le dernier démarrage.
- Les valeurs sont recalculées après chaque appel API : si les headers `X-RateLimit-*` sont fournis, ils sont utilisés directement, sinon le compteur local journalier prend le relais (mise à jour par `AutomationService` lors de `poll_meter()` et de chaque commande envoyée).
- **Conseil d'exploitation** : lorsque le compteur restant descend sous 200, ralentir les actions manuelles et/ou augmenter `poll_interval_seconds` pour éviter de saturer la limite quotidienne — le bandeau sert d'alerte visuelle.
- Le badge est mis en évidence sur mobile (stacké sous le titre) pour garder l'information disponible même sur petits écrans.

### Carte Settings

Configuration complète orientée mobile avec :

- **Automatisation & mode** : interrupteur principal et menu `winter/summer`
- **Fenêtre horaire** : cases à cocher par jour + sélecteurs horaires 24h
- **Profils Winter/Summer** : paramètres de température, mode AC et ventilation
- **Scènes SwitchBot** : configuration des scènes favorites pour le contrôle rapide

> ℹ️ **Astuce** : Les scènes permettent de définir des configurations complexes directement dans l'application SwitchBot officielle, offrant plus de flexibilité que les paramètres basiques.

### Carte Current Status

Affiche en temps réel :

- Dernière lecture de température/humidité
- État supposé de la climatisation
- Dernière action et horodatage
- Messages d'erreur éventuels

### Contrôle manuel

#### Actions rapides

- **`Run once`** : Exécute immédiatement un cycle d'automatisation
- **`Quick off`** : Éteint le climatiseur en utilisant la scène OFF configurée (ou la commande `turnOff` en cas de scène non configurée)

#### Scènes SwitchBot

Les scènes permettent d'exécuter des configurations complexes prédéfinies dans l'application SwitchBot officielle :

- **`Aircon ON – Hiver`** : Active la scène d'hiver configurée (par exemple : chauffage à 20°C)
- **`Aircon ON – Été`** : Active la scène d'été configurée (par exemple : climatisation à 24°C)
- **`Aircon ON – Mode neutre`** : Active le mode ventilation (ventilateur sans chauffage/rafraîchissement)
- **`Aircon OFF`** : Éteint le climatiseur (utilisée par l'automatisation avec l'option *turn_off_outside_windows*)

#### Indicateurs visuels

- **Bouton vert** : Scène configurée et prête à l'emploi
- **Bouton rouge** : Scène non configurée (cliquer pour configurer)
- **Animation** : Scène en cours d'exécution
- **Icône ⚠️** : Avertissement de configuration manquante

> ℹ️ **Fonctionnement de l'automatisation** :
> - L'automatisation utilise d'abord les scènes configurées (`winter`/`summer`/`off`)
> - Si une scène n'est pas configurée, elle utilise les commandes `setAll`/`turnOff` (nécessite `aircon_device_id`)
> - Vérifiez les messages d'état pour les erreurs de configuration

### Configuration des scènes

1. **Créer des scènes** dans l'application SwitchBot :
   - Hiver : Configuration de chauffage
   - Été : Configuration de climatisation
   - Ventilation : Mode ventilateur uniquement
   - Arrêt : Éteindre le climatiseur

2. **Récupérer les UUID** :
   - Via l'API SwitchBot (`GET /v1.1/scenes`)
   - Ou depuis l'application mobile (Paramètres > Aide > À propos > Détails de l'API)

3. **Configurer les scènes** :
   - Cliquez sur un bouton rouge pour configurer
   - Collez l'UUID de la scène correspondante
   - Sauvegardez les paramètres

4. **Vérification** :
   - Les boutons passent au vert une fois configurés
   - Les scènes sont testables directement depuis l'interface

> 💡 **Bonnes pratiques** :
> - Configurez toujours la scène `off` pour un arrêt propre
> - Testez chaque scène après configuration
> - Consultez les logs en cas d'erreur avec `LOG_LEVEL=debug`
> - Les scènes offrent plus de fiabilité que les commandes IR individuelles

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

- **Flash messages** : Succès (vert), avertissements (orange), erreurs (rouge)
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
