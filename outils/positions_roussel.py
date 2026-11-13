"""Positions de Fabien Roussel (lot 7, étape 5) — BROUILLON à relire.

Sources (archivées le 13/11/2026) :
  - site de campagne https://www.fabienroussel2027.fr : manifeste « VIVRE ! » (sans mesures chiffrées) et page « Matériel » ;
  - plan « Jeunesse 2027-2032 » (document de campagne, 12 p.), seul programme détaillé publié par la campagne ;
  - PCF, son parti : « Cahiers thématiques des Jours heureux » (Sécurité sociale, Logement, Mobilités, Paix & défense),
    documents du parti antérieurs à la campagne → positions tirées de ces cahiers marquées « à confirmer » si elles
    ne sont pas reprises par la campagne.
Pas encore de programme présidentiel complet : couverture volontairement limitée à ce qui est écrit.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
SITE = "https://www.fabienroussel2027.fr"
MAT = SITE + "/materiel"
NB = "https://assets.nationbuilder.com/pcf/pages/"
PJ = NB + "44609/attachments/original/1791282014/Plan_Jeunesse_2027-2032.pdf"
SECU = NB + "36196/attachments/original/1766073347/document_-_cahier_se%CC%81cu_v2.pdf"
LOG = NB + "36197/attachments/original/1766073372/document_-_cahier_logement_ppp.pdf"
MOB = NB + "36198/attachments/original/1766073432/document_-_cahier_mobilite_ppp.pdf"
PAIX = NB + "41211/attachments/original/1779954906/document_cahier_paix_ppp_stc.pdf"

P = {
    # Plan Jeunesse 2027-2032 (campagne)
    "edu1": (1, PJ, "Les classes compteront 2 à 4 élèves de moins, soit 18 à 19 élèves au primaire", False),
    "edu2": (0.5, PJ, "Ces recrutements s'accompagneront de la fin du gel du point d'indice, ainsi que d'une hausse des salaires", True),
    "edu4": (1, PJ, "Parcoursup et MonMaster seront supprimés et la sélection à l'entrée de l'université prendra fin", False),
    "edu5": (-1, PJ, "Parcoursup et MonMaster seront supprimés et la sélection à l'entrée de l'université prendra fin", False),
    "eu6": (-1, PJ, "3,5 Md€ passent du budget de la défense à celui de l'école", True),
    # Site de campagne
    "eco7": (1, SITE, "Des centaines de milliards d'argent public […] sont donnés sans contrepartie aux grandes entreprises", True),
    "soli1": (1, MAT, "Affiche Blocage des prix", True),
    "ecl7": (0.5, MAT, "Affiche L'énergie est notre avenir, nationalisons-la", True),
    # Cahier « Sécurité sociale » (PCF)
    "retr3": (1, SECU, "La retraite à 60 ans, un impératif !", False),
    "retr1": (1, SECU, "La retraite à 60 ans, un impératif !", True),
    "retr2": (-1, SECU, "La retraite à 60 ans, un impératif !", True),
    "retr4": (-1, SECU, "La retraite à 60 ans, un impératif !", True),
    "retr5": (-1, SECU, "La capitalisation « système cannibale »", False),
    "retr6": (1, SECU, "Développer les cotisations sociales, contre la fiscalisation", True),
    "retr8": (0.5, SECU, "Les carrières longues et la pénibilité doivent être pris en compte pour l'âge de départ", True),
    "san4": (0.5, SECU, "Le 100 % passe par le développement des services publics", True),
    # Cahier « Logement » (PCF)
    "log1": (1, LOG, "Généraliser l'encadrement des loyers", False),
    "log2": (-1, LOG, "Généraliser l'encadrement des loyers", True),
    "log3": (1, LOG, "Créer 200 000 nouveaux logements sociaux par an", False),
    "log4": (-1, LOG, "Nous voulons renforcer cette loi SRU : en élevant les critères à 30 % de logements sociaux", False),
    "log5": (1, LOG, "En durcissant les sanctions à l'encontre des maires qui ne souhaitent pas construire", False),
    # Cahier « Mobilités » (PCF)
    "log6": (1, MOB, "Nous rappelons dans ce cadre notre volonté de nationaliser les autoroutes", False),
    "log7": (-1, MOB, "Notre volonté de nationaliser les autoroutes, dont la privatisation a constitué un scandaleux hold-up", True),
    "log9": (0.5, MOB, "Faire baisser de 30 % les billets de train, tendre vers la gratuité des TER et des transports en commun", False),
    "ecl4": (1, MOB, "L'absence de taxation sur le kérosène, aberration économique et écologique", False),
    # Cahier « Paix & défense nationale » (PCF)
    "eu4": (0.5, PAIX, "La réintégration de la France dans le commandement intégré de l'OTAN en 2007 [citée parmi les reculs]", True),
    "eu9": (0.5, PAIX, "Nous dénonçons le refus de l'UE et de la France de prendre la moindre initiative de paix", True),
}
