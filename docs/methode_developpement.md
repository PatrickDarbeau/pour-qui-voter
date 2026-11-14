# Comment ce projet est fabriqué — méthode de développement et rôle de chacun

*Note de transparence, 14/11/2026. « Pour qui voter ? » est développé avec l'aide de deux intelligences artificielles. Cette note explique qui fait quoi, ce que l'IA apporte, ce qu'elle ne fait pas, et où se situent l'imagination et les décisions humaines. Elle sera mise à jour si la méthode change.*

---

## 1. Les trois intervenants

| | **Le développeur** (éditeur du projet) | **Claude** (Opus 5.5, Anthropic) | **Hermès** (agent de recherche, modèle GLM 5.3, Z.ai) |
|---|---|---|---|
| **Nature** | Une personne | Assistant de programmation (Claude Code), qui travaille dans le dossier du projet sur l'ordinateur du développeur | Agent autonome installé sur une machine virtuelle du développeur, piloté par Claude |
| **Rôle en une phrase** | Il imagine, décide et assume | Il conçoit, écrit, vérifie et coordonne | Il cherche et relève |
| **Responsabilité** | Totale : contenu publié, neutralité, choix éditoriaux ; mais il ne peut pas tout contrôler lui-même (voir §3) | Qualité technique et exactitude de ce qu'il produit, sous contrôle du développeur | Aucune décision : ses livrables sont des brouillons, tous revérifiés |

---

## 2. Ce que fait chacun

### Le développeur — imagination et arbitrage

- **L'idée et l'intention** : un comparateur gratuit, neutre, **hors ligne**, qui ne collecte aucune donnée, et que chacun peut **modifier**.
- **Les principes non négociables** : neutralité, transparence des sources, aucune requête réseau, vie privée, licence libre.
- **Les choix de contenu** : les thèmes, la liste des candidats retenus et suivis, la date limite proposée aux équipes de campagne.
- **Les arbitrages éditoriaux** : il retient, refuse ou remplace les propositions de Claude (mesures, règles, organisation du catalogue).
- **Les décisions de publication** : rendre le dépôt public, publier une préversion, lancer la démo en ligne. Aucune publication ne se fait sans son accord.
- **Les questions qui orientent le travail** : « Comment les mesures ont-elles été choisies ? Part de subjectivité ? Limites ? » Ce sont ses questions qui ont conduit à écrire la méthode, les règles de saisie et cette note.
- **Le contrôle** : il relit, refuse, corrige, et peut à tout moment changer de direction.
- **Les limites de ce contrôle** : il ne peut pas tout vérifier lui-même. Relire chaque ligne de code, rouvrir chaque source et recontrôler chaque position demanderait des moyens coûteux en temps et en effectifs, hors de portée d'un projet porté par une seule personne. Il accorde donc à l'IA une **confiance assumée**, encadrée par des règles écrites, des vérifications automatiques et une traçabilité complète (voir §3 et §5).

### Claude (Opus 5.5) — conception, écriture, vérification

- **Le code** : l'application (HTML, CSS, JavaScript sans dépendance), le calcul du score, le mode Édition, l'export PDF, les outils en Python (validation, assemblage des packs, comparaison, paquet ZIP), les tests, les workflows de publication.
- **Les documents** : README, notice du développeur, méthode, notes d'enseignements après chaque relevé, note aux candidats.
- **Le brouillon du catalogue** : les 172 mesures et leurs contrepoints, rédigés selon des règles écrites, puis **soumis au développeur**.
- **La coordination d'Hermès** : il rédige ses consignes, programme ses tâches, surveille leur exécution, relance une tâche en échec et rapatrie ses livrables.
- **La vérification** : chaque citation proposée par Hermès est **retrouvée mot pour mot dans sa source**, page web ou PDF, par un script avant d'être saisie. Le 14/11/2026, sur 412 positions proposées, 393 ont été retenues et 19 écartées.
- **L'analyse critique de son propre travail** : les notes d'enseignements et la note de réflexion sur le catalogue relèvent ses erreurs et les limites de la méthode.
- **Ce qu'il ne fait pas seul** : publier, ajouter un candidat, modifier la veille d'Hermès, saisir un mot de passe, trancher une question éditoriale. Il propose ; le développeur décide.

