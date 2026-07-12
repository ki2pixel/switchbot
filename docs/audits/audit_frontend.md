# Audit Frontend Complet - SwitchBot Dashboard

**Date :** 2026-07-12
**Portée :** Templates Jinja, CSS, JavaScript, assets vendor, accessibilité, performance, architecture SPA
**Méthode :** Analyse statique du code source (9 templates, 10 fichiers JS, 9 fichiers CSS, assets vendor)

---

## 1. Vue d'ensemble de l'architecture

### Stack frontend
- **Templates :** Jinja2 (9 pages : `index`, `settings`, `actions`, `history`, `devices`, `quota`, `login`, `503`, `_footer_nav`)
- **CSS :** Bootstrap 5 local + thème custom (`theme.css` 24 Ko) + CSS critique inline + 7 feuilles page-specific
- **JS :** Vanilla JS (pas de framework), SPA router custom, Chart.js pour l'historique
- **Assets :** 100% offline-first (aucun CDN), fonts Space Grotesk locales, Font Awesome local
- **Icônes :** Font Awesome + SVG inline pour les scènes

### Inventaire des assets

| Fichier | Taille | Rôle |
|---|---|---|
| `vendor/css/bootstrap.min.css` | 228 Ko | Framework CSS |
| `vendor/js/chart.umd.min.js` | 204 Ko | Graphiques historique |
| `vendor/fontawesome/css/all.min.css` | 104 Ko | Icônes |
| `vendor/fontawesome/webfonts/fa-solid-900.ttf` | 412 Ko | Icônes (format TTF) |
| `vendor/fontawesome/webfonts/fa-solid-900.woff2` | 156 Ko | Icônes (format WOFF2) |
| `vendor/fontawesome/webfonts/fa-brands-400.ttf` | 204 Ko | Icônes brands (non utilisées) |
| `vendor/fonts/SpaceGrotesk-*.ttf` | 3 x 68 Ko = 204 Ko | Police texte |
| `vendor/js/chartjs-adapter-date-fns.bundle.min.js` | 52 Ko | Adaptateur date Chart.js |
| `css/theme.css` | 24 Ko | Thème global |
| `js/history.js` | 28 Ko | Dashboard historique |
| `js/loaders.js` | 16 Ko | Loaders + interceptors CSRF |
| `js/spa-router.js` | 12 Ko | Routeur SPA |

**Poids total brut des assets vendor :** ~1,7 Mo (avant gzip)
**Poids des assets custom (CSS+JS) :** ~80 Ko

---

## 2. Constats par priorite

### P1 - Critique

#### P1.1 - Routeur SPA : desynchronisation CSS et double navigation
**Fichiers :** `./switchbot_dashboard/static/js/spa-router.js:80-152`, `./switchbot_dashboard/templates/_footer_nav.html`

Le routeur SPA intercepte les clics sur les liens `data-loader`, fetch la page HTML, extrait `#app-content` et l'injecte. Trois problemes majeurs :

1. **CSS non synchronise correctement.** Le routeur detecte les feuilles page-specific via le pattern `/\/static\/css\/(index|settings|actions|history|devices)\.css/` mais ne retire que celles qui matchent ce pattern. Les feuilles `theme.css`, `sticky-footer.css`, `sticky-cards.css` et `bootstrap.min.css` sont dupliquees car elles portent le meme `href` sur chaque page et le routeur les reinjecte sans verifier les doublons de preload links (`link[rel="preload"][as="style"]`).

