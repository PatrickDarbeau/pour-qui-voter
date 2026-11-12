# Pour qui voter ? — Présidentielle 2027

Ce comparateur confronte vos priorités aux programmes des candidats. Il fonctionne **hors ligne** : aucune de vos réponses ne quitte votre appareil.

## Utilisation
Décompressez l'archive, puis ouvrez `index.html` dans votre navigateur avec un double-clic. Il n'y a rien à installer.

## Développement
| Commande | Rôle |
|---|---|
| `python outils/demo.py` | Régénère le jeu de démonstration (candidats fictifs) |
| `python outils/valider.py --publier` | Contrôle `data/donnees.json` et génère `data/donnees.js` |
| `python outils/maj.py candidats` · `collecter` · `diff A B` · `publier --version AAAA.MM.JJ` | Mise à jour des données (voir la notice du développeur) |
| `node tests/score.test.js` | Lance les tests du calcul de concordance |
| `python -m unittest tests/test_outils.py` | Teste le validateur et l'outil de mise à jour |
| `python outils/paquet.py` | Construit l'archive ZIP pour les utilisateurs dans `dist/` |
| `node tests/hors_ligne.mjs` | Ouvre l'archive en `file://` avec Chrome et vérifie qu'aucune requête réseau n'est faite |
| `python -m http.server 8765` | Lance un serveur local (facultatif) |
| `node tests/pdf.mjs docs/exemples/resultats-exemple.pdf` | Génère un PDF des résultats (serveur local lancé) pour contrôler l'impression |

Le cahier des charges complet se trouve dans [CAHIER_DES_CHARGES.md](CAHIER_DES_CHARGES.md) (la liste des lots est au §10).
Le suivi des lots, l'échéancier des packs et la procédure de mise à jour sont dans [docs/NOTICE_DEVELOPPEUR.md](docs/NOTICE_DEVELOPPEUR.md).

## Démo en ligne
La démo se publie sur GitHub Pages avec le workflow manuel **« Démo en ligne »** (onglet *Actions*), une fois le dépôt rendu public.
En démo en ligne, un bandeau invite à télécharger l'application et le mode Édition est désactivé.
Pour tester ce mode en local : ajoutez `?demo` à l'adresse (ex. `http://localhost:8765/?demo`).
Les liens de téléchargement se règlent dans `assets/js/config.js`.