### Hermès (GLM 5.3) — recherche documentaire

- **Le relevé des positions** : pour chaque candidat, il cherche le site de campagne, le programme et le site du parti, puis relève la position du candidat sur chaque mesure, avec une citation de moins de 30 mots, l'URL et la date.
- **La veille hebdomadaire** : chaque samedi à 07:00, il relève les candidats suivis et, par rotation, complète ceux déjà saisis. Une tâche manquée est rattrapée dès que possible.
- **Les propositions hors catalogue** : il signale les propositions importantes qui ne correspondent à aucune mesure. C'est l'origine des 7 paires de mesures ajoutées le 14/11.
- **Ses limites, constatées** :
  - une tâche a échoué sans explication ;
  - certaines citations étaient tronquées ;
  - il a conclu à tort qu'une candidate « s'opposait » aux deux options d'un même débat ;
  - des rattachements à des mesures chiffrées étaient trop larges.

  C'est pourquoi **rien de ce qu'il produit n'est saisi sans un minimum de vérification**.

---

## 3. En parallèle : l'IA et l'humain

| Domaine | Ce que l'IA apporte | Ce que le développeur apporte |
|---|---|---|
| **Idée** | — | L'idée du comparateur, son public, son esprit (civique, gratuit, hors ligne) |
| **Principes** | Leur traduction technique (aucune requête réseau, politique de sécurité du contenu, tests hors ligne) | Leur choix : neutralité, vie privée, transparence, liberté de modifier |
| **Catalogue des mesures** | Un brouillon complet et équilibré, des règles de rédaction, des propositions d'ajouts motivées | Le choix des thèmes, la validation, le refus ou le remplacement de chaque proposition |
| **Positions des candidats** | La recherche (Hermès), puis la vérification mot pour mot et la saisie (Claude) | Les règles d'arbitrage à appliquer à tous, la relecture finale |
| **Code et tests** | L'écriture, les tests, la correction des erreurs | Les demandes d'évolution, l'essai en conditions réelles |
| **Documentation** | La rédaction, en français et en anglais | Les questions qui obligent à expliquer, l'exigence de transparence |
| **Publication** | La préparation (paquet, empreinte, notes de version) | La décision de publier, et quand |
| **Erreurs** | Leur détection et leur correction, tracées dans les notes | L'arbitrage quand une correction touche à l'équité |

**En résumé** : l'IA apporte la **capacité de travail**. En trois jours, plus de 160 enregistrements, des milliers de lignes de code et de documentation, et 775 positions vérifiées. Le développeur apporte **l'intention, l'imagination et le jugement**. L'IA ne décide ni de ce qui est juste, ni de ce qui est neutre, ni de ce qui est publié.

### Une confiance assumée, et encadrée

Le développeur arbitre, mais il ne contrôle pas tout dans le détail : un contrôle exhaustif demanderait une équipe et un temps dont le projet ne dispose pas. Il fait donc **confiance à l'IA**, en connaissance de cause, et cette confiance repose sur trois appuis :

- **des règles écrites**, identiques pour tous, que l'IA applique et que chacun peut lire ;
- **des vérifications automatiques** : citations retrouvées mot pour mot dans leur source, validateur des données, tests ;
- **une transparence complète** : tout le travail est public et tracé (code, données, consignes, rapports bruts, erreurs), pour que chacun, électeur, équipe de campagne ou journaliste, puisse contrôler à son tour et signaler une erreur.

Cette confiance n'est pas aveugle : elle est **limitée** par ces garde-fous et **révocable** à chaque arbitrage.

---

## 4. Comment le travail circule

