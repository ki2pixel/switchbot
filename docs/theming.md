# Thème et Styles

## Vue d'ensemble

Le dashboard utilise un thème sombre immersif par défaut, conçu pour la lisibilité sur desktop comme sur mobile. L'architecture CSS respecte les principes DRY et facilite les extensions futures.

## Architecture des feuilles de style

### Fichiers CSS

- **`static/css/theme.css`** : Palette de couleurs, variables globales, composants partagés
- **`static/css/index.css`** : Styles spécifiques à la page d'accueil (carte Settings, interactions)
- **`static/css/devices.css`** : Styles spécifiques à la page `/devices` (grille, cartes, boutons)

> 📝 **Décision du 2026-01-09 17:20** : Externalisation complète des styles pour maintenance et cohérence (voir `memory-bank/decisionLog.md`).

### Variables CSS

La palette est centralisée dans `theme.css` :

```css
:root {
  /* Couleurs de fond */
  --sb-bg: #0a0a0a;
  --sb-card: #1a1a1a;
  --sb-card-hover: #252525;
  
  /* Texte */
  --sb-text: #e0e0e0;
  --sb-text-muted: #a0a0a0;
  --sb-text-dim: #666;
  
  /* Accents */
  --sb-accent: #3b82f6;
  --sb-accent-hover: #60a5fa;
  --sb-success: #22c55e;
  --sb-warning: #f59e0b;
  --sb-danger: #ef4444;
  
  /* Bordures et ombres */
  --sb-border: #333;
  --sb-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
  --sb-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
}
```

## Composants globaux

### Cartes (Cards)

```css
.card {
  background: var(--sb-card);
  border: 1px solid var(--sb-border);
  border-radius: 12px;
  box-shadow: var(--sb-shadow);
  transition: all 0.2s ease;
}

.card:hover {
  background: var(--sb-card-hover);
  box-shadow: var(--sb-shadow-lg);
}
```

### Boutons

```css
.btn {
  background: var(--sb-accent);
  color: white;
  border: none;
  border-radius: 20px;
  padding: 8px 16px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.btn:hover {
  background: var(--sb-accent-hover);
  transform: translateY(-1px);
}
```

### Formulaires

```css
.form-control {
  background: var(--sb-bg);
  border: 1px solid var(--sb-border);
  color: var(--sb-text);
  border-radius: 8px;
}

.form-control:focus {
  border-color: var(--sb-accent);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
```

## Spécificités par page

### Page d'accueil (`index.css`)

- **Carte Settings** : Layout mobile-first avec grille responsive
- **Contrôles temporels** : Chips pour les jours, dropdowns compactes
- **Profils saisonniers** : Groupement visuel des paramètres
- **Badge "mobile friendly"** : Indicateurs d'optimisation tactile

### Page Devices (`devices.css`)

- **Grille responsive** : 1 colonne mobile, 2+ colonnes desktop
- **Boutons "Copier l'ID"** : Retour visuel "Copié ✓" avec transition
- **Accordéons JSON** : `<details>` stylisés pour le debug
- **Badges Hub/Standalone** : Différenciation visuelle de la topologie

## Accessibilité et contrast

### Ratios de contraste

Les couleurs respectent WCAG AA (4.5:1 minimum) :

- Texte normal : `--sb-text` sur `--sb-card` = 7.8:1 ✅
- Texte secondaire : `--sb-text-muted` sur `--sb-card` = 5.2:1 ✅
- Boutons primaires : texte blanc sur `--sb-accent` = 4.7:1 ✅

### États focus

```css
.btn:focus,
.form-control:focus {
  outline: 2px solid var(--sb-accent);
  outline-offset: 2px;
}
```

## Personnalisation

### Ajouter une nouvelle couleur

1. Définir la variable dans `theme.css` :

```css
:root {
  --sb-info: #06b6d4;
  --sb-info-hover: #22d3ee;
}
```

2. Utiliser dans les feuilles spécifiques :

```css
.btn-info {
  background: var(--sb-info);
}
```

### Créer une variante de thème

Pour un thème clair futur :

```css
[data-theme="light"] {
  --sb-bg: #ffffff;
  --sb-card: #f8fafc;
  --sb-text: #1a1a1a;
  /* ... autres variables */
}
```

### Extensibilité

- **Nouveaux composants** : Ajouter dans `theme.css` si réutilisable
- **Styles spécifiques** : Ajouter dans la feuille de page concernée
- **Animations** : Utiliser `transition` cohérentes (0.2s ease)

## Bonnes pratiques

### Performance

- Variables CSS pour éviter les répétitions
- Transitions hardware-accelerated (`transform`, `opacity`)
- Minimum de sélecteurs imbriqués

### Maintenance

- Commenter les décisions non évidentes
- Regrouper les styles par fonction (layout, composants, utilitaires)
- Tester sur mobile et desktop après chaque modification

### Tests visuels

- Contraste WCAG sur tous les textes
- Rendu cohérent entre navigateurs
- Comportement tactile sur mobile
- États hover/focus clairs

---

*Voir aussi [Configuration](configuration.md) pour les paramètres, [Tests](testing.md) pour la validation visuelle, et `memory-bank/systemPatterns.md` pour les patterns CSS.*
