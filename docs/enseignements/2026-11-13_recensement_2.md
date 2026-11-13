# Note d'enseignements n°2 — recherche complémentaire (Attal, Roussel, Zemmour, Le Pen, Riner)

**Date** : 13/11/2026 · **Lot** : 7 (étape 5, suite) · **Périmètre** : reprise de la recherche pour les 5 candidats restants ; 3 programmes saisis (Attal 27 positions, Roussel 27, Zemmour 15) ; 2 toujours sans source (Le Pen, Riner). Total : 8 candidats, 365 positions.
**Analyse chiffrée associée** : [2026-11-13_analyse_comparative_2.md](2026-11-13_analyse_comparative_2.md) (`python outils/comparer.py 2`). Note précédente : [n°1](2026-11-13_recensement_1.md).

---

## 1. Ce qui fonctionne

- **Relancer la recherche un jour plus tard paie** : le site de campagne d'Attal (attalpresident.fr) n'avait pas été trouvé le 12/11. Il a été trouvé le 13/11 en testant les noms de domaine plausibles (`gabrielattal2027.fr` redirige vers `attalpresident.fr`). Ses **mentions légales** (éditeur Renaissance, directeur de la publication Gabriel Attal) ont permis de confirmer qu'il est officiel.
- **Les liens des pages déjà archivées** mènent aux documents utiles : la page « Matériel » du site de Roussel donne le *Plan Jeunesse 2027-2032* ; le site du PCF donne ses cahiers thématiques.
- **Le contrôle `robots.txt` et la pause d'une seconde** ont été appliqués à chaque site (aucun refus cette fois).

## 2. Ce qui ne fonctionne pas

### 2.1 Programmes très inégalement publiés à cinq mois du scrutin

| Candidat | Ce qui est publié par la campagne | Positions | Couverture |
|---|---|---:|---:|
| Mélenchon | livre-programme complet | 111 | 70 % |
| Glucksmann, Philippe, Lisnard, Retailleau | programme thématique ou livret | 44–50 | 28–32 % |
| Attal | 96 mesures « annoncées » au fil de la campagne | 27 | 17 % |
| Roussel | manifeste + un plan sectoriel (jeunesse) | 27 | 17 % |
| Zemmour | 5 priorités en une page | 15 | 9 % |
| Le Pen, Riner | rien d'exploitable | 0 | — |

Le biais de couverture relevé dans la note n°1 s'aggrave : l'écart va désormais de 9 % à 70 %. **Le score sur les seules mesures exprimées (piste n°1 de la note n°1) devient indispensable avant toute diffusion.**

### 2.2 Recours au parti : équité à surveiller

- **Roussel** : 19 positions sur 27 viennent des *Cahiers thématiques des Jours heureux* du PCF (documents du parti, antérieurs à la campagne). Elles sont marquées « à confirmer » quand elles sont déduites ou anciennes. Le même traitement avait été appliqué à Glucksmann (Place publique) et Retailleau (LR) ; il faut l'écrire en règle (piste n°4 de la note n°1).
- **Zemmour** : aucun recours au parti. Le site de Reconquête ne publie pas de programme : il renvoie vers une **plateforme participative** (contributions de citoyens). Ces contributions n'engagent pas le candidat et n'ont pas été utilisées.

### 2.3 Pièges rencontrés

- **Domaine parqué** : `teddyriner2027.fr` est une page d'hébergeur, sans lien avec le candidat.
- **Site d'une campagne passée** : `mlafrance.fr` est le site de **2022** de Marine Le Pen (compte à rebours du second tour 2022). À exclure : le risque est de saisir un programme périmé, comme le PDF NFP 2024 de la note n°1.
- **Page « programme » morte** : `pcf.fr/le_programme` renvoie une page « non trouvée ».
- **Outil de recherche** : la recherche web intégrée était indisponible ; un autre moteur a servi. Les **agrégateurs** (votons-2027, monvote2027, poligraph, etc.) remontent en tête des résultats mais **n'ont pas été utilisés comme sources**, conformément à la règle « site officiel d'abord ».

### 2.4 Codage

- Taux « à confirmer » plus élevé que pour les 5 premiers : Roussel 15/27, Attal 13/27, Zemmour 7/15. Les programmes courts obligent à **déduire** (ex. « supprimer l'AME » → contre « maintenir l'AME »). Ces déductions sont signalées, mais la règle de codage reste à écrire.
- Plusieurs mesures du programme d'Attal (IA, géoénergie, protection de l'enfance, gens du voyage, cause animale, plan eau) **n'ont pas d'équivalent dans le catalogue** : même constat que dans la note n°1 pour les autres candidats.

## 3. Interprétation des résultats

À lire avec prudence : les taux reposent souvent sur moins de 15 mesures communes.

- **Les deux pôles se confirment** : Roussel s'aligne sur Mélenchon (100 % sur 23 mesures communes) et Glucksmann (100 % sur 10). Zemmour s'aligne sur Lisnard, Philippe et Retailleau (91–100 %, mais sur 3 à 11 mesures).
- **Attal se place au centre-droit du tableau** : 100 % d'accord avec Philippe (14 mesures), 86–92 % avec Retailleau et Lisnard, mais 64 % avec Glucksmann. Les points communs avec ce dernier : Mercosur, prix planchers agricoles, Europe.
- **Roussel et Zemmour n'ont aucune mesure commune** dans l'état actuel des données : le comparateur ne peut pas les situer l'un par rapport à l'autre.
- **15 consensus** (contre 8) : salaire des enseignants et refus des 64 ans à 7 candidats ; Mercosur, regroupement familial, peines planchers, prix planchers agricoles… Les consensus progressent mécaniquement quand on ajoute des candidats aux programmes courts, qui reprennent des thèmes très partagés.
- **Orphelines : 16** (contre 23). Restent orphelines notamment l'OTAN, le vote blanc, les amendes proportionnelles aux revenus et l'anonymat en ligne : le catalogue reste à revoir.

## 4. Pistes d'amélioration (complètent la note n°1)

| # | Piste | Priorité |
|---|---|---|
| 8 | **Veille hebdomadaire** des sites officiels (`python outils/maj.py collecter --decouvrir`) et test des noms de domaine plausibles pour les candidats sans site | Haute |
| 9 | **Seuil de publication** : n'afficher un candidat dans le classement qu'au-delà d'un minimum de positions (ex. 20) ou d'une couverture minimale, et l'indiquer clairement | Haute |
| 10 | Liste noire des **domaines trompeurs** (parqués, campagnes passées) dans la notice de collecte | Moyenne |
| 11 | Afficher sur chaque fiche la **nature de la source principale** (programme complet / plan sectoriel / priorités / parti) | Moyenne |

## 5. Suites

- **Le Pen** : collecter à la main les pages du RN (le site bloque les robots), ou attendre un site de campagne 2027.
- **Riner** : retrouver l'adresse du site « La France qu'on veut » (annoncé en ligne le 09/11/2026 par la presse, introuvable sous les noms testés).
- **Zemmour** : surveiller le meeting du 21/11/2026 (Toulon), annoncé comme lancement de campagne.
- Prochaine note : après Le Pen et Riner, ou après la révision du score et du catalogue.
