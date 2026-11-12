# Cahier des charges — « Pour qui voter ? » (Présidentielle 2027)

## 1. Contexte et objectif

L'élection présidentielle française aura lieu en deux tours : le **premier tour le dimanche 18 avril 2027** et le **second tour le dimanche 2 mai 2027**. L'application web « Pour qui voter ? » aide un électeur à **comparer ses priorités avec les programmes des candidats**. L'utilisateur choisit, thème par thème, les propositions qui lui tiennent le plus à cœur. Le système calcule ensuite le **taux de concordance** avec chaque candidat et présente un classement. Le candidat le mieux classé est suggéré comme « vote préférentiel ».

L'outil a une vocation **informative et non partisane**. Il ne donne pas de consigne de vote : il propose un éclairage.

**Exigence structurante — confidentialité** : l'application doit pouvoir être **téléchargée et utilisée entièrement en local**, sans aucune connexion réseau pendant le questionnaire. La mise en ligne est **secondaire** : elle sert uniquement de **démonstration** (voir §6 bis).

**Exigence structurante — données** : la liste des candidats et leurs mesures sont établies à partir de **recherches sur internet** (programmes officiels, sites de campagne, presse). Une **procédure de mise à jour** documentée et outillée est fournie (voir §9 bis).

## 2. Périmètre

| Inclus | Exclu (V1) |
|---|---|
| Base de mesures classées par thème, modifiable | Comptes utilisateurs publics |
| Base de candidats avec fiche de profil, modifiable | Commentaires et forum |
| Questionnaire de sélection | Application mobile native |
| Calcul et affichage des résultats | Import automatique des programmes (scraping) |
| Back-office d'administration | Multilingue |
| Paquet téléchargeable et utilisable hors ligne | |
| Procédure et outil de mise à jour des données depuis internet | |
| Version de démonstration en ligne (statique) | Back-office collaboratif en ligne (PHP) |

## 3. Acteurs

- **Visiteur (électeur)** : répond au questionnaire et consulte les résultats et les fiches des candidats. Aucune inscription n'est requise.
- **Administrateur / contributeur** : gère les thèmes, les mesures, les candidats et les correspondances entre mesures et candidats.

## 4. Exigences fonctionnelles

### 4.1 Base des thèmes et des mesures
- **F1** : CRUD des **thèmes** (exemples : Économie, Emploi, Santé, Éducation, Écologie, Sécurité, Justice, Immigration, Europe et international, Institutions, Agriculture, Numérique, Logement, Retraites, Culture). Chaque thème a un nom, une icône, une couleur et un ordre d'affichage.
- **F2** : CRUD des **mesures** : intitulé court, description, thème, source ou explication, statut (actif ou brouillon).
- **F3** : formulation **neutre** des mesures. Une mesure ne doit jamais citer de candidat.
- **F4** : les mesures **opposées** peuvent être liées entre elles (exemple : « retraite à 60 ans » / « retraite à 65 ans »). Cette liaison permet de détecter un désaccord.

### 4.2 Base des candidats
- **F5** : CRUD des **candidats** : nom, prénom, parti ou mouvement, photo, date de naissance, parcours, slogan, site officiel, lien vers le programme PDF, statut (déclaré, investi, officiellement qualifié, retiré).
- **F6** : **positions** du candidat sur chaque mesure, avec l'une des valeurs suivantes :
  `soutient (+1)` / `soutient partiellement (+0,5)` / `ne se prononce pas (0)` / `s'oppose (−1)`. Chaque position est accompagnée d'une **source obligatoire** (URL et date) et d'une citation courte facultative.
- **F7** : fiche de profil publique du candidat, avec ses positions regroupées par thème.

