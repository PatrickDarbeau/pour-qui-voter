"""Positions de Bruno Retailleau (lot 7, étape 5) — BROUILLON à relire.

Source : propositions des Républicains, dont il est le président et le candidat désigné
(https://republicains.fr/nos-propositions/ et 8 documents PDF de décembre 2025 à septembre 2026, archivés le 12/11/2026).
Attention : ce sont des propositions du parti ; la brochure « Le travail gagnant » est préfacée par le candidat.
Complété le 12/11/2026 par ses tribunes et entretiens publiés sur le site de LR (rubrique du candidat).
Thèmes encore peu couverts : sécurité, santé (hors fin de vie), outre-mer, culture, numérique.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
U = "https://republicains.fr/wp-content/uploads/"
PROP = "https://republicains.fr/nos-propositions/"
TRAVAIL = U + "2026/01/51705_LesRepublicains_Brochures_A5-40P_DEF.pdf"
PRODUIRE = U + "2026/02/LR_Produire_Plus_LIVRET.pdf"
AGRI = U + "2026/03/LR_Agriculture.pdf"
ELEC = U + "2026/05/LR_Electricite_vFF070626.pdf"
LOGEMENT = U + "2026/05/LR_Logement.pdf"
IA = U + "2026/07/LR_IA.pdf"
ECOLE = U + "2026/09/LR_Ecole_vF.pdf"
A = "https://republicains.fr/actualites/"
TRIB_TRAVAIL = A + "2026/05/02/priorite-travail-france-35h-salaires-retraites/"
ENT_CONSTIT = A + "2026/09/02/en-france-la-seule-cour-supreme-cest-le-peuple-je-lui-donnerai-le-dernier-mot/"
ENT_SCHENGEN = A + "2026/08/02/lespace-schengen-doit-etre-reserve-aux-europeens/"
ENT_JUSTICE = A + "2026/06/06/il-faut-creer-une-cour-disciplinaire-de-la-magistrature/"
VIDEO_FIN_VIE = A + "2026/07/15/une-grande-nation-ne-repond-pas-a-la-souffrance-par-la-mort/"

P = {
    "eco5": (1, PRODUIRE, "Cotisation sur la valeur ajoutée des entreprises (CVAE) : suppression définitive", False),
    "trav2": (-1, TRIB_TRAVAIL, "Instaurer la Priorité Travail, c'est sortir des 35 heures par le haut", False),
    "trav3": (1, TRIB_TRAVAIL, "Que l'organisation du temps de travail soit laissée à la négociation collective […] en arrêtant de se référer à une durée hebdomadaire de 35 heures", False),
    "trav4": (1, TRAVAIL, "Elle réduit la durée maximale d'indemnisation, adapte les droits en fonction de la conjoncture", False),
    "trav5": (-1, TRAVAIL, "Réformer l'assurance chômage, en resserrant les conditions d'indemnisation", False),
    "trav8": (1, TRAVAIL, "Au-delà [de 1 623 heures], les heures travaillées sont exonérées de cotisations sociales, salariales comme patronales", False),
    "retr5": (1, PRODUIRE, "Notre proposition de créer un étage de retraite par capitalisation pour tous", False),
    "retr6": (-1, PRODUIRE, "Créer un étage de retraite par capitalisation pour tous", False),
    "soli4": (0.5, TRAVAIL, "Si elle s'investit dans une formation ou une recherche active d'emploi, justifiant d'au moins quinze heures d'activité hebdomadaires, son RIA est complété", True),
    "edu2": (0.5, ECOLE, "135 euros nets de plus par mois en début de carrière, jusqu'à 300 euros en milieu", False),
    "edu4": (-1, ECOLE, "Rétablir l'évaluation qui dit la vérité et la sélection au mérite", True),
    "edu5": (1, ECOLE, "Rétablir l'évaluation qui dit la vérité et la sélection au mérite", True),
    "ecl1": (-1, PROP, "Inscrire le parc nucléaire dans une trajectoire « 80 ans »", False),
    "ecl2": (1, ELEC, "Nous confirmerons la commande de huit EPR2 supplémentaires dès les deux premières années du mandat", False),
    "ecl9": (0.5, PRODUIRE, "Nous mettrons fin aux soutiens publics aux nouvelles capacités solaires et éoliennes et reporterons les projets déjà autorisés", False),
    "ecl10": (-1, PRODUIRE, "Nous mettrons fin aux soutiens publics aux nouvelles capacités solaires et éoliennes", False),
    "agri1": (-1, AGRI, "Même marché, même règles : interdiction des sur-transpositions", True),
    "agri2": (1, AGRI, "Aligner nos règles sur l'Europe, pas au-delà", False),
    "agri4": (0.5, PRODUIRE, "La France portera au niveau européen l'imposition systématique de clauses de réciprocité dans tous les accords commerciaux", True),
    "agri8": (1, PRODUIRE, "Déclaration des retenues d'eau agricoles comme étant d'Intérêt général majeur", False),
    "agri9": (-1, PRODUIRE, "Déclaration des retenues d'eau agricoles comme étant d'Intérêt général majeur", False),
    "log1": (-1, LOGEMENT, "Nous supprimerons l'encadrement des loyers", False),
    "log2": (1, LOGEMENT, "Nous supprimerons l'encadrement des loyers", False),
    "log4": (0.5, LOGEMENT, "Les quotas aveugles de la loi SRU, imposés depuis Paris, laisseront place à des contrats fondés sur les besoins réels des territoires", False),
    "log5": (-1, LOGEMENT, "Les quotas aveugles de la loi SRU […] laisseront place à des contrats", False),
    "num4": (-1, IA, "Refuser a priori ces technologies quand nos voisins les utilisent, c'est a[ccepter un retard]", True),
    "num5": (0.5, IA, "Garanties […] interdiction de la reconnaissance faciale en temps réel dans l'espace public à des fins de surveillance de masse", True),
    "num9": (1, IA, "Héberger les données sensibles (État, santé, secteurs vitaux) en Europe, à la norme SecNumCloud", False),
    # --- Tribunes et entretiens du candidat (site de LR)
    "retr1": (-1, TRIB_TRAVAIL, "Nous ne ferons pas l'économie de partir un peu plus tard à la retraite", False),
    "retr2": (0.5, TRIB_TRAVAIL, "Nous ne ferons pas l'économie de partir un peu plus tard à la retraite, en prenant en compte […] la pénibilité", True),
    "retr3": (-1, TRIB_TRAVAIL, "Nous ne ferons pas l'économie de partir un peu plus tard à la retraite", False),
    "retr4": (-1, TRIB_TRAVAIL, "Nous ne ferons pas l'économie de partir un peu plus tard à la retraite", True),
    "retr8": (0.5, TRIB_TRAVAIL, "En prenant en compte, évidemment, la pénibilité des métiers", False),
    "soli9": (1, TRIB_TRAVAIL, "Un revenu familial, pour aider toutes les familles : 240 euros pour chaque enfant, quel que soit le niveau de revenus des parents", False),
    "imm7": (0.5, TRIB_TRAVAIL, "Pour en bénéficier, les nouveaux venus devront justifier de cinq ans d'activité", True),
    "imm8": (-1, ENT_CONSTIT, "La fin des aides sociales automatiques pour les étrangers […] serait appliquée aujourd'hui", True),
    "imm1": (0.5, ENT_CONSTIT, "Le peuple français doit pouvoir décider, par référendum, de toute question législative […] la politique migratoire", True),
    "ins1": (0.5, ENT_CONSTIT, "Alléger les contraintes nécessaires à l'organisation d'un référendum d'initiative partagée : plutôt que 5 millions de signatures, il en faudrait moitié moins", True),
    "eu1": (-1, ENT_SCHENGEN, "Je ne suis pas du tout fédéraliste", False),
    "eu2": (1, ENT_CONSTIT, "Remettre le droit de l'UE à sa juste place : au-dessus des lois […] mais en dessous de notre Constitution", False),
    "eu3": (-1, ENT_CONSTIT, "Sinon, c'est un Frexit juridique, que je ne souhaite pas", False),
    "jus6": (0.5, ENT_JUSTICE, "Le Conseil constitutionnel a censuré un texte pourtant timide sur le durcissement de la justice des mineurs", True),
    "jus7": (-1, ENT_JUSTICE, "Le Conseil constitutionnel a censuré un texte pourtant timide sur le durcissement de la justice des mineurs", True),
    "san7": (-1, VIDEO_FIN_VIE, "Une grande nation ne répond pas à la souffrance par la mort", False),
}
