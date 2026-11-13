# Consigne Hermès — veille du 18/11/2026 (Le Pen : réforme des retraites ; Riner : site de campagne)

Projet « Pour qui voter ? » : comparateur **neutre** des programmes de l'élection présidentielle française de 2027.
Dossier de travail : `/home/patrick/workspace/Projets/pour-qui-voter/`.

## Contexte

- Rapport du 13/11/2026 : `2026-11-13_sources-lepen-riner.md` (dans le dossier de travail). Le lire d'abord.
- **Marine Le Pen** a annoncé qu'elle présenterait le **17/11/2026** sa réforme des retraites « de manière extrêmement précise » et chiffrée. Positions déjà relevées (à confirmer) : retour de l'âge légal à 62 voire 60 ans ; retraite à 60 ans pour les carrières longues ; « véritable pilier de capitalisation ».
- **Teddy Riner** (« La France qu'on veut ») : le site de campagne, annoncé en ligne le 09/11/2026, serait `riner2027.fr` (l'Instagram vérifié affiche `contact@riner2027.fr`) ; il répondait par une erreur 530 le 13/11.

## Travail demandé

1. **Le Pen** : relever ce que la candidate a présenté le 17/11/2026 sur les retraites : âge légal, durée de cotisation, carrières longues, capitalisation, financement, pénibilité, minimum de pension, indexation. Chercher d'abord sur `marinelepen.com` et `rassemblementnational.fr` (document, page ou vidéo de présentation), puis dans la presse reconnue des 17 et 18/11 (franceinfo, Le Monde, Le Figaro, Les Échos, BFMTV, LCP, Public Sénat).
2. **Riner** : tester `https://riner2027.fr` (et `www.`). S'il répond, vérifier les mentions légales (éditeur, directeur de la publication) et relever toute page de programme ou de propositions. Sinon, noter le code d'erreur et les adresses essayées.
3. Signaler tout autre programme ou document de campagne publié depuis le 13/11 par ces deux candidats.

## Règles strictes

- Sources, par ordre de priorité : (a) site de campagne 2027 du candidat ; (b) site officiel du parti ou du mouvement ; (c) à défaut, entretien, discours ou annonce du candidat rapporté par un média reconnu, **signalé comme tel**.
- **Jamais** d'agrégateurs ni de comparateurs (votons-2027, monvote2027, poligraph, politograph, objectif2027, france-vote, programme-candidat, elysee2027, candidatspresidentielles2027, presidentielle-france, elyseescope…).
- Écarter tout document antérieur à 2026 (programme RN 2022, `mlafrance.fr`, programme de gouvernement 2024), sauf reprise explicite par la campagne 2027. Domaines parqués exclus : `marinelepen2027.fr`, `marinepresidente.fr`, `teddyriner2027.fr`.
- Citations **exactes**, entre guillemets, de moins de 30 mots, copiées du texte réellement consulté, avec l'URL et la date de publication.
- N'inventer rien : écrire « non trouvé » et lister les adresses essayées. Ton neutre, aucun jugement sur les propositions.
- Ne rien modifier d'autre que le fichier livrable. Ne créer aucune tâche programmée (cron) : les relances sont gérées par Claude.

## Livrable

Écrire le fichier `/home/patrick/workspace/Projets/pour-qui-voter/2026-11-18_veille-lepen-riner.md` :

1. Un résumé de 5 lignes au plus.
2. Un tableau `| Candidat | Thème | Proposition | Citation exacte | URL | Date | Nature de la source (campagne / parti / presse) |`.
3. Les points devenus obsolètes dans le rapport du 13/11 (par exemple l'adresse du site de Riner).
4. Les adresses essayées sans résultat et les points de vigilance.

Terminer la réponse par le chemin du fichier écrit.