### 4.3 Parcours électeur
- **F8** : page d'accueil avec la présentation, la méthode, l'avertissement de neutralité et un bouton « Commencer ».
- **F9** : sélection des **thèmes prioritaires** (facultative). Ces thèmes reçoivent un coefficient de poids ×2.
- **F10** : questionnaire **thème par thème**. Les mesures s'affichent sous forme de cartes. Pour chacune, l'utilisateur peut cocher « Je soutiens », « Je m'oppose » ou « Indifférent », et éventuellement marquer la mesure comme **essentielle** (★, poids ×3).
- **F11** : une barre de progression est affichée. L'utilisateur peut revenir en arrière et passer un thème.
- **F12** : l'ordre des mesures est **aléatoire** dans chaque thème pour limiter les biais.

### 4.4 Calcul de concordance
- **F13** : algorithme de base. Pour chaque candidat *c* :
  ```
  score(c) = Σ  poids(m) × accord(u_m, c_m)
            / Σ  poids(m) × 1          (mesures où u_m ≠ indifférent)
  accord = u_m × c_m   (u_m ∈ {+1, −1}, c_m ∈ {+1, +0.5, 0, −1})
  poids  = 1 × (2 si thème prioritaire) × (3 si mesure essentielle)
  ```
  Le résultat est ramené sur l'échelle de 0 à 100 % avec la formule `(score + 1) / 2 × 100`.
- **F14** : un **taux de couverture** est affiché pour chaque candidat. Il indique la part des mesures choisies sur lesquelles le candidat s'est prononcé, afin de ne pas favoriser les programmes les plus détaillés.
- **F15** : le **résultat** comprend un classement en barres, le candidat en tête désigné comme « vote préférentiel », un détail par thème (radar ou barres), ainsi que la liste des points d'accord et de désaccord avec leurs sources.
- **F16** : les **ex æquo** (écart inférieur à 2 points) sont signalés explicitement.

### 4.5 Résultats et partage
- **F17** : export du résultat en PDF ou en impression, et lien de partage. Les réponses sont encodées dans l'URL ou le *hash* et ne sont jamais stockées sur le serveur.
- **F18** : bouton « Recommencer » et sauvegarde locale des réponses (`localStorage`).

