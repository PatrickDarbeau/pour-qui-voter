# Note d'enseignements n°5 — positions des six candidats ajoutés (relevés d'Hermès)

**Date** : 14/11/2026 · **Lot** : 7 (étape 5, suite) · **Périmètre** : positions de Nathalie Arthaud, François Asselineau, Nicolas Dupont-Aignan, Florian Philippot, François Ruffin et Marine Tondelier, relevées par Hermès (consigne `docs/hermes/consigne_positions_2026-11-14.md`), puis vérifiées et saisies par Claude. Total : 16 candidats, dont 15 classés (773 positions) ; Teddy Riner reste sans position (relevé hebdomadaire en cours).
**Analyse chiffrée** : [2026-11-14_analyse_comparative_5.md](2026-11-14_analyse_comparative_5.md) (`python outils/comparer.py 5`). Note précédente : [n°4](2026-11-13_recensement_4.md).

---

## 1. Ce qui fonctionne

- **La file GLM a enchaîné les six relevés sans intervention** (00:20 → 03:10), en respectant le quota (0 % → 42 % de la tranche de 5 h).
- **Vérification automatique des citations** : un script télécharge chaque source (pages HTML et PDF) et cherche chaque citation mot pour mot, après normalisation de la typographie (apostrophes, guillemets, césures de fin de ligne des PDF). Sur 412 positions proposées, **393 sont retenues** avec une citation retrouvée dans sa source.
- **Sources officielles d'abord** : 380 positions viennent de documents de campagne ou de parti (programmes PDF, livrets, sites), une poignée de la presse. Aucun agrégateur.
- **Les fichiers de positions sont générés** (`outils/positions_<id>.py`), avec la date de consultation propre au candidat et le type de source (programme PDF, site officiel, presse) ; `outils/positions.py` accepte désormais ces deux informations.

| Candidat | Proposées | Retenues | À confirmer | Écartées | Source principale |
|---|---:|---:|---:|---:|---|
| Arthaud | 33 | 31 | 23 | 2 | brochure de campagne (juin 2026), dépliant (nov. 2026), fiches de Lutte ouvrière |
| Asselineau | 23 | 23 | 5 | 0 | upr.fr (Frexit, discours de rentrée 2026) ; programme 2027 « en cours d'élaboration » |
| Dupont-Aignan | 89 | 85 | 4 | 4 | livrets thématiques de Debout la France (2025-2026) |
| Philippot | 67 | 67 | 14 | 0 | livret « Projet pour la France » (sept. 2026), charte des Patriotes |
| Ruffin | 57 | 56 | 20 | 1 | cahiers de nouspresident.fr (9 cahiers, 3 plans) |
| Tondelier | 131 | 131 | 28 | 0 | programme des Écologistes (208 p., 557 mesures), livrets de campagne |

## 2. Ce qui ne fonctionne pas ou reste fragile

### 2.1 Robustesse de la veille

- **La tâche de Marine Tondelier a échoué** (erreur de l'agent, sans détail). L'échec a **arrêté le flux pqv** dans la file GLM, ce qui aurait bloqué le relevé de Teddy Riner prévu à 07:00. Relance manuelle à 05:27, réussie à 06:10.
- **Le rattrapage ne couvre pas les échecs** : `pqv_hebdo.sh` considère un candidat comme traité dès que sa tâche est en file, même si elle échoue ensuite. À corriger : relancer automatiquement une tâche terminée sans livrable, et reprendre le flux pqv après un échec isolé.

### 2.2 Citations écartées (vérification)

- **Dupont-Aignan** : eco10 et san7, citations introuvables dans la source indiquée (san7 renvoyait à la page d'accueil du site, dont le contenu change) ; retr1 et retr4, article du *Monde* payant, donc non vérifiable.
- **Ruffin** : agri2, déduction sans aucun passage cité. Sept autres déductions reprennent le passage d'une mesure voisine (« idem eco1 », « miroir d'imm4 ») : retenues, marquées « à confirmer ».
- **Fausses alertes corrigées** : les césures de fin de ligne des PDF (« démo-/lissent ») et un mauvais décodage des accents sur certaines pages faisaient échouer la vérification ; puis la suppression des traits d'union de fin de ligne cassait les mots composés (« libre-/échange »). Six citations ont été contrôlées à l'œil et retenues.
- **Coquille de la source** : Debout la France écrit « l'installations des éoliennes » ; la citation saisie suit la source à la lettre.

### 2.3 Interprétation et équité

- **Positions déduites nombreuses chez Arthaud** (23 sur 31) : Lutte ouvrière ne présente pas de programme électoral (« un programme révolutionnaire à imposer par les luttes »). Hermès a donc souvent conclu d'un principe général. Ces positions sont marquées « à confirmer ».
- **Renvoi dos à dos ≠ position** : Hermès notait Arthaud « s'oppose » à la fois à l'accord avec le Mercosur et au refus de cet accord, parce que Lutte ouvrière renvoie dos à dos libre-échange et protectionnisme. Les deux valeurs ont été retirées (« ne se prononce pas »). **Règle proposée** : quand un candidat rejette les deux termes d'une alternative, ne pas noter de position. À appliquer à tous.
- **Couverture très inégale** : Tondelier 83 % et Dupont-Aignan 54 %, contre Asselineau 15 % (programme 2027 non publié, l'UPR renvoie de nombreux sujets à un choix « après le Frexit »). Le score de proximité ne porte que sur les mesures où l'électeur et le candidat se prononcent tous deux, mais un candidat peu couvert peut obtenir un score élevé sur peu de mesures.
- **Taux d'accord sur de petits effectifs** : l'analyse affiche par exemple 100 % d'accord entre Asselineau et Mélenchon, sur 14 mesures communes seulement. Ces chiffres ne disent rien de la proximité générale de deux candidats.
- **Candidature de Marine Tondelier** : le vote des adhérents des Écologistes (10-13 décembre 2026) décidera de son maintien ou d'un ralliement. À suivre au recensement.

## 3. Pistes

1. Rendre le rattrapage robuste aux échecs (relance d'une tâche sans livrable, reprise du flux pqv) — à valider par l'éditeur, puisque cela modifie la veille.
2. Écrire la règle « renvoi dos à dos » dans la consigne d'Hermès et dans la méthode, puis l'appliquer aux 15 candidats.
3. Relire en priorité les positions « à confirmer » d'Arthaud et de Ruffin.
4. Intégrer le script de vérification des citations au dépôt (`outils/`), pour le relancer à chaque relevé.
