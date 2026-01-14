# **Évaluation Comparative des Solutions d'Hébergement PostgreSQL Managées en Tier Gratuit pour les Startups et Prototypes en 2026**

L'évolution des infrastructures de bases de données cloud-natives a atteint un point de maturité sans précédent en 2026, redéfinissant les attentes des développeurs en phase de démarrage de projet. Pour un prototype ou une application naissante, le choix de la base de données ne repose plus uniquement sur la robustesse du moteur — PostgreSQL étant devenu le standard de facto — mais sur l'agilité, la capacité d'intégration et, surtout, la viabilité économique de l'offre gratuite. Le passage d'une gestion manuelle sur des serveurs privés virtuels (VPS) à des solutions managées serverless ou conteneurisées permet de décharger les équipes techniques des tâches d'exploitation critiques pour se concentrer sur la logique métier.1

Cette analyse approfondie examine les acteurs dominants du marché, notamment Neon, Supabase et Aiven, tout en évaluant des alternatives pertinentes telles que Northflank, Koyeb et Render. L'objectif est de fournir une vision exhaustive des capacités opérationnelles, des contraintes techniques et des trajectoires de croissance offertes par ces services en 2026\.

## **Architecture Serverless et Flexibilité : L'Approche Disruptive de Neon**

Neon s'est imposé comme une solution de rupture technologique en introduisant une architecture où le stockage et le calcul sont physiquement dissociés. Cette séparation permet une élasticité quasi infinie et une gestion granulaire des ressources, ce qui est particulièrement bénéfique pour les projets dont le trafic est intermittent ou imprévisible.3

### **Limites et Quotas de l'Offre Gratuite**

Le plan gratuit de Neon, révisé fin 2025 pour répondre aux besoins croissants des développeurs, propose désormais une structure de quotas très compétitive. Chaque utilisateur peut créer jusqu'à 100 projets, une limite exceptionnellement haute qui favorise l'expérimentation multi-services et le micro-déploiement.5 L'unité de mesure fondamentale pour le calcul est l'heure-CU (Compute Unit hour). Un Compute Unit (CU) alloue approximativement 1 vCPU et 4 Go de RAM.4

L'offre gratuite inclut 100 heures-CU par projet et par mois. Ce volume permet une grande souplesse : une instance de 0,25 CU peut fonctionner pendant 400 heures mensuelles, couvrant ainsi plus de la moitié d'un mois en fonctionnement continu, tandis qu'une instance de 1 CU pourra fonctionner pendant 100 heures.4 La formule mathématique régissant cette consommation est la suivante :  
$CU\_{hours} \= Size\_{CU} \\times Time\_{hours}$.6  
En termes de stockage, Neon limite chaque projet à 0,5 Go.5 Bien que cela puisse paraître modeste, l'architecture de Neon optimise l'utilisation grâce au partage de données entre les branches. Le transfert de données sortantes (egress) est plafonné à 5 Go par mois.5

### **Fonctionnalités PostgreSQL et Innovations de Plateforme**

Neon supporte les versions les plus récentes de PostgreSQL, de la version 14 à la version 17, assurant aux développeurs l'accès aux dernières optimisations du moteur.6 L'innovation majeure réside dans le "Database Branching". En utilisant un modèle de "Copy-on-Write" (CoW), Neon permet de créer instantanément des copies isolées de la base de données pour le développement ou le test.5 Ces branches ne consomment du stockage supplémentaire que pour les données qui divergent de la branche parente, ce qui rend le processus à la fois rapide et économique.5

Le support des extensions est robuste, incluant notamment PostGIS pour les données géospatiales et pgvector pour les applications intégrant de l'intelligence artificielle et des recherches de similarité.4 L'accès superuser n'est pas fourni directement pour maintenir la stabilité de la plateforme managée, mais des rôles avec des privilèges étendus permettent la quasi-totalité des opérations administratives nécessaires.5

### **Expérience Développeur et Écosystème**

