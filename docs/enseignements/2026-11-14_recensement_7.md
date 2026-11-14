# Note d'enseignements n°7 — règles de saisie écrites et appliquées à tous

**Date** : 14/11/2026 · **Lot** : 7 (étape 5, suite) · **Périmètre** : bloc B2 de la [note de réflexion sur le catalogue](../reflexion_catalogue_2026-11-14.md). Règles de saisie écrites ([regles_saisie_positions.md](../regles_saisie_positions.md)), intégrées à la consigne d'Hermès et appliquées aux 16 candidats. Total : 775 positions (−2), pack `2026.11.14-test` (non publié).
**Analyse chiffrée** : [2026-11-14_analyse_comparative_7.md](2026-11-14_analyse_comparative_7.md) (`python outils/comparer.py 7`). Note précédente : [n°6](2026-11-14_recensement_6.md).

---

## 1. Ce qui fonctionne

- **Six règles écrites** (R1 à R6) : valeurs, mesures chiffrées, renvoi dos à dos, paires opposées, « à confirmer », citation et source. Elles reprennent ce qui était appliqué au cas par cas et le rendent identique pour tous.
- **Deux règles sont contrôlées par les outils** :
  - `outils/valider.py` signale toute paire de mesures opposées où un candidat a la même valeur (R4) et toute position de presse non marquée « à confirmer » (R5) ; un test couvre ces deux alertes ;
  - `outils/positions.py` marque d'office « à confirmer » toute position tirée de la presse (R5).
- **La consigne d'Hermès reprend les règles** dès le relevé du 21/11 (fichier envoyé et vérifié sur la VM).

## 2. Corrections appliquées

| Règle | Candidat | Mesure | Avant → après |
|---|---|---|---|
| R3 renvoi dos à dos | Arthaud | eu1 / eu2 (intégration européenne / compétences rendues aux États) | −1 / −1 → *rien* |
| R2 seuil | Ruffin | trav1 SMIC +10 % (« SMIC à 1 600 € », environ +98 €) | 1 → 0,5 |
| R2 seuil | Attal | edu2 enseignants +15 % (« 200 à 500 € ») | 1 → 0,5 |
| R2 sans chiffre | Lisnard | jus5 20 000 places de prison ; eco9 déficit sous 3 % | 1 → 0,5 |
| R2 sans chiffre | Philippe | jus5 20 000 places de prison | 1 → 0,5 |
| R5 presse | Ruffin, Dupont-Aignan | positions tirées de la presse | désormais « à confirmer » |
| R6 citation | Ruffin | eu2 : citation tronquée par des guillemets imbriqués | rétablie en entier |

Paires examinées et conservées (R4) : Zemmour eco1/eco2 (troisième option : suppression de tout impôt sur la fortune), Tondelier eco3/eco4 et Philippot jus6/jus7 (positions intermédiaires explicites). Elles sont déclarées dans `PAIRES_EXAMINEES` (`outils/valider.py`) pour ne plus déclencher d'alerte.

## 3. Ce qui reste fragile

- **R2 dépend des chiffres donnés par les sources** : comparer « SMIC à 1 600 € » à « +10 % » suppose de connaître le SMIC de référence. Seuls les chiffres cités par une source ont été utilisés ; les autres cas restent à « 0,5, à confirmer ».
- **Le contrôle automatique ne voit que les paires** : une incohérence entre deux mesures non reliées (par exemple sur les retraites, qui ont plusieurs âges) n'est pas détectée.
- **Le citation-extracteur a montré une faiblesse** : les guillemets imbriqués (« … "compétences" … ») coupaient la citation. Trois citations très courtes (moins de 4 mots) ont été repérées et sont exactes ; aucun autre cas tronqué.
- **Version du pack** : le pack installé a changé depuis la préversion publiée ; il porte désormais le numéro `2026.11.14-test` pour ne pas confondre deux contenus sous le même numéro.

## 4. Pistes

1. Ajouter le contrôle des citations (script de vérification mot pour mot) aux outils du dépôt, avec un test sur les guillemets imbriqués.
2. Relire les « à confirmer » par ordre de poids : d'abord les mesures quasi unanimes, puis les candidats peu couverts.
