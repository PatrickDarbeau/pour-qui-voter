# Note — Permettre de soutenir le projet par un don

*Note de travail, à valider avant toute mise en place. Les frais et les règles fiscales évoluent : vérifiez-les sur le site de chaque plateforme et auprès de l'administration fiscale avant d'ouvrir un compte.*

---

## 1. Principes à respecter

Un comparateur électoral repose sur la confiance. Les dons ne doivent jamais faire douter de sa neutralité.

| Principe | Mise en œuvre |
|---|---|
| **Neutralité** | Refuser tout don d'un candidat, d'un parti, d'une association de financement électoral ou d'un mandataire financier. L'écrire noir sur blanc sur la page de dons. |
| **Indépendance** | Les dons ne donnent aucun droit sur le contenu : ni mesures, ni positions, ni ordre d'affichage. |
| **Transparence** | Publier une fois par an, ou à la fin de la campagne, le total reçu et son utilisation : hébergement, nom de domaine, matériel, temps. |
| **Vie privée** | Aucun module de paiement intégré dans l'application. Un **simple lien** vers la plateforme, pour que l'application reste sans traceur ni connexion. |
| **Facultatif** | Le don ne débloque rien. L'outil reste entièrement gratuit. |

> **Point juridique à vérifier.** Le projet n'est ni un candidat ni un parti : les plafonds de dons électoraux (Code électoral, art. L52-8) ne devraient pas s'appliquer. Mais recevoir de l'argent d'une personne morale liée à la campagne pourrait être requalifié en aide à un candidat. Refuser ces dons, comme indiqué ci-dessus, écarte ce risque. En cas de doute, demandez un avis écrit à la CNCCFP ou à un juriste.

---

## 2. Les solutions possibles

| Plateforme | Pour qui | Points forts | Points faibles |
|---|---|---|---|
| **Liberapay** | Particuliers et associations | Plateforme associative à but non lucratif, sans commission de la plateforme (seuls les frais bancaires s'appliquent), sans publicité, adaptée au logiciel libre, dons ponctuels ou récurrents | Moins connue du grand public, interface sobre |
| **GitHub Sponsors** | Particuliers ayant un compte GitHub | Directement sur le dépôt (bouton « Sponsor »), pas de commission sur les comptes personnels (à vérifier), crédible pour un projet open source | Réservé aux personnes qui ont un compte GitHub, public plutôt technique |
| **Ko-fi** | Particuliers | Très simple, « offrez-moi un café », dons ponctuels sans commission sur l'offre gratuite (à vérifier) | Image « créateur de contenu », passe par PayPal ou Stripe |
| **Buy Me a Coffee** | Particuliers | Simple et connu | Commission sur chaque don, entreprise commerciale |
| **Tipeee** | Créateurs français | Plateforme française, interface en français, public francophone | Commission, orientée vers les créateurs de vidéos |
| **Open Collective** | Projets collectifs | Comptabilité publique automatique : chaque dépense est visible, idéal pour la transparence | Nécessite un « hôte fiscal » et prend une commission, plus lourd à mettre en place |
| **HelloAsso** | **Associations uniquement** | Française, sans frais pour l'association (contribution volontaire du donateur), permet d'émettre des reçus fiscaux si l'association y a droit | Il faut créer une association loi 1901 |
| **PayPal (lien direct)** | Tous | Universel | Frais, image commerciale, compte PayPal souvent nécessaire |
| **Virement (IBAN)** | Tous | Aucun intermédiaire | Révèle des coordonnées bancaires personnelles : **déconseillé** |

---

## 3. Recommandation

### Maintenant, en solo : **Liberapay et GitHub Sponsors**
- **Liberapay** comme lien principal : non lucratif, sans commission de plateforme, cohérent avec un projet libre et respectueux de la vie privée.
- **GitHub Sponsors** en complément, visible sur le dépôt une fois qu'il sera public.
- En option, **Ko-fi** pour un public moins technique (« offrez un café »).

### Plus tard, si le projet grandit : **une association et HelloAsso**
Si plusieurs personnes contribuent, ou si l'outil est repris par des établissements scolaires :
1. créer une association loi 1901 (objet : éducation civique et outils numériques citoyens) ;
2. ouvrir une page **HelloAsso** ;
3. demander, si l'objet s'y prête, le rescrit fiscal « intérêt général », qui permet aux donateurs de déduire une partie de leur don de leurs impôts. **À ne pas annoncer avant d'avoir obtenu la reconnaissance.**

---

## 4. Fiscalité (particulier, sans association)

- Les dons reçus via Liberapay, Ko-fi, etc. sont en principe des **revenus imposables**, à déclarer en bénéfices non commerciaux (BNC). Un régime simplifié (micro-BNC) existe en dessous d'un certain seuil.
- **Aucun reçu fiscal** ne peut être délivré par un particulier : les donateurs ne bénéficient d'aucune réduction d'impôt. Ne pas laisser croire le contraire.
- Conserver un relevé annuel des dons reçus.

*À confirmer auprès du centre des finances publiques ou sur impots.gouv.fr.*

---

## 5. Intégration dans le projet

**Dans l'application** (simple lien, pas de bouton de paiement ni de script tiers) :
- un lien « ❤ Soutenir le projet » dans le pied de page ;
- une question dans la page Aide, « Comment soutenir le projet ? », qui renvoie vers une page « Soutenir » ;
- jamais pendant le questionnaire ni sur la page de résultats, pour ne pas mélanger choix politique et sollicitation.

**Page « Soutenir » (texte prêt à l'emploi)**
```
Soutenir « Pour qui voter ? »

Cet outil est gratuit, sans publicité et sans collecte de données. Il est développé bénévolement.

Si vous le trouvez utile, vous pouvez participer aux frais (hébergement, nom de domaine) et au temps passé à rechercher et sourcer les positions des candidats.

→ Faire un don sur Liberapay : [LIEN_LIBERAPAY]
→ Devenir sponsor sur GitHub : [LIEN_GITHUB_SPONSORS]

Engagements :
• Aucun don n'est accepté de la part d'un candidat, d'un parti ou d'une structure liée à une campagne.
• Les dons ne donnent aucune influence sur le contenu.
• Le total reçu et son utilisation seront publiés à la fin de la campagne.

Vous ne pouvez pas donner ? Partager l'outil autour de vous, signaler une erreur ou relire des mesures, c'est aussi une grande aide. Merci !
```

**Sur le dépôt GitHub :**
- fichier `.github/FUNDING.yml` (affiche le bouton « Sponsor ») :
  ```yaml
  github: [PatrickDarbeau]
  liberapay: [IDENTIFIANT_LIBERAPAY]
  ```
- une section « Soutenir » dans le LISEZMOI.

**Dans la campagne de promotion :** une seule mention discrète en fin d'article Substack et dans la description YouTube. Pas de message dédié aux dons sur les réseaux pendant la campagne électorale.

---

## 6. Étapes de mise en place

| # | Action | Qui |
|---|---|---|
| 1 | Décider des plateformes retenues | Vous |
| 2 | Créer le compte Liberapay (et GitHub Sponsors, qui demande une validation) | Vous (identité et coordonnées bancaires) |
| 3 | Me transmettre les liens publics | Vous |
| 4 | Ajouter la page « Soutenir », le lien en pied de page, la question d'aide, `FUNDING.yml` | Moi |
| 5 | Ouvrir le relevé des dons et préparer le bilan de transparence | Vous |

Je ne peux ni créer les comptes ni saisir de coordonnées bancaires à votre place.
