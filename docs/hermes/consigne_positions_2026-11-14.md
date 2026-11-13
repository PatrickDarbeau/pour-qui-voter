# Consigne Hermès — programmes et positions de six candidats (14/11/2026)

Projet « Pour qui voter ? » : comparateur **neutre** des programmes de l'élection présidentielle française de 2027.
Dossier de travail : `/home/patrick/workspace/Projets/pour-qui-voter/`.

Chaque tâche traite **un seul candidat**, indiqué dans le message de lancement. Lire toute cette consigne, puis ne traiter que la section de ce candidat.

## Contexte

Le comparateur demande à l'électeur son avis sur **158 mesures** réparties en 17 thèmes. Pour chaque candidat, il faut savoir s'il **soutient**, **soutient en partie** ou **s'oppose à** chaque mesure, preuve à l'appui. Six candidats viennent d'être ajoutés sans aucune position ; ils sont affichés « positions non encore saisies » et ne sont pas classés.

La liste des mesures se trouve dans le fichier `mesures_par_theme.md` du dossier de travail (référence de la mesure, intitulé, précision, mesure opposée). **La lire en entier avant de commencer.**

## Travail demandé (pour le candidat de la tâche)

1. **Trouver les sources** : site de campagne 2027, programme (page ou PDF), site du parti ou du mouvement, puis déclarations récentes. Noter pour chaque source son URL, sa nature et sa date. Signaler si un programme complet est publié, annoncé ou absent.
2. **Relever les positions** : pour chaque mesure de `mesures_par_theme.md` sur laquelle une source permet de conclure, indiquer la position du candidat.
   - `1` = soutient ; `0.5` = soutient en partie (version atténuée, condition, étape) ; `-1` = s'oppose (ou défend la mesure contraire).
   - **Ne rien écrire** pour une mesure sur laquelle aucune source ne permet de conclure : l'absence vaut « ne se prononce pas ».
   - Mesures par paires opposées (colonne « mesure opposée ») : les réponses doivent être cohérentes. Soutenir l'une implique en général de s'opposer à l'autre ; ne l'écrire que si la source le permet.
   - Une position déduite d'un principe général, sans mention de la mesure, doit être signalée « déduite ».
3. **Propositions hors catalogue** : lister les propositions importantes du candidat qui ne correspondent à aucune mesure (elles serviront à la révision du catalogue).

## Règles strictes

- Sources, par ordre de priorité : (a) site de campagne 2027 du candidat ; (b) site officiel du parti ou du mouvement ; (c) à défaut, entretien, discours ou annonce du candidat rapporté par un média reconnu (franceinfo, Le Monde, Le Figaro, Libération, Les Échos, Le Parisien, Ouest-France, AFP, BFMTV, LCP, Public Sénat, France 24…), **signalé comme presse**.
- **Jamais** d'agrégateurs ni de comparateurs (votons-2027, monvote2027, poligraph, politograph, objectif2027, france-vote, programme-candidat, elysee2027, candidatspresidentielles2027, presidentielle-france, elyseescope, candidator, republique2027…), ni Wikipédia comme source d'une position.
- Écarter les programmes des élections précédentes (2017, 2022, européennes 2024, législatives 2024), **sauf** reprise explicite dans un document de la campagne 2027 ; dans ce cas, citer le document de 2027.
- Citations **exactes**, entre guillemets, de **moins de 30 mots**, copiées du texte réellement consulté, avec l'URL de la page (ou du PDF et le numéro de page) et la date de publication.
- N'inventer rien : écrire « non trouvé » et lister les adresses essayées. Ton neutre, aucun jugement sur les propositions.
- Ne rien modifier d'autre que le fichier livrable. Ne créer aucune tâche programmée (cron) : les relances sont gérées par Claude.

## Sections par candidat

### arthaud — Nathalie Arthaud (Lutte ouvrière)
- Site de campagne : `https://www.nathalie-arthaud.info` (rubrique « Nos positions », page « Élection présidentielle 2027 — Le camp des travailleurs »).
- Parti : `https://www.lutte-ouvriere.org`.
- Livrable : `2026-11-14_positions-arthaud.md`.

### asselineau — François Asselineau (Union populaire républicaine)
- Parti : `https://www.upr.fr` (programme, propositions, communiqués de 2026).
- `https://www.asselineau2027.fr` est réservé mais vide le 13/11/2026 : le revérifier, sans s'y limiter.
- Livrable : `2026-11-14_positions-asselineau.md`.

### dupont_aignan — Nicolas Dupont-Aignan (Debout la France)
- Parti : `https://www.debout-la-france.fr` (projet, propositions 2027). Chercher un éventuel site de campagne 2027.
- Livrable : `2026-11-14_positions-dupont-aignan.md`.

### philippot — Florian Philippot (Les Patriotes)
- Parti : `https://les-patriotes.fr` (projet pour la France). Chercher un éventuel site de campagne 2027.
- Livrable : `2026-11-14_positions-philippot.md`.

### ruffin — François Ruffin (Debout !)
- Mouvement : `https://debout.fr`. Site de député (contexte seulement) : `https://francoisruffin.fr`. Chercher un éventuel site de campagne 2027 ou un programme publié après l'échec de la primaire unitaire.
- Livrable : `2026-11-14_positions-ruffin.md`.

### tondelier — Marine Tondelier (Les Écologistes)
- Site de campagne : `https://marinetondelier.fr` (engagements pour 2027).
- Parti : `https://lesecologistes.fr` (projet, motions, programme 2027).
- Livrable : `2026-11-14_positions-tondelier.md`.

## Livrable (un fichier par candidat, dans le dossier de travail)

1. **Résumé** de 5 lignes au plus : sources trouvées, existence d'un programme complet, nombre de positions relevées.
2. **Sources** : `| URL | Nature (campagne / parti / presse) | Date | Contenu |`.
3. **Positions** : `| Réf. mesure | Intitulé (abrégé) | Valeur (1 / 0.5 / -1) | Citation exacte | URL (et page) | Date | Nature | Déduite (oui/non) |`, dans l'ordre des thèmes de `mesures_par_theme.md`.
4. **Propositions hors catalogue** : `| Thème | Proposition | Citation exacte | URL |`.
5. **Adresses essayées sans résultat et points de vigilance.**

Terminer la réponse par le chemin du fichier écrit.
