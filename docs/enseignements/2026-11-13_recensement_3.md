# Note d'enseignements n°3 — recherche confiée à Hermès (Le Pen, Riner)

**Date** : 13/11/2026 · **Lot** : 7 (étape 5, suite) · **Périmètre** : premiers sources et positions de Marine Le Pen (15 positions) ; Teddy Riner toujours sans position. Total : 9 candidats, 380 positions.
**Rapport brut d'Hermès** : [recherche_hermes_2026-11-13_lepen_riner.md](../recherche_hermes_2026-11-13_lepen_riner.md). **Analyse chiffrée** : [2026-11-13_analyse_comparative_3.md](2026-11-13_analyse_comparative_3.md) (`python outils/comparer.py 3`). Notes précédentes : [n°1](2026-11-13_recensement_1.md), [n°2](2026-11-13_recensement_2.md).

---

## 1. Ce qui fonctionne

- **Hermès apporte ce qui manquait** : en 12 minutes, il a trouvé le **site officiel de campagne marinelepen.com** (mentions légales : éditeur RN, directrice de la publication Marine Le Pen), que la recherche du 12/11 n'avait pas trouvé. Pour Riner, il a trouvé un indice sérieux : l'adresse de contact `contact@riner2027.fr` affichée sur le compte Instagram vérifié du candidat.
- **La consigne a été respectée** : hiérarchie des sources, agrégateurs exclus, pièges signalés (programme 2022 du RN, programme de gouvernement 2024, site `mlafrance.fr` de 2022), « non trouvé » écrit quand c'était le cas, points de vigilance sincères (chiffrages divergents entre journaux, transcription automatique d'un discours).
- **La vérification croisée par Claude a confirmé les citations utilisées** : bandeaux de la page d'accueil du RN, article franceinfo/AFP du 14/10/2026, article du Monde du 06/10/2026. Aucune citation inventée n'a été relevée sur les passages contrôlés.

## 2. Ce qui ne fonctionne pas

### 2.1 Canal utilisé

La consigne a d'abord été envoyée par l'**interface web** d'Hermès, ce qui contourne la **file GLM** (gestion du quota et priorité donnée aux autres projets). La file était vide et le quota à 0 %, donc sans conséquence cette fois. **Désormais : passer par SSH** (`ssh hermes`), avec une consigne écrite en fichier, une tâche créée en pause et ajoutée à la file, et un rapport écrit dans un fichier (procédure des skills Hermès). L'export de la session (`hermes sessions export … --format md`) a permis d'archiver le rapport.

### 2.2 Programmes absents ou indirects

| Candidat | Source principale | Nature | Positions |
|---|---|---|---:|
| Le Pen | bandeaux du site du RN + presse (contre-budget du 06/10, retraites du 14/10) | parti + **presse** | 15 (12 « à confirmer ») |
| Riner | entretien au *Parisien* repris par BFMTV, LCP, Ouest-France | **presse seulement** | 0 |

- **Le Pen** : le site de campagne ne contient qu'un formulaire de soutien. Les bandeaux du RN (TVA à 5,5 % sur l'énergie, RIC, nucléaire, retraite à 60 ans pour les carrières longues) reprennent des engagements déjà présents en 2022 ; ils sont affichés en contexte de campagne 2027, d'où leur prise en compte. Les autres positions viennent de la presse et sont toutes « à confirmer ».
- **Riner** : trois pistes seulement (assouplir les 35 h « sans les remettre en question », ne pas exclure une part de capitalisation, augmenter le salaire net par des allègements de charges). **Décision : aucune position saisie** — trois positions issues de la presse ne permettent pas un classement honnête. Le candidat reste affiché « positions non encore saisies ».
- **Site de Riner** : `riner2027.fr` répond par une erreur serveur (530) le 13/11 : le site existe probablement mais il est hors service. À revérifier.

### 2.3 Équité

Le Pen est le **premier candidat dont la majorité des positions vient de la presse**. La règle « source non officielle → à confirmer » a été appliquée (et vérifiée par un test automatique). Il faudra toutefois l'afficher clairement dans l'application (piste n°11 de la note n°2 : nature de la source sur chaque fiche).

## 3. Interprétation des résultats

- **Le Pen ne s'aligne nettement sur aucun bloc** : 55 à 73 % d'accord avec chacun des autres candidats, sur 6 à 11 mesures communes. Ses positions sur les retraites (retour à 62 voire 60 ans, contre le maintien à 64 ans) la rapprochent de la gauche ; celles sur l'immigration (priorité nationale), le nucléaire et la fiscalité du patrimoine la rapprochent de la droite. Seul Zemmour atteint 100 %, mais sur 4 mesures seulement.
- Ce résultat illustre une **limite de la mesure « accord / désaccord »** : avec peu de mesures communes, un candidat peut paraître « central » simplement parce que ses positions connues se répartissent sur des thèmes différents. Le nombre de mesures communes doit toujours être lu avec le taux.
- **Consensus renforcés** : le refus de conserver l'âge légal à 64 ans réunit maintenant 8 candidats ; le RIC en réunit 5 (Attal, Glucksmann, Le Pen, Mélenchon, Retailleau).

## 4. Pistes d'amélioration (complètent les notes n°1 et n°2)

| # | Piste | Priorité |
|---|---|---|
| 12 | **Hermès par SSH et file GLM** pour toute recherche : consigne en fichier dans le dépôt, rapport en fichier, vérification par Claude avant saisie | Haute |
| 13 | **Revérification programmée** : réforme des retraites de Le Pen (17/11/2026), site de Riner (riner2027.fr), meeting de Zemmour (21/11/2026) | Haute |
| 14 | Dans l'application, signaler les positions issues de la **presse** (badge distinct de « à confirmer ») | Moyenne |

## 5. Suites

- **Veille confiée à Hermès par SSH (fait le 13/11)** : consignes [18/11](../hermes/consigne_veille_2026-11-18.md) (retraites de Le Pen, site de Riner) et [23/11](../hermes/consigne_veille_2026-11-23.md) (meeting de Zemmour, site de Riner). Les tâches sont créées en pause (GLM 5.3) et une ligne de crontab de la VM les ajoute à la file GLM à 9 h ces jours-là ; elle s'efface ensuite. Livrables attendus dans `~/workspace/Projets/pour-qui-voter/` sur la VM, à vérifier par Claude avant toute saisie.
- **Constat** : lors de la recherche du 13/11 par l'interface web, Hermès avait **programmé seul** une revérification pour le 18/11, hors file GLM et sans modèle fixé. Elle a été mise en pause (tâche `a67c43e0fa8c`) et remplacée. Les consignes interdisent désormais à Hermès de créer des tâches.
- Riner : saisir ses positions dès qu'un programme ou un site est publié.