L'expérience utilisateur sur Neon est centrée sur l'automatisation. L'intégration avec des plateformes comme Vercel permet de provisionner automatiquement des bases de données de prévisualisation pour chaque branche de code, un atout majeur pour les pipelines CI/CD modernes.10 La plateforme propose également une mise en veille automatique après 5 minutes d'inactivité, ce qui préserve le quota d'heures-CU, bien que cela implique un temps de "cold start" d'environ 500ms à 2 secondes lors de la réactivation par une requête entrante.4

L'observabilité est assurée par une rétention d'un jour pour les métriques et les logs dans le plan gratuit, permettant un débogage rapide des interactions récentes.5

### **Sauvegarde et Haute Disponibilité**

La résilience est nativement intégrée grâce à la redondance du stockage distribué. Pour la récupération de données, Neon inclut une fonctionnalité de restauration immédiate (PITR) gratuite, limitée à une fenêtre de 6 heures ou à 1 Go de modifications de données.5 Cette fenêtre est cruciale pour corriger les erreurs de manipulation ou les échecs de migration de schéma durant les phases de prototypage intense.4

### **Évolution vers les Plans Payants**

Le passage au plan "Launch" commence à partir d'un minimum de 5 $ par mois ou selon un modèle basé sur l'usage réel.4 Les tarifs de stockage ont été agressivement réduits à environ 0,35 $ par Go-mois pour rester compétitifs face aux fournisseurs de cloud traditionnels.4 La migration est transparente puisqu'elle ne nécessite aucun déplacement de données, seulement une levée logicielle des quotas du plan gratuit.5

| Métrique | Offre Gratuite Neon (2026) |
| :---- | :---- |
| Projets inclus | 100 5 |
| Heures-CU par projet | 100 6 |
| Stockage par projet | 0,5 Go 5 |
| Bande passante (Egress) | 5 Go 6 |
| Branches par projet | 10 5 |
| Connexions max (Pooler) | 10 000 8 |
| Rétention Monitoring | 1 jour 6 |

## **L'Approche Backend-as-a-Service : Supabase et l'Intégration Verticale**

Supabase ne se présente pas comme un simple hébergeur PostgreSQL, mais comme une alternative open-source à Firebase, où la base de données PostgreSQL sert de fondation à un ensemble de services intégrés tels que l'authentification, le stockage de fichiers et les fonctions edge.2

### **Limites et Quotas de l'Offre Gratuite**

Le plan gratuit de Supabase permet de gérer jusqu'à 2 projets actifs simultanément.14 La base de données incluse est une instance PostgreSQL dédiée (mais tournant sur des ressources partagées) de 500 Mo.14 Contrairement au modèle de Neon basé sur le temps, Supabase offre une base de données "toujours allumée", sous réserve d'une activité minimale : les projets inactifs pendant plus de 7 jours sont mis en veille automatique pour optimiser les ressources de l'infrastructure.14

En plus de la base de données, l'offre gratuite comprend :

* Authentification pour 50 000 utilisateurs actifs mensuels (MAU).15  
* Stockage d'objets (fichiers) de 1 Go avec une limite de transfert de 5 Go.14  
* 500 000 invocations de fonctions Edge par mois.15  
* 2 millions de messages via le service Realtime.14

### **Fonctionnalités PostgreSQL et Support**

Supabase utilise des versions standard de PostgreSQL (actuellement la version 15, avec un déploiement progressif de la version 18 prévu pour 2026).3 L'accès superuser est restreint pour garantir l'intégrité de la plateforme gérée, mais les utilisateurs disposent du rôle postgres qui bénéficie de privilèges étendus pour gérer les schémas, les rôles et les extensions.18

Le catalogue d'extensions est l'un des plus complets du marché, avec plus de 50 extensions préinstallées et activables en un clic, dont PostGIS, pgvector, pgcrypto, et pg\_cron.18 Cette richesse fonctionnelle permet de bâtir des applications complexes (géolocalisation, IA, tâches planifiées) sans sortir de l'écosystème gratuit.14

### **Expérience Développeur et Observabilité**

