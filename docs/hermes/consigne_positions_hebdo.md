# Consigne Hermès — veille hebdomadaire des programmes et positions

*Relance automatique chaque semaine (script `pqv_hebdo.sh`, crontab de la VM). Candidats traités : `candidats_hebdo.txt` (chaque semaine) et `candidats_rotation.txt` (un groupe par semaine, mode « complément »). Modifier ces fichiers uniquement à la demande de l'éditeur.*

Projet « Pour qui voter ? » : comparateur **neutre** des programmes de l'élection présidentielle française de 2027.
Dossier de travail : `/home/patrick/workspace/Projets/pour-qui-voter/`.

Chaque tâche traite **un seul candidat** et porte une **date de relevé** (AAAA-MM-JJ), tous deux indiqués dans le message de lancement. Lire toute cette consigne, puis ne traiter que la section de ce candidat.

## Contexte

Le comparateur demande à l'électeur son avis sur **172 mesures** réparties en 17 thèmes. **14 mesures ont été ajoutées le 14/11/2026** (eco11 à eco14, ecl11, ecl12, sec10, sec11, eu10, eu11, ins13 à ins16) : pour chaque candidat, quel que soit le mode, chercher en priorité sa position sur ces mesures. Pour chaque candidat, il faut savoir s'il **soutient**, **soutient en partie** ou **s'oppose à** chaque mesure, preuve à l'appui. Les candidats suivis chaque semaine sont ceux dont les positions sont absentes ou incomplètes ; un candidat sans position est affiché « positions non encore saisies » et n'est pas classé.

La liste des mesures se trouve dans le fichier `mesures_par_theme.md` du dossier de travail (référence de la mesure, intitulé, précision, mesure opposée). **La lire en entier avant de commencer.**

## Deux modes, indiqués dans le message de lancement

- **Mode « relevé »** (candidats sans positions ou presque) : relever toutes les positions, comme décrit ci-dessous.
- **Mode « complément »** (candidats déjà saisis) : lire d'abord la section du candidat dans `positions_actuelles.md` (positions déjà saisies dans le comparateur, avec leur source). Ne pas les recopier. Chercher en priorité :
  1. les mesures **non encore couvertes** pour lesquelles une source permet maintenant de conclure ;
  2. une **source officielle** (campagne ou parti) pour les positions marquées « à confirmer » ;
  3. toute position saisie que la source **contredit** ou que le candidat a **modifiée** (citer la nouvelle source).

## Travail demandé (pour le candidat de la tâche)

