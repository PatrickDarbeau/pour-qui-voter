# Notice du développeur — suivi du projet et mise à jour des données

Ce document de travail sert au mainteneur. Mettez-le à jour à chaque lot terminé et à chaque pack publié.
Les règles du projet se trouvent dans le [cahier des charges](../CAHIER_DES_CHARGES.md) : §9 bis pour la procédure, §9 ter pour la gouvernance des données, §10 pour le planning.

\---

## 1\. Suivi des lots de développement

État : ✅ terminé · 🔄 en cours · ⏳ à faire

|Lot|Contenu|Échéance visée|État|Commit / remarque|
|-|-|-|-|-|
|L1|Format `donnees.json`, validateur, jeu de démonstration|12/11/2026|✅|`913fc2f`|
|L2|Parcours électeur, calcul du score, interface « bulletin de vote »|12/11/2026|✅|`913fc2f` — reste à vérifier l'ouverture par double-clic|
|L3|Mode Édition : CRUD, matrice mesures × candidats, import/export|27/11/2026|✅|voir journal (12/11/2026)|
|L4|Résultats détaillés (graphique par thème), export PDF, lien de partage|04/12/2026|✅|radar + carte de chaleur, impression, partage|
|L5|`outils/maj.py`, import/export de packs (F29 à F40)|18/12/2026|✅|`maj.py` candidats/collecter/diff/publier ; import avec aperçu, empreinte, fusion|
|L6|Accessibilité, tests, paquet ZIP, démo en ligne, mode second tour|08/01/2027|✅|`paquet.py`, tests hors ligne et Python, mode démo, second tour, workflow Pages manuel|
|L7|Recherche et saisie des données réelles, puis packs réguliers|dès le 11/01/2027|⏳|avec Hermès pour la recherche|
|—|**Jalon : version complète publiée**|**15/03/2027**|⏳|impératif|

> À chaque lot terminé : cocher la ligne, noter le commit et ajouter une entrée au §5 (journal).

\---

## 2\. Échéancier des packs de données

Règle (CDC §9 ter) : un pack par mois jusqu'à fin janvier 2027, puis un par semaine jusqu'au premier tour.
Les packs hebdomadaires sont publiés le **vendredi**.

|N°|Date|Type|Contenu attendu|État|
|-|-|-|-|-|
|P0|12/11/2026|démo|Candidats fictifs (actuel)|✅|
|P1|15/01/2027|mensuel|Premier pack réel : candidats déclarés ou pressentis, 15 thèmes, 120 mesures minimum|⏳|
|P2|29/01/2027|mensuel|Compléments, corrections|⏳|
|P3|05/02/2027|hebdo||⏳|
|P4|12/02/2027|hebdo||⏳|
|P5|19/02/2027|hebdo||⏳|
|P6|26/02/2027|hebdo||⏳|
|P7|05/03/2027|hebdo||⏳|
|P8|12/03/2027|hebdo|Pack livré avec la version complète (jalon du 15/03)|⏳|
|PX|publication de la liste officielle (date à confirmer, vers mi-mars)|exceptionnel|Retrait des non-qualifiés, statut « officiellement qualifié »|⏳|
|P9|19/03/2027|hebdo||⏳|
|P10|26/03/2027|hebdo||⏳|
|P11|02/04/2027|hebdo||⏳|
|P12|09/04/2027|hebdo||⏳|
|P13|16/04/2027|hebdo|**Dernier pack avant le premier tour (18/04)**|⏳|
|P14|19/04/2027|second tour|Deux candidats qualifiés, mode second tour activé|⏳|
|P15|26/04/2027|hebdo|Ajustements avant le second tour (02/05)|⏳|
|PF|03/05/2027|final|Pack archivé, fin de la maintenance|⏳|

Le **jeudi précédent**, le développeur lance la collecte (étapes 1 à 3). Le **vendredi**, il fait la relecture et la publication (étapes 4 à 6).

\---

## 3\. Réaliser un pack : pas à pas

> Les commandes `maj.py` sont disponibles. L'étape 3 (extraction) reste manuelle, dans le mode Édition de l'application ; exportez ensuite le pack (JSON) et copiez-le dans `data/donnees.json` avant l'étape 5.