2. **Double navigation footer.** `_footer_nav.html` est inclus dans chaque page via `{% include %}`, donc le HTML remplace contient deja un `#footer-bar`. Apres injection, le DOM a temporairement deux footer-bar (l'ancien hors `#app-content` + le nouveau injecte). Le routeur ne nettoie que `#app-content`, pas le footer qui est en dehors.

3. **Re-execution des scripts globaux.** `executePageScripts()` filtre les scripts via `globalScripts` (loaders, alerts, bottom-nav, performance-optimizer, advanced-optimizer, spa-router), mais ce filtre se fait par `src.endsWith()`. Si un script a un query string (`?v=123`), le filtre echoue et le script est re-execute. Les interceptors CSRF dans `loaders.js` seraient alors re-installes en chaine, each fetch interception s'ajoutant en couche.

#### P1.2 - CTA collant chevauche la navigation mobile
**Fichiers :** `./switchbot_dashboard/static/css/index.css:159-176`, `./switchbot_dashboard/static/css/critical.css:236-247`

Le `.scene-actions-wrapper` en `position: sticky; bottom: calc(75px + env(safe-area-inset-bottom) * 1.1)` sur mobile, avec `margin: 1rem 0`. Le `#footer-bar` est en `position: fixed; bottom: 0; height: 62px+`. Sur un ecran 375px :
- Le CTA sticky se positionne a ~75px du bas
- Le footer fait ~62px de haut
- Resultat : le CTA est a 13px au-dessus du footer, mais son contenu (padding 1rem + bouton 56px) depasse et chevauche le footer

De plus, `margin: 1rem -1rem -1rem` dans la version inline critique cree un debordement horizontal de 16px de chaque cote.

#### P1.3 - Font Awesome : formats TTF et WOFF2 charges en double
**Fichiers :** `./switchbot_dashboard/static/vendor/fontawesome/css/all.min.css`

Font Awesome 6 declare ses fontes en `@font-face` avec `src: url(...woff2) format('woff2'), url(...ttf) format('truetype')`. Le navigateur telecharge normalement seulement le WOFF2 (premier format supporte). Cependant, le fichier TTF de 412 Ko est presente sur le disque et reste reference. Le vrai probleme est que **fa-brands-400** (204 Ko TTF + 116 Ko WOFF2 = 320 Ko) est charge mais **aucune icone brand n'est utilisee** dans tout le projet. L'audit n'a trouve que des icones `fa-solid` (home, cog, bolt, chart-pie, chart-line, microchip, lock, sync-alt, etc.).

### P2 - Important

#### P2.1 - Loader non annonce aux lecteurs d'ecran
**Fichier :** `./switchbot_dashboard/static/js/loaders.js:93-96`

L'overlay local a `aria-hidden="true"` fixe des la creation. Quand `showLoader()` active l'overlay, il change `aria-hidden` en `"false"` dans le `requestAnimationFrame`, mais le spinner a `role="status"` et un `sr-only` texte - le tout a l'interieur d'un parent qui etait `aria-hidden` au moment du rendu initial. Les lecteurs d'ecran peuvent ne pas annoncer le changement d'etat `aria-hidden` dynamique de maniere fiable.

Le loader global (`ensureGlobalLoader`) a le meme probleme : `aria-hidden="true"` a la creation, change en `"false"` par `showGlobalLoader()`, mais le `role="status"` du spinner n'est pas dans un `aria-live` region.

#### P2.2 - Optimiseurs de performance fantomes
**Fichiers :** `./switchbot_dashboard/static/js/performance-optimizer.js`, `./switchbot_dashboard/static/js/advanced-optimizer.js`

Ces deux fichiers ont ete simplifies a des no-ops (30 et 29 lignes respectivement). Ils ne font que `console.log('Simplified ...')` et ne contiennent plus ni `requestAnimationFrame`, ni observers, ni worker. **Cependant, ils sont toujours charges sur `index.html` et `settings.html`**, ajoutant 2 requetes HTTP et 2 executions de script pour un `console.log` de debug. Le `perf-worker.js` (99 lignes, web worker complet) n'est reference dans aucun template.

#### P2.3 - XSS potentiel via innerHTML dans history.js
**Fichier :** `./switchbot_dashboard/static/js/history.js:519`

```javascript
tdState.innerHTML = airconStateHTML;
```

`formatAirconState()` retourne du HTML statique (badges Bootstrap) depuis un `stateMap` hardcoded. Les valeurs proviennent de l'API `/history/api/latest`, mais le `state` est compare a des cles fixes (`'on'`, `'off'`, `'unknown'`). **Le risque est faible** car aucune donnee utilisateur n'est interpolated directement. Cependant, `showMockDataWarning()` (ligne 324) et `renderChartErrorState()` (ligne 361) utilisent aussi `innerHTML` avec des templates string - ces derniers sont statiques et sans donnees dynamiques.

#### P2.4 - bottom-nav.js cible une classe inexistante
**Fichier :** `./switchbot_dashboard/static/js/bottom-nav.js:6`

```javascript
this.nav = document.querySelector('.sb-bottom-nav');
```

Le footer reel utilise `#footer-bar` avec la classe `footer-bar-1` (voir `./switchbot_dashboard/templates/_footer_nav.html:2`). La classe `.sb-bottom-nav` n'existe dans aucun template. Le JS initialise donc un `BottomNavigation` avec `this.nav = null`, et le `if (this.nav)` court-circuite tout le comportement (scroll hide/show, active state, ripple). **Le fichier est 100% mort.**

#### P2.5 - `sr-only` classe non definie
**Fichiers :** `./switchbot_dashboard/static/js/loaders.js:106`, `./switchbot_dashboard/templates/history.html:132,148,168`

La classe `sr-only` est utilisee dans les loaders (texte pour lecteurs d'ecran) et dans history.html (descriptions de graphiques, caption de table). **Aucune regle CSS `.sr-only` n'existe** dans `theme.css`, `critical.css`, ou les CSS page-specific. Bootstrap 5 inclut normalement cette classe, mais elle est dans `bootstrap.min.css` qui est charge en asynchrone (preload) sur `index.html`. Sur les autres pages (`settings.html`, `actions.html`, etc.) elle est chargee en bloquant, donc presente. Le risque est que sur `index.html`, le texte `sr-only` soit visible brievement avant que Bootstrap ne se charge.

#### P2.6 - Font "Roboto" referencee mais absente
**Fichier :** `./switchbot_dashboard/static/css/sticky-footer.css:83`

```css
font-family: "Roboto", sans-serif !important;
```

Applique au `.nav-text` du footer avec `!important`. La police Roboto n'est ni telechargee, ni presente dans `./switchbot_dashboard/static/vendor/fonts/`. Le navigateur fallback sur `sans-serif` system. Cette regle `!important` force un font-family different du reste de l'app (Space Grotesk) pour le texte de navigation, creant une inconsistency visuelle.

### P3 - Mineur

#### P3.1 - Duplication massive CSS entre critical.css et inline
**Fichiers :** `./switchbot_dashboard/static/css/critical.css` (418 lignes), `./switchbot_dashboard/templates/index.html:20-438` (418 lignes inline)

Le contenu de `critical.css` est **identique** au `<style>` inline dans `index.html`. Les deux definissent les memes variables, les memes regles, les memes media queries. `critical.css` n'est reference dans aucun template (pas de `<link>` vers lui). C'est un fichier mort de 8 Ko qui se desynchronisera inevitablement.

#### P3.2 - Hiérarchie de titres incorrecte
**Fichiers :** `./switchbot_dashboard/templates/actions.html`, `./switchbot_dashboard/templates/history.html`, `./switchbot_dashboard/templates/devices.html`

- `actions.html` : `h1` (ligne 21) puis `h2` (ligne 50) - correct
- `history.html` : `h1` (ligne 21) puis `h2` (ligne 123, 143, 160) - correct
- `devices.html` : `h1` (ligne 19) puis `h2` (ligne 34, 49, 136) puis `h3` (ligne 62, 149) - correct
- `settings.html` : `h1` (ligne 21) puis `h2` (ligne 49) - correct, mais les sous-sections "Profil hiver" et "Profil ete" utilisent `h2` (ligne 348, 403) au lieu de `h3`, rompant la hierarchie

#### P3.3 - Landmarks HTML manquants sur certaines pages
**Fichiers :** `./switchbot_dashboard/templates/login.html`, `./switchbot_dashboard/templates/503.html`

`login.html` et `503.html` n'ont pas de balise `<main>`. Le contenu est directement dans `<body> > <div>`. Les autres pages ont correctement `<main class="sb-page__content">`.

#### P3.4 - Incoherence du comportement footer desktop vs mobile
**Fichiers :** `./switchbot_dashboard/static/css/critical.css:418-426`, `./switchbot_dashboard/static/css/sticky-footer.css:12-35`, `./switchbot_dashboard/static/css/theme.css:695-703`

Trois sources contradictoires :
- `critical.css` inline : `#footer-bar { display: none }` sur `min-width: 769px`
- `sticky-footer.css` : `#footer-bar { display: flex !important }` sur `min-width: 769px`
- `theme.css` : `.sb-bottom-nav { display: none }` sur `min-width: 769px` (mais cette classe n'est pas utilisee)

`sticky-footer.css` gagne grace au `!important`. Le footer est donc visible sur desktop, ce qui est probablement l'intention, mais la regle inline dans `critical.css` est morte et source de confusion.

#### P3.5 - Pas de `prefers-color-scheme: light`
**Fichiers :** `./switchbot_dashboard/static/css/theme.css`, `./switchbot_dashboard/templates/index.html:12-16`

Le script de boot force `root.dataset.theme = 'dark'` inconditionnellement. Le `prefersDark` est detecte mais seulement pour `color-scheme`. Il n'y a pas de theme clair implemente. Le `503.html` utilise `class="sb-bg"` (sans `sb-dark`) qui n'est pas defini, le corps de la page n'aura pas le gradient dark.

#### P3.6 - Requetes API history sans gestion de timeout
**Fichier :** `./switchbot_dashboard/static/js/history.js:343,372,381`

Les appels `fetch()` vers `/history/api/data`, `/history/api/aggregates`, `/history/api/latest` n'ont pas de `AbortController` ni timeout. Si le serveur est lent, les requetes s'accumulent. Le polling toutes les 30 secondes (ligne 600) peut empiler les requetes si les reponses sont lentes. Le `visibilitychange` handler (ligne 284) arrete le polling quand l'onglet est cache, ce qui attenue le risque.

#### P3.7 - Test coverage insuffisante
**Fichier :** `./tests/test_frontend_loaders.py`

Les 6 tests frontend existants verifies :
- Presence de classes CSS dans `theme.css`
- Presence de fonctions dans `loaders.js`
- Presence d'attributs `data-loader` dans les templates
- Existence de la doc

**Manques :**
- Aucun test du routeur SPA
- Aucun test du comportement responsive (CTA mobile, footer)
- Aucun test d'accessibilite (WCAG, ARIA, navigation clavier)
- Aucun test de `history.js` (Chart.js, polling, filtres)
- Aucun test de `devices.js` (copy to clipboard)
- Aucun test de `settings.js` (compteur de jours selectionnes)
- `test_loader_js_file_exists` verifie `setupFormLoaders` et `setupButtonLoaders` qui sont des no-ops vides (ligne 309-310 de `loaders.js`)

---

## 3. Analyse par categorie

### 3.1 Performance

**Poids initial de la page d'accueil (index.html) :**
- HTML : ~20 Ko (inline critical CSS compris)
- CSS : bootstrap.min.css (228 Ko) + theme.css (24 Ko) + index.css (8 Ko) + sticky-cards.css (4 Ko) + sticky-footer.css (8 Ko) + fontawesome (104 Ko) = ~376 Ko
- JS : loaders (16 Ko) + spa-router (12 Ko) + alerts (4 Ko) + bottom-nav (4 Ko) + perf-optimizer (4 Ko) + advanced-optimizer (4 Ko) = ~44 Ko
- Fonts : 3 x SpaceGrotesk TTF = 204 Ko + fa-solid WOFF2 (156 Ko) = 360 Ko
- **Total premier rendu : ~800 Ko** (avant gzip, avant Chart.js qui n'est charge que sur history)

**Problemes :**
- Font Awesome complet (104 Ko CSS + 156 Ko WOFF2) pour ~15 icones utilisees. Un subset ou des SVG inline reduirait de ~250 Ko.
- `fa-brands-400` charge mais inutilise : 320 Ko de bandwidth gaspille.
- Fonts en TTF (non-compresses) au lieu de WOFF2 (30-50% plus petit). Space Grotesk existe en WOFF2 sur Google Fonts.
- `bootstrap.min.css` complet alors que le projet utilise peut-etre 20% des classes. Pas de purge CSS.
- `performance-optimizer.js` et `advanced-optimizer.js` sont des no-ops charges pour rien.
- Le critical CSS inline (418 lignes) est duplique dans `critical.css` (fichier mort).

**Points positifs :**
- `font-display: swap` sur toutes les `@font-face` (evite FOIT)
- Preload des ressources critiques dans `<head>`
- `prefers-reduced-motion` respecte globalement
- Chart.js avec LTTB decimation et `animation: false`
- `parsing: false, normalized: true` sur Chart.js pour performance
- Page Visibility API pour pauser le polling history
- Pas de CDN, tout est local (offline-first)

### 3.2 Accessibilite (WCAG 2.1)

**Conforme :**
- `lang="fr"` sur tous les templates
- Labels associes aux inputs via `for`/`id` dans settings, login, history
- `role="alert"` sur les messages flash
- `aria-live="polite"` sur les conteneurs de messages
- `aria-label` sur les boutons de scene avec texte descriptif
- `aria-describedby` sur les champs de formulaire avec texte d'aide
- `aria-current="page"` sur le lien de navigation actif
- Touch targets 44x44px minimum sur mobile (`sticky-footer.css:324-336`)
- `prefers-reduced-motion` et `prefers-contrast: high` supportes
- Caption `sr-only` sur la table history
- `aria-describedby` sur les canvas des graphiques avec description textuelle

**Non conforme :**
- `.sr-only` non defini hors Bootstrap (peut flash sur index.html)
- Loader overlay `aria-hidden` qui masque le `role="status"` du spinner
- Pas de skip-link (lien "Aller au contenu")
- Pas de `role="banner"` sur le header, `role="contentinfo"` sur le footer
- `503.html` et `login.html` sans landmark `<main>`
- Font Awesome icônes decoratives sans `aria-hidden="true"` dans le footer nav
- `focus` management apres navigation SPA : le focus reste sur le lien clique, pas deplace vers le nouveau contenu
- Pas de `lang` attribute sur les contenus en anglais (ex: "ON", "OFF", "FAN")
- Table history : pas de `scope` sur les `<th>`

### 3.3 Securite frontend

**Conforme :**
- CSRF token injecte via meta tag + interceptors Fetch/XHR dans `loaders.js`
- Hidden `csrf_token` field dans tous les formulaires POST
- Pas de `eval()` ni `Function()` dans le JS
- Pas de `document.write()`
- SVG inline avec `focusable="false"` et `role="img"`

**Risques :**
- `innerHTML` utilise dans `history.js` (3 occurrences) - contenu statique, risque faible
- `spa-router.js:137` : `currentContent.innerHTML = newContent.innerHTML` - le contenu vient d'un `fetch` same-origin, donc le HTML est confiance, mais sans sanitization
- Pas de CSP (Content-Security-Policy) header visible dans les templates
- `spa-router.js:243` : `loadScriptDynamic` cree des `<script>` elements avec `src` du document parse - un attacker qui controle la page destination pourrait injecter un script

### 3.4 Qualite du code JavaScript

**Architecture :**
- IIFE pour l'encapsulation (loaders, alerts, devices, settings, history)
- Class-based pour SPARouter, BottomNavigation, HistoryDashboard
- Global namespace minimal : `SwitchBotRouter`, `SwitchBotLoaders`, `historyDashboard`, `SwitchBotDevicesInitialized`
- Event delegation pour les loaders (sur `document`)

**Problemes :**
- `bottom-nav.js` : 141 lignes de code mort (cible `.sb-bottom-nav` inexistant)
- `performance-optimizer.js` et `advanced-optimizer.js` : no-ops charges pour rien
- `perf-worker.js` : 99 lignes de web worker complet, non reference dans aucun template
- `loaders.js:233-235` : `setTimeout(() => { form.submit(); }, 1000)` - delai artificiel de 1s avant soumission du formulaire, degrade l'UX
- `loaders.js:243-246` : `setTimeout(finalizeSubmission, 10000)` - double cleanup qui peut conflict avec le failsafe 15s
- `spa-router.js:28` : `console.log` de debug en production
- `history.js:479` : `console.log('Elements found:', ...)` de debug en production
- `spa-router.js:243` : selection par `script[src="${src}"]` - vulnerable aux caractere speciaux dans l'URL (selector injection)

### 3.5 Qualite du code CSS

**Architecture :**
- Design tokens via CSS custom properties (variables `--sb-*`)
- 9 feuilles CSS : 1 globale (`theme.css`), 1 critique (inline + fichier mort), 7 page-specific
- Glassmorphism system coherent
- Dark mode uniquement, pas de light mode

**Problemes :**
- `critical.css` : 418 lignes dupliquees avec le `<style>` inline de `index.html`
- `sticky-footer.css` : contient des variantes `footer-bar-1` a `footer-bar-5` dont seule la 1 est utilisee (90 lignes de CSS mort)
- `sticky-cards.css` : 118 lignes de classes utilitaires (`rounded-*`, `shadow-*`, `card-style`) dont la plupart ne sont pas utilisees dans les templates
- `theme.css:73-75` : valeurs invalides `--sb-will-change-transform: will-change: transform;` et `--sb-transform-gpu: transform: translateZ(0);` - ces "variables" contiennent des declarations CSS completes, utilisables uniquement via `content` ou similaire, pas via `var()`
- `index.css:159-161` : `.scene-actions-wrapper { display: none; }` puis `@media (max-width: 767px) { .scene-actions-wrapper { display: block; } }` - masque le CTA sur desktop alors qu'il est visible sur mobile
- `sticky-footer.css:83` : `font-family: "Roboto", sans-serif !important` - Roboto non charge
- Plusieurs regles `!important` qui rendent le CSS difficile a surcharger
- `backdrop-filter: blur(20px)` utilise massivement - impact batterie sur mobile

### 3.6 Templates et structure HTML

**Conforme :**
- Doctype HTML5 sur tous les templates
- Meta viewport correct
- Meta charset UTF-8
- CSRF token meta
- Structure semantique (`<main>`, `<section>`, `<article>`, `<header>`)
- Formulaires avec labels associes

**Problemes :**
- `index.html` : 418 lignes de CSS inline dans le `<head>` (devrait etre externalise ou au moins sync avec `critical.css`)
- `index.html:466-473` : script inline pour appliquer `backgroundColor` et `color` - redondant avec le CSS
- `settings.html:63-64` : indentation cassee apres le checkbox "Automatisation activee" - le `<div class="row g-3">` qui suit est mal imbrique dans le `<div class="form-check form-switch">`
- `settings.html` : pas de `data-loader` sur le formulaire de scenes (seul le formulaire principal en a un)
- `devices.html` : pas de script `alerts.js` charge (inconsistency avec les autres pages)
- `quota.html` : pas de `alerts.js` non plus, mais utilise `data-auto-dismiss` qui depend de `alerts.js`
- Aucun template n'a de `<noscript>` fallback

---

## 4. Matrice de compatibilite navigateur

| Feature | Chrome | Firefox | Safari | iOS Safari |
|---|---|---|---|---|
| CSS Custom Properties | OK | OK | OK | OK |
| `backdrop-filter` | OK | OK (103+) | OK | OK |
| `env(safe-area-inset-*)` | OK | N/A | OK | OK |
| `DOMParser` | OK | OK | OK | OK |
| `navigator.clipboard` | OK | OK | OK | OK (13.4+) |
| `Chart.js` time scale | OK | OK | OK | OK |
| `requestIdleCallback` | OK | N/A | N/A | N/A |
| Web Worker (`perf-worker.js`) | OK | OK | OK | OK |

**Note :** `requestIdleCallback` est utilise dans `index.html:648` mais n'est pas supporte par Firefox/Safari. Le code a un fallback (`if ('requestIdleCallback' in globalThis)`) donc pas de crash, mais la logique ne s'execute pas.

---

## 5. Points positifs globaux

1. **Offline-first strict** : aucun CDN, tous les assets sont locaux
2. **Design system coherent** : variables CSS `--sb-*` partout, glassmorphism consistent
3. **CSRF protection** : interceptors Fetch/XHR + hidden fields, bien implemente
4. **Accessibilite de base** : labels, ARIA, `prefers-reduced-motion`, touch targets 44px
5. **Polling intelligent** : Page Visibility API pour pauser le polling history
6. **Chart.js optimise** : LTTB decimation, animation desactivee, parsing rapide
7. **Responsive design** : breakpoints coherents (480/576/768/992/1200), mobile-first sur plusieurs composants
8. **Loaders avec failsafe** : 15s timeout, cleanup automatique, delegation d'events
9. **SPA avec graceful degradation** : fallback vers navigation full-page si erreur

---

## 6. Recommandations actionnables (par ordre de priorite)

### Immediate (P1)

1. **Refondre le routeur SPA** ou le desactiver temporairement. Problemes : double footer, CSS desync, re-execution de scripts. Solution : soit passer aux fragments HTML ( HTMX-style) avec un endpoint dedie, soit desactiver l'interception et revenir a une navigation full-page.

2. **Corriger le CTA mobile** : supprimer `margin: 1rem -1rem -1rem` dans la version inline, ajuster `bottom` a `calc(62px + env(safe-area-inset-bottom) + 1rem)` pour eviter le chevauchement avec le footer.

3. **Supprimer `fa-brands-400`** : retirer la reference dans `all.min.css` ou utiliser un subset Font Awesome contenant uniquement les icones solid utilisees (~15 icones). Gain : ~320 Ko.

### Court terme (P2)

4. **Supprimer les fichiers morts** : `critical.css` (duplique), `performance-optimizer.js` (no-op), `advanced-optimizer.js` (no-op), `perf-worker.js` (non reference), `bottom-nav.js` (cible inexistant). Retirer leurs `<script>` des templates.

5. **Corriger le loader ARIA** : retirer `aria-hidden="true"` de l'overlay a la creation, le gerer dynamiquement. Ajouter un `aria-live="polite"` region pour annoncer le debut/fin de chargement.

6. **Corriger `sr-only`** : deplacer la definition Bootstrap `.sr-only` dans `theme.css` ou le CSS inline pour garantir sa presence avant le chargement de Bootstrap.

7. **Retirer `font-family: "Roboto"` de `sticky-footer.css`** : utiliser `inherit` ou la variable `--sb-*` du design system.

8. **Convertir les fonts Space Grotesk en WOFF2** : reduit de ~204 Ko a ~90 Ko (3 fichiers).

9. **Ajouter `AbortController` aux fetch de `history.js`** : timeout 10s par requete, evite l'empilement.

### Moyen terme (P3)

10. **Nettoyer le CSS mort** : `sticky-footer.css` variantes 2-5 (~90 lignes), `sticky-cards.css` classes non utilisees, regles `!important` superflues.

11. **Corriger la hierarchie des titres** dans `settings.html` (h2 -> h3 pour les profils).

12. **Ajouter `<main>` dans `login.html` et `503.html`**.

13. **Ajouter un skip-link** "Aller au contenu" en debut de body.

14. **Purger Bootstrap** : utiliser PurgeCSS ou un build custom pour ne garder que les classes utilisees. Gain estime : ~150 Ko.

15. **Etendre les tests** : ajouter des tests pour le routeur SPA, le responsive, l'accessibilite (axe-core), `history.js`, `devices.js`.

16. **Ajouter une CSP** : `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'` au minimum.

17. **Retirer les `console.log`** de production dans `spa-router.js:28`, `history.js:479`.

18. **Supprimer le delai artificiel** de 1s dans `loaders.js:233-235` avant la soumission des formulaires.

---

## 7. Metriques estimees (sans Lighthouse)

| Metrique | Estimation | Seuil Google | Statut |
|---|---|---|---|
| Poids total page d'accueil | ~800 Ko | < 500 Ko | Orange |
| Nombre de requetes | ~15 | < 20 | OK |
| LCP (estime) | 1.5-2.5s | < 2.5s | Orange (depend reseau) |
| CLS | < 0.05 | < 0.1 | OK (dimensions explicites) |
| FID/INP | < 50ms | < 100ms | OK (JS leger) |
| Coverage CSS | ~30% | > 80% | Rouge (Bootstrap non purge) |
| Coverage JS | ~70% | > 80% | Orange (fichiers morts) |

**Note :** Ces estimations sont bases sur l'analyse statique. Une vraie mesure Lighthouse sur environnement de production est necessaire pour valider.

---

*Aucun fichier du depot n'a ete modifie. Audit uniquement.*