1. **Trouver les sources** : site de campagne 2027, programme (page ou PDF), site du parti ou du mouvement, puis déclarations récentes. Noter pour chaque source son URL, sa nature et sa date. Signaler si un programme complet est publié, annoncé ou absent.
2. **Relever les positions** : pour chaque mesure de `mesures_par_theme.md` sur laquelle une source permet de conclure, indiquer la position du candidat.
   **Règles de saisie (identiques pour tous les candidats, adoptées le 14/11/2026) :**
   - **R1 Valeurs** : `1` = soutient ; `0.5` = soutient en partie (version atténuée, condition, étape, échéance plus lointaine) ; `-1` = s'oppose (ou défend la mesure contraire). **Ne rien écrire** si aucune source ne permet de conclure : l'absence vaut « ne se prononce pas ». Ne jamais deviner.
   - **R2 Mesures chiffrées** : même sens et chiffre égal ou plus ambitieux = `1` ; même sens mais chiffre moins ambitieux, fourchette commençant sous le seuil, ou aucun chiffre = `0.5` ; sens contraire = `-1`. Pour comparer un montant à un pourcentage, n'utiliser que des chiffres donnés par une source ; sinon `0.5`, signalée « déduite ».
   - **R3 Renvoi dos à dos** : si le candidat rejette les deux options d'une paire de mesures opposées (« ni l'un ni l'autre »), ne rien écrire sur aucune des deux ; le signaler dans les points de vigilance.
   - **R4 Paires opposées** (colonne « mesure opposée ») : jamais `1` sur les deux ; `-1` sur les deux seulement si le candidat défend une troisième option qui exclut les deux (l'expliquer) ; `0.5` sur les deux seulement pour une position intermédiaire explicite. Soutenir l'une n'implique de s'opposer à l'autre que si la source le permet.
   - **R5 Déduite** : une position déduite d'un principe général, ou reprenant le passage d'une mesure voisine, doit être signalée « déduite » (colonne Déduite = oui). Une position tirée de la presse est signalée comme presse (colonne Nature).
3. **Changements depuis le relevé précédent** : chercher dans le dossier de travail le fichier le plus récent `*_positions-<candidat>.md` (antérieur à la date du relevé). S'il existe, le lire d'abord et indiquer ce qui est nouveau (source, programme publié, position ajoutée ou modifiée) et ce qui n'est plus valable. Ne pas recopier les positions inchangées sans les avoir revérifiées sur la source.
4. **Propositions hors catalogue** : lister les propositions importantes du candidat qui ne correspondent à aucune mesure (elles serviront à la révision du catalogue).

## Règles strictes

- Sources, par ordre de priorité : (a) site de campagne 2027 du candidat ; (b) site officiel du parti ou du mouvement ; (c) à défaut, entretien, discours ou annonce du candidat rapporté par un média reconnu (franceinfo, Le Monde, Le Figaro, Libération, Les Échos, Le Parisien, Ouest-France, AFP, BFMTV, LCP, Public Sénat, France 24…), **signalé comme presse**.
- **Jamais** d'agrégateurs ni de comparateurs (votons-2027, monvote2027, poligraph, politograph, objectif2027, france-vote, programme-candidat, elysee2027, candidatspresidentielles2027, presidentielle-france, elyseescope, candidator, republique2027…), ni Wikipédia comme source d'une position.
- Écarter les programmes des élections précédentes (2017, 2022, européennes 2024, législatives 2024), **sauf** reprise explicite dans un document de la campagne 2027 ; dans ce cas, citer le document de 2027.
- Citations **exactes**, entre guillemets, de **moins de 30 mots**, copiées du texte réellement consulté, avec l'URL de la page (ou du PDF et le numéro de page) et la date de publication.
- N'inventer rien : écrire « non trouvé » et lister les adresses essayées. Ton neutre, aucun jugement sur les propositions.
- Ne rien modifier d'autre que le fichier livrable. Ne créer aucune tâche programmée (cron) : les relances sont gérées par Claude.

## Sections par candidat (points de départ ; d'autres sources officielles peuvent exister)

### arthaud — Nathalie Arthaud (Lutte ouvrière)
- Site de campagne : `https://www.nathalie-arthaud.info` (rubrique « Nos positions », page « Élection présidentielle 2027 — Le camp des travailleurs »).
- Parti : `https://www.lutte-ouvriere.org`.

### asselineau — François Asselineau (Union populaire républicaine)
- Parti : `https://www.upr.fr` (programme, propositions, communiqués de 2026).
- `https://www.asselineau2027.fr` est réservé mais vide le 13/11/2026 : le revérifier, sans s'y limiter.

### dupont_aignan — Nicolas Dupont-Aignan (Debout la France)
- Parti : `https://www.debout-la-france.fr` (projet, propositions 2027). Chercher un éventuel site de campagne 2027.

### philippot — Florian Philippot (Les Patriotes)
- Parti : `https://les-patriotes.fr` (projet pour la France). Chercher un éventuel site de campagne 2027.

### ruffin — François Ruffin (Debout !)
- Mouvement : `https://debout.fr`. Site de député (contexte seulement) : `https://francoisruffin.fr`. Chercher un éventuel site de campagne 2027 ou un programme publié après l'échec de la primaire unitaire.

### tondelier — Marine Tondelier (Les Écologistes)
- Site de campagne : `https://marinetondelier.fr` (engagements pour 2027).
- Parti : `https://lesecologistes.fr` (projet, motions, programme 2027).

### riner — Teddy Riner (sans étiquette, « La France qu'on veut »)
- Site de campagne annoncé : `https://riner2027.fr` (erreur 530 le 13/11/2026 ; contact `contact@riner2027.fr` affiché sur son compte Instagram vérifié). Tester `https://riner2027.fr` et `https://www.riner2027.fr` ; s'ils répondent, vérifier les mentions légales.
- À défaut : entretiens et déclarations rapportés par la presse reconnue (signalés comme presse). Domaine parqué exclu : `teddyriner2027.fr`.

### Candidats en mode « complément » (déjà saisis : voir `positions_actuelles.md`)
- **attal** — Gabriel Attal (Renaissance) : `https://attalpresident.fr/programme`.
- **glucksmann** — Raphaël Glucksmann (Place publique) : `https://glucks2027.fr`, `https://place-publique.eu`.
- **lepen** — Marine Le Pen (Rassemblement national) : `https://marinelepen.com`, `https://rassemblementnational.fr`. Écarter le programme de 2022 et le site `mlafrance.fr`.
- **lisnard** — David Lisnard (Nouvelle Énergie) : `https://www.unenouvelleenergie.fr/notre-programme/`.
- **melenchon** — Jean-Luc Mélenchon (La France insoumise) : `https://melenchon2027.fr/programme/livre/`.
- **philippe** — Édouard Philippe (Horizons) : `https://www.edouardphilippe.fr/programme`.
- **retailleau** — Bruno Retailleau (Les Républicains) : `https://republicains.fr/nos-propositions/`.
- **roussel** — Fabien Roussel (Parti communiste français) : `https://www.fabienroussel2027.fr`.
- **zemmour** — Éric Zemmour (Reconquête) : `https://www.ericzemmour.fr/priorites`.

## Livrable (un fichier par candidat, dans le dossier de travail)

Nom du fichier : `<date du relevé>_positions-<candidat>.md`, par exemple `2026-11-21_positions-ruffin.md` (tirets à la place des « _ » du nom du candidat).


1. **Résumé** de 5 lignes au plus : sources trouvées, existence d'un programme complet, nombre de positions relevées.
2. **Sources** : `| URL | Nature (campagne / parti / presse) | Date | Contenu |`.
3. **Positions** : `| Réf. mesure | Intitulé (abrégé) | Valeur (1 / 0.5 / -1) | Citation exacte | URL (et page) | Date | Nature | Déduite (oui/non) |`, dans l'ordre des thèmes de `mesures_par_theme.md`.
4. **Changements depuis le relevé précédent** (ou « premier relevé ») ; en mode « complément », séparer : positions nouvelles, sources officielles trouvées pour des positions « à confirmer », positions contredites ou modifiées.
5. **Propositions hors catalogue** : `| Thème | Proposition | Citation exacte | URL |`.
6. **Adresses essayées sans résultat et points de vigilance.**

Terminer la réponse par le chemin du fichier écrit.