### Pack de démonstration (candidats fictifs)
- Il est conservé à part : `data/demo/donnees-demo.json`. Les données réelles, dans `data/donnees.json`, peuvent évoluer sans le toucher.
- Pour le régénérer : `python outils/demo.py`. L'option `--installer` le copie aussi dans `data/donnees.json`, pour des tests seulement.
- Il est fourni dans l'archive ZIP (`exemples/donnees-demo.json`) et s'importe dans l'application.
- Pour la démo en ligne : workflow « Démo en ligne », choix `demo` (candidats fictifs) ou `reelles`.

### Après le premier tour — activer le mode second tour

* \[ ] Dans Édition › Candidats, section « Mode second tour » : choisir les deux qualifiés, cocher « Activer ».
* \[ ] Exporter le pack, le copier dans `data/donnees.json`, puis publier (pack P14 du 19/04/2027).

### Étape 1 — Veille des candidats (30 min)

* \[ ] Consulter les annonces de candidature, de retrait et de ralliement de la semaine.
* \[ ] À partir de mars : consulter les publications du Conseil constitutionnel (parrainages, puis liste officielle).
* \[ ] Mettre à jour la liste : ajouter ou retirer des candidats, changer le `statut`, renseigner `site\_officiel` et `pages\_programme`.
* Commande : `python outils/maj.py candidats`

### Étape 2 — Collecte des sources (1 à 2 h)

* \[ ] Pour chaque candidat, ouvrir son **site officiel** et repérer les pages programme, les pages thématiques et les PDF.
* \[ ] Archiver chaque page et chaque PDF dans `data/sources/AAAA-MM-JJ/<candidat>/`, en notant l'URL et la date de consultation.
* \[ ] Compléter avec la presse ou les interviews si le site officiel est muet sur une mesure.
* Commande : `python outils/maj.py collecter` (elle archive les pages et signale celles qui ont changé depuis la collecte précédente)
* Hermès peut être sollicité pour cette recherche. Ses résultats sont toujours à vérifier.

### Étape 3 — Extraction (2 à 4 h)

* \[ ] Commencer par les pages signalées comme modifiées.
* \[ ] Pour chaque proposition repérée, la rattacher à une mesure existante, ou créer une nouvelle mesure formulée de façon **neutre**, sans nom de candidat.
* \[ ] Noter la position (+1, +0,5, 0 ou −1), la source (`source\_url`, `source\_type`, `source\_date`) et une citation courte.
* \[ ] Une source qui n'est ni le site officiel ni le programme doit être marquée `a\_confirmer: true`.
* Résultat : `brouillon.json`

### Étape 4 — Relecture humaine (obligatoire)

* \[ ] Relire **chaque** position modifiée ou ajoutée, en ouvrant la source.
* \[ ] Vérifier la neutralité des intitulés de mesures.
* \[ ] Vérifier l'équilibre : même effort de recherche pour chaque candidat.

### Étape 5 — Contrôle

```bash
python outils/valider.py
```

* \[ ] Aucune ERREUR.
* \[ ] Les alertes (couverture faible, thème trop pauvre) sont expliquées ou corrigées.
* \[ ] `node tests/score.test.js` passe.

### Étape 6 — Publication

```bash
python outils/maj.py publier --version AAAA.MM.JJ
```

* \[ ] La commande valide le pack, fixe la version et la date, retire les marques « modifié localement », rédige le `journal` à partir des différences avec le pack précédent (ou utilisez `--journal "texte"`), puis génère `data/donnees.js`.
* \[ ] Elle écrit `dist/donnees-AAAA-MM-JJ.json` et son fichier `.sha256`, et affiche la **ligne à copier dans le registre** (§4).
* \[ ] Pour comparer deux packs à tout moment : `python outils/maj.py diff ancien.json nouveau.json`.
* \[ ] Construire le ZIP de l'application : `python outils/paquet.py` (écrit `dist/pour-qui-voter-<version>.zip` et son `.sha256`).
* \[ ] Vérifier l'archive : `node tests/hors\_ligne.mjs` (ouverture par double-clic, aucune requête réseau).
* \[ ] Publier le pack, son empreinte et le ZIP sur la page de démonstration et sur le dépôt.
* \[ ] Commit : `git commit -m "Pack PN du JJ/MM/AAAA"` puis `git tag pack-AAAA-MM-JJ`.
* \[ ] Mettre à jour le §2 (état ✅) et le §4 (registre).

