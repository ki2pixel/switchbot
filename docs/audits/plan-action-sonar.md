# Plan de Remédiation SonarCloud

**TL;DR** : Ne faites jamais confiance aux données d'API injectées via `innerHTML`. L'audit SonarCloud révèle une faille XSS critique ; remplacez l'injection dynamique par la création de nœuds DOM sécurisés pour bloquer toute exécution de script malveillant.

## Le Piège de l'Injection Directe

Vous affichez le tableau des derniers enregistrements dans le Dashboard. L'API vous renvoie des données JSON. Vous utilisez des *template strings* et `innerHTML` pour générer les lignes du tableau rapidement. C'est concis et ça fonctionne très bien. 

Jusqu'au jour où le champ `last_action` (manipulé depuis IFTTT) contient une balise `<script>`. Votre interface vient d'exécuter du code malveillant sur le poste du client sans aucun avertissement. 

> [!CAUTION]
> Une vulnérabilité XSS critique (Blocker `jssecurity:S5696`) a été identifiée à la ligne 440 de `history.js` lors de l'injection des données non assainies dans `tbody.innerHTML`.

L'audit SonarCloud complet remonte 134 anomalies. Voici notre plan d'attaque, structuré en 3 phases pour isoler la sécurité immédiate du refactoring continu.

---

## Phase 1 : Sécurité Critique & Bugs

Cette phase cible la vulnérabilité Blocker, les failles mineures de journalisation, et les bugs fonctionnels avérés.

- **Remédiation XSS (`history.js`)** : Interdiction formelle de `innerHTML` pour rendre des variables dynamiques issues de l'API. Nous allons privilégier la création d'éléments DOM via `document.createElement`.
- **Assainissement des Logs (S5145)** : Filtrage systématique des entrées utilisateur dans la configuration de la journalisation pour empêcher l'injection de journaux.
- **Correction des 4 Bugs Immédiats** : 
  - Ajout de la balise `<title>` manquante sur la page principale `index.html`.
  - Résolution de la surcharge CSS invalide (`padding-top` défini deux fois ou mal écrasé) dans `sticky-footer.css`.
  - Suppression des instanciations inutiles et redondantes de l'objet `BottomNavigation`.

### ❌ L'Approche Vulnérable (Injection HTML)

```javascript
// history.js - Ligne 440
tbody.innerHTML = latestRecords.map(record => {
    return `
        <tr>
            <td>${record.timestamp}</td>
            <td>${record.last_action}</td> <!-- Vulnérabilité XSS -->
        </tr>
    `;
}).join('');
```

### ✅ L'Approche Sécurisée (Création DOM)

```javascript
// history.js
tbody.innerHTML = ''; // Seule utilisation acceptable (vider le conteneur)
latestRecords.forEach(record => {
    const tr = document.createElement('tr');
    
    const tdTime = document.createElement('td');
    tdTime.textContent = record.timestamp;
    
    const tdAction = document.createElement('td');
    tdAction.textContent = record.last_action || '--'; // Échappement natif
    
    tr.append(tdTime, tdAction); // Appends all other columns...
    tbody.appendChild(tr);
});
```

> [!NOTE]
> L'utilisation de la propriété `textContent` garantit que la chaîne est insérée en tant que texte pur. Toute balise HTML (y compris `<script>`) sera affichée textuellement sans être interprétée.

---

## Phase 2 : Refactoring de Complexité

Le Dashboard s'alourdit. Les fonctions critiques de `automation.py`, `routes.py`, et `loaders.js` dépassent le seuil autorisé de complexité cognitive (score > 15). 

- **Aplatissement (`loaders.js`)** : La fonction `setupFormLoaders` s'enfonce sur 4 niveaux d'indentation. Nous utiliserons le modèle du retour anticipé (*early return*).
- **Responsabilité Unique (`automation.py` & `routes.py`)** : Extraction de la logique métier (notamment la gestion IFTTT) en sous-fonctions distinctes.
- **Consolidation des Constantes (S1192)** : Les chaînes littérales dupliquées plus de 3 fois dans `routes.py` seront mutualisées sous forme de variables constantes en haut de fichier.

### ❌ Le "Nesting" Profond

```javascript
const setupFormLoaders = () => {
    forms.forEach((form) => {
        form.addEventListener('submit', (event) => {
            const submitButton = form.querySelector('button');
            if (submitButton && !submitButton.disabled) {
                // ... Trop de niveaux
            }
        });
    });
};
```

### ✅ Le "Early Return" (Garde de Clause)

```javascript
const handleFormSubmit = (event, form) => {
    const submitButton = form.querySelector('button');
    if (!submitButton || submitButton.disabled) return;
    
    // ... Logique de chargement à plat
};

const setupFormLoaders = () => {
    forms.forEach(form => form.addEventListener('submit', e => handleFormSubmit(e, form)));
};
```

---

## Phase 3 : Modernisation & Accessibilité

Il s'agit d'appliquer les standards HTML5/JS modernes et d'éliminer la dette technique (Major/Minor Code Smells) de l'interface.

- **Logging des Exceptions** : Remplacement du verbeux `logging.error(..., exc_info=True)` par la méthode canonique `logging.exception()`.
- **Méthodes DOM Obsolètes** : Remplacement de l'ancestral `parentNode.removeChild` par la méthode native moderne `childNode.remove()` dans la gestion des overlays `loaders.js`.
- **Modernisation JavaScript** : Utilisation du chaînage optionnel (*optional chaining* `?.`), de l'API `dataset` pour les attributs de données, et de `globalThis` plutôt que l'objet `window` absolu.
- **Accessibilité Mobile** : Ajout d'attributs sémantiques `Aria-checked` sur les switches, réparation des labels orphelins (associés via `for=id`), et validation complète du bottom nav.

### ❌ L'Ancienne École

```python
# automation.py
except Exception as e:
    logging.error("Erreur inattendue", exc_info=True)

// loaders.js
if (overlay.parentElement) {
    overlay.parentElement.removeChild(overlay);
}
```

### ✅ L'Approche Moderne

```python
# automation.py
except Exception as e:
    logging.exception("Erreur inattendue")

// loaders.js
overlay?.remove();
```

---

## Comparatif des Approches DOM

| Approche | Vitesse d'écriture | Sécurité (XSS) | Charge de Maintenance |
| -------- | ------------------ | -------------- | --------------------- |
| `innerHTML` + Template | ✅ Très rapide | ❌ Faible (Vulnérable) | ❌ Élevée |
| `document.createElement`| ❌ Plus long | ✅ Maximale | ✅ Basse |
| Bibliothèques (ex: React)| ✅ Rapide | ✅ Maximale | ❌ Complexe (Build) |

---

## La Règle d'Or : Le Texte N'est Jamais du Code

Tout ce qui provient d'une API, d'une base de données ou d'une saisie utilisateur doit être traité par défaut comme du texte compromis. Confinez-le dans un contexte purement textuel (via `textContent` ou `innerText`) et laissez le moteur de rendu du navigateur se charger de l'échappement.