1. **Le développeur formule une demande**, souvent en une phrase : « Explique le choix des mesures », « Soumets-moi les paires avant de les ajouter ».
2. **Claude réalise ou propose.** Quand la demande touche au contenu éditorial, il **soumet d'abord** : propositions de mesures, couleurs des candidats, règles de saisie.
3. **Si une recherche est nécessaire, Claude rédige une consigne pour Hermès.** La tâche entre dans une file d'attente qui respecte le quota du modèle, puis Hermès dépose son livrable sur sa machine virtuelle.
4. **Claude rapatrie le livrable**, vérifie chaque citation à sa source et saisit ce qui est vérifié. Il écarte le reste, en le justifiant.
5. **Les contrôles automatiques s'exécutent** : validateur des données, tests du score, test hors ligne, cohérence des paires de mesures.
6. **Chaque étape est tracée.** Elle est enregistrée dans l'historique Git, inscrite au journal de la [notice du développeur](NOTICE_DEVELOPPEUR.md) (§5) et, après chaque relevé, décrite dans une [note d'enseignements](enseignements/README.md) qui dit ce qui a fonctionné, ce qui n'a pas fonctionné, et pourquoi.
7. **Le développeur arbitre et publie.**

---

## 5. Les garde-fous

- **Toute position est sourcée et citée.** La citation est vérifiée mot pour mot dans la source. Une position déduite ou tirée de la presse est marquée « à confirmer ».
- **Des [règles de saisie](regles_saisie_positions.md) écrites, identiques pour tous les candidats**, en partie contrôlées automatiquement.
- **Rien n'est publié sans l'accord du développeur.** La veille d'Hermès (candidats suivis, fréquence, consigne) ne change que sur sa demande.
- **Les données restent des brouillons** jusqu'à la relecture humaine. L'application l'affiche par un bandeau « données provisoires ».
- **Tout est public** : code, données, consignes données à Hermès, rapports bruts d'Hermès (`docs/hermes/rapports/`), notes d'erreurs et de limites.

## 6. Position de l'éditeur sur les questions éthiques

Utiliser l'intelligence artificielle pour un outil d'aide au vote pose des questions éthiques et philosophiques. La réponse relève du **jugement personnel** et de l'expérience de chacun. Ces questions ne sont pas plus grandes que celles que posent les médias dits d'opinion, qui sélectionnent, hiérarchisent et commentent l'information.

Publier un tel outil relève de la **liberté d'opinion et d'expression**, garantie par la Déclaration des droits de l'homme et du citoyen de 1789. Son article 10 dispose que nul ne doit être inquiété pour ses opinions, et son article 11 fait de la libre communication des pensées et des opinions « un des droits les plus précieux de l'Homme ».

À la différence d'un média d'opinion, ce comparateur ne défend aucune ligne : c'est pourquoi ses choix sont publics, documentés et contestables.

Chacun reste libre d'utiliser ce comparateur ou non, d'en contester les choix et d'en construire sa propre version : le code et les données sont ouverts et modifiables.

## 7. Limites de cette méthode

- **Les IA peuvent se tromper avec assurance.** Les vérifications réduisent ce risque sans l'annuler : une citation exacte peut être mal interprétée.
- **La neutralité ne se décrète pas.** Le catalogue reflète des choix, ceux du développeur et les propositions de Claude. Une relecture par des personnes de sensibilités différentes est prévue avant le premier pack réel, le 15/01/2027.
- **Les modèles ont leurs propres biais**, issus de leurs données d'entraînement. Les règles écrites et la vérification à la source servent à les contenir, pas à les supprimer.
- **Le développeur reste le seul responsable** de ce qui est publié.

Voir aussi : [méthode de choix des mesures](methode_choix_mesures.md) · [note de réflexion sur le catalogue](reflexion_catalogue_2026-11-14.md) · [règles de saisie](regles_saisie_positions.md) · [veille d'Hermès](hermes/) · [journal](NOTICE_DEVELOPPEUR.md).
