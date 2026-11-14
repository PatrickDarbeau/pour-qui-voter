"""Positions de Nicolas Dupont-Aignan — BROUILLON à relire.

Source : relevé d'Hermès du 14/11/2026 (docs/hermes/rapports/2026-11-14_positions-dupont-aignan.md).
Chaque citation a été retrouvée mot pour mot dans la source le 14/11/2026 (vérification automatique,
césures et typographie normalisées). « À confirmer » = position déduite d'un principe général
ou d'un passage portant sur une mesure voisine.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
DATE_SOURCE = "2026-11-14"

S0 = 'https://la1ere.franceinfo.fr/nicolas-dupont-aignan-les-ultramarins-en-ont-ras-le-bol-des-petites-magouilles-politiciennes-dans-la-gestion-de-l-eau-1754289.html'
S1 = 'https://www.debout-la-france.fr/projet/culture-patrimoine/'
S2 = 'https://www.debout-la-france.fr/projet/dependance-fin-de-vie/'
S3 = 'https://www.debout-la-france.fr/projet/environnement-energie/'
S4 = 'https://www.debout-la-france.fr/projet/equilibre-territoire-monde-rural/'
S5 = 'https://www.debout-la-france.fr/projet/instruction-publique/'
S6 = 'https://www.debout-la-france.fr/projet/outre-mer/'
S7 = 'https://www.debout-la-france.fr/projet/retraites/'
S8 = 'https://www.debout-la-france.fr/projet/sante/'
S9 = 'https://www.debout-la-france.fr/projet/sciences-souverainete-industrielle/'
S10 = 'https://www.debout-la-france.fr/wp-content/uploads/2025/04/Defense-Nationale-2025_04-15-Livret.pdf'
S11 = 'https://www.debout-la-france.fr/wp-content/uploads/2025/10/Securite-2025_10-31_Livret.pdf'
S12 = 'https://www.debout-la-france.fr/wp-content/uploads/2026/01/Agriculture-2026_01-08_Livret.pdf'
S13 = 'https://www.debout-la-france.fr/wp-content/uploads/2026/03/Immigration-et-assimilation-2026_03-03_Livret.pdf'
S14 = 'https://www.debout-la-france.fr/wp-content/uploads/2026/06/Justice-2026_06-10_Livret.pdf'
S15 = 'https://www.debout-la-france.fr/wp-content/uploads/2026/06/Refonder-et-moraliser-notre-democratie-2026_06-09_Livret.pdf'
S16 = 'https://www.debout-la-france.fr/wp-content/uploads/2026/09/Logement-2026_09-30_brochure.pdf'
S17 = 'https://www.debout-la-france.fr/wp-content/uploads/2026/11/Economie-2026_11-12_Livret.pdf'

P = {
    'agri3': (1, S12, 'Ces prix garantis seront rétablis sur quelques grandes productions agricoles (lait, viande, céréales) assortis de quotas de production.', False, 'programme_pdf'),
    'agri4': (1, S12, 'Rompre les accords déloyaux de libre-échange signés par la Commission de Bruxelles, CETA, Nouvelle-Zélande, Kenya, Ukraine et Mercosur', False, 'programme_pdf'),
    'agri5': (-1, S12, 'Rompre les accords déloyaux de libre-échange signés par la Commission de Bruxelles, CETA, Nouvelle-Zélande, Kenya, Ukraine et Mercosur', False, 'programme_pdf'),
    'agri6': (0.5, S12, 'Réserver aux producteurs français 50% puis progressivement 80% des commandes publiques, notamment des cantines scolaires', False, 'programme_pdf'),
    'cult3': (0.5, S1, 'Division par 2 du budget de 4 milliards à 2 milliards.', False),
    'cult6': (1, S1, 'Remplacer le pass culture totalement dévoyé par un « ticket découverte culturelle', False),
    'cult7': (-1, S1, 'Remplacer le pass culture totalement dévoyé par un « ticket découverte culturelle', False),
    'cult8': (0.5, S1, 'Instaurer la gratuité des musées le dimanche pour tous les Français.', False),
    'ecl1': (-1, S3, "Abandonner l'objectif de 50% de nucléaire dans la production électrique en 2035, maintenir le nucléaire à 70% de la production d'électricité minimum.", False),
    'ecl2': (1, S17, 'Les programmes de construction des EPR2 et de déploiement des petits réacteurs modulaires français pour remplacer nos centrales en fin de vie seront accélérés.', False, 'programme_pdf'),
    'ecl5': (1, S17, "Sortant du marché européen de fixation du prix de l'électricité.", False, 'programme_pdf'),
    'ecl6': (-1, S17, "Sortant du marché européen de fixation du prix de l'électricité.", False, 'programme_pdf'),
    'ecl7': (1, S17, "Rétablissant le monopole de production et de distribution d'EDF.", False, 'programme_pdf'),
    'ecl8': (-1, S17, "Rétablissant le monopole de production et de distribution d'EDF.", False, 'programme_pdf'),
    'ecl9': (0.5, S17, "Supprimer les aides de l'État à l'installations des éoliennes et des panneaux solaires en annulant le décret sur la PPE3", False, 'programme_pdf'),
    'ecl10': (-1, S17, "Supprimer les aides de l'État à l'installations des éoliennes et des panneaux solaires en annulant le décret sur la PPE3", False, 'programme_pdf'),
    'eco1': (-1, S16, "Exclure la résidence principale de l'Impôt sur la Fortune Immobilière (IFI).", True, 'programme_pdf'),
    'eco2': (0.5, S16, "Exclure la résidence principale de l'Impôt sur la Fortune Immobilière (IFI).", False, 'programme_pdf'),
    'eco5': (1, S17, 'Baisser les impôts de production', False, 'programme_pdf'),
    'eco7': (1, S17, "Accorder un crédit d'impôt production pour les entreprises qui réinvestissent leurs bénéfices sur le sol français.", False, 'programme_pdf'),
    'eco9': (0.5, S17, "il est possible d'économiser 40 milliards par an au terme des 5 ans", True, 'programme_pdf'),
    'edu2': (1, S5, 'Augmenter de 15 % en 4 ans les salaires nets des professeurs.', False),
    'edu3': (1, S5, 'Uniforme obligatoire, niveau de langage minimum et vouvoiement.', False),
    'edu4': (-1, S5, 'Réformer le système Parcoursup afin de le rendre équitable et transparent.', False),
    'edu6': (1, S10, "Instaurer un service national civique obligatoire de trois mois avec option militaire d'une année", False, 'programme_pdf'),
    'edu8': (1, S5, 'Accepter les créations de classes demandées par les établissements privés pour répondre à la forte demande des familles.', True),
    'eu1': (-1, S15, "Sortir de l'Union européenne pour rapatrier nos compétences au niveau national, seul cadre de l'exercice de notre démocratie.", False, 'programme_pdf'),
    'eu2': (1, S15, "Sortir de l'Union européenne pour rapatrier nos compétences au niveau national, seul cadre de l'exercice de notre démocratie.", False, 'programme_pdf'),
    'eu3': (1, S15, "Au terme du moratoire d'un an, les Français seront consultés par référendum sur la sortie et le nouveau traité de coopération entre les peuples européens.", False, 'programme_pdf'),
    'eu4': (1, S10, "Sortir du commandement intégré de l'OTAN pour regagner notre indépendance militaire et stratégique", False, 'programme_pdf'),
    'eu5': (-1, S10, "Sortir du commandement intégré de l'OTAN pour regagner notre indépendance militaire et stratégique", False, 'programme_pdf'),
    'eu6': (0.5, S10, 'augmenter notre budget de défense pour atteindre le chiffre raisonnable de 2,5% du PIB', False, 'programme_pdf'),
    'eu7': (0.5, S10, "la possibilité leur sera ouverte de remplacer ce service civil de 3 mois par un service militaire d'un an", False, 'programme_pdf'),
    'eu8': (-1, S17, "Mettre fin aux aides à l'Ukraine", False, 'programme_pdf'),
    'eu9': (1, S17, "Mettre fin aux aides à l'Ukraine", False, 'programme_pdf'),
    'imm1': (0.5, S13, 'Supprimer le droit du sol via un référendum, tout en maintenant la possibilité de devenir Français par naturalisation.', False, 'programme_pdf'),
    'imm2': (1, S13, 'Supprimer le droit du sol via un référendum, tout en maintenant la possibilité de devenir Français par naturalisation.', False, 'programme_pdf'),
    'imm3': (-1, S13, 'Supprimer le droit du sol via un référendum, tout en maintenant la possibilité de devenir Français par naturalisation.', False, 'programme_pdf'),
    'imm4': (-1, S13, 'Durcir les règles de rapprochement familial et supprimer la régularisation pour les étrangers en situation irrégulière', False, 'programme_pdf'),
    'imm5': (1, S13, 'Durcir les règles de rapprochement familial et supprimer la régularisation pour les étrangers en situation irrégulière', False, 'programme_pdf'),
    'imm6': (1, S13, "en conditionnant le rapprochement des conjoints au revenu, au logement, à l'assimilation des principes républicains et à la maîtrise de la langue", False, 'programme_pdf'),
    'imm7': (1, S13, 'Supprimer les aides sociales non contributives pour les étrangers (RSA, allocations familiales, aides au logement…)', False, 'programme_pdf'),
    'imm8': (-1, S13, 'Supprimer les aides sociales non contributives pour les étrangers (RSA, allocations familiales, aides au logement…)', False, 'programme_pdf'),
    'imm9': (1, S13, 'Condamner les étrangers en situation irrégulière et délictueuse à une peine de prison ferme, sans accès aux aides sociales financières, et les contraindre à quitter le territoire national', False, 'programme_pdf'),
    'ins1': (1, S15, "Instaurer le référendum d'initiative citoyenne constituant (RIC) pour rendre les citoyens acteurs de l'élaboration des lois et maîtres de leur Constitution.", False, 'programme_pdf'),
    'ins3': (1, S15, 'Si le vote blanc est majoritaire, le scrutin est reporté et les candidats battus ne peuvent pas se représenter.', False, 'programme_pdf'),
    'ins4': (-1, S15, 'Si le vote blanc est majoritaire, le scrutin est reporté et les candidats battus ne peuvent pas se représenter.', False, 'programme_pdf'),
    'ins5': (1, S15, "Revenir au septennat avec la possibilité d'un référendum révocatoire d'initiative citoyenne à mi-mandat.", False, 'programme_pdf'),
    'ins6': (-1, S15, "Revenir au septennat avec la possibilité d'un référendum révocatoire d'initiative citoyenne à mi-mandat.", False, 'programme_pdf'),
    'jus1': (1, S14, 'Réinstaurer et élargir les peines planchers pour toute agression contre policiers, gendarmes, pompiers, enseignants, soignants.', False, 'programme_pdf'),
    'jus5': (1, S11, 'Créer 40 000 places de prison nouvelles', False, 'programme_pdf'),
    'jus6': (1, S14, 'Baisser la majorité pénale à 16 ans.', False, 'programme_pdf'),
    'jus7': (-1, S14, "Abroger l'ordonnance de 1945 concernant la justice des mineurs.", False, 'programme_pdf'),
    'jus8': (0.5, S14, 'la France devra faire passer le budget de la justice de 12,9 milliards à 15 milliards.', False, 'programme_pdf'),
    'jus9': (1, S14, 'Instaurer une peine de perpétuité réelle et non modifiable', False, 'programme_pdf'),
    'log4': (0.5, S16, 'Adapter la loi Solidarité et renouvellement urbain (SRU) en incluant les logements en accession sociale dans le quota des logements sociaux.', False, 'programme_pdf'),
    'log8': (0.5, S4, "Faire en sorte que chaque français dispose d'un hôpital à moins de 45 minutes en voiture", False),
    'num4': (0.5, S9, "aucune raison sécuritaire, pandémique, climatique, ne doit astreindre l'individu à une surveillance omniprésente de ses faits et gestes", True),
    'num6': (0.5, S17, "Créant une taxe sur l'exploitation des données personnelles (recettes supplémentaires de 5 milliards d'euros par an au terme de 5 ans)", False, 'programme_pdf'),
    'num7': (1, S9, 'Prendre les initiatives pour faire de la France la championne des logiciels libres et déploiement de logiciels souverains', False),
    'num8': (1, S5, "Interdiction de l'usage des objets connectés dans l'enceinte des établissements.", False),
    'num9': (1, S9, "Création d'un hébergement souverain français en remettant en cause le choix de solution des GAFAM licenciées (Cloud de Confiance)", False),
    'om1': (0.5, S6, 'Favoriser la concurrence dans la distribution afin de lutter contre la vie chère.', False),
    'om2': (0.5, S0, "s'il y a un Outre-mer qui veut être indépendant, on fait un référendum, cela ne me choque pas", False, 'presse'),
    'om5': (0.5, S6, 'Le conserver quand il y a des productions locales.', False),
    'om6': (1, S0, "C'est à l'État de reprendre l'eau potable […] je suis prêt à mettre un milliard d'euros sur la table", False, 'presse'),
    'om7': (1, S13, 'Supprimer le droit du sol via un référendum, tout en maintenant la possibilité de devenir Français par naturalisation.', False, 'programme_pdf'),
    'om8': (-1, S13, 'Supprimer le droit du sol via un référendum, tout en maintenant la possibilité de devenir Français par naturalisation.', False, 'programme_pdf'),
    'om9': (1, S6, "Améliorer la continuité territoriale en divisant par deux le prix des billets d'avion", False),
    'retr5': (1, S17, "Doter chaque nouveau-né français d'un capital de 10 000 euros qui sera bloqué jusqu'à sa retraite", False, 'programme_pdf'),
    'retr6': (-1, S17, 'un socle de retraite par capitalisation, qui viendrait en complément de la retraite par répartition', False, 'programme_pdf'),
    'retr8': (0.5, S7, 'Mieux prendre en compte la pénibilité du travail pour tous les travailleurs du privé et du public', False),
    'san1': (0.5, S8, "Faire de l'objectif de zéro poste non pourvu à l'hôpital en fin de quinquennat une priorité absolue", False),
    'san3': (1, S8, "Créer, afin de mettre fin aux déserts médicaux, une bourse pour les étudiants en médecine en échange de laquelle ils s'engageront à s'installer dans une zone sous-dotée", False),
    'san5': (1, S13, "Supprimer l'Aide Médicale d'État (AME) et mettre en place dans chaque département un dispensaire d'urgence pour les étrangers en situation irrégulière", False, 'programme_pdf'),
    'san6': (-1, S13, "Supprimer l'Aide Médicale d'État (AME) et mettre en place dans chaque département un dispensaire d'urgence pour les étrangers en situation irrégulière", False, 'programme_pdf'),
    'san8': (1, S2, "Doubler le nombre d'unités de soins palliatifs (USP) afin d'améliorer la prise en charge de la douleur", False),
    'sec1': (1, S11, '10 000 policiers et gendarmes supplémentaires nets en 5 ans.', False, 'programme_pdf'),
    'sec4': (1, S11, 'Instaurer une présomption de légitime défense pour permettre aux policiers de se défendre contre des agresseurs.', False, 'programme_pdf'),
    'sec5': (-1, S11, 'Instaurer une présomption de légitime défense pour permettre aux policiers de se défendre contre des agresseurs.', False, 'programme_pdf'),
    'soli1': (0.5, S17, 'Baisser de 40 centimes le prix des carburants', False, 'programme_pdf'),
    'soli3': (0.5, S17, 'TVA à zéro sur une liste de 50 produits de première nécessité', False, 'programme_pdf'),
    'trav1': (0.5, S17, 'Augmenter le SMIC à 1 600 euros net (98 euros supplémentaires par mois)', False, 'programme_pdf'),
    'trav7': (0.5, S17, "Nous favoriserons la cogestion en réduisant l'impôt sur les sociétés pour toute entreprise qui attribuera un pourcentage des sièges aux salariés", False, 'programme_pdf'),
    'trav8': (1, S17, 'Cette défiscalisation concernera les cotisations salariales (le net sera égal au brut).', False, 'programme_pdf'),
}
