# Note d'enseignements n°4 — six candidats ajoutés (fiches de profil)

**Date** : 13/11/2026 · **Lot** : 7 (étape 3, suite) · **Périmètre** : fiches de profil de Nathalie Arthaud, François Asselineau, Nicolas Dupont-Aignan, Florian Philippot, François Ruffin et Marine Tondelier, à la demande de l'éditeur (liste [`candidatures_serieuses.txt`](../candidatures_serieuses.txt), plus Nathalie Arthaud). Aucune position saisie. Total : 16 candidats, dont 9 avec positions (380 positions, inchangées).
**Analyse chiffrée** : [2026-11-13_analyse_comparative_4.md](2026-11-13_analyse_comparative_4.md) (`python outils/comparer.py 4`). Notes précédentes : [n°1](2026-11-13_recensement_1.md), [n°2](2026-11-13_recensement_2.md), [n°3](2026-11-13_recensement_3.md).

---

## 1. Ce qui fonctionne

- **Le format uniforme des fiches tient** : les six fiches ont été remplies avec la même grille (naissance « Ville (département) », formation, profession, biographie courte, site, portrait 3:4), contrôlée par le test `TestFichesCandidats`. Aucune adaptation du code de l'application n'a été nécessaire.
- **Les portraits de l'infobox Wikipédia conviennent tous** : les six sont sous licence libre (CC BY 4.0 ou CC BY-SA 4.0) et cadrés correctement par le recadrage automatique (`outils/portraits.py`).
- **Le traitement des candidats sans positions est clair** : ils apparaissent dans la liste avec le badge « Positions non encore saisies », leur fiche l'indique, et ils sont listés à part dans les résultats, sans être classés.
- **Biographies sourcées et neutres** : faits repris de la page de portraits de franceinfo (source FI du recensement), complétés par Wikipédia pour la naissance, la formation et la profession.

## 2. Ce qui ne fonctionne pas ou reste fragile

### 2.1 Sites officiels

| Candidat | Site retenu | Type | Remarque |
|---|---|---|---|
| Arthaud | nathalie-arthaud.info | campagne | page « Élection présidentielle 2027 » |
| Asselineau | upr.fr | parti | `asselineau2027.fr` est réservé mais vide (logo seul) |
| Dupont-Aignan | debout-la-france.fr | parti | pas de site de campagne trouvé |
| Philippot | les-patriotes.fr | parti | pas de site de campagne trouvé |
| Ruffin | debout.fr | mouvement | `francoisruffin.fr` est son site de député |
| Tondelier | marinetondelier.fr | campagne | « Candidate à l'élection présidentielle » |

Un nom de domaine qui répond n'est pas une preuve : le titre et le contenu de chaque site ont été lus avant de le retenir.

### 2.2 Données Wikipédia incomplètes

- L'infobox ne renseigne pas la **formation de Nathalie Arthaud** ni la **profession de Marine Tondelier** : ces champs ont été repris du corps de l'article (sections « Biographie » et « Parcours professionnel »).
- Lieux de naissance à Paris avant 1968 : notés « (Seine) », l'ancien département, comme pour Éric Zemmour (Montreuil, 1958).
- Les requêtes vers l'API de Wikipédia échouaient pour les titres contenant « ç » : l'adresse n'était pas encodée. Les outils doivent toujours encoder les titres (`urllib.parse.urlencode`).

### 2.3 Équité de traitement

- **Seize candidats, neuf classés** : sept candidats n'ont aucune position. Plus la liste s'allonge, plus l'écart de traitement se voit. Les positions des sept candidats en attente sont la priorité suivante.
- **Couleurs** : celles des six nouveaux candidats ont été **proposées par Claude** selon la même logique (tendance politique) ; elles restent à valider par l'éditeur.
- **Biographie d'Asselineau** : la source FI mentionne un renvoi en correctionnelle. Ce fait n'est pas repris dans la fiche, car il est sans effet sur la candidature (contrairement à la condamnation de Marine Le Pen, liée à son éligibilité). **Décision à confirmer par l'éditeur**, pour appliquer une règle identique à tous.

## 3. Pistes

1. Relever les positions des sept candidats en attente, en commençant par ceux qui ont un programme publié (sites de campagne d'Arthaud et de Tondelier).
2. Écrire la règle sur les procédures judiciaires dans les biographies (quand les mentionner).
3. Revoir les couleurs des six nouveaux candidats dans le mode Édition, puis les reporter dans `outils/candidats.py`.
