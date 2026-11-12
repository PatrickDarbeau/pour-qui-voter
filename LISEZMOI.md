# Pour qui voter ? — Présidentielle 2027

Ce comparateur confronte vos priorités aux programmes des candidats. Il fonctionne **hors ligne** : aucune de vos réponses ne quitte votre appareil.

## Utilisation
Décompressez l'archive, puis ouvrez `index.html` dans votre navigateur avec un double-clic. Il n'y a rien à installer.

## Développement
| Commande | Rôle |
|---|---|
| `python outils/demo.py` | Régénère le jeu de démonstration (candidats fictifs) |
| `python outils/valider.py --publier` | Contrôle `data/donnees.json` et génère `data/donnees.js` |
| `node tests/score.test.js` | Lance les tests du calcul de concordance |
| `python -m http.server 8765` | Lance un serveur local (facultatif) |

Le cahier des charges complet se trouve dans [CAHIER_DES_CHARGES.md](CAHIER_DES_CHARGES.md).
