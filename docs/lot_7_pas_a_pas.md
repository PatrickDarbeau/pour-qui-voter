# Lot 7 — Contenu réel, pas à pas

*Note de travail du 12/11/2026.* Le lot 7 consiste à remplacer les candidats fictifs par les **données réelles** et à les tenir à jour jusqu'au 2 mai 2027. C'est le lot le plus long : il s'agit surtout de recherche et de relecture, beaucoup plus que de code.

Voir aussi : [cahier des charges](../CAHIER_DES_CHARGES.md) §9 bis et §9 ter, et [notice du développeur](NOTICE_DEVELOPPEUR.md) §2 (échéancier des packs) et §3 (procédure).

---

## 1. Les étapes

| # | Étape | Contenu | Qui | Échéance | État |
|---|---|---|---|---|---|
| **1** | **Thèmes** | Arrêter la liste des thèmes, avec leur icône et leur couleur | Moi (proposition) → vous (validation) | fin novembre 2026 | ✅ liste validée le 12/11/2026 (§2) |
| **2** | **Catalogue des mesures** | Rédiger 130 à 170 mesures **neutres**, de 8 à 10 par thème, sans citer aucun candidat. Relier les mesures opposées. | Moi (rédaction) → vous et une seconde personne (relecture de neutralité) | mi-décembre | 🔄 brouillon de 158 mesures le 12/11/2026 ([catalogue_mesures.md](catalogue_mesures.md)), à relire |
| **3** | **Recensement des candidats** | Candidats déclarés ou pressentis : identité, parti, **site officiel**, pages programme, statut | Recherche web (Hermès ou moi) → vérification | mi-décembre, puis en continu | 🔄 liste soumise le 12/11/2026 ([recensement_candidats.md](recensement_candidats.md)) |
| **4** | **Première collecte** | `maj.py collecter` sur les sites officiels : archivage des pages et des PDF. Premier test réel de `collecter`. | Moi | fin décembre | ⏳ |
| **5** | **Saisie des positions** | Pour chaque candidat et chaque mesure : position, source, date et citation. Mention « à confirmer » si la source n'est pas officielle. | Hermès ou moi (brouillon) → **relecture humaine obligatoire** | début janvier | ⏳ |
| **6** | **Contrôle et équilibre** | `valider.py`, couverture par candidat, même effort de recherche pour chacun, relecture de neutralité | Vous + moi | 12–14 janvier | ⏳ |
| **7** | **Premier pack réel (P1)** | `maj.py publier`, archive ZIP, test hors ligne, registre, journal | Moi → vous (publication) | **15/01/2027** | ⏳ |
| **8** | **Rythme de croisière** | Un pack par mois, puis un par semaine dès février. Pack exceptionnel à la publication de la liste officielle (mi-mars). Pack « second tour » le 19/04, pack final le 03/05. | Procédure de la notice | jusqu'au 03/05/2027 | ⏳ |

**En parallèle, à décider avant le 15/01/2027** : passage du dépôt en public, démo en ligne, début de la campagne de promotion.

---

## 2. Thèmes retenus (17)

| Ordre | Icône | Thème | Remarque |
|---|---|---|---|
| 1 | 💶 | Économie et fiscalité | |
| 2 | 👷 | Travail et emploi | |
| 3 | 👵 | Retraites | |
| 4 | 🩺 | Santé | |
| 5 | 🤝 | Solidarités et pouvoir d'achat | |
| 6 | 🎓 | Éducation et jeunesse | |
| 7 | 🎭 | Culture | ajouté le 12/11/2026 |
| 8 | 🌿 | Écologie et énergie | |
| 9 | 🚜 | Agriculture et alimentation | |
| 10 | 🏠 | Logement et territoires | |
| 11 | 🌴 | Outre-mer | ajouté le 12/11/2026 |
| 12 | 💻 | Numérique et libertés | |
| 13 | 🛡️ | Sécurité | |
| 14 | ⚖️ | Justice | |
| 15 | 🧭 | Immigration | |
| 16 | 🇪🇺 | Europe et international | inclut la défense |
| 17 | 🏛️ | Institutions et démocratie | |

*Non retenu pour l'instant* : le sport, qu'on pourra rattacher à « Culture » ou à « Éducation et jeunesse » si besoin.

Avec 8 à 10 mesures par thème, le catalogue comptera **136 à 170 mesures**. C'est un volume qui reste raisonnable pour l'utilisateur, car les thèmes et les mesures se passent librement.

---

## 3. Règles de rédaction des mesures (étape 2)

Méthode détaillée, limites et améliorations possibles : [methode_choix_mesures.md](methode_choix_mesures.md).
Bilan chiffré, mis à jour à chaque modification : [bilan_catalogue.md](bilan_catalogue.md).

> **À faire plus tard** : ajouter des contrepoints aux thèmes déséquilibrés (Travail, Solidarités, Éducation, Numérique, puis Retraites et Institutions). Voir la notice §7.

- **Neutre** : aucun nom de candidat ou de parti, aucun adjectif qui juge (« injuste », « courageux »…).
- **Concrète et vérifiable** : « Porter le SMIC à 1 600 € net », plutôt que « Améliorer les salaires ».
- **Une seule idée par mesure**.
- **Équilibrée** : pour chaque grand débat, proposer les options des différentes sensibilités, et relier les mesures opposées entre elles (champ `opposee_a`).
- **Couverture** : chaque mesure doit pouvoir être rattachée à la position d'au moins un candidat. Une mesure qu'aucun candidat ne porte sera retirée à l'étape 6.
- **Relecture** : chaque thème est soumis pour validation avant de passer au suivant.

---

## 4. Points d'attention

- **La neutralité** est le point le plus sensible. Les étapes 2 et 6 demandent un regard extérieur.
- **Mes connaissances s'arrêtent avant aujourd'hui** (novembre 2026). Les candidatures et les programmes doivent être **recherchés sur le web et vérifiés**, pas tirés de ma mémoire.
- **Les données réelles** remplaceront `data/donnees.json`. Le pack de démo reste à part dans `data/demo/`.
- **Liste officielle des candidats** : elle sera publiée par le Conseil constitutionnel vers la mi-mars. Il faudra prévoir du temps à ce moment-là.
- **Journal** : chaque étape terminée est notée dans le journal du projet (notice §5).
