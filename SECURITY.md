# Sécurité

*English summary: please report security issues privately via GitHub's “Report a vulnerability” button (Security tab), never in a public issue. Answers are given in French or English.*

« Pour qui voter ? » est un outil civique : sa valeur tient à la **fiabilité de ses données** autant qu'à celle de son code. Une position de candidat falsifiée est, pour ce projet, un problème de sécurité au même titre qu'une faille dans le code.

## Signaler une faille

**En privé uniquement.** Ne publiez pas de ticket public pour une faille : elle serait visible de tous avant d'être corrigée.

1. Ouvrez l'onglet **Security** du dépôt, puis **Report a vulnerability** (signalement privé de GitHub).
2. Décrivez le problème, la version concernée (numéro du pack ou de la préversion) et, si possible, les étapes pour le reproduire.

Seul le mainteneur du projet voit ces signalements.

## Ce qui relève de ce canal

- **Intégrité des données** : pack de données modifié, archive publiée dont l'empreinte SHA-256 ne correspond pas à celle indiquée, position ou citation altérée en dehors du circuit de saisie documenté.
- **Application** : exécution de code non prévue (par exemple par un fichier importé dans le mode Édition), contournement de la politique de sécurité du contenu, requête réseau inattendue (l'application n'en fait aucune).
- **Chaîne de publication** : workflow GitHub Actions, site de démonstration (GitHub Pages), préversions.

## Ce qui n'en relève pas

Un **désaccord sur une position**, une citation que vous jugez inexacte, une formulation de mesure que vous estimez orientée ou une proposition absente : utilisez les [tickets publics](https://github.com/PatrickDarbeau/pour-qui-voter/issues). Ces échanges ont vocation à être publics, par transparence.

## Délais

Le projet est maintenu par une seule personne, bénévolement. Objectifs :

- **accusé de réception** sous 7 jours ;
- **premier diagnostic** sous 14 jours ;
- **correction** dès que possible, en priorité absolue pendant la campagne présidentielle.

Une fois la faille corrigée, elle est décrite publiquement, avec votre accord, en vous créditant si vous le souhaitez.

## Versions suivies

Seuls la **dernière version publiée** et le site de démonstration sont corrigés. Les préversions plus anciennes ne le sont pas : téléchargez la plus récente depuis la page [Releases](https://github.com/PatrickDarbeau/pour-qui-voter/releases).

## Vérifier une archive téléchargée

Chaque archive publiée est accompagnée de son empreinte SHA-256 (fichier `.sha256` de même nom). Pour la vérifier :

- Windows (PowerShell) : `Get-FileHash .\pour-qui-voter-<version>.zip -Algorithm SHA256`
- macOS / Linux : `sha256sum pour-qui-voter-<version>.zip`

Si l'empreinte diffère de celle de la page Releases, n'utilisez pas l'archive et signalez-le.
