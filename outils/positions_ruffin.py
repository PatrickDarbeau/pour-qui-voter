"""Positions de François Ruffin — BROUILLON à relire.

Source : relevé d'Hermès du 14/11/2026 (docs/hermes/rapports/2026-11-14_positions-ruffin.md).
Chaque citation a été retrouvée mot pour mot dans la source le 14/11/2026 (vérification automatique,
césures et typographie normalisées). « À confirmer » = position déduite d'un principe général
ou d'un passage portant sur une mesure voisine.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
DATE_SOURCE = "2026-11-14"

S0 = 'https://debout.fr/notre-manifeste/'
S1 = 'https://legrandcontinent.eu/fr/2026/02/25/pour-une-declaration-dindependance-la-doctrine-ruffin-sur-leurope'
S2 = 'https://nouspresident.fr/education-une-ecole-de-tous-les-savoirs/'
S3 = 'https://nouspresident.fr/face-a-la-crise-du-logement/'
S4 = 'https://nouspresident.fr/nos-plans-daction/'
S5 = 'https://nouspresident.fr/plan-data-centers/'
S6 = 'https://nouspresident.fr/plan-de-redressement/'
S7 = 'https://nouspresident.fr/pour-proteger-notre-industrie-relocaliser-100-produits-strategiques/'
S8 = 'https://nouspresident.fr/pour-une-democratie-en-continu-vive-les-etats-generaux/'
S9 = 'https://nouspresident.fr/pour-une-exception-agriculturelle-francaise/'
S10 = 'https://nouspresident.fr/separation-argent-etat/'
S11 = 'https://nouspresident.fr/statut-travailleurs-essentiels/'
S12 = 'https://nouspresident.fr/travaillisme-ecologique/'

P = {
    'agri1': (0.5, S9, "Nous voulons une transition vers une agriculture paysanne exigeante, l'agriculture biologique en première ligne, qui sorte pas à pas des intrants de synthèse", True),
    'agri3': (1, S9, "des prix minimums garantis, une répartition juste de l'argent public, la fin de la guerre des prix", False),
    'agri4': (1, S7, "nous proposons aussi de déclencher, dès notre arrivée au pouvoir, les mesures de sauvegarde de l'accord commercial entre l'Union européenne et le Mercosur", False),
    'agri5': (-1, S7, 'Dès notre arrivée au pouvoir, nous mettrons un terme aux négociations pour les accords de libre-échange', False),
    'agri6': (0.5, S9, 'Nous viserons un seuil de 30 % à horizon 2030 et 50 % à horizon 2035', False),
    'agri7': (0.5, S9, "Ce que nous combattons, c'est le modèle hors-sol suspendu au soja importé", True),
    'agri8': (-1, S9, "la Macronie s'allie aux fervents défenseurs des pesticides et des méga-bassines", True),
    'agri9': (0.5, S9, "la Macronie s'allie aux fervents défenseurs des pesticides et des méga-bassines", True),
    'ecl1': (-1, S12, 'Nous poursuivrons aussi la construction des six réacteurs EPR2', True),
    'ecl2': (1, S12, 'Nous poursuivrons aussi la construction des six réacteurs EPR2', False),
    'ecl3': (1, S12, 'Interdiction des vols intérieurs là où existe une alternative en train avec un trajet de moins de 4 heures', False),
    'ecl4': (0.5, S0, "C'est la taxe carbone sur l'essence des Gilets jaunes quand le kérozène des avions et le fioul des porte-conteneurs est détaxé", True),
    'ecl5': (1, S12, 'retour à un service public dont les prix de vente seront basés sur les coûts réels de production', False),
    'ecl6': (-1, S7, 'Nous ne devons plus accepter une Europe qui profite de notre électricité décarbonée, mais nous enferme dans des marchés énergétiques spéculatifs', True),
    'ecl7': (1, S12, "Nous supprimerons la concurrence sur la vente d'électricité aux consommateurs", False),
    'ecl8': (-1, S12, 'nous reviendrons progressivement à un modèle 100% public de production', True),
    'ecl9': (-1, S12, "nous poursuivrons le développement de l'énergie éolienne, car elle produit davantage en hiver", True),
    'ecl10': (0.5, S12, "nous poursuivrons le développement de l'énergie éolienne, car elle produit davantage en hiver", False),
    'eco1': (0.5, S4, 'Taxe Zucman, imposition des grandes successions, dividende climatique', False),
    'eco2': (-1, S4, 'Taxe Zucman, imposition des grandes successions, dividende climatique', True),
    'eco5': (-1, S7, "l'excès en France des impôts de production pour la seule industrie n'est pas de 15 ou 20 milliards d'euros par an, mais de moins de 5 milliards", True),
    'eco7': (1, S7, "Celui qui touche l'argent public garde les emplois, investit dans les usines, forme les salariés, respecte les sous-traitants. Sinon, il rembourse.", False),
    'eco8': (-1, S7, "Celui qui touche l'argent public garde les emplois, investit dans les usines, forme les salariés, respecte les sous-traitants. Sinon, il rembourse.", True),
    'edu1': (0.5, S2, "en augmentant le budget de l'Éducation nationale à nombre d'élèves décroissant, on peut réduire la taille des classes", False),
    'edu2': (0.5, S2, 'La revalorisation portera sur une hausse pérenne de la grille indiciaire, hors de toute logique de pacte ou de contreparties', False),
    'edu4': (0.5, S2, 'il faut remplacer Parcoursup par un système plus juste, plus transparent, et qui traite les jeunes comme des humains', False),
    'edu7': (0.5, S2, "le privé doit atteindre des objectifs de mixité sociale, et perdre son financement public s'il s'y refuse", False),
    'eu1': (-1, S1, "La France doit s'y opposer avec fermeté : la diplomatie et la défense relèvent des États et doivent le rester", False, 'presse'),
    'eu2': (1, S1, "La Commission dispose déjà d'assez de « compétences »", False, 'presse'),
    'eu4': (0.5, S1, "Nous avions raison de ne pas vouloir mettre tous nos œufs dans le panier de l'OTAN, raison de maintenir une autonomie stratégique", True, 'presse'),
    'imm4': (1, S0, 'Tous les travailleurs et travailleuses sur notre territoire doivent être régularisés pour ne plus vivre dans la peur du lendemain', False),
    'imm5': (-1, S0, 'Tous les travailleurs et travailleuses sur notre territoire doivent être régularisés pour ne plus vivre dans la peur du lendemain', True),
    'imm7': (-1, S3, "Outre la xénophobie et le racisme qui sous-tendent cette proposition, celle-ci ne serait d'aucune efficacité", False),
    'imm8': (1, S3, "Outre la xénophobie et le racisme qui sous-tendent cette proposition, celle-ci ne serait d'aucune efficacité", True),
    'ins1': (1, S8, 'Nous ferons un RIC législatif pour proposer des lois, un RIC abrogatif pour supprimer des lois injustes, un RIC constitutionnel', False),
    'ins7': (0.5, S10, 'Les candidats à un mandat électif seront obligés de présenter un bulletin n°2 du casier judiciaire vierge', False),
    'ins10': (1, S10, 'encadrer strictement le pantouflage et interdire le rétro-pantouflage', False),
    'ins11': (-1, S10, "comme l'ont fait les Lituaniens", True),
    'ins12': (0.5, S8, "imposer des réformes à coups de 49.3 contre l'avis unanime des syndicats et de l'immense majorité des Françaises et Français", True),
    'log1': (1, S3, "En plus d'étendre cet encadrement des loyers à l'ensemble des agglomérations, nous proposons de le généraliser à l'ensemble du territoire", False),
    'log2': (-1, S3, 'Nous encadrerons les loyers partout', False),
    'log3': (1, S3, "L'objectif est donc de produire chaque année 200 000 logements, dont 40 000 spécifiquement pour les étudiants et les jeunes travailleurs", False),
    'log4': (-1, S3, 'Pire encore, il souhaite abroger la loi SRU qui impose aux communes de plus de 3 500 habitants', False),
    'num7': (1, S7, 'nous proposons de développer un éco-système basé sur le logiciel libre et les communs numériques', False),
    'num8': (0.5, S2, 'mieux rémunérer les enseignants, mieux les former, bannir les smartphones des salles de classe', False),
    'num9': (1, S5, "La qualification SecNumCloud deviendra effectivement obligatoire pour héberger les données de l'État, des secteurs vitaux", False),
    'retr3': (1, S11, 'Des mesures fortes, concrètes, comme le SMIC à 1 600€ ou la retraite à 60 ans', False),
    'retr4': (-1, S0, "Le premier pas, ce sont des impôts justes et l'abrogation de la retraite à 64 ans", False),
    'retr8': (0.5, S11, 'pour quatre trimestres cotisés dans un métier exposé à la pénibilité, un trimestre supplémentaire de retraite sera accordé', False),
    'soli1': (-1, S6, 'plus ciblée que les réductions à la pompe qui couvrent tous les rouleurs', True),
    'soli2': (1, S6, 'La remise à plat des avantages fiscaux actuels est également plus ciblée que les réductions à la pompe', False),
    'trav1': (0.5, S11, 'Des mesures fortes, concrètes, comme le SMIC à 1 600€ ou la retraite à 60 ans', False),  # R2 (règles de saisie, 14/11/2026)
    'trav3': (-1, S11, 'y compris si les règles négociées sont moins favorables que la loi', True),
    'trav6': (1, S11, "nous indexerons les salaires sur l'inflation, comme cela a existé jusqu'en 1982", False),
    'trav7': (1, S8, "Par le haut : c'est un tiers de salariés dans le conseil d'administration", False),
    'trav9': (0.5, S0, "Oui nous mettons une limite à l'accumulation car elle ne peut se faire que sur le dos du travail des autres", True),
}
