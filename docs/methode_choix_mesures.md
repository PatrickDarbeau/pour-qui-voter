# Note — Méthode de choix des mesures et améliorations possibles

*Note de travail du 12/11/2026 (lot 7, étape 2).* Elle accompagne le brouillon du catalogue : [catalogue_mesures.md](catalogue_mesures.md), dont la source est `outils/catalogue.py`.

---

## 1. Point de départ

- Les **20 mesures du jeu de démonstration**, jugées pertinentes.
- Des **propositions publiques soumises au débat**, reprises comme idées et **reformulées de façon neutre**, sans en citer la source.
- Les **17 thèmes** validés (voir [lot_7_pas_a_pas.md](lot_7_pas_a_pas.md) §2).
- L'objectif : **8 à 10 mesures par thème**, soit 136 à 170 mesures au total. Le brouillon en compte **158**.

---

## 2. Méthode

### 2.1 Repérer les grands débats de chaque thème
Pour chaque thème, une question : *sur quoi les partis et les candidats français s'opposent-ils régulièrement ?*
La réponse s'appuie sur la connaissance générale du débat public jusqu'à mi-2026 : programmes de 2022, élections européennes et législatives de 2024, réformes récentes et controverses.

Exemples :
- **Retraites** : l'âge légal (60, 62, 64 ou 65 ans) et le mode de financement (répartition ou capitalisation) ;
- **Santé** : les déserts médicaux, l'aide médicale d'État, la fin de vie ;
- **Immigration** : le droit du sol, les régularisations, la « priorité nationale ».

### 2.2 Règles appliquées
| Règle | Mise en œuvre |
|---|---|
| **Les deux options de chaque débat clivant** | Quand une mesure correspond à une sensibilité, on ajoute l'option opposée ou le statu quo, reliées par le champ `opposee_a` (↔). Un candidat de n'importe quel bord trouve ainsi des mesures qu'il soutient et d'autres qu'il rejette. |
| **Couverture de tout l'éventail politique** | De la gauche radicale à la droite nationale. Exemples : semaine de 32 heures face à durée du travail fixée par accord, RIC face à statu quo, sortie de l'OTAN face à maintien. |
| **Mesures concrètes et vérifiables** | Avec des chiffres quand c'est possible : « 150 000 logements sociaux par an », plutôt que « plus de logements ». |
| **Formulation neutre** | Aucun nom de parti ou de candidat, aucun adjectif qui juge. Les expressions reprises du débat sont entre guillemets, par exemple « priorité nationale ». |
| **Une seule idée par mesure** | Pour que l'électeur puisse se prononcer clairement. |
| **Quelques mesures consensuelles** | Sans contrepoint (eau potable outre-mer, caméra-piéton) : elles mesurent les priorités plus que les clivages. |

### 2.3 Origine des mesures (brouillon du 12/11/2026)
| Origine | Nombre |
|---|---|
| Rédigées pour le catalogue | 121 |
| Contrepoints ajoutés pour l'équilibre | 17 |
| Reprises du jeu de démonstration | 20 |
| **Total** | **158** |

---

## 3. Limites connues

- **Une sélection subjective** : d'autres débats auraient pu être retenus, et l'ordre ou le poids des sujets reflète un choix.
- **Des connaissances arrêtées à mi-2026** : certains statu quo cités (âge de 64 ans, impôt sur la fortune immobilière, aide médicale d'État, droit du sol à Mayotte…) ont pu évoluer. **Ils sont à vérifier.**
- **Un choix pas encore confronté aux vrais programmes de 2027** : certaines mesures pourraient n'être portées par aucun candidat, et des propositions phares pourraient manquer.
- **Un équilibre inégal selon les thèmes** : certains thèmes ont surtout des paires opposées, d'autres surtout des mesures sans contrepoint.
- **Des formulations perfectibles** : une mesure peut paraître neutre à son auteur sans l'être pour un lecteur d'une autre sensibilité.

---

## 4. Améliorations possibles

### 4.1 Avant le premier pack réel (15/01/2027)
| # | Amélioration | Comment | Étape du lot 7 |
|---|---|---|---|
| A1 | **Relecture de neutralité croisée** | Au moins deux relecteurs de sensibilités différentes, avec une grille simple : formulation neutre ? contrepoint juste ? | 2 |
| A2 | **Vérifier les faits cités** | Contrôler chaque statu quo sur des sources officielles (Légifrance, service-public.fr, vie-publique.fr) | 2 |
| A3 | **Confronter le catalogue aux programmes réels** | Pour chaque candidat recensé, lister ses 10 propositions phares et vérifier qu'elles figurent dans le catalogue ; sinon, ajouter une mesure et son contrepoint | 3 à 5 |
| A4 | **Retirer les mesures orphelines** | Une mesure qu'aucun candidat ne porte, ni pour ni contre, est retirée ou fusionnée | 6 |
| A5 | **Équilibrer les thèmes** | Viser au moins une paire opposée par thème, et compléter les mesures sans contrepoint quand le débat existe (cantine gratuite, musées gratuits…) | 6 |
| A6 | **Croiser avec des comparateurs existants** | Vérifier qu'aucun grand débat n'est oublié, en reformulant toujours avec nos propres mots et sans reprendre leurs listes | 3 |

### 4.2 Pendant la campagne
| # | Amélioration | Comment |
|---|---|---|
| B1 | **Suivre l'actualité des programmes** | À chaque pack hebdomadaire, ajouter les nouvelles propositions marquantes (avec leur contrepoint) et retirer celles qui sont abandonnées |
| B2 | **Exploiter les signalements** | Les remarques des utilisateurs sur une formulation jugée orientée sont examinées en priorité |
| B3 | **Tracer chaque changement** | Toute modification d'une mesure figure dans le journal du pack (`maj.py publier`) |

### 4.3 Améliorations de l'outil (facultatives)
| # | Amélioration | Intérêt |
|---|---|---|
| C1 | **Fiche de relecture générée automatiquement** | Un tableau par thème avec des cases « neutre ? / contrepoint ? / fait vérifié ? », à remplir par chaque relecteur |
| C2 | **Indicateur d'équilibre dans `valider.py`** | Alerte si un thème n'a aucune paire opposée, ou si un candidat n'a des positions que sur une minorité de thèmes |
| C3 | **Champ « statu quo » vérifié** | Marquer les mesures qui décrivent la situation actuelle, avec la date et la source de vérification |
| C4 | **Statistiques de couverture par candidat et par thème** | Visualiser les déséquilibres de recherche avant chaque publication |

---

## 5. Décisions déjà prises

- Pas de référence à des sources d'inspiration externes dans le catalogue : les mesures sont reformulées et neutres (12/11/2026).
- Pack de démonstration conservé à part : `data/demo/donnees-demo.json`.
