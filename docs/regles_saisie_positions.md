# Règles de saisie des positions

*Adoptées le 14/11/2026 (bloc B2 de la [note de réflexion sur le catalogue](reflexion_catalogue_2026-11-14.md)). Elles s'appliquent **de la même façon à tous les candidats**, qu'une position soit relevée par Hermès, par Claude ou par l'éditeur. Elles sont reprises dans la consigne d'Hermès ([consigne_positions_hebdo.md](hermes/consigne_positions_hebdo.md)). Toute modification de ces règles est décidée par l'éditeur et notée dans le journal ([NOTICE_DEVELOPPEUR.md](NOTICE_DEVELOPPEUR.md) §5).*

---

## R1. Les quatre valeurs

| Valeur | Sens | Quand l'utiliser |
|---|---|---|
| `1` | Soutient | La source défend la mesure telle qu'elle est écrite (ou va plus loin dans le même sens, voir R2) |
| `0.5` | Soutient en partie | Version atténuée, condition, étape, échéance plus lointaine, ou même sens sans chiffre (voir R2) |
| `-1` | S'oppose | La source rejette la mesure ou défend la mesure contraire |
| *(rien)* | Ne se prononce pas | Aucune source ne permet de conclure. **Ne jamais deviner.** |

## R2. Mesures chiffrées (seuils)

Quand la mesure contient un chiffre (montant, pourcentage, effectif, âge, date) :

| Ce que dit le candidat | Valeur |
|---|---|
| Même sens, chiffre **égal ou plus ambitieux** que celui de la mesure | `1` |
| Même sens, chiffre **moins ambitieux** | `0.5` |
| Même sens, **sans chiffre** (« augmenter », « renforcer », « réduire ») | `0.5` |
| Même sens, mais une **fourchette** qui commence sous le seuil | `0.5` |
| **Sens contraire** | `-1` |

« Plus ambitieux » s'entend dans le sens de la mesure : plus de recrutements, un SMIC plus élevé, moins d'élèves par classe, un déficit plus bas. Pour comparer un montant à un pourcentage, n'utiliser que les chiffres donnés par une source (par exemple « 1 600 € net, soit 98 € de plus par mois ») ; sinon, `0.5` et « à confirmer ».

## R3. Renvoi dos à dos : pas de position

Quand un candidat **rejette les deux options** d'une paire de mesures opposées (par exemple « libre-échange ou protectionnisme sont deux politiques possibles pour la bourgeoisie »), il ne se prononce **sur aucune des deux** au sens du questionnaire : **ne rien noter** sur l'une ni sur l'autre. Le signaler dans les propositions hors catalogue ou les points de vigilance.

## R4. Cohérence des paires opposées

Les mesures reliées par le champ « mesure opposée » se lisent ensemble.

- Soutenir l'une (`1`) n'implique de s'opposer à l'autre (`-1`) que si la source le permet ; sinon, laisser l'autre vide.
- **Jamais `1` sur les deux.**
- **`-1` sur les deux** n'est admis que si le candidat défend une **troisième option** qui exclut les deux (par exemple supprimer tout impôt sur la fortune : contre le rétablissement de l'ISF et contre le maintien de l'IFI). Sinon, c'est un renvoi dos à dos (R3).
- **`0.5` sur les deux** est admis pour une position intermédiaire explicite (par exemple excuse de minorité maintenue, mais appréciée par le juge).
- `outils/valider.py` signale automatiquement toute paire où un candidat a la même valeur, pour relecture.

## R5. « À confirmer »

Une position est marquée **à confirmer** quand :

- elle vient de la **presse** ou d'une interview, et non d'un document du candidat ou de son parti ;
- elle est **déduite** d'un principe général, sans que la mesure soit citée ;
- elle reprend le passage d'une **mesure voisine** (« miroir » d'une autre mesure de la paire) ;
- un chiffre a dû être **converti** sans source (R2).

Une position « à confirmer » compte dans le score ; elle est signalée dans l'application et doit être revérifiée en priorité.

## R6. Citation et source

- Citation **exacte**, de moins de 30 mots, copiée du texte consulté, avec l'URL (et la page d'un PDF) et la date. Elle est vérifiée mot pour mot dans la source avant saisie.
- Sources, par ordre de priorité : site de campagne 2027, site du parti ou du mouvement, puis presse de référence (R5). Jamais d'agrégateur ni de comparateur, ni Wikipédia.
- Pas de programme d'une élection précédente, sauf reprise explicite dans un document de 2027.
- Une position sans citation vérifiable n'est **pas saisie**.

---

## Application aux positions existantes (14/11/2026)

Les règles ont été appliquées aux 16 candidats :

| Règle | Candidat | Mesure | Avant | Après | Motif |
|---|---|---|---|---|---|
| R3 | Arthaud | agri4, agri5 (Mercosur) | −1 / −1 | *(rien)* | retiré le 14/11 : libre-échange et protectionnisme renvoyés dos à dos |
| R3 | Arthaud | eu1, eu2 (intégration européenne / compétences rendues aux États) | −1 / −1 | *(rien)* | rejette l'UE et le retour aux frontières nationales |
| R2 | Ruffin | trav1 (SMIC +10 %) | 1 | 0.5 | « SMIC à 1 600 € », soit environ +98 € par mois, moins que +10 % |
| R2 | Attal | edu2 (enseignants +15 %) | 1 | 0.5 | fourchette « 200 à 500 € » qui commence sous le seuil |
| R2 | Lisnard | jus5 (20 000 places de prison) | 1 | 0.5 | « augmentation des places de prison », sans chiffre |
| R2 | Philippe | jus5 (20 000 places de prison) | 1 | 0.5 | « loi d'accélération de la construction de prisons », sans chiffre |
| R2 | Lisnard | eco9 (déficit sous 3 %) | 1 | 0.5 | « plan de réduction des déficits », sans chiffre |

Paires examinées et conservées (R4) : Zemmour eco1/eco2 (troisième option : suppression de tout impôt sur la fortune), Tondelier eco3/eco4 et Philippot jus6/jus7 (positions intermédiaires explicites).