L'un des principaux arguments de Supabase est son interface d'administration "tout-en-un". Elle comprend un éditeur SQL puissant avec assistance par IA (postgres.new), un explorateur de données visuel et des outils de gestion de l'authentification.10 La plateforme génère automatiquement des APIs REST et GraphQL à partir du schéma de la base de données, ce qui accélère considérablement le développement front-end.2

Pour l'observabilité, Supabase propose désormais une API de métriques et des journaux d'audit (rétention d'une heure en tier gratuit) qui permettent de surveiller la santé de la base de données et des fonctions associées.15

### **Sauvegarde et Résilience**

Le plan gratuit ne propose pas de sauvegardes automatiques avec restauration granulaire (PITR).14 Les utilisateurs doivent s'appuyer sur des outils externes ou des sauvegardes manuelles via la CLI pour sécuriser leurs données.9 La résilience est assurée par l'infrastructure AWS sur laquelle repose Supabase, offrant une haute disponibilité matérielle sans toutefois proposer de SLA financier pour le tier gratuit.3

### **Évolution vers les Plans Payants**

Le plan Pro débute à 25 $ par mois et par projet.14 Ce plan supprime la mise en veille des projets, augmente le stockage inclus à 8 Go et active les sauvegardes quotidiennes avec une rétention de 7 jours.14 Un point fort de la tarification Supabase est le "Spend Cap", qui permet de limiter les coûts aux 25 $ de base, évitant toute surfacturation imprévue en cas de pic de trafic.24 Au-delà du quota, le stockage supplémentaire est facturé 0,125 $ par Go.14

| Ressource | Quota Plan Gratuit Supabase |
| :---- | :---- |
| Nombre de projets | 2 14 |
| Taille Base de Données | 500 Mo 14 |
| Bande passante (Egress) | 5 Go 15 |
| Utilisateurs Auth (MAU) | 50 000 16 |
| Stockage de fichiers | 1 Go 14 |
| Invocations Edge Functions | 500 000 15 |

## **Aiven : L'Excellence de l'Open Source sur VM Dédiée**

Aiven se distingue en proposant une version "pure" de PostgreSQL sur une infrastructure de machines virtuelles (VM) dédiées, offrant une isolation et une prévisibilité de performance supérieures aux instances partagées.25

### **Limites et Spécifications du Tier Gratuit**

L'offre gratuite d'Aiven fournit une instance PostgreSQL tournant sur une VM avec 1 vCPU et 1 Go de RAM.25 Le stockage est limité à 1 Go, ce qui est supérieur à Neon et Supabase.3 Contrairement à ses concurrents, Aiven ne met pas systématiquement les bases de données en veille après quelques minutes d'inactivité, bien que la plateforme se réserve le droit de suspendre les services manifestement inutilisés après notification.26

Une restriction importante concerne le choix de l'infrastructure : l'utilisateur ne peut pas choisir le fournisseur de cloud ni la région précise dans le plan gratuit ; les instances sont généralement déployées sur DigitalOcean dans une sélection de régions mondiales (Amérique du Nord, Europe, Asie).3

### **Fonctionnalités et Accès PostgreSQL**

Aiven supporte les versions 13, 14, 15 et 16 de PostgreSQL, permettant une grande compatibilité avec les applications existantes.3 L'accès est fourni via l'utilisateur avnadmin. Comme pour les autres services managés, l'accès superuser complet n'est pas autorisé, mais les privilèges accordés permettent de gérer l'intégralité du cycle de vie des données et des extensions.28

Le support des extensions est très large, incluant PostGIS, TimescaleDB, et l'extension maison aiven\_extras qui facilite la gestion des bases de données par des non-superutilisateurs.3 En revanche, le tier gratuit limite le nombre de connexions simultanées à 20 et n'autorise pas l'utilisation de poolers de connexions comme PgBouncer.26

### **Expérience Développeur et Administration**

Aiven privilégie une approche orientée "Infrastructure-as-Code". En plus d'une console web épurée, le service offre une intégration complète avec Terraform et un opérateur Kubernetes, ce qui est idéal pour les équipes souhaitant automatiser leur infrastructure dès le départ.3 Des outils d'optimisation basés sur l'IA sont également inclus gratuitement pour analyser les requêtes et suggérer des indexations.25

L'observabilité est un point fort, avec des graphiques de performance et un accès aux logs intégrés nativement, sans configuration complexe.25

### **Sauvegarde et Disponibilité**

Le plan gratuit inclut des sauvegardes pour la reprise après sinistre, bien que les fonctionnalités de restauration granulaire (PITR) soient réservées aux plans supérieurs.25 La stabilité est assurée par le déploiement sur des nœuds dédiés, bien que le SLA de 99,99% ne s'applique pas officiellement au tier gratuit.26

### **Passage au Plan Payant**

Aiven propose un plan intermédiaire "Developer" à partir de 5 $ par mois.27 Ce plan augmente le stockage à 8 Go, garantit que le service ne sera jamais arrêté pour inactivité et offre un support technique de base.26 Pour des besoins de production critique avec haute disponibilité et choix de la région, il faut passer au plan "Professional".27

| Composant | Spécification Aiven Free |
| :---- | :---- |
| Type d'instance | VM Dédiée (1 vCPU) 25 |
| RAM | 1 Go 26 |
| Stockage | 1 Go 3 |
| Connexions Max | 20 26 |
| Versions PG | 13, 14, 15, 16 3 |
| Monitoring | Logs et métriques inclus 26 |

## **Analyse des Alternatives : Render, Northflank et Koyeb**

D'autres acteurs proposent des services PostgreSQL intégrés à des plateformes applicatives plus larges, chacun avec des compromis spécifiques pour leurs offres gratuites.

### **Render : Une Solution pour le Prototypage Éphémère**

Render propose une base de données PostgreSQL gratuite mais avec une contrainte majeure de durée : elle expire 30 jours après sa création.8 Après cette période, l'utilisateur dispose de 14 jours pour passer à un plan payant, sans quoi les données sont définitivement supprimées.29

* **Quotas :** 1 Go de stockage, ressources CPU/RAM partagées.8  
* **Limites :** Pas de sauvegardes, instance unique, mise en veille après inactivité avec redémarrage lent.29  
* **Usage idéal :** Hackathons ou démonstrations techniques temporaires.

### **Northflank : L'Approche Conteneurisée et Toujours Active**

Northflank offre un "Sandbox Tier" qui permet de déployer deux services et deux bases de données gratuitement.13 Contrairement au modèle serverless, Northflank promet un calcul "always-on", évitant les délais de réveil des instances.32

* **Quotas :** Ressources CPU/RAM limitées (environ 0,1 vCPU et 256 Mo RAM pour les plus petites instances).13  
* **Fonctionnalités :** Support complet de PostGIS, intégration CI/CD native, et environnements de prévisualisation automatiques pour les Pull Requests.13  
* **Observabilité :** Logs et métriques en temps réel inclus nativement.32

### **Koyeb : Le Serverless avec Presence Mondiale**

Koyeb propose une instance PostgreSQL serverless intégrée à sa plateforme de déploiement global.3

* **Quotas :** 0,25 vCPU, 1 Go RAM, 1 Go de stockage et 50 heures d'activité par mois.3  
* **Fonctionnalités :** Version 14, 15 et 16, mise en veille après 5 minutes d'inactivité, support de PostGIS et pgvector.3  
* **Localisation :** Possibilité de choisir entre Francfort, Washington D.C. et Singapour, ce qui est rare pour un tier gratuit.3

## **Synthèse Comparative des Fonctionnalités Techniques**

Le choix d'une solution pour un projet critique en coût doit mettre en balance les limites immédiates et les capacités techniques offertes.

### **Comparaison des Versions et Extensions**

| Fournisseur | Versions PostgreSQL | Support PostGIS | Support pgvector | Branchement / PITR |
| :---- | :---- | :---- | :---- | :---- |
| **Neon** | 14, 15, 16, 17 6 | Oui 6 | Oui 4 | Oui (Branchement \+ 6h PITR) 5 |
| **Supabase** | 15, 18 (Beta) 19 | Oui 18 | Oui 20 | Non (Restauration manuelle) 14 |
| **Aiven** | 13, 14, 15, 16 3 | Oui 28 | Oui 28 | Non (Sauvegarde DR uniquement) 26 |
| **Northflank** | 12 à 17 13 | Oui 36 | Oui 36 | Non (Sauvegarde planifiée payante) 32 |
| **Koyeb** | 14, 15, 16 3 | Oui 3 | Oui 3 | Non 35 |

### **Évaluation de l'Accès et de la Sécurité**

Tous les fournisseurs analysés utilisent un modèle d'accès restreint où l'utilisateur ne possède pas les privilèges SUPERUSER au sens strict de PostgreSQL, mais dispose de rôles administratifs suffisants pour 99% des besoins applicatifs (création de schémas, de tables, installation d'extensions approuvées).18 La sécurité des données au repos et en transit est un standard en 2026, avec un chiffrement TLS activé par défaut sur toutes les plateformes.9

Aiven et Northflank se distinguent par une approche plus proche des standards Kubernetes et VM, offrant une meilleure isolation réseau, tandis que Supabase et Neon misent sur une intégration logicielle profonde pour simplifier la sécurité (comme le Row Level Security intégré à l'Auth pour Supabase).9

## **Analyse de l'Expérience Développeur et de l'Intégration CI/CD**

L'agilité d'une équipe de démarrage dépend souvent de la fluidité avec laquelle elle peut déployer et tester ses changements de schéma.

### **Automatisation et Workflows**

* **Neon** mène la danse avec le branchement natif. Un développeur peut créer une branche de la base de données en moins d'une seconde pour tester une migration complexe, puis fusionner ses changements sans risque pour la production.4  
* **Supabase** offre une expérience centrée sur le tableau de bord. La possibilité de modifier le schéma via une interface graphique ou via des migrations contrôlées par la CLI rend l'outil accessible aussi bien aux débutants qu'aux experts.10  
* **Northflank** propose une orchestration de services complète. Si votre application nécessite un worker en tâche de fond et un cache Redis, Northflank permet de lier ces services à PostgreSQL avec une découverte de service automatique, simplifiant énormément la configuration réseau initiale.33

### **Outils d'Observabilité et Maintenance**

L'observabilité est devenue un standard même pour les offres gratuites.

* **Aiven** fournit des métriques détaillées sur l'utilisation du CPU, de la RAM et des entrées/sorties disque, ce qui est crucial pour identifier quand l'instance de 1 Go de RAM commence à saturer.25  
* **Supabase** intègre désormais des outils d'analyse de requêtes (Index Advisor) directement dans l'éditeur de table, aidant les développeurs à optimiser leurs performances avant même de rencontrer des problèmes de charge.23  
* **Neon** permet de suivre la consommation des CU-heures en temps réel, évitant ainsi l'épuisement soudain du quota mensuel.5

## **Sauvegarde, Résilience et Haute Disponibilité**

La fiabilité des données est le critère qui sépare souvent les solutions de "jouet" des outils de développement sérieux.

### **Politiques de Sauvegarde**

| Solution | Sauvegarde Automatique (Free) | Méthode de Restauration | Résilience |
| :---- | :---- | :---- | :---- |
| **Neon** | Oui (Continu) 5 | PITR (Fenêtre de 6h) 6 | Stockage distribué multi-nœuds 3 |
| **Supabase** | Non 14 | Export manuel (pg\_dump) 9 | Infrastructure AWS standard 3 |
| **Aiven** | Oui (Quotidien) 26 | Restauration par support/Admin 25 | VM Dédiée 25 |
| **Northflank** | Non (Options payantes) 32 | Export manuel / Snapshot payant | Orchestration Kubernetes 33 |
| **Koyeb** | Limité 35 | \- | Design tolérant aux pannes 3 |

La haute disponibilité avec basculement automatique (failover) n'est généralement pas incluse dans les tiers gratuits, qui reposent sur des instances uniques. Cependant, l'architecture de Neon, qui sépare le stockage du calcul, offre une forme de résilience supérieure : si le nœud de calcul tombe, un nouveau peut être rattaché au stockage persistant presque instantanément.3

## **Stratégie d'Évolution et Viabilité Économique à Long Terme**

Pour un projet de démarrage, il est vital de comprendre à quel moment le coût va cesser d'être nul et comment cette transition sera gérée.

### **Les Déclencheurs de l'Upgrade**

Plusieurs facteurs forcent le passage à un plan payant :

1. **Le Volume de Données :** Dépasser les 500 Mo (Supabase/Neon) ou 1 Go (Aiven) est le premier motif d'upgrade.  
2. **La Continuité de Service :** La mise en veille automatique peut être inacceptable pour une application grand public qui exige une réponse instantanée même après une période d'inactivité.4  
3. **La Sécurité des Données :** Dès que les données deviennent critiques, l'absence de PITR (sur Supabase) ou la fenêtre de 6h (sur Neon) pousse vers les plans payants offrant 7 à 30 jours de rétention.6

### **Analyse des Coûts Post-Gratuité**

* **Aiven** offre le chemin de croissance le plus doux avec son plan "Developer" à 5 $/mois, ce qui en fait l'option la moins chère pour lever les restrictions du plan gratuit.27  
* **Neon** propose une approche par l'usage. Le plan "Launch" ($5 min) est très flexible, permettant de payer précisément pour les ressources consommées, ce qui est idéal pour les startups à croissance variable.4  
* **Supabase** fait un saut plus important à 25 $/mois, mais ce prix inclut un ensemble de services (Auth, Storage, Functions) qui, s'ils étaient pris séparément ailleurs, coûteraient probablement plus cher.14

| Fournisseur | Premier Prix Payant | Avantages Clés | Migration |
| :---- | :---- | :---- | :---- |
| **Aiven** | 5 $ / mois 27 | 8 Go stockage, pas de mise en veille 27 | Automatique |
| **Neon** | \~5-19 $ / mois 4 | Calcul illimité, 7 jours PITR 6 | Transparente |
| **Supabase** | 25 $ / mois 14 | Sauvegardes, pas de veille, 8 Go DB 16 | Transparente |
| **Northflank** | 2,70 $ / mois 13 | Ressources dédiées (min) 13 | Changement de plan |

## **Recommandations Finales pour le Choix de la Solution**

Selon la nature du projet applicatif, le choix optimal varie :

1. Pour une application mobile ou web complète (Full-Stack) :  
   Supabase est le choix recommandé. L'intégration de l'authentification et des APIs automatiques permet de réduire le "Time-to-Market" de manière spectaculaire. Les 50 000 MAU gratuits offrent une marge de croissance confortable avant toute dépense.9  
2. Pour un projet nécessitant des environnements de test complexes :  
   Neon est imbattable. Le branchement de base de données permet une agilité DevOps que les autres plateformes ne peuvent égaler, tout en offrant le meilleur système de récupération de données gratuit (PITR 6h).4  
3. Pour une base de données PostgreSQL "pure" et stable :  
   Aiven est la solution de choix. Avec ses VM dédiées et son support des versions standard, elle offre une expérience prévisible et une transition très économique vers le premier niveau payant à 5 $.8  
4. Pour un prototype éphémère ou un test technique :  
   Render ou Neon conviennent parfaitement. Render pour sa simplicité extrême de mise en place, Neon pour sa puissance technique sans engagement.13

L'année 2026 marque l'apogée des offres "Free-to-Start", où les contraintes ne sont plus sur les fonctionnalités de PostgreSQL lui-même, mais sur les ressources allouées. La décision doit donc se fonder sur l'écosystème global de développement et la trajectoire de mise à l'échelle prévue pour l'application.

#### **Sources des citations**

1. 5 Best Free PostgreSQL Hosting 2026 \- Bitcatcha, consulté le janvier 14, 2026, [https://www.bitcatcha.com/web-hosting/free/postgresql/](https://www.bitcatcha.com/web-hosting/free/postgresql/)  
2. Best managed PostgreSQL solutions for developers: Top 5 in 2026, consulté le janvier 14, 2026, [https://www.instaclustr.com/education/postgresql/best-managed-postgresql-solutions-for-developers-top-5-in-2026/](https://www.instaclustr.com/education/postgresql/best-managed-postgresql-solutions-for-developers-top-5-in-2026/)  
3. Top PostgreSQL Database Free Tiers in 2026 \- Koyeb, consulté le janvier 14, 2026, [https://www.koyeb.com/blog/top-postgresql-database-free-tiers-in-2026](https://www.koyeb.com/blog/top-postgresql-database-free-tiers-in-2026)  
4. Neon Serverless Postgres Pricing 2026: Complete Breakdown & Cost Comparison \- Vela, consulté le janvier 14, 2026, [https://vela.simplyblock.io/articles/neon-serverless-postgres-pricing-2026/](https://vela.simplyblock.io/articles/neon-serverless-postgres-pricing-2026/)  
5. Pricing — Neon, consulté le janvier 14, 2026, [https://neon.com/pricing](https://neon.com/pricing)  
6. Neon plans \- Neon Docs, consulté le janvier 14, 2026, [https://neon.com/docs/introduction/plans](https://neon.com/docs/introduction/plans)  
7. How to Make the Most of Neon's Free Plan, consulté le janvier 14, 2026, [https://neon.com/blog/how-to-make-the-most-of-neons-free-plan](https://neon.com/blog/how-to-make-the-most-of-neons-free-plan)  
8. Run Postgres For Free: Top 3 Options \- DEV Community, consulté le janvier 14, 2026, [https://dev.to/hackmamba/run-postgres-for-free-top-3-options-2pk6](https://dev.to/hackmamba/run-postgres-for-free-top-3-options-2pk6)  
9. Supabase vs Neon Comparison: Features, Pricing & Use Cases \- Leanware, consulté le janvier 14, 2026, [https://www.leanware.co/insights/supabase-vs-neon](https://www.leanware.co/insights/supabase-vs-neon)  
10. Supabase vs Neon: The Battle of PostgreSQL Titans | by Berto Mill | Medium, consulté le janvier 14, 2026, [https://bertomill.medium.com/supabase-vs-neon-the-battle-of-postgresql-titans-418044159d1f](https://bertomill.medium.com/supabase-vs-neon-the-battle-of-postgresql-titans-418044159d1f)  
11. Managed Postgres · Fly Docs \- Fly.io, consulté le janvier 14, 2026, [https://fly.io/docs/mpg/](https://fly.io/docs/mpg/)  
12. Vercel Postgres Transition Guide \- Neon Docs, consulté le janvier 14, 2026, [https://neon.com/docs/guides/vercel-postgres-transition-guide](https://neon.com/docs/guides/vercel-postgres-transition-guide)  
13. Best PostgreSQL hosting providers for developers in 2026 | Blog \- Northflank, consulté le janvier 14, 2026, [https://northflank.com/blog/best-postgresql-hosting-providers](https://northflank.com/blog/best-postgresql-hosting-providers)  
14. Pricing & Fees | Supabase, consulté le janvier 14, 2026, [https://supabase.com/pricing](https://supabase.com/pricing)  
15. About billing on Supabase, consulté le janvier 14, 2026, [https://supabase.com/docs/guides/platform/billing-on-supabase](https://supabase.com/docs/guides/platform/billing-on-supabase)  
16. Supabase Pricing 2025: Free, Pro & Enterprise Costs | MetaCTO, consulté le janvier 14, 2026, [https://www.metacto.com/blogs/the-true-cost-of-supabase-a-comprehensive-guide-to-pricing-integration-and-maintenance](https://www.metacto.com/blogs/the-true-cost-of-supabase-a-comprehensive-guide-to-pricing-integration-and-maintenance)  
17. Supabase pricing model: How it works and how to build your own \- Orb Billing, consulté le janvier 14, 2026, [https://www.withorb.com/blog/supabase-pricing](https://www.withorb.com/blog/supabase-pricing)  
18. Roles, superuser access and unsupported operations | Supabase Docs, consulté le janvier 14, 2026, [https://supabase.com/docs/guides/database/postgres/roles-superuser](https://supabase.com/docs/guides/database/postgres/roles-superuser)  
19. Any estimate on Supabase timeline for upgrade to PostgreSQL 18? \- Reddit, consulté le janvier 14, 2026, [https://www.reddit.com/r/Supabase/comments/1ps8fqd/any\_estimate\_on\_supabase\_timeline\_for\_upgrade\_to/](https://www.reddit.com/r/Supabase/comments/1ps8fqd/any_estimate_on_supabase_timeline_for_upgrade_to/)  
20. Postgres Extensions | Supabase Features, consulté le janvier 14, 2026, [https://supabase.com/features/postgres-extensions](https://supabase.com/features/postgres-extensions)  
21. Supabase Blog: the Postgres development platform, consulté le janvier 14, 2026, [https://supabase.com/blog](https://supabase.com/blog)  
22. Changelog \- Supabase, consulté le janvier 14, 2026, [https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0xOFQxOTowNTozN1rOAG3scg==\&restPage=2](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0wOS0xOFQxOTowNTozN1rOAG3scg%3D%3D&restPage=2)  
23. Changelog \- Supabase, consulté le janvier 14, 2026, [https://supabase.com/changelog](https://supabase.com/changelog)  
24. The Complete Guide to Supabase Pricing Models and Cost Optimization \- Flexprice, consulté le janvier 14, 2026, [https://flexprice.io/blog/supabase-pricing-breakdown](https://flexprice.io/blog/supabase-pricing-breakdown)  
25. Create hosted PostgreSQL® database for FREE \- Aiven, consulté le janvier 14, 2026, [https://aiven.io/free-postgresql-database](https://aiven.io/free-postgresql-database)  
26. Service pricing | Aiven docs, consulté le janvier 14, 2026, [https://aiven.io/docs/platform/concepts/service-pricing](https://aiven.io/docs/platform/concepts/service-pricing)  
27. Introducing Developer Tier for Aiven for PostgreSQL® services, consulté le janvier 14, 2026, [https://aiven.io/blog/new-developer-tier-for-aiven-for-postgres](https://aiven.io/blog/new-developer-tier-for-aiven-for-postgres)  
28. Extensions on Aiven for PostgreSQL® | Aiven docs, consulté le janvier 14, 2026, [https://aiven.io/docs/products/postgresql/reference/list-of-extensions](https://aiven.io/docs/products/postgresql/reference/list-of-extensions)  
29. Deploy for Free – Render Docs, consulté le janvier 14, 2026, [https://render.com/docs/free](https://render.com/docs/free)  
30. From Zero to Deployed: My Portfolio Power-Up (Free Render \+ PostgreSQL Magic), consulté le janvier 14, 2026, [https://medium.com/@aish\_v/from-zero-to-deployed-my-portfolio-power-up-free-render-postgresql-magic-da661d115d9e](https://medium.com/@aish_v/from-zero-to-deployed-my-portfolio-power-up-free-render-postgresql-magic-da661d115d9e)  
31. Render vs Vercel (2026): Which platform suits your app architecture better? | Blog, consulté le janvier 14, 2026, [https://northflank.com/blog/render-vs-vercel](https://northflank.com/blog/render-vs-vercel)  
32. Pricing \- Northflank, consulté le janvier 14, 2026, [https://northflank.com/pricing](https://northflank.com/pricing)  
33. Best PaaS for full-stack microservices in 2026 | Blog \- Northflank, consulté le janvier 14, 2026, [https://northflank.com/blog/best-paas-for-full-stack-microservices](https://northflank.com/blog/best-paas-for-full-stack-microservices)  
34. Disaster recovery — Use cases \- Northflank, consulté le janvier 14, 2026, [https://northflank.com/use-cases/disaster-recovery-for-kubernetes](https://northflank.com/use-cases/disaster-recovery-for-kubernetes)  
35. Pricing for intensive infractrucure \- Koyeb, consulté le janvier 14, 2026, [https://www.koyeb.com/pricing](https://www.koyeb.com/pricing)  
36. Databases — Features — Northflank, consulté le janvier 14, 2026, [https://northflank.com/features/databases](https://northflank.com/features/databases)