# Notice du développeur — suivi du projet et mise à jour des données

Ce document de travail sert au mainteneur. Mettez-le à jour à chaque lot terminé et à chaque pack publié.
Les règles du projet se trouvent dans le [cahier des charges](../CAHIER_DES_CHARGES.md) : §9 bis pour la procédure, §9 ter pour la gouvernance des données, §10 pour le planning.

---

## 1. Suivi des lots de développement

État : ✅ terminé · 🔄 en cours · ⏳ à faire

| Lot | Contenu | Échéance visée | État | Commit / remarque |
|---|---|---|---|---|
| L1 | Format `donnees.json`, validateur, jeu de démonstration | 12/11/2026 | ✅ | `913fc2f` |
| L2 | Parcours électeur, calcul du score, interface « bulletin de vote » | 12/11/2026 | ✅ | `913fc2f` — reste à vérifier l'ouverture par double-clic |
| L3 | Mode Édition : CRUD, matrice mesures × candidats, import/export | 27/11/2026 | ⏳ | |
| L4 | Résultats détaillés (graphique par thème), export PDF, lien de partage | 04/12/2026 | ⏳ | |
| L5 | `outils/maj.py`, import/export de packs (F29 à F40) | 18/12/2026 | ⏳ | |
| L6 | Accessibilité, tests, paquet ZIP, démo en ligne, mode second tour | 08/01/2027 | ⏳ | |
| L7 | Recherche et saisie des données réelles, puis packs réguliers | dès le 11/01/2027 | ⏳ | avec Hermès pour la recherche |
| — | **Jalon : version complète publiée** | **15/03/2027** | ⏳ | impératif |

> À chaque lot terminé : cocher la ligne, noter le commit et ajouter une entrée au §5 (journal).

---

## 2. Échéancier des packs de données

Règle (CDC §9 ter) : un pack par mois jusqu'à fin janvier 2027, puis un par semaine jusqu'au premier tour.
Les packs hebdomadaires sont publiés le **vendredi**.

| N° | Date | Type | Contenu attendu | État |
|---|---|---|---|---|
| P0 | 12/11/2026 | démo | Candidats fictifs (actuel) | ✅ |
| P1 | 15/01/2027 | mensuel | Premier pack réel : candidats déclarés ou pressentis, 15 thèmes, 120 mesures minimum | ⏳ |
| P2 | 29/01/2027 | mensuel | Compléments, corrections | ⏳ |
| P3 | 05/02/2027 | hebdo | | ⏳ |
| P4 | 12/02/2027 | hebdo | | ⏳ |
| P5 | 19/02/2027 | hebdo | | ⏳ |
| P6 | 26/02/2027 | hebdo | | ⏳ |
| P7 | 05/03/2027 | hebdo | | ⏳ |
| P8 | 12/03/2027 | hebdo | Pack livré avec la version complète (jalon du 15/03) | ⏳ |
| PX | publication de la liste officielle (date à confirmer, vers mi-mars) | exceptionnel | Retrait des non-qualifiés, statut « officiellement qualifié » | ⏳ |
| P9 | 19/03/2027 | hebdo | | ⏳ |
| P10 | 26/03/2027 | hebdo | | ⏳ |
| P11 | 02/04/2027 | hebdo | | ⏳ |
| P12 | 09/04/2027 | hebdo | | ⏳ |
| P13 | 16/04/2027 | hebdo | **Dernier pack avant le premier tour (18/04)** | ⏳ |
| P14 | 19/04/2027 | second tour | Deux candidats qualifiés, mode second tour activé | ⏳ |
| P15 | 26/04/2027 | hebdo | Ajustements avant le second tour (02/05) | ⏳ |
| PF | 03/05/2027 | final | Pack archivé, fin de la maintenance | ⏳ |

Le **jeudi précédent**, le développeur lance la collecte (étapes 1 à 3). Le **vendredi**, il fait la relecture et la publication (étapes 4 à 6).

---

## 3. Réaliser un pack : pas à pas

> Les commandes `maj.py` seront disponibles à la fin du lot 5. D'ici là, les étapes 1 à 3 se font à la main, et l'étape 4 dans `data/donnees.json`, puis dans le mode Édition une fois le lot 3 livré.

### Étape 1 — Veille des candidats (30 min)
- [ ] Consulter les annonces de candidature, de retrait et de ralliement de la semaine.
- [ ] À partir de mars : consulter les publications du Conseil constitutionnel (parrainages, puis liste officielle).
- [ ] Mettre à jour la liste : ajouter ou retirer des candidats, changer le `statut`, renseigner `site_officiel` et `pages_programme`.
- Commande : `python outils/maj.py candidats`

### Étape 2 — Collecte des sources (1 à 2 h)
- [ ] Pour chaque candidat, ouvrir son **site officiel** et repérer les pages programme, les pages thématiques et les PDF.
- [ ] Archiver chaque page et chaque PDF dans `data/sources/AAAA-MM-JJ/<candidat>/`, en notant l'URL et la date de consultation.
- [ ] Compléter avec la presse ou les interviews si le site officiel est muet sur une mesure.
- Commande : `python outils/maj.py collecter` (elle archive les pages et signale celles qui ont changé depuis la collecte précédente)
- Hermès peut être sollicité pour cette recherche. Ses résultats sont toujours à vérifier.

### Étape 3 — Extraction (2 à 4 h)
- [ ] Commencer par les pages signalées comme modifiées.
- [ ] Pour chaque proposition repérée, la rattacher à une mesure existante, ou créer une nouvelle mesure formulée de façon **neutre**, sans nom de candidat.
- [ ] Noter la position (+1, +0,5, 0 ou −1), la source (`source_url`, `source_type`, `source_date`) et une citation courte.
- [ ] Une source qui n'est ni le site officiel ni le programme doit être marquée `a_confirmer: true`.
- Résultat : `brouillon.json`

### Étape 4 — Relecture humaine (obligatoire)
- [ ] Relire **chaque** position modifiée ou ajoutée, en ouvrant la source.
- [ ] Vérifier la neutralité des intitulés de mesures.
- [ ] Vérifier l'équilibre : même effort de recherche pour chaque candidat.

### Étape 5 — Contrôle
```bash
python outils/valider.py
```
- [ ] Aucune ERREUR.
- [ ] Les alertes (couverture faible, thème trop pauvre) sont expliquées ou corrigées.
- [ ] `node tests/score.test.js` passe.

### Étape 6 — Publication
```bash
python outils/valider.py --publier
```
- [ ] Renseigner dans `donnees.json` : `version` (au format `AAAA.MM.JJ`), `date`, `demo: false`, et le `journal` des changements.
- [ ] Copier le pack sous `donnees-AAAA-MM-JJ.json` et noter son **empreinte SHA-256**, affichée par le validateur.
- [ ] Construire le ZIP de l'application (commande prévue au lot 6).
- [ ] Publier le pack, son empreinte et le ZIP sur la page de démonstration et sur le dépôt.
- [ ] Commit : `git commit -m "Pack PN du JJ/MM/AAAA"` puis `git tag pack-AAAA-MM-JJ`.
- [ ] Mettre à jour le §2 (état ✅) et le §4 (registre).

---

## 4. Registre des packs publiés

| N° | Version | Date | Candidats | Mesures | Positions | SHA-256 (16 premiers caractères) | Principales modifications |
|---|---|---|---|---|---|---|---|
| P0 | 2026.11.12-demo | 12/11/2026 | 4 (fictifs) | 20 | 80 | `5b12cbbaaaffa620` | Jeu de démonstration |

---

## 5. Journal du projet

| Date | Événement |
|---|---|
| 12/11/2026 | Cahier des charges validé. Lots 1 et 2 réalisés (`913fc2f`). Notice créée. |

---

## 6. Points de vigilance
- **Neutralité** : aucune mesure ne doit être formulée à l'avantage d'un candidat. En cas de doute, faire relire par une seconde personne.
- **Signalements d'erreur** (F40) : les traiter avant le pack suivant et les noter dans le journal.
- **Dates clés** : liste officielle des candidats (mars), premier tour le 18/04/2027, second tour le 02/05/2027.
- **Ne jamais** intégrer de réponses d'utilisateurs aux packs ou aux sources.
