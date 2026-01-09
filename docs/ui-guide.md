# Guide d'Utilisation et Interface

## Vue d'ensemble

Le dashboard propose une interface mobile-first avec thème sombre immersif, organisée autour de deux pages principales :

- **Page d'accueil (`/`)** : Contrôle de l'automatisation et des réglages
- **Page devices (`/devices`)** : Inventaire et configuration des équipements

## Page d'accueil (`/`)

### Carte Settings

Configuration complète orientée mobile avec :

- **Automatisation & mode** : interrupteur principal et menu `winter/summer`
- **Fenêtre horaire** : cases à cocher par jour + dropdowns 24 h
- **Profils Winter/Summer** : dropdowns bornés pour températures, mode AC, ventilation

> 📝 **Décision** : Cette approche mobile-first avec thème sombre a été implémentée le 2026-01-09 16:47 (voir `memory-bank/decisionLog.md`).

### Carte Current Status

Affiche en temps réel :

- Dernière lecture de température/humidité
- État supposé de la climatisation
- Dernière action et horodatage
- Messages d'erreur éventuels

### Actions rapides

Boutons pour contrôle manuel :

- `Run once` : Déclenche manuellement `AutomationService.run_once`
- `Chauffage (Hiver)` / `Clim (Été)` / `Off` : Change le mode et exécute immédiatement
- `Aircon ON (setAll)` / `Aircon OFF` : Commandes directes hors automatisation

> 📝 Chaque action met à jour `state.json` pour maintenir la cohérence UI.

## Page Devices (`/devices`)

### Inventory Snapshot

Carte de synthèse montrant :

- Compteur de devices physiques (`deviceList`)
- Compteur de télécommandes IR (`infraredRemoteList`)
- Confirmation de synchronisation du compte

### Cartes individuelles

Pour chaque device/remote :

- **Nom et type** avec icône appropriée
- **Badge Hub/Standalone** pour la topologie
- **Métadonnées** : firmware, statut cloud, batterie
- **Bouton "Copier l'ID"** avec retour visuel "Copié ✓"
- **Accordéon JSON** pour debug (payload brut)

> 💡 Le retour clipboard s'affiche 1,8 s puis revient à l'état normal. Décision du 2026-01-09 17:00 dans `memory-bank/decisionLog.md`.

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

---

*Voir aussi [Configuration](configuration.md) pour les paramètres, [Theming](theming.md) pour la personnalisation visuelle, et `memory-bank/decisionLog.md` pour les décisions UX.*
