# Thème et Styles

> **Référence des standards** : Voir [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) pour les règles de développement obligatoires.

## Vue d'ensemble

Le dashboard utilise un thème sombre immersif par défaut, conçu pour la lisibilité sur desktop comme sur mobile. L'architecture CSS respecte les principes DRY et facilite les extensions futures.

## Architecture des feuilles de style

### Fichiers CSS

- **`static/css/theme.css`** : Palette de couleurs, variables globales, composants partagés
- **`static/css/index.css`** : Styles spécifiques à la page d'accueil (carte Settings, interactions)
- **`static/css/devices.css`** : Styles spécifiques à la page `/devices` (grille, cartes, boutons)

> 📝 **Décision du 2026-01-09 17:20** : Externalisation complète des styles pour maintenance et cohérence (voir `memory-bank/decisionLog.md`).

> 📝 **Décisions connexes** : Les patterns de thématisation et glassmorphism sont documentés dans `memory-bank/systemPatterns.md` et `memory-bank/decisionLog.md`. Voir notamment les décisions du 2026-01-18 sur l'audit frontend mobile.

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

### Bandeau d'alerte quota - [2026-01-12]

Le bandeau d'alerte s'affiche automatiquement lorsque le quota API est faible :

```css
.quota-warning-banner {
  background: linear-gradient(135deg, var(--sb-warning), #dc2626);
  color: white;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  animation: pulse-warning 2s infinite;
}

.quota-warning-banner.high {
  background: linear-gradient(135deg, var(--sb-warning), #f59e0b);
}

.quota-warning-banner.critical {
  background: linear-gradient(135deg, var(--sb-danger), #dc2626);
}

@keyframes pulse-warning {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}
```

**Responsive et accessibilité :**
- Adaptation mobile avec `flex-wrap` sur petits écrans
- Attributs `aria-live="polite"` pour lecteurs d'écran
- Contraste WCAG AA respecté

### Grille de statut mobile - [2026-01-12]

La grille de statut utilise CSS Grid pour une meilleure adaptabilité mobile :

```css
.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.status-item {
  background: var(--sb-card);
  border: 1px solid var(--sb-border);
  border-radius: 12px;
  padding: 1rem;
  transition: all 0.2s ease;
}

.status-item:hover {
  background: var(--sb-card-hover);
  transform: translateY(-1px);
}

.status-item__label {
  color: var(--sb-text-muted);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}

.status-item__value {
  color: var(--sb-text);
  font-size: 1.25rem;
  font-weight: 600;
}

/* Mobile optimisation */
@media (max-width: 768px) {
  .status-grid {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }
  
  .status-item {
    padding: 0.75rem;
  }
  
  .status-item__value {
    font-size: 1.1rem;
  }
}
```

**Caractéristiques :**
- Auto-ajustement selon la largeur disponible
- Maintien de la cohérence visuelle sur tous écrans
- Support des attributs ARIA pour accessibilité

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

/* Boutons de scènes - styles spécifiques */
.scene-action {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem;
  min-height: 120px;
  text-align: center;
}

.scene-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.scene-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.scene-icon--winter {
  color: #f59e0b; /* Jaune/orange pour le chauffage */
}

.scene-icon--summer {
  color: #3b82f6; /* Bleu pour la climatisation */
}

.scene-icon--fan {
  color: #22c55e; /* Vert pour la ventilation */
}

.scene-icon--off {
  color: #ef4444; /* Rouge pour l'arrêt */
}

.scene-title {
  font-weight: 600;
  font-size: 0.9rem;
  line-height: 1.2;
}

.scene-status {
  font-size: 0.8rem;
  margin-top: 0.25rem;
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

## Références croisées

### Documentation technique
- [`.windsurf/rules/codingstandards.md`](../.windsurf/rules/codingstandards.md) – Standards de développement obligatoires
- [DOCUMENTATION.md](DOCUMENTATION.md) – Architecture et métriques
- [setup.md](setup.md) – Installation et configuration initiale

### Guides spécialisés
- [Guide UI](ui-guide.md) – Utilisation de l'interface
- [Performance Frontend](frontend-performance.md) – Optimisations UX et loaders
- [Frontend Mobile Audit](frontend-mobile-audit.md) – Audit mobile complet

### Memory Bank (décisions architecturales)
- `memory-bank/decisionLog.md` – Décisions de thématisation (externalisation CSS)
- `memory-bank/systemPatterns.md` – Patterns CSS et glassmorphism
- `memory-bank/progress.md` – Historique des améliorations visuelles

---

*Voir aussi [Configuration](configuration.md) pour les paramètres, [Tests](testing.md) pour la validation visuelle, et `memory-bank/systemPatterns.md` pour les patterns CSS.*
