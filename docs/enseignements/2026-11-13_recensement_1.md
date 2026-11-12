# Note d'enseignements n°1 — premier recensement et saisie de 5 programmes

**Date** : 13/11/2026 · **Lot** : 7 (étapes 3 à 5 bis) · **Périmètre** : catalogue de 158 mesures (17 thèmes), 10 candidatures retenues, positions saisies pour 5 candidats (Glucksmann, Lisnard, Mélenchon, Philippe, Retailleau) — 296 positions, sources archivées le 12/11/2026.
**Analyse chiffrée associée** : [2026-11-13_analyse_comparative.md](2026-11-13_analyse_comparative.md) (`python outils/comparer.py`).

> Note de travail interne. Elle décrit la qualité de la méthode et des données, pas la valeur des programmes.

---

## 1. Ce qui fonctionne

- **La chaîne d'outils** : `catalogue.py` → `candidats.py` → `positions_<id>.py` → `positions.py` → `assembler.py` → `valider.py` produit un pack valide, testé, installable hors ligne. Chaque position porte une URL source et une citation courte : elle est vérifiable.
- **Le site officiel comme source principale** : quand il existe un programme détaillé (Mélenchon, Philippe, Glucksmann, Lisnard), la saisie est rapide et peu ambiguë.
- **L'archivage daté** des pages (`data/sources/AAAA-MM-JJ/`) permet de justifier une position même si la page change ensuite.
- **Le marquage « à confirmer »** isole les cas douteux au lieu de les masquer.
- **Le catalogue discrimine bien sur les grands clivages** : retraites, durée du travail, nucléaire, eau agricole, immigration, justice des mineurs. Sur ces mesures, les 5 candidats se répartissent nettement (voir § 3 de l'analyse).

## 2. Ce qui ne fonctionne pas (ou pas encore)

### 2.1 Couverture très inégale → biais de score

| | Mélenchon | les 4 autres |
|---|---:|---:|
| Mesures exprimées | 111 (70 %) | 44 à 50 (28 à 32 %) |

Le programme le plus détaillé est mécaniquement avantagé ou pénalisé : dans le calcul actuel, un silence vaut 0, ce qui **tire les candidats peu couverts vers 50 %** et rend les scores des programmes détaillés plus extrêmes (très haut ou très bas). Un utilisateur peut croire à une proximité « moyenne » qui n'est qu'un manque de données.

### 2.2 Catalogue mal ajusté aux programmes réels

- **23 mesures orphelines** (15 %) : aucun des 5 ne se prononce (OTAN, budget défense 3 %, vote blanc, amendes proportionnelles aux revenus, anonymat en ligne…). Elles ne départagent personne et allongent le questionnaire.
- **Propositions phares absentes du catalogue** : règle d'or budgétaire constitutionnelle et allocation familiale dès le 1er enfant (Philippe), réforme des droits de succession et plafonnement des aides à 70 % du SMIC (Retailleau), contribution climat sur les hauts patrimoines (Glucksmann), chèque-éducation (Lisnard), garantie d'autonomie des jeunes (Mélenchon), état d'urgence contre le narcotrafic (plusieurs). Le comparateur passe à côté de ce que les candidats mettent eux-mêmes en avant.
- **Mesures « miroirs »** (65 ans / 62 ans / 60 ans ; réguler / supprimer l'encadrement des loyers ; maintenir / supprimer le droit du sol…) : un même désaccord est compté deux ou trois fois. Cela gonfle les taux d'accord entre candidats d'un même bloc (96–98 %) et sur-pondère certains thèmes.
- **Thèmes déséquilibrés** en couverture : Solidarités (0 à 5 positions), Culture (0 pour 3 candidats), Europe (0 pour Mélenchon, ce qui est probablement une lacune de collecte et non une absence de position).

### 2.3 Sources hétérogènes

- **Candidat ou parti ?** Retailleau : documents des Républicains + tribunes ; Glucksmann : livret de campagne + texte de Place publique. Le niveau d'engagement n'est pas le même.
- **Dates** : certaines pages de Lisnard sont antérieures à la campagne 2027 ; Philippe a mis à jour son programme le 12/11/2026, le jour de la collecte.
- **Piège évité de justesse** : le PDF hébergé sur le site de Mélenchon était le programme NFP 2024, pas le programme 2027.

### 2.4 Codage des positions

- **64 positions sur 296 (22 %) « à confirmer »**, très inégalement réparties (Glucksmann 18, Retailleau 15, Lisnard 11, Mélenchon 10, Philippe 10).
- Le **« soutient en partie » (½)** est appliqué au cas par cas : il manque une règle écrite.
- **Positions déduites** : quand un candidat soutient A, on code parfois « contre » la mesure opposée B. C'est logique mais ce n'est pas une citation ; à signaler comme déduction.
- Quelques codages **surprenants à revérifier en priorité** (consensus ou clivage inattendu) : Lisnard « + » sur la suppression de Parcoursup, Retailleau « + » sur le RIC, Philippe « + » sur la « priorité nationale », Glucksmann « + » sur l'exécution systématique des OQTF.

### 2.5 Équité de traitement

- **Effort de recherche inégal** : il a fallu chercher des tribunes pour Retailleau, faute de programme consolidé ; les autres ont été saisis depuis une source unique.
- **5 candidats sans positions** : Attal, Le Pen, Riner (pas de programme publié), Roussel et Zemmour (différés). Les publier côte à côte avec des candidats complets serait trompeur sans signalement.
- **Pièges du web** : agrégateurs de candidatures peu fiables, domaines parqués au nom de candidats, site du RN bloquant les robots (collecte manuelle nécessaire).

## 3. Interprétation des résultats (analyse comparative)

À lire avec les réserves du § 2 : 5 candidats, couverture partielle, positions en brouillon.

- **Deux pôles nets** : Lisnard, Philippe et Retailleau sont d'accord à 96 % sur les mesures qu'ils partagent (26–27 mesures communes) ; Glucksmann et Mélenchon à 98 % (40 mesures communes). Entre les pôles, l'accord tombe à 11–42 %.
- **Glucksmann est le plus « transversal »** : 38 à 42 % d'accord avec Lisnard et Philippe, contre 11 à 18 % pour Mélenchon. Les points de passage concernent l'énergie (nucléaire et renouvelables), l'OQTF et certaines mesures d'éducation.
- **Philippe se distingue du pôle Lisnard/Retailleau** sur l'éolien et le solaire (pour), et sur la reconnaissance faciale (ciblée).
- **48 mesures clivantes**, concentrées sur les retraites, le travail, l'agriculture et l'eau, l'énergie, la justice et l'immigration. Ce sont celles qui « font » le résultat d'un utilisateur.
- **8 consensus**, dont 2 unanimes : la hausse du salaire des enseignants, et le refus de conserver l'âge légal à 64 ans (les uns veulent l'abaisser, les autres le relever). Les consensus apportent peu à la comparaison mais sont des repères utiles.
- **Ce que les chiffres ne disent pas** : l'intensité (une mesure phare vs une ligne en passant), le calendrier, le financement. Les taux de proximité élevés sont en partie gonflés par les mesures miroirs (§ 2.2).

## 4. Pistes d'amélioration proposées

| # | Piste | Effet attendu | Priorité |
|---|---|---|---|
| 1 | **Score calculé sur les seules mesures exprimées**, avec un **seuil de couverture** (ex. < 30 % des réponses de l'utilisateur couvertes → résultat signalé « peu fiable ») | Supprime l'avantage du programme le plus long | Haute, avant publication |
| 2 | **Révision du catalogue à partir des programmes** : retirer ou fusionner les orphelines, ajouter les propositions phares, regrouper les mesures miroirs en une seule question à curseur | Questionnaire plus court et plus pertinent | Haute |
| 3 | **Règles de codage écrites** (½, déduction, silence, position de parti) + relecture croisée des 64 « à confirmer » | Homogénéité | Haute |
| 4 | **Hiérarchie et datation des sources** : programme officiel du candidat > livret de campagne > parti > tribune/entretien ; date affichée sur chaque position | Transparence | Moyenne |
| 5 | **Procédure de recherche identique pour chaque candidat** (même liste de vérifications, même durée, mêmes types de sources) et compte rendu par candidat | Équité | Moyenne |
| 6 | **Afficher les candidats sans positions** à part, hors classement | Honnêteté du résultat | Fait dans ce lot |
| 7 | Contrôle de cohérence automatique : un candidat ne peut pas être « + » sur deux mesures miroirs incompatibles | Qualité | Basse |

## 5. Décisions et suites

- Les 10 candidats sont intégrés au pack de test ; les 5 sans positions sont **exclus du score** et listés à part (« positions non encore saisies »).
- Prochaine note : après la saisie des positions de Roussel et Zemmour, ou après la révision du catalogue.
