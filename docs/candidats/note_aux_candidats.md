# Note aux candidats à l'élection présidentielle de 2027 et à leurs équipes de campagne

**Objet** : faire figurer l'intégralité de vos positions dans le comparateur « Pour qui voter ? »
**Date** : novembre 2026

> Champs à compléter par l'éditeur avant envoi : `[ADRESSE_CONTACT_EDITEUR]`, `[SIGNATURE]`.

---

Madame, Monsieur,

« Pour qui voter ? » est un comparateur de programmes **gratuit, neutre et non officiel**, destiné aux électeurs de l'élection présidentielle des 18 avril et 2 mai 2027. L'électeur donne son avis sur des mesures concrètes ; l'outil calcule sa concordance avec chaque candidat et affiche le détail des accords et des désaccords, **chaque position étant accompagnée de sa source**.

L'outil fonctionne hors ligne : aucune réponse d'électeur n'est collectée. Il n'est lié à aucun parti, ne reçoit aucun financement de candidats ou de partis, et son code comme ses données sont publics : <https://github.com/PatrickDarbeau/pour-qui-voter>. Une démonstration est accessible en ligne : <https://patrickdarbeau.github.io/pour-qui-voter/>.

## 1. Comment vos positions sont établies aujourd'hui

Vos positions sont relevées par l'éditeur à partir des documents publics, dans cet ordre de priorité :

1. votre site de campagne et votre programme ;
2. le site de votre parti ou de votre mouvement ;
3. à défaut, la presse de référence ; la position est alors signalée **« à confirmer »**.

Chaque position est accompagnée d'un **extrait exact** et d'un **lien vers sa source**. Une mesure sur laquelle aucune source ne permet de conclure est notée « ne se prononce pas » : elle ne compte ni pour ni contre vous.

Un candidat dont aucune position n'a pu être relevée est **listé, mais pas classé**. Un candidat dont le programme n'est que partiellement publié n'est comparé que sur les mesures connues : son taux de **couverture**, affiché à côté de son score, est alors faible.

## 2. Ce que nous vous proposons

Pour que **l'intégralité de vos positions** figure dans le comparateur, et non seulement celles que nous avons pu relever, nous vous invitons à adresser à l'éditeur :

1. **Un exemplaire de votre programme** : document PDF ou lien stable vers la page officielle qui le publie.
2. **Le questionnaire de réponse rempli**, qui reprend les **172 mesures** (17 thèmes) retenues dans le comparateur :
   - à remplir : [questionnaire_mesures.csv](questionnaire_mesures.csv) (tableur, une ligne par mesure) ;
   - à consulter ou imprimer : [mesures_par_theme.md](mesures_par_theme.md).

Pour chaque mesure, indiquez :

| Colonne | Contenu attendu |
|---|---|
| **position** | `soutient`, `soutient en partie`, `ne se prononce pas` ou `s'oppose` |
| **extrait_du_programme** | la phrase de votre programme qui justifie la réponse (citation exacte, courte) |
| **lien_ou_page_du_document** | l'adresse de la page, ou le numéro de page du document transmis |
| **commentaire** | facultatif : une nuance, une condition, un calendrier |

Certaines mesures vont par paires opposées (par exemple : rétablir l'impôt sur la fortune / conserver l'IFI) ; la colonne `mesure_opposee` les signale. Vos deux réponses doivent être cohérentes.

## 3. Règles de prise en compte

Ces règles s'appliquent de la même façon à tous les candidats.

- **Une réponse doit s'appuyer sur un document public.** Une position qui ne figure dans aucun document publié ne peut pas être retenue : l'électeur doit pouvoir vérifier la source.
- **L'éditeur vérifie chaque réponse** au regard du document cité. En cas d'écart entre la réponse et le programme publié, c'est le programme qui fait foi, et l'écart vous est signalé.
- **Les réponses retenues sont publiées avec leur source**, comme toutes les autres positions. Le questionnaire rempli peut être rendu public.
- **Les mesures ne sont pas modifiées à la demande d'un candidat.** Une suggestion (mesure manquante, formulation jugée orientée) est la bienvenue ; si elle est retenue, elle s'applique à tous les candidats lors de la révision suivante du catalogue.
- **Absence de réponse** : vos positions continuent d'être relevées à partir de vos documents publics, sans aucune pénalité.
- **Correction** : vous pouvez à tout moment signaler une position erronée ; elle est corrigée dans la mise à jour suivante des données, et la correction est inscrite au journal public des modifications.

## 4. Calendrier

- Premier jeu de données réelles : **15 janvier 2027**. Pour y figurer, merci d'envoyer vos documents **avant le 5 janvier 2027**.
- Les données sont ensuite mises à jour régulièrement jusqu'au scrutin ; un envoi plus tardif est pris en compte dans la mise à jour suivante.

## 5. Envoi

- par courriel : `[ADRESSE_CONTACT_EDITEUR]` ;
- ou en ouvrant un ticket public sur le dépôt du projet : <https://github.com/PatrickDarbeau/pour-qui-voter/issues> (le ticket et ses pièces jointes sont visibles de tous).

Merci d'indiquer le nom du candidat, la personne à contacter dans l'équipe de campagne et, pour le programme, sa date de publication.

Nous vous remercions de votre attention et de votre contribution à une information des électeurs **complète, vérifiable et équitable**.

`[SIGNATURE]`
Éditeur de « Pour qui voter ? »

---

*Pièces jointes : [questionnaire_mesures.csv](questionnaire_mesures.csv) · [mesures_par_theme.md](mesures_par_theme.md). La méthode de calcul est détaillée dans l'application (page « Méthode ») et dans le [README](../../LISEZMOI.md#résultats---méthode).*
