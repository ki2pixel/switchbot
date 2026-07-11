| Priorité | Constat |
|---|---|
| P1 | La navigation SPA est instable : après `Accueil → Réglages`, le navigateur affiche deux navigations, deux liens actifs, conserve `index.css` et ne charge pas `settings.css`. Le routeur remplace du HTML sans synchroniser les assets de page. [spa-router.js](/home/kidpixel/SwitchBot/switchbot_dashboard/static/js/spa-router.js:96) |
| P1 | Sur mobile, le CTA collant recouvre la barre de navigation fixe. À 375 px, il chevauche la nav de 46 px et déborde horizontalement de 4 px. Cause : marge négative et `bottom: 1rem`. [index.css](/home/kidpixel/SwitchBot/switchbot_dashboard/static/css/index.css:163) · [sticky-footer.css](/home/kidpixel/SwitchBot/switchbot_dashboard/static/css/sticky-footer.css:38) |
| P2 | Le loader n’est pas annoncé aux lecteurs d’écran : l’overlay est `aria-hidden`, donc son spinner étiqueté est également masqué. [loaders.js](/home/kidpixel/SwitchBot/switchbot_dashboard/static/js/loaders.js:94) |
| P2 | Les deux graphiques Historique n’ont ni alternative textuelle ni libellé accessible ; la table n’a pas de légende. [history.html](/home/kidpixel/SwitchBot/switchbot_dashboard/templates/history.html:115) |
| P2 | La page d’accueil charge deux optimiseurs qui maintiennent un `requestAnimationFrame`, des observers, un worker et des intervalles périodiques. Cela ajoute du travail continu sans mesure exploitable enregistrée. [performance-optimizer.js](/home/kidpixel/SwitchBot/switchbot_dashboard/static/js/performance-optimizer.js:118) · [advanced-optimizer.js](/home/kidpixel/SwitchBot/switchbot_dashboard/static/js/advanced-optimizer.js:609) |
| P2 | Les assets initiaux pèsent déjà ~700 Ko bruts pour Bootstrap, Font Awesome et les trois fontes Space Grotesk, avant le HTML et les scripts. Les optimiseurs ouvrent aussi des préconnexions Google/jsDelivr alors que les dépendances sont locales. [advanced-optimizer.js](/home/kidpixel/SwitchBot/switchbot_dashboard/static/js/advanced-optimizer.js:36) |
| P3 | Plusieurs pages n’ont pas de landmark `<main>` et les pages Actions/Historique sautent de `h1` à `h5`. [actions.html](/home/kidpixel/SwitchBot/switchbot_dashboard/templates/actions.html:49) |
| P3 | Le fichier [critical.css](/home/kidpixel/SwitchBot/switchbot_dashboard/static/css/critical.css:316) est désynchronisé du CSS inline et contient une référence Google Fonts invalide/non utilisée. |

Points positifs : interface visuellement cohérente, `lang="fr"`, labels de formulaires solides, navigation clavier globalement correcte, `prefers-reduced-motion` présent et bonnes annonces ARIA dans les formulaires.

Les 32 tests existants passent, mais ils ne couvrent ni la navigation SPA, ni le responsive mobile, ni l’accessibilité des graphiques. Les objectifs LCP/CLS annoncés ne sont pas vérifiables sans une vraie mesure Lighthouse sur environnement de production.

Ordre conseillé :

1. Désactiver temporairement l’interception SPA, ou la refondre autour de fragments HTML et d’un gestionnaire d’assets.
2. Corriger le CTA mobile : supprimer la marge négative, le placer au-dessus de la nav fixe et porter les cibles à 44 px.
3. Simplifier les optimiseurs, alléger les fontes/icônes, puis mesurer réellement.
4. Corriger les alternatives des graphiques et le statut des loaders.

Aucun fichier du dépôt n’a été modifié.

Note de transparence : le tout premier démarrage local a chargé les variables du projet et déclenché le polling SwitchBot avant que je l’arrête ; le compteur est passé de 10 000 à 9 993. Aucune action POST n’a été envoyée ; tous les autres essais ont utilisé une instance isolée simulée.