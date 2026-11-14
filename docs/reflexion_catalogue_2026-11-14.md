# Note de réflexion — le catalogue des mesures après les premiers relevés

*Note de travail du 14/11/2026, rédigée par Claude à la demande de l'éditeur, après la saisie des positions des 16 candidats (777 positions, pack 2026.11.13-test.3). Elle fait suite à la note de méthode du 12/11/2026 : [methode_choix_mesures.md](methode_choix_mesures.md). **Rien n'est encore modifié** : les propositions de la partie 5 attendent la décision de l'éditeur.*

---

## 1. Comment les mesures ont été choisies (rappel)

Le catalogue compte **158 mesures réparties en 17 thèmes**, rédigées le 12/11/2026 (`outils/catalogue.py`).

- **Point de départ** : les 20 mesures du jeu de démonstration, les 17 thèmes validés, une cible de 8 à 10 mesures par thème.
- **Question posée pour chaque thème** : *sur quoi les partis et les candidats s'opposent-ils régulièrement ?* La réponse s'appuie sur la connaissance générale du débat public jusqu'à mi-2026 (programmes de 2022, élections de 2024, réformes et controverses récentes), et non sur les programmes de 2027, encore inexistants.
- **Règles** : formulation neutre (aucun nom de parti, aucun adjectif qui juge) ; une seule idée par mesure ; un chiffre quand c'est possible ; pour chaque débat clivant, l'option opposée ou le statu quo, reliés par le champ `opposee_a` ; quelques mesures consensuelles, qui mesurent les priorités plus que les clivages.
- **Origine** : 121 mesures rédigées pour le catalogue, 17 contrepoints ajoutés pour l'équilibre, 20 reprises de la démonstration. On compte 49 paires opposées et 59 mesures sans contrepoint.

Ni le README ni la FAQ de l'application n'expliquent aujourd'hui ce choix.

---

## 2. Où se loge la subjectivité

Le catalogue n'est pas neutre « par construction » : il est le résultat de choix. On peut les rendre explicites et vérifiables, pas les supprimer.

| Étape | Nature du choix | Effet possible |
|---|---|---|
| **Choix des débats** | Quels sujets entrent, lesquels restent dehors ; combien de mesures par thème | Un candidat dont les propositions phares sont absentes paraît « peu couvert », ou mal classé |
| **Seuils chiffrés** | « SMIC +10 % », « enseignants +15 % », « 150 000 logements sociaux » | Un candidat qui propose un autre montant n'est, à la lettre, ni pour ni contre ; la correspondance devient une interprétation |
| **Formulation** | Choix des mots, du statu quo, de l'ordre des paires | Une mesure peut sembler neutre à son auteur et orientée à un lecteur d'une autre sensibilité |
| **Correspondance position ↔ mesure** | « Soutient en partie », « déduite », « à confirmer » | Jugement d'Hermès, puis de Claude ; reproductible seulement si les règles sont écrites |
| **Poids** | Toutes les mesures pèsent 1 par défaut | Un thème à 12 mesures pèse plus qu'un thème à 9 dans un score sans priorités |

---

## 3. Ce que montrent les données (16 candidats, 777 positions)

### 3.1 Des mesures qui ne départagent personne

- **3 mesures orphelines**, sans aucune position : vérification d'identité sur les réseaux sociaux, droit à l'anonymat en ligne, publication des rémunérations des hauts fonctionnaires.
- **26 mesures** n'ont qu'une ou deux positions, dont plusieurs paires entières : légitime défense des policiers, contrôle de la police, amendes routières selon les revenus, révocation du président par RIC, RSA et activité.
- **Mesures quasi unanimes** : « Conserver l'âge légal à 64 ans » (12 candidats contre, aucun pour), « Augmenter le salaire des enseignants de 15 % » (11 pour), « Instaurer le RIC » (10 pour), « S'opposer à l'accord avec le Mercosur » (9 pour). Elles n'influent pas sur le classement relatif des candidats ; elles restent utiles à l'électeur pour exprimer une priorité.
- **Doute sur une unanimité** : 11 candidats « pour » un chiffre aussi précis que « +15 % » laisse penser que des propositions différentes (montant autre, revalorisation non chiffrée) ont été rattachées trop largement. À vérifier.

### 3.2 Des débats absents

Les relevés d'Hermès contiennent une section « Propositions hors catalogue ». Plusieurs débats y reviennent chez plusieurs candidats :

| Débat absent | Candidats qui le portent (relevés du 14/11) | Remarque |
|---|---|---|
| Sortie de l'euro, Frexit direct | Asselineau, Philippot | Le catalogue n'a qu'un « référendum sur la sortie de l'UE » (eu3) |
| Impôt minimal sur les très hauts patrimoines (« taxe Zucman ») | Ruffin, Tondelier | Distinct de l'ISF (eco1) et de l'impôt lié à la nationalité (eco3) |
| Préférence pour les produits français dans la commande publique (« Buy French Act ») | Dupont-Aignan, Ruffin | Débat transpartisan, absent du catalogue |
| Suppression du Sénat ou des régions, réduction du nombre d'élus | Asselineau, Philippot | Le thème Institutions n'en parle pas |
| Prix de l'électricité, tarif réglementé | Dupont-Aignan, Philippot | Les mesures ecl5 à ecl8 portent sur le marché, pas sur le prix |
| Fin de la vente des voitures thermiques neuves en 2035 | Philippot | Débat européen récurrent |
| Peine de mort (référendum sur son rétablissement) | Dupont-Aignan | Sujet sensible : à traiter avec un contrepoint strict |
| Dépénalisation de l'usage de toutes les drogues | Tondelier | Le catalogue ne traite que du cannabis (sec8) |
| SMIC nettement plus élevé (2 000 € ou 2 200 € net) | Arthaud, Tondelier | Le seuil « +10 % » ne distingue pas ces propositions |

Cette liste est **partielle** : elle ne couvre que les sept candidats relevés le 14/11. Les relevés « complément » des neuf autres candidats (à partir du 21/11) la compléteront.

### 3.3 Des paires opposées qui piègent la saisie

- **Renvoi dos à dos** : Lutte ouvrière rejette à la fois le libre-échange et le protectionnisme. Hermès a noté Nathalie Arthaud « s'oppose » aux deux mesures de la paire Mercosur (agri4 et agri5), ce qui la faisait paraître favorable à l'accord. Les deux valeurs ont été retirées le 14/11.
- **Contrepoint mal symétrique** : certaines paires ne s'excluent pas vraiment (« répartition uniquement » contre « part de capitalisation » : Teddy Riner défend la répartition sans exclure la capitalisation). Une position « en partie » sur l'une n'implique rien sur l'autre.

### 3.4 Des faits datés non vérifiés

Les statu quo cités (âge légal de 64 ans, IFI, aide médicale d'État, droit du sol à Mayotte, etc.) reposent sur une connaissance arrêtée à mi-2026. Ils n'ont pas encore été contrôlés sur des sources officielles (amélioration A2 de la note de méthode).

### 3.5 Pas encore de relecture croisée

La relecture de neutralité par au moins deux personnes de sensibilités différentes (amélioration A1) n'a pas été faite. C'est la principale faiblesse du catalogue avant le pack réel du 15/01/2027.

---

## 4. Limites qu'il faut accepter et dire

- **Un questionnaire ne résume pas un programme** : 158 mesures, même bien choisies, ne rendent compte ni de la cohérence d'un projet, ni de la crédibilité d'un candidat, ni de sa personnalité, ni de ses alliances.
- **Couverture inégale** : de 3 % (Riner, programme non publié) à 83 % (Tondelier). Le score de concordance ne porte que sur les mesures où le candidat a une position : un candidat peu couvert peut obtenir un score élevé sur peu d'éléments. L'application affiche la couverture, mais l'écart est grand.
- **Le catalogue évolue pendant la campagne** : chaque ajout ou retrait change les scores. Il faut le dire, et le tracer.
- **L'outil reste modifiable** : en mode Édition, chacun peut changer les mesures. C'est une réponse partielle à la subjectivité (« faites votre propre catalogue »), pas une garantie de neutralité du catalogue officiel.

---

## 5. Propositions (à décider par l'éditeur)

### A. Le catalogue, avant le pack réel du 15/01/2027

| # | Proposition | Effet attendu |
|---|---|---|
| A1 | Ajouter **environ 8 paires** pour les débats absents (§3.2), chacune avec son contrepoint | Couvrir les propositions phares de tous les bords ; environ 174 mesures |
| A2 | **Remplacer les seuils rigides** par l'objectif, avec le chiffre en description (ex. « Augmenter nettement le SMIC », description : « au moins +10 % ») et écrire la règle : montant inférieur = « en partie », montant supérieur = « soutient » | Correspondance moins arbitraire, résultat plus juste pour les candidats qui chiffrent autrement |
| A3 | **Garder les mesures orphelines jusqu'au 15/01**, puis les retirer ou les fusionner si elles le restent | Ne pas retirer trop tôt un sujet que les programmes n'ont pas encore abordé |
| A4 | **Plafonner à 10 mesures par thème** (12 pour Institutions), en compensant les ajouts par des retraits | Éviter qu'un thème pèse plus qu'un autre par simple nombre de mesures |
| A5 | Revérifier la paire « enseignants +15 % » et les autres unanimités suspectes | Corriger les rattachements trop larges |

### B. Les règles et la méthode

| # | Proposition |
|---|---|
| B1 | **Règle d'entrée d'une mesure** : proposée par au moins deux candidats de partis différents, ou proposition phare d'un candidat, toujours assortie d'un contrepoint. Règle de sortie : orpheline au moment d'un pack réel. |
| B2 | **Règles de saisie écrites, identiques pour tous** : « renvoi dos à dos = pas de position » ; « seuil chiffré » (A2) ; « déduite d'un principe général = à confirmer » (déjà appliquée). À intégrer à la consigne d'Hermès. |
| B3 | **Relecture de neutralité croisée** (au moins deux relecteurs de sensibilités différentes) avant le 15/01/2027, avec une grille simple : formulation neutre ? contrepoint juste ? fait vérifié ? |
| B4 | **Vérifier chaque statu quo** sur Légifrance, service-public.fr ou vie-publique.fr, avec la date de vérification. |
| B5 | **Compiler chaque semaine les propositions « hors catalogue »** des relevés d'Hermès, pour décider des ajouts sur une base objective (nombre de candidats, diversité des bords). |
| B6 | **Tracer chaque changement du catalogue** dans le journal du pack (déjà prévu par `maj.py publier`). |

### C. Le README et la FAQ

| # | Proposition |
|---|---|
| C1 | Ajouter au README (et au LISEZMOI) une section **« Comment les mesures ont été choisies »** : origine, règles, part de subjectivité, limites, lien vers la note de méthode et vers cette note. |
| C2 | Ajouter à la FAQ de l'application trois questions : **« Comment les mesures ont-elles été choisies ? »**, **« Pourquoi telle proposition n'y figure-t-elle pas ? »** (avec un renvoi vers les tickets pour la proposer), **« Que veulent dire "soutient en partie" et "à confirmer" ? »** |
| C3 | Dire clairement, dans les deux, que le **catalogue évolue pendant la campagne** et que chaque changement est tracé. |

### Ordre suggéré

1. C (README et FAQ) : immédiat, sans effet sur les scores.
2. B2 (règles de saisie) : rapide, et utile dès les relevés du 21/11.
3. A1, A2, A5 : avant la fin novembre, pour que les relevés de décembre portent sur le catalogue révisé.
4. B3, B4 : avant le pack réel du 15/01/2027.
5. A3, A4 : au moment du pack réel.
