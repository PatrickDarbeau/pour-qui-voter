# Note — Licence et responsabilité

*Note de travail du 12/11/2026. Orientation, pas un avis juridique : à faire vérifier en cas de doute.*
**Décision du 12/11/2026 : code sous EUPL 1.2, données sous CC BY-SA 4.0.** Mise en place : fichiers `LICENCE`, `LICENCE-DONNEES`, `MENTIONS-LEGALES.md`, page « Mentions légales » de l'application, champ `licence` des packs.

---

## 1. Faut-il une licence ? Oui

Sans licence, le code reste « tous droits réservés » par défaut : personne n'a légalement le droit de le copier, de le modifier ni de le redistribuer. Ce serait contraire à l'objectif, en particulier pour les établissements scolaires qui voudraient l'adapter.

**Il ne faut pas rédiger sa propre licence** : une licence faite maison est souvent ambiguë et peu fiable. Il faut reprendre une licence standard, avec une licence pour le code et une autre pour les données.

---

## 2. Code : comparatif

| | **MIT** | **EUPL 1.2** | **AGPL 3.0** |
|---|---|---|---|
| **En une phrase** | « Faites-en ce que vous voulez, citez-moi. » | « Libre, et les versions modifiées restent libres. » | Comme l'EUPL, en plus strict. |
| **Texte officiel en français** | ❌ anglais seulement | ✅ oui, avec valeur juridique | ❌ anglais (traductions non officielles) |
| **Adaptée au droit français et européen** | Moyennement | ✅ conçue pour | Moyennement |
| **Un tiers peut reprendre l'outil et le fermer** (version payante, avec publicité ou traceurs) | ⚠️ **Oui** | ❌ Non : il doit publier ses modifications | ❌ Non |
| **Une école peut l'adapter librement** | ✅ | ✅ | ✅ |
| **Obligation de partager les modifications d'une version mise en ligne** | ❌ | ✅ | ✅ |
| **Simplicité, notoriété** | ⭐⭐⭐ la plus connue | ⭐⭐ connue des administrations | ⭐⭐ connue des développeurs |
| **Compatibilité avec d'autres licences** | Excellente | Bonne : prévue pour fonctionner avec les principales licences libres | Moyenne |
| **Exclusion de garantie (« tel quel »)** | ✅ | ✅ | ✅ |

**Le point qui décide** : voulez-vous empêcher qu'un tiers reprenne le comparateur, y ajoute des traceurs ou de la publicité, et le diffuse sans montrer ses modifications ?
- **Oui** → **EUPL 1.2**. C'est la recommandation pour un outil civique respectueux de la vie privée.
- **Non, diffusion la plus large possible, sans contrainte** → **MIT**.

L'AGPL n'apporte rien de plus que l'EUPL ici, et elle n'a pas de texte officiel en français.

---

## 3. Données : comparatif

| | **CC BY 4.0** | **CC BY-SA 4.0** | **ODbL** |
|---|---|---|---|
| **Règle** | Citer la source | Citer la source **et** partager dans les mêmes conditions | Spécifique aux bases de données, avec partage dans les mêmes conditions |
| **Un média peut reprendre les positions des candidats** | ✅ librement | ✅ si son travail dérivé reste ouvert | ✅ même règle |
| **Une version corrigée par un tiers revient au public** | ❌ pas obligatoirement | ✅ | ✅ |
| **Simplicité** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ plus technique |
| **Texte en français** | ✅ | ✅ | traduction non officielle |

**Recommandation** : **CC BY-SA 4.0**, cohérente avec l'EUPL. **CC BY 4.0** si l'on veut faciliter au maximum la reprise par la presse.

**Documentation et textes** : **CC BY 4.0** (réutilisation libre, avec citation de la source).

---

## 4. En résumé

| Profil | Code | Données |
|---|---|---|
| **Outil civique protégé** (recommandé) | EUPL 1.2 | CC BY-SA 4.0 |
| **Diffusion maximale, sans contrainte** | MIT | CC BY 4.0 |

---

## 5. Se dégager de toute responsabilité : en partie seulement

- Les licences libres contiennent déjà une clause « fourni tel quel, sans garantie », et l'EUPL en a une. C'est la protection de base.
- **En droit français, on ne peut pas s'exonérer de tout.** Une clause qui exclut toute responsabilité ne couvre pas la faute lourde ou intentionnelle, par exemple le fait de fausser délibérément les positions d'un candidat.
- **La meilleure protection est la méthode, plus que la clause** : neutralité, sources citées pour chaque position, avertissement « aide à la décision, pas une consigne de vote », corrections rapides en cas de signalement. Tout cela existe déjà dans l'application et dans la notice du développeur.
- À ajouter : une **clause de limitation de responsabilité** claire. Elle doit dire que l'outil est informatif, que des erreurs sont possibles, que l'utilisateur reste seul responsable de son vote, et qu'aucune garantie d'exactitude ni d'exhaustivité n'est donnée.

---

## 6. Deux obligations à ne pas oublier

- **Mentions légales**, obligatoires pour la démo en ligne. Elles doivent indiquer l'éditeur et l'hébergeur (GitHub). Un particulier qui n'agit pas à titre professionnel peut rester anonyme sur le site, à condition d'avoir communiqué son identité à l'hébergeur. **À vérifier.**
- **Politique de confidentialité** : courte, puisque l'outil ne collecte aucune donnée. Il est utile de l'écrire noir sur blanc.

---

## 7. Mise en place (une fois la décision prise)

| # | Action |
|---|---|
| 1 | Ajouter `LICENCE` (texte officiel EUPL 1.2 ou MIT) et `LICENCE-DONNEES` (CC BY-SA 4.0 ou CC BY 4.0) |
| 2 | Rédiger `MENTIONS-LEGALES.md` : éditeur, hébergeur, limitation de responsabilité, politique de confidentialité |
| 3 | Ajouter une page « Mentions légales » dans l'application, avec un lien dans le pied de page |
| 4 | Indiquer la licence des données dans les packs (champ `licence`) et dans l'archive ZIP |
| 5 | Mettre à jour le LISEZMOI et le journal du projet |
