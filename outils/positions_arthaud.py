"""Positions de Nathalie Arthaud — BROUILLON à relire.

Source : relevé d'Hermès du 14/11/2026 (docs/hermes/rapports/2026-11-14_positions-arthaud.md).
Chaque citation a été retrouvée mot pour mot dans la source le 14/11/2026 (vérification automatique,
césures et typographie normalisées). « À confirmer » = position déduite d'un principe général
ou d'un passage portant sur une mesure voisine.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
Règle R3 (renvoi dos à dos, docs/regles_saisie_positions.md) : agri4/agri5 (Mercosur) et eu1/eu2 non saisies.
"""
DATE_SOURCE = "2026-11-14"

S0 = 'https://www.lutte-ouvriere.org/journal/article/campagne-nathalie-arthaud-209794.html'
S1 = 'https://www.lutte-ouvriere.org/journal/article/retraites-toujours-mensonges-194912.html'
S2 = 'https://www.lutte-ouvriere.org/medias/document/fichiers/2026/06/brochure-ete-2026.pdf'
S3 = 'https://www.lutte-ouvriere.org/medias/document/fichiers/2026/11/Depliant-NA-3nov.pdf'
S4 = 'https://www.lutte-ouvriere.org/portail/breves/retraites-campagne-grand-patronat-197487.html'
S5 = 'https://www.lutte-ouvriere.org/portail/editoriaux/pouvoir-dachat-faut-augmenter-salaires-209689.html'
S6 = 'https://www.lutte-ouvriere.org/portail/qui-sommes-nous/libre-echange-protectionnisme-deux-politiques-bourgeoisie-165657'
S7 = 'https://www.lutte-ouvriere.org/portail/qui-sommes-nous/qui-sommes-nous-ecologie'
S8 = 'https://www.lutte-ouvriere.org/portail/qui-sommes-nous/qui-sommes-nous-europe'
S9 = 'https://www.lutte-ouvriere.org/portail/qui-sommes-nous/qui-sommes-nous-nos-idees-et-positions-politiques-logement-un-droit-fondamental-conquerir'
S10 = 'https://www.lutte-ouvriere.org/portail/qui-sommes-nous/qui-sommes-nous-nos-idees-et-positions-politiques-quitter-lunion-europeenne-et-retrouver-de-la-souverainete-une-diversion-et-un-mensonge'
S11 = 'https://www.lutte-ouvriere.org/portail/qui-sommes-nous/travailleurs-francais-immigres-laissons-diviser-164193'

P = {
    'ecl1': (-1, S7, 'Le principal danger du nucléaire ne réside pas dans la technique elle-même', True),
    'eco5': (-1, S2, 'Pour réduire les impôts de ces grands groupes, financer leurs investissements, les exonérer de cotisations sociales, ils démolissent les droits des travailleurs', True, 'programme_pdf'),
    'eco6': (1, S2, 'Levée du secret commercial et du secret des affaires pour rendre publics les comptes de ces grandes entreprises, y compris ceux qui sont cachés !', False, 'programme_pdf'),
    'eco9': (-1, S0, "le gouvernement brandit cette dette comme s'il braquait la population avec une arme, elle sert de prétexte pour justifier les attaques", True),
    'edu4': (1, S3, "contre des conditions d'éducation indignes et la sélection dans le système éducatif", True, 'programme_pdf'),
    'edu5': (-1, S3, "contre des conditions d'éducation indignes et la sélection dans le système éducatif", True, 'programme_pdf'),
    'edu6': (-1, S3, 'les discours se multiplient pour préparer la jeunesse à mourir « pour la patrie', True, 'programme_pdf'),
    'eu3': (-1, S10, "Sortir de l'Union européenne ne réglera pas les problèmes des travailleurs.", False),
    'eu6': (-1, S2, "Ministres et députés imposent l'austérité budgétaire mais votent 36 milliards de rallonge pour l'armée quasiment sans discussion.", True, 'programme_pdf'),
    'eu7': (-1, S3, 'les discours se multiplient pour préparer la jeunesse à mourir « pour la patrie', True, 'programme_pdf'),
    'eu8': (-1, S2, "Chaque missile lancé au-dessus du golfe Persique, chaque Rafale qui vole dans le ciel de l'Ukraine vient remplir un peu plus leurs coffres-forts.", True, 'programme_pdf'),
    'imm4': (1, S2, "Régularisation de tous les sans-papiers, liberté de circulation et d'installation pour chaque être humain de cette planète !", False, 'programme_pdf'),
    'imm5': (-1, S2, "Régularisation de tous les sans-papiers, liberté de circulation et d'installation pour chaque être humain de cette planète !", True, 'programme_pdf'),
    'imm7': (-1, S11, 'La « préférence nationale', False),
    'imm8': (1, S11, 'quelle que soient leur origine, leur nationalité et leur religion, pour défendre leurs droits', True),
    'imm9': (-1, S2, "À bas les barbelés, les traques, les expulsions ! À bas l'Europe-forteresse !", True, 'programme_pdf'),
    'log3': (0.5, S9, "planifier la construction ou la rénovation du nombre de logements nécessaires à l'échelle de la société", True),
    'retr2': (-1, S4, 'Âge de départ repoussé à 65 ans, 45 années de cotisation pour espérer toucher une pension complète… Édouard Philippe relaie les revendications révoltantes du Medef.', False),
    'retr4': (-1, S3, 'les travailleurs usés par les années sont forcés de continuer de plus en plus tard', True, 'programme_pdf'),
    'retr5': (-1, S2, "la suppression de la notion d'âge légal de départ et la mise en place d'un système par capitalisation. Voilà le vrai visage du « candidat du peuple", True, 'programme_pdf'),
    'retr6': (1, S1, "C'est dans les caisses, bien remplies, des capitalistes qu'il faut puiser pour payer l'intégralité des retraites des travailleurs.", True),
    'san1': (1, S2, "Si nous demandions au personnel des hôpitaux, des Ehpad […] d'établir une liste d'embauches […] des centaines de milliers d'emplois à créer tout de suite !", True, 'programme_pdf'),
    'san9': (1, S2, 'Ils veulent baisser les salaires, les pensions et les allocations, réduire les indemnités des chômeurs, rembourser encore moins les soins et les médicaments…', True, 'programme_pdf'),
    'soli3': (-1, S5, 'Les politiciens qui proposent de baisser les taxes ou les cotisations sociales pour augmenter le salaire net nous tendent un piège.', True),
    'trav1': (1, S3, "Exigeons L'AUGMENTATION des salaires, des retraites et des pensions, le SMIC à 2 200 € et leur INDEXATION sur l'inflation.", False, 'programme_pdf'),
    'trav2': (0.5, S2, 'Il faut baisser le temps et la charge de travail sans perte de salaire pour permettre à tous de vivre.', False, 'programme_pdf'),
    'trav3': (-1, S2, "ils voudraient que l'on travaille plus en gagnant moins", True, 'programme_pdf'),
    'trav4': (-1, S3, 'Les grands patrons et le gouvernement fabriquent le chômage et en plus ils osent dénigrer les chômeurs pour réduire leurs droits.', True, 'programme_pdf'),
    'trav6': (1, S2, 'augmentation massive des salaires, des allocations et des pensions et leur indexation sur la hausse des prix', False, 'programme_pdf'),
}
