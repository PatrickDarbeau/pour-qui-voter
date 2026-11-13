# Consigne Hermès — veille du 23/11/2026 (Zemmour : meeting de Toulon ; Riner : site de campagne)

Projet « Pour qui voter ? » : comparateur **neutre** des programmes de l'élection présidentielle française de 2027.
Dossier de travail : `/home/patrick/workspace/Projets/pour-qui-voter/`.

## Contexte

- **Éric Zemmour** (Reconquête) tient le **21/11/2026 à Toulon** un meeting annoncé comme le lancement de sa campagne. Au 13/11, sa seule source officielle était la page « priorités » de son site (`https://www.ericzemmour.fr/priorites`, 5 priorités). Le site de Reconquête renvoie vers une plateforme participative de contributions citoyennes, qui **n'engage pas le candidat** et ne doit pas être utilisée.
- **Teddy Riner** : voir la veille du 18/11 (`2026-11-18_veille-lepen-riner.md` dans le dossier de travail, si elle existe). Le site `riner2027.fr` répondait par une erreur 530 le 13/11.

## Travail demandé

1. **Zemmour** : relever les propositions annoncées lors du meeting du 21/11/2026 et tout programme, livret ou page publiés depuis le 13/11 sur `ericzemmour.fr` ou `parti-reconquete.fr`. À défaut, utiliser la presse reconnue des 21 au 23/11 (franceinfo, Le Monde, Le Figaro, Les Échos, BFMTV, LCP, Public Sénat, Var-Matin).
2. **Riner** : retester `https://riner2027.fr` (et `www.`) ; s'il répond, vérifier les mentions légales et relever toute page de programme ou de propositions.
3. Signaler tout autre document de campagne publié depuis le 13/11 par ces deux candidats.

## Règles strictes

- Sources, par ordre de priorité : (a) site de campagne 2027 du candidat ; (b) site officiel du parti ou du mouvement ; (c) à défaut, entretien, discours ou annonce du candidat rapporté par un média reconnu, **signalé comme tel**.
- **Jamais** d'agrégateurs ni de comparateurs (votons-2027, monvote2027, poligraph, politograph, objectif2027, france-vote, programme-candidat, elysee2027, candidatspresidentielles2027, presidentielle-france, elyseescope…), ni la plateforme participative de Reconquête.
- Écarter tout document antérieur à 2026 (programme Reconquête 2022), sauf reprise explicite par la campagne 2027. Domaine parqué exclu : `teddyriner2027.fr`.
- Citations **exactes**, entre guillemets, de moins de 30 mots, copiées du texte réellement consulté, avec l'URL et la date de publication.
- N'inventer rien : écrire « non trouvé » et lister les adresses essayées. Ton neutre, aucun jugement sur les propositions.
- Ne rien modifier d'autre que le fichier livrable. Ne créer aucune tâche programmée (cron) : les relances sont gérées par Claude.

## Livrable

Écrire le fichier `/home/patrick/workspace/Projets/pour-qui-voter/2026-11-23_veille-zemmour-riner.md` :

1. Un résumé de 5 lignes au plus.
2. Un tableau `| Candidat | Thème | Proposition | Citation exacte | URL | Date | Nature de la source (campagne / parti / presse) |`.
3. Les adresses essayées sans résultat et les points de vigilance.

Terminer la réponse par le chemin du fichier écrit.