### 4.6 Administration
- **F19** : l'édition se fait **uniquement en local**, par un mode « Édition » intégré à l'application, sans mot de passe (l'utilisateur est seul sur sa machine). Il n'y a pas de back-office en ligne.
- **F20** : **matrice d'édition** sous forme de tableau mesures × candidats, pour saisir rapidement les positions.
- **F21** : **import/export JSON et CSV** de toute la base (sauvegarde et contribution).
- **F22** : historique des modifications (qui, quand, ancienne valeur et nouvelle valeur).
- **F23** : prévisualisation du questionnaire avant publication.

### 4.7 Installation locale
- **F24** : l'application est distribuée sous forme d'une **archive ZIP**. Après décompression, un double-clic sur `index.html` suffit : aucun serveur, PHP ou base de données n'est nécessaire.
- **F25** : en option, un lanceur `lancer.bat` / `lancer.sh` démarre un mini-serveur local (`python -m http.server` ou `php -S localhost:8000`) pour ceux qui le préfèrent.
- **F26** : **zéro appel réseau** pendant l'utilisation. Toutes les bibliothèques (Chart.js, polices) sont embarquées dans l'archive ; aucun CDN ni aucune police distante.
- **F27** : les modifications faites en mode Édition sont enregistrées dans le navigateur, puis exportées dans un fichier `donnees.json` que l'utilisateur conserve ou réimporte.
- **F28** : l'écran d'accueil affiche la **version des données** (date de dernière mise à jour, nombre de candidats et de mesures) et leur origine (voir F39). Il alerte si elles datent de plus de 30 jours, ou de plus de 7 jours à partir de février 2027.

## 5. Exigences non fonctionnelles

| Domaine | Exigence |
|---|---|
| **Neutralité** | Méthode publiée, sources visibles, ordre aléatoire des candidats en cas d'égalité, aucune couleur partisane imposée |
| **Vie privée / RGPD** | Les opinions politiques sont des **données sensibles** (art. 9 RGPD). En local, rien ne quitte la machine. En ligne, les réponses ne sont pas stockées côté serveur et le calcul se fait dans le navigateur. Aucun traceur, aucun analytics, aucun cookie. Une politique CSP `connect-src 'none'` bloque tout appel réseau depuis le questionnaire |
| **Portabilité** | Fonctionne en `file://` sous Windows, macOS et Linux |
| **Accessibilité** | RGAA / WCAG 2.1 AA : navigation au clavier, contrastes suffisants, textes alternatifs |
| **Responsive** | Mobile d'abord (largeur minimale de 360 px) |
| **Performance** | Première page en moins de 2 s en 4G, poids JS inférieur à 200 ko |
| **Compatibilité** | Deux dernières versions de Chrome, Firefox, Safari et Edge |
| **Sécurité** | Requêtes préparées (PDO), jeton CSRF, échappement HTML, HTTPS obligatoire, limitation des tentatives de connexion |
| **Maintenabilité** | Code commenté en français, README, données séparées du code |

## 6. Architecture technique proposée

**Choix retenu** : une application **100 % statique** (HTML, CSS et JavaScript sans framework). Elle fonctionne aussi bien en local (double-clic) qu'en ligne, sur n'importe quel hébergement (mutualisé, GitHub Pages, Netlify), sans PHP ni base de données.

```
┌──────────────── Paquet local (ZIP) ────────────────┐
│ index.html ── app.js ── score.js ── edition.js     │
│        │                                           │
│        ▼ chargé par <script> (compatible file://)  │
│ data/donnees.js  (window.DONNEES = {...})          │
│ localStorage : réponses + modifications locales    │
└────────────────────────────────────────────────────┘
              ▲ remplacé lors d'une mise à jour
┌──────── Outil de mise à jour (hors appli) ─────────┐
│ outils/maj.py : collecte → brouillon → validation  │
│ → génère data/donnees.js + journal des sources     │
└────────────────────────────────────────────────────┘
```

- Les données sont chargées via un fichier `donnees.js` et non via `fetch()`, que les navigateurs bloquent en `file://`.
- Le format source de référence reste `donnees.json` ; `donnees.js` en est une simple enveloppe générée.
- Aucun composant serveur (PHP ou base de données) n'est prévu.

## 6 bis. Version de démonstration en ligne

La mise en ligne est secondaire. Elle sert à présenter l'outil et à inviter à le télécharger.

- **Contenu** : exactement les mêmes fichiers statiques que le ZIP, déposés sur un hébergement statique gratuit (GitHub Pages, Netlify, ou un hébergement mutualisé).
- **Bandeau permanent** : « Version de démonstration — pour une confidentialité totale, téléchargez l'application et utilisez-la sur votre ordinateur », avec un bouton de téléchargement du ZIP.
- **Mode Édition désactivé** en ligne : la consultation et le questionnaire restent accessibles.
- **Confidentialité identique** : le calcul se fait dans le navigateur. Il n'y a ni formulaire envoyé, ni analytics, ni cookie, et aucune réponse ne transite par le serveur.
- **Lien de partage** (F17) : il est désactivé par défaut en ligne, car il encode les réponses dans l'URL. On peut le réactiver seulement après un avertissement explicite.
- **Données** : la démonstration peut utiliser le jeu réel ou un jeu fictif. Un indicateur « Données de démonstration » s'affiche si les candidats sont fictifs.
- **Pas de garantie de service** : la démonstration peut être arrêtée à tout moment ; la référence reste le paquet local.

### Arborescence
```
/index.html            application (pages gérées en JS : accueil, questionnaire,
                       résultats, fiches, méthode, édition)
/assets/css, /assets/js, /assets/lib (Chart.js embarqué), /assets/fonts
/assets/img/candidats
/data/donnees.json     base de référence
/data/donnees.js       base chargée par l'appli (générée)
/data/sources/         captures et journal des sources
/outils/maj.py         outil de mise à jour assistée
/outils/valider.py     contrôle de cohérence du JSON
/lancer.bat, /lancer.sh (facultatifs)
/LISEZMOI.md
```

## 7. Modèle de données

```
theme(id, nom, slug, icone, couleur, ordre)
mesure(id, theme_id → theme, intitule, description, source_url, actif, opposee_a → mesure NULL)
candidat(id, nom, prenom, parti, photo, date_naissance, biographie, slogan,
         site_officiel, pages_programme[], programme_url, statut, couleur,
         derniere_collecte)
position(candidat_id → candidat, mesure_id → mesure, valeur ∈ {-1,0,0.5,1},
         source_url, source_type ∈ {site_officiel, programme_pdf, presse, interview, vote},
         source_date, citation, a_confirmer, PK(candidat_id, mesure_id))
admin(id, login, mot_de_passe_hash, role)
journal(id, admin_id, table_nom, ligne_id, ancien, nouveau, date)
```

## 8. Maquettes (descriptif)

1. **Accueil** : titre, compte à rebours jusqu'au prochain tour (18 avril, puis 2 mai 2027), explication en trois étapes, bouton « Commencer ».
2. **Thèmes prioritaires** : grille de tuiles cliquables.
3. **Questionnaire** : onglets de thèmes en haut, cartes de mesures avec trois boutons et une étoile, boutons « Précédent » et « Suivant ».
4. **Résultats** : podium, barres horizontales avec % de concordance et de couverture, accordéon de détail par candidat, graphique radar par thème.
5. **Fiche candidat** : photo, identité, parcours, positions par thème avec sources.
6. **Admin** : tableau de bord, listes CRUD, matrice des positions.

## 9. Contenu initial

- Environ 15 thèmes et 8 à 12 mesures par thème, soit **120 à 180 mesures**.
- Candidats déclarés ou pressentis, mis à jour jusqu'à la publication de la liste officielle par le Conseil constitutionnel (mars 2027).
- Chaque position doit être **sourcée** (programme officiel, interview, vote parlementaire).

## 9 bis. Procédure de mise à jour des données

La collecte se fait à partir de recherches sur internet, mais **jamais pendant l'utilisation du questionnaire** : c'est une étape séparée, lancée volontairement par la personne qui maintient les données.

### Sources, par ordre de fiabilité
1. Sources officielles :
   - Conseil constitutionnel : liste officielle des candidats et parrainages.
   - **Site officiel de chaque candidat** (ou de son parti ou mouvement de campagne) : programme en ligne, programme PDF, pages thématiques, propositions, communiqués et biographie. C'est la **source principale** pour les positions et pour la fiche de profil.
2. Comparateurs reconnus et presse nationale (dossiers « programmes »).
3. Interviews, débats, votes parlementaires des candidats.

Une source de niveau 3 seule entraîne une position marquée « à confirmer ».

### Étapes
| # | Étape | Outil | Sortie |
|---|---|---|---|
| 1 | **Veille candidats** : vérifier les déclarations, retraits et la liste officielle | recherche web + `maj.py candidats` | liste à jour |
| 2 | **Collecte des programmes** : parcourir le site officiel de chaque candidat (URL enregistrée dans sa fiche), archiver les pages programme et les PDF, et noter la date de consultation. Compléter ensuite par les autres sources | `maj.py collecter` | `data/sources/AAAA-MM-JJ/<candidat>/` (copies, URL, empreinte) |
| 3 | **Extraction** : repérer les mesures dans chaque programme et les rattacher aux mesures neutres existantes, ou proposer de nouvelles mesures | manuel, ou assisté par IA en option | `brouillon.json` |
| 4 | **Relecture humaine obligatoire** : valider chaque position et sa source, et reformuler les mesures de façon neutre | mode Édition de l'appli | positions validées |
| 5 | **Contrôle** : mesures sans source, candidats sans position, doublons, mesures déséquilibrées | `valider.py` | rapport |
| 6 | **Publication** : générer `donnees.js`, incrémenter la version et dater, rédiger le journal des modifications | `maj.py publier` | nouveau ZIP |

### Règles
- **Fréquence** : mensuelle jusqu'en janvier 2027, puis hebdomadaire de février au 18 avril 2027. Une mise à jour immédiate est faite à la publication de la liste officielle, puis le 19 avril pour le second tour.
- **Mode second tour** : à partir des résultats du premier tour, l'application propose un questionnaire limité aux **deux candidats qualifiés** pour le second tour du 2 mai 2027. Les réponses déjà données sont réutilisées ; les autres candidats restent consultables mais sont grisés.
- **Suivi des sites officiels** : `maj.py` compare l'empreinte des pages archivées d'une collecte à l'autre et signale les pages de programme modifiées, ajoutées ou supprimées. Ces pages sont à relire en priorité.
- **Priorité de la source officielle** : en cas de contradiction entre le site officiel du candidat et une autre source, la position du site officiel est retenue, et l'écart est noté en commentaire.
- **Diff lisible** : chaque mise à jour affiche ce qui a changé (ajout, suppression, changement de position), avec la source.
- **Équilibre** : le même effort de recherche pour chaque candidat ; un indicateur de couverture par candidat est suivi.
- **Extraction assistée** : si une IA est utilisée à l'étape 3, ses propositions restent un brouillon jusqu'à la relecture humaine. Seuls les textes publics des programmes lui sont envoyés, jamais les réponses d'un utilisateur.
- **Distribution** : par packs de données (voir §9 ter). Il n'y a jamais de mise à jour automatique en ligne, pour rester hors ligne par défaut.

## 9 ter. Gouvernance des données

Le modèle est **mixte** : le développeur maintient la base de référence, et l'utilisateur reste libre de l'utiliser, de la modifier ou de la refaire.

### Rôles
| Rôle | Responsabilités |
|---|---|
| **Mainteneur officiel** (développeur) | Il applique la procédure du §9 bis et publie les packs de données officiels. Il traite les signalements d'erreur et tient le journal des modifications. |
| **Utilisateur** | Il choisit quand importer un pack officiel. Il peut corriger ou compléter localement les données, produire son propre pack et proposer des corrections au mainteneur. |

### Pack de données
- **F29** : un pack est un fichier unique `donnees-AAAA-MM-JJ.json` qui contient :
  - `version` (exemple : `2027.03.15`), `date`, `origine` (`officiel` ou `local`) et `auteur` ;
  - les thèmes, les mesures, les candidats et les positions avec leurs sources ;
  - le `journal` des modifications depuis la version précédente.
- **F30** : chaque pack officiel est accompagné de son **empreinte SHA-256**, publiée sur la page de démonstration et sur le dépôt du projet. L'application calcule et affiche l'empreinte du pack importé, pour que l'utilisateur puisse vérifier qu'il n'a pas été modifié.
- **F31** : les packs officiels se téléchargent depuis la page de démonstration ou le dépôt du projet (par exemple, la page « Releases » de GitHub). Le ZIP de l'application contient toujours le dernier pack officiel disponible au moment de sa publication.

### Import d'un pack
- **F32** : l'utilisateur importe un pack avec le bouton « Importer un pack ». L'application ne se connecte jamais seule à internet.
- **F33** : avant de remplacer les données, l'application affiche un **aperçu des changements** (candidats et mesures ajoutés ou retirés, positions modifiées) et demande confirmation.
- **F34** : un pack invalide est refusé avec un message clair : format incorrect, version plus ancienne que celle en place (sauf confirmation explicite), ou contrôles de `valider.py` en échec.
- **F35** : avant chaque import, une **sauvegarde** des données en place est conservée, et l'utilisateur peut revenir en arrière.

### Modifications locales
- **F36** : toute position, mesure ou fiche modifiée par l'utilisateur est **marquée « modifiée localement »**.
- **F37** : à l'import d'un nouveau pack officiel, chaque élément modifié localement donne lieu à un choix : « garder ma version » ou « prendre la version officielle ». Un choix global est aussi proposé.
- **F38** : l'utilisateur peut exporter ses modifications comme pack `origine: local`, pour son propre usage ou pour les proposer au mainteneur.

### Transparence
- **F39** : l'écran d'accueil et la page de résultats indiquent l'origine des données : « Pack officiel du JJ/MM/AAAA » ou « Données modifiées localement (N éléments) ».
- **F40** : un lien « Signaler une erreur » prépare un message contenant la référence de la mesure, du candidat et de la source contestée, sans aucune réponse personnelle de l'utilisateur. L'envoi reste manuel (courriel ou ticket sur le dépôt).

### Calendrier de publication des packs
| Période | Rythme |
|---|---|
| Jusqu'à fin janvier 2027 | Un pack par mois |
| Février au 18 avril 2027 | Un pack par semaine |
| Publication de la liste officielle des candidats (mars 2027) | Pack exceptionnel immédiat |
| 19 avril 2027 | Pack « second tour » (deux candidats qualifiés) |
| Après le 2 mai 2027 | Pack final archivé, fin de maintenance |

## 10. Planning indicatif

| Lot | Contenu | Durée |
|---|---|---|
| L1 | Format `donnees.json`, validateur, jeu de données de démo | 1 sem. |
| L2 | Parcours électeur et calcul du score (fonctionne en `file://`) | 2 sem. |
| L3 | Mode Édition (CRUD, matrice, import/export) | 2 sem. |
| L4 | Résultats détaillés, fiches, export PDF | 1 sem. |
| L5 | Outil de mise à jour `maj.py`, procédure, import et export de packs (F29 à F40) | 1,5 sem. |
| L6 | Accessibilité, tests, paquet ZIP, version de démonstration en ligne | 1 sem. |
| L7 | Recherche et saisie du contenu réel, puis mises à jour jusqu'au 2 mai 2027 | continu |
| — | **Jalon impératif** : version complète publiée au plus tard mi-mars 2027, soit environ un mois avant le premier tour du 18 avril | |

## 11. Critères d'acceptation

- Un parcours complet (30 mesures) prend moins de 10 minutes sur mobile.
- Le score calculé correspond au calcul manuel sur trois cas de test documentés.
- Aucune réponse de l'utilisateur n'est transmise au serveur (vérification via l'onglet réseau).
- Le ZIP décompressé fonctionne par double-clic sur `index.html`, **machine déconnectée d'internet**, avec Chrome, Firefox et Edge.
- L'onglet réseau ne montre **aucune requête externe** pendant un parcours complet.
- Une mise à jour complète (étapes 1 à 6) produit un diff lisible et un `donnees.json` validé sans erreur.
- L'import d'un pack officiel affiche l'aperçu des changements et l'empreinte SHA-256, et conserve les modifications locales choisies par l'utilisateur.
- Un pack corrompu ou plus ancien est refusé, et la sauvegarde permet de revenir à l'état précédent.
- Un administrateur ajoute un candidat et ses positions sans toucher au code.
- Le score Lighthouse est d'au moins 90 en accessibilité et en performance.

## 12. Mentions légales et précautions

- Avertissement visible : « Cet outil ne remplace pas la lecture des programmes. »
- Respect des règles d'équité du temps de parole en période électorale (recommandations de l'Arcom) : tous les candidats officiels sont traités de la même façon.
- Mentions légales, politique de confidentialité, contact pour signaler une erreur de position.