\---

## 4\. Registre des packs publiés

|N°|Version|Date|Candidats|Mesures|Positions|SHA-256 (16 premiers caractères)|Principales modifications|
|-|-|-|-|-|-|-|-|
|P0|2026.11.12-demo|12/11/2026|4 (fictifs)|20|80|`8a0762515f617e00`|Jeu de démonstration (republié avec `maj.py publier`)|

\---

## 5\. Journal du projet

|Date|Événement|Commit|
|-|-|-|
|12/11/2026|Cahier des charges rédigé et validé : installation locale, données issues des sites officiels, démo en ligne secondaire, gouvernance des packs, dates des deux tours.|—|
|12/11/2026|**Lots 1 et 2** : format des données, validateur, jeu de démonstration (candidats fictifs), parcours électeur, calcul du score testé, interface « bulletin de vote ».|`913fc2f`|
|12/11/2026|Notice du développeur créée (suivi des lots, échéancier des packs, procédure).|`86d2bbc`|
|12/11/2026|Dépôt GitHub privé créé (PatrickDarbeau/pour-qui-voter) ; adresse e-mail des commits remplacée par l'adresse anonyme GitHub (historique réécrit).|`752caa2`|
|12/11/2026|Résultats groupés par thème ; en-tête civique avec messages contre l'abstention.|`51e6f9d`|
|12/11/2026|Couleur propre à chaque thème ; correction de la politique de sécurité qui bloquait les barres de score.|`c033da7`|
|12/11/2026|**Lot 3** : mode Édition (thèmes, mesures, candidats, matrice des positions sourcées, import/export JSON et CSV, sauvegarde et restauration).|`609cd5b`|
|12/11/2026|Kit de campagne de promotion (YouTube, LinkedIn, X, Substack, autres canaux).|`29b4cdb`|
|12/11/2026|Édition › Mesures : sections dépliables par thème, filtre, ajout direct dans un thème.|`ee3b7c6`|
|12/11/2026|Thèmes prioritaires : pastille « ✓ Prioritaire » à la place de la croix.|`624df42`|
|12/11/2026|Page Méthode réécrite en langage simple, avec exemple chiffré.|`145d27c`|
|12/11/2026|Accueil : boutons Poursuivre, Voir mes résultats, Recommencer à zéro.|`81854de`|
|12/11/2026|Page Aide (questions fréquentes) et bulles d'aide au survol.|`c9959af`|
|12/11/2026|Fenêtre d'avertissement au démarrage (outil non officiel, aide à la décision).|`1d4e926`|
|12/11/2026|**Lot 4** : radar et tableau coloré par thème, mise en page PDF, lien de partage avec avertissement.|`068f716`|
|12/11/2026|PDF testé avec un vrai rendu Chrome et corrigé (4 pages) ; script `tests/pdf.mjs` et exemple.|`c16d4fe`|
|12/11/2026|Usage pédagogique et adaptation à d'autres élections (avertissement et Aide).|`d431e53`|
|12/11/2026|Page Aide : boutons Retour et Continuer le questionnaire.|`dabf007`|
|12/11/2026|Note sur les dons rédigée ; **mise en place reportée** (voir §7).|`c722160`|
|12/11/2026|Notice : décisions reportées et points à vérifier (§7).|`0377175`|
|12/11/2026|**Lot 5** : `outils/maj.py` (candidats, collecter, diff, publier) ; import de pack avec aperçu des changements, empreinte SHA-256, contrôle de version et choix pour les modifications locales. Pack de démo republié.|`9d51ff6`|
|12/11/2026|**Lot 6** : mode second tour (réglage dans Édition › Candidats), mode démo en ligne (bandeau, édition désactivée), accessibilité (lien d'évitement, titres de page, barres de progression), archive ZIP avec lanceurs, test hors ligne (13 contrôles) et tests Python (11), workflow GitHub Pages manuel.|`0566b4f`|
|12/11/2026|Règle adoptée : le journal est mis à jour après chaque lot ou mise à jour, dans le même commit.|—|
|12/11/2026|Page Méthode, §2 : rappel que thèmes prioritaires et mesures essentielles sont facultatifs.|`a90bb84`|
|12/11/2026|Page Méthode : boutons en bas de page (Retour, Voir mes résultats, Continuer le questionnaire), communs avec l'Aide.|`6c7b3ae`|
|12/11/2026|Accueil : « ? » rouge sur le bulletin animé qui tombe dans l'urne.|`5e9f0e3`|
|12/11/2026|Accueil, étape 3 : « détail des accords et désaccords avec les candidats ».|`4266ce4`|
|12/11/2026|Aide : nouvelle question « Et pour le second tour ? » (pack du 19/04, réponses conservées, activation manuelle).|`1e4ff84`|
|12/11/2026|Fiche candidat : boutons « ← Tous les candidats » et « Voir mes résultats » en bas de page.|`e1e89c8`|
|12/11/2026|Note sur les licences et la responsabilité ([LICENCES.md](LICENCES.md)) ; décision en attente (§7).|`9411627`|
|12/11/2026|Licences adoptées : **EUPL 1.2** (code) et **CC BY-SA 4.0** (données). Fichiers LICENCE, LICENCE-DONNEES, MENTIONS-LEGALES.md ; page « Mentions légales » et lien en pied de page ; champ `licence` dans les packs ; licences incluses dans l'archive ZIP ; test hors ligne étendu (15 contrôles).|`23bd0d1`|
|12/11/2026|Pack de démonstration (candidats fictifs) conservé à part dans `data/demo/donnees-demo.json` ; fourni dans l'archive (`exemples/`) ; choix « demo » ou « réelles » pour la démo en ligne ; question dans l'Aide ; test dédié.|`5211fcb`|
|12/11/2026|Démo en ligne : mode Édition en **essai** (thèmes, mesures, positions modifiables dans le navigateur du visiteur), **candidats verrouillés** (liste, fiches, second tour), import de packs désactivé ; CDC §6 bis, LISEZMOI et Aide mis à jour ; test hors ligne étendu (20 contrôles).|`2f836b2`|
|12/11/2026|**Lot 7 démarré** : note [lot_7_pas_a_pas.md](lot_7_pas_a_pas.md) (8 étapes) ; étape 1 validée — 17 thèmes (culture et outre-mer ajoutés).|`494b4a5`|
|12/11/2026|Lot 7, étape 2 : premières mesures rédigées à partir de propositions publiques, reformulées de façon neutre avec leurs contrepoints.|`d1072e7`|
|12/11/2026|Lot 7, étape 2 : **brouillon du catalogue** — 158 mesures sur 17 thèmes (20 issues de la démo, 17 contrepoints, 121 nouvelles), 8 à 12 par thème, mesures opposées reliées ; généré par `outils/catalogue.py` → `data/brouillon/catalogue.json` et [catalogue_mesures.md](catalogue_mesures.md).|`762fb75`|
|12/11/2026|Catalogue : plus aucune référence à une source d'inspiration externe ; les mesures sont reformulées et neutres (origine « nouveau »).|`a480918`|
|12/11/2026|Notice §7 : ajout du nettoyage de l'historique Git et du choix du nom affiché, à faire avant le passage en public.|`11896d3`|
|12/11/2026|Note [methode_choix_mesures.md](methode_choix_mesures.md) : méthode de choix des mesures, limites, améliorations possibles (A1–A6 avant le 15/01, B1–B3 pendant la campagne, C1–C4 outils).|`c216461`|
|12/11/2026|Bilan du catalogue [bilan_catalogue.md](bilan_catalogue.md), régénéré automatiquement par `python outils/catalogue.py` : 158 mesures, 49 paires opposées, 59 mesures sans contrepoint.|`36f2c1f`|
|12/11/2026|Reporté : ajout de contrepoints aux thèmes déséquilibrés (notice §7).|`db02c26`|
|12/11/2026|Lot 7, étape 3 : **recensement des candidats** ([recensement_candidats.md](recensement_candidats.md)) — 3 sources croisées (franceinfo, Candidator, République 2027) : 36 déclarés confirmés par au moins 2 sources, 13 à une seule source, 3 contradictoires, 9 pressentis. Soumis à validation avant les fiches de profil.|`cb63ce1`|
|12/11/2026|Lot 7, étape 3 : 10 candidats retenus (`candidatures_probables.txt`) ; **fiches de profil** en brouillon ([fiches_candidats.md](fiches_candidats.md)) générées par `outils/candidats.py` : biographies sourcées, sites vérifiés (1 site de campagne, 8 sites de parti ou mouvement, 1 sans site), couleurs neutres, points à vérifier listés.|`aac0103`|
|12/11/2026|Lot 7, étape 4 : **première collecte** ([collecte_2026-11-12.md](collecte_2026-11-12.md)) — 24 pages archivées ; pages programme trouvées pour 5 candidats (Glucksmann, Lisnard, Mélenchon, Philippe, Retailleau) ; à compléter pour Attal, Le Pen (site protégé), Riner, Roussel, Zemmour. `maj.py collecter` : options `--pack` et `--decouvrir`, respect de robots.txt, pause d'une seconde.|`a4ae818`|
|12/11/2026|Lot 7, étape 4 : recherche complémentaire — sites de campagne trouvés pour **Roussel** (fabienroussel2027.fr) et **Zemmour** (ericzemmour.fr), collectés ; 7 candidats sur 10 avec pages programme. Restent Attal, Le Pen et Riner. Sites écartés après vérification : ancien site des législatives 2024 d'Attal, domaines parqués au nom de Marine Le Pen.|`8594029`|
|12/11/2026|Lot 7, étape 5 : **positions de Jean-Luc Mélenchon** en brouillon ([positions_melenchon.md](positions_melenchon.md)) — 111 mesures sur 158 (61 soutient, 10 en partie, 40 s'oppose ; 10 à confirmer), chacune avec extrait et lien vers le chapitre de « L'Avenir en commun » (6e éd.). Le PDF du site (contrat NFP 2024) a été écarté. Outil `outils/positions.py`.|`6b90f3b`|
|12/11/2026|Lot 7, étape 5 : **positions de David Lisnard** en brouillon ([positions_lisnard.md](positions_lisnard.md)) — 45 mesures sur 158, chacune avec extrait et lien vers la page du programme de Nouvelle Énergie (3 axes + 5 pages thématiques, ajoutées à la collecte).|`84e0e83`|
|12/11/2026|Lot 7, étape 5 : **positions de Bruno Retailleau** en brouillon ([positions_retailleau.md](positions_retailleau.md)) — 28 mesures sur 158, sourcées dans les propositions des Républicains (page + 8 PDF ajoutés à la collecte). Thèmes non couverts par ces documents : immigration, sécurité, justice, santé, institutions, Europe. Bibliothèque `pypdf` installée pour lire les PDF.|`d790a0d`|
|12/11/2026|Lot 7, étape 5 : positions de **Bruno Retailleau** complétées par 18 tribunes et entretiens du candidat publiés sur le site de LR (35 h, retraites, référendum et Constitution, Europe, immigration, justice des mineurs, fin de vie, politique familiale) : 44 mesures sur 158 (contre 28).|`d3d2d35`|
|12/11/2026|Lot 7, étape 5 : **positions de Raphaël Glucksmann** en brouillon ([positions_glucksmann.md](positions_glucksmann.md)) — 50 mesures sur 158, sourcées dans le livret de campagne « Révolution écologique » (glucks2027.fr) et le projet « Acte I » de Place publique. Fiche mise à jour : primaire gagnée le 11/10/2026 (66,17 %), site de campagne glucks2027.fr.|`c6aa556`|
|12/11/2026|Lot 7, étape 5 : **positions d'Édouard Philippe** en brouillon ([positions_philippe.md](positions_philippe.md)) — 46 mesures sur 158, sourcées dans le programme de son site de campagne edouardphilippe.fr (15 thèmes, mis à jour le 12/11/2026). Fiche : site de campagne au lieu du site d'Horizons.|`db2a762`|
|12/11/2026|**Pack de test** installé dans l'application (`outils/assembler.py --installer`) : 158 mesures, 5 candidats (Glucksmann, Lisnard, Mélenchon, Philippe, Retailleau), 296 positions ; version `2026.11.12-test`, marqué « brouillon » (bandeau « données provisoires »). Alerte ajoutée si les réponses enregistrées ou des données locales ne correspondent plus au pack. Tous les tests passent. Saisie des 5 autres candidats en pause.|`a1ab527`|
|13/11/2026|Lot 7 : outil `comparer.py` (analyse comparative) + **note d'enseignements n°1** (`docs/enseignements/`) ; pack de test à **10 candidats** — les 5 sans positions (Attal, Le Pen, Riner, Roussel, Zemmour) sont hors classement et signalés « positions non encore saisies »|7198626|
|13/11/2026|Interface : consignes numérotées en tête du parcours — 1 thèmes prioritaires (facultatif), 2 avis et ★ essentielles, 3 classement et détail sourcé|76b9445|
|13/11/2026|Édition › Positions : ascenseur horizontal en haut du tableau, synchronisé avec celui du bas (masqué si le tableau tient en largeur)|00e5ee4|
|13/11/2026|Lot 7 : positions d'**Attal** (27, site attalpresident.fr trouvé), **Roussel** (27, plan Jeunesse + cahiers PCF), **Zemmour** (15, priorités) — 8 candidats, 365 positions ; Le Pen et Riner toujours sans source ; **note d'enseignements n°2**|46dd648|
|13/11/2026|Lot 7 : recherche **Le Pen / Riner confiée à Hermès** (rapport archivé, citations vérifiées) — site marinelepen.com trouvé, **Le Pen 15 positions** ; Riner sans position (3 pistes de presse seulement) ; 9 candidats, 380 positions ; **note d'enseignements n°3**|766a42d|
|13/11/2026|Lot 7 : **veille programmée chez Hermès par SSH** (file GLM) — consignes dans `docs/hermes/` : 18/11 (réforme des retraites de Le Pen, site de Riner), 23/11 (meeting de Zemmour à Toulon, site de Riner) ; ajout automatique à la file à 9 h ces jours-là ; tâche créée seule par Hermès depuis l'interface web supprimée|b2f267d|
|13/11/2026|Lot 7 : **couleurs des candidats** relevées dans le mode Édition et mises par défaut (choix de l'éditeur : tendance politique, remplace la palette neutre) ; **fiches complétées depuis Wikipédia** (date et lieu de naissance, âge calculé, formation, profession, lien vers l'article) ; **portraits libres** de Wikimedia Commons recadrés en 3:4 (`outils/portraits.py`, crédits sous chaque photo et dans les mentions légales) ; fiche au format uniforme (photo, identité, parcours, positions) et vignettes dans la liste|5d49d88|
|13/11/2026|**README.md en anglais** pour GitHub (présentation, principes, état, commandes, licences) ; lien croisé avec LISEZMOI.md|7b7f6ef|
|13/11/2026|**Captures d'écran dans le README** (accueil, questionnaire, candidats), dans docs/captures/|15dc162|
|13/11/2026|**LISEZMOI.md aligné sur README.md** : version française complète (captures, principes, état, organisation, commandes, contribution, licences)|fcf9681|
|13/11/2026|**Chapitre « Résultats - Méthode »** dans README.md et LISEZMOI.md : contenu de la page de résultats, calcul du score, exemple chiffré, origine des positions ; capture des résultats prise avec le pack de démonstration (candidats fictifs)|f0d33a9|
|13/11/2026|**Dépôt GitHub rendu public** à la demande de l'auteur (historique vérifié : adresses noreply seulement, aucun secret) ; README et LISEZMOI ne conditionnent plus la démo en ligne à la publication du dépôt|651d9c4|
|13/11/2026|**Première version publiée** (préversion v2026.11.13-test) : workflow « Version » (.github/workflows/release.yml) qui, à l'envoi d'une étiquette v<version du pack>, contrôle les données, construit l'archive ZIP et publie la release (préversion si « -test » ou « -demo ») avec le texte de docs/versions/<étiquette>.md ; liens de téléchargement vers /releases (la page /releases/latest ignore les préversions)|e6d4961|
|13/11/2026|**Démo en ligne publiée** sur GitHub Pages (source « GitHub Actions » activée ; workflow « Démo en ligne » lancé avec le pack de démonstration, candidats fictifs) : https://patrickdarbeau.github.io/pour-qui-voter/ ; adresse ajoutée au README et au LISEZMOI|fdcaba2|
|13/11/2026|**Lien vers le recensement des candidats** (docs/recensement_candidats.md) dans la section Documentation du README et du LISEZMOI|314121d|
|13/11/2026|**Recensement** : Christine Lagarde ajoutée aux pressentis (§D), absente de R27 et de Candidator, sources de presse Le Monde (06/11) et franceinfo (08/11)|a977071|
|13/11/2026|**README et LISEZMOI** : captures du radar (trois candidats les plus proches) et de la carte de chaleur (tous les candidats, thème par thème), rendu impression/PDF, pack de démonstration|bce3cff|
|13/11/2026|**README et LISEZMOI** : principe « Modifiable et personnalisable » (mode Édition : ajout, modification, suppression, export/import avec aperçu et sauvegarde) ; « Réutilisable » recentré sur les autres élections|à venir|
|—|**Prochaine étape : lot 7** — tests utilisateur du pack de test ; relecture des rapports de veille d'Hermès (18/11, 23/11) puis mise à jour des positions de Le Pen, Zemmour et Riner. Premier pack réel le 15/01/2027.||

\---

## 6\. Points de vigilance

* **Neutralité** : aucune mesure ne doit être formulée à l'avantage d'un candidat. En cas de doute, faire relire par une seconde personne.
* **Signalements d'erreur** (F40) : les traiter avant le pack suivant et les noter dans le journal.
* **Dates clés** : liste officielle des candidats (mars), premier tour le 18/04/2027, second tour le 02/05/2027.
* **Ne jamais** intégrer de réponses d'utilisateurs aux packs ou aux sources.

\---

## 7\. Décisions reportées et points à vérifier

|Sujet|État|À faire avant de lancer|Référence|
|-|-|-|-|
|**Dons**|Reporté (décision du 12/11/2026)|☐ Vérifier les frais réels de chaque plateforme retenue<br>☐ Vérifier le régime fiscal des dons reçus par un particulier (impots.gouv.fr)<br>☐ Vérifier l'absence de risque au regard du droit électoral ; en cas de doute, demander un avis à la CNCCFP<br>☐ Choisir les plateformes, créer les comptes, transmettre les liens|[DONS.md](DONS.md)|
|**Dépôt public, licence et responsabilité**|Licences choisies le 12/11/2026 ; passage en public vers le 08/01/2027|☑ Licences : EUPL 1.2 (code), CC BY-SA 4.0 (données)<br>☑ Mentions légales, limitation de responsabilité, politique de confidentialité<br>☐ Mentions légales : compléter l'éditeur (nom ou anonymat déclaré à l'hébergeur) et vérifier l'adresse de l'hébergeur<br>☐ Vérifier qu'aucun fichier personnel n'est présent<br>☐ **Nettoyer l'historique Git avant le passage en public** (tout l'historique devient visible) : retirer la note de travail supprimée sur la source d'inspiration et neutraliser les messages de commit qui la citent (réécriture + envoi forcé) — option recommandée parmi : ne rien changer / nettoyer / repartir d'un historique neuf<br>☐ Décider du nom affiché : « Patrick Darbeau » ou pseudonyme GitHub, dans les commits, les licences et les mentions légales|[LICENCES.md](LICENCES.md), [MENTIONS-LEGALES.md](../MENTIONS-LEGALES.md)|
|**Catalogue : équilibre des thèmes**|Reporté (décision du 12/11/2026)|☐ Ajouter des contrepoints aux thèmes déséquilibrés : Travail et emploi, Solidarités et pouvoir d'achat, Éducation et jeunesse, Numérique et libertés (5 mesures sans contrepoint chacun), puis Retraites et Institutions (4)<br>☐ Relancer `python outils/catalogue.py` et vérifier le bilan|[bilan_catalogue.md](bilan_catalogue.md), [methode_choix_mesures.md](methode_choix_mesures.md) (A5)|
|**Dates légales de la campagne**|À vérifier|☐ Date limite d'inscription sur les listes électorales 2027<br>☐ Début exact de la réserve électorale|[CAMPAGNE.md](promotion/CAMPAGNE.md)|



