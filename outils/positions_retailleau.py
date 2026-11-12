"""Positions de Bruno Retailleau (lot 7, étape 5) — BROUILLON à relire.

Source : propositions des Républicains, dont il est le président et le candidat désigné
(https://republicains.fr/nos-propositions/ et 8 documents PDF de décembre 2025 à septembre 2026, archivés le 12/11/2026).
Attention : ce sont des propositions du parti ; la brochure « Le travail gagnant » est préfacée par le candidat.
Thèmes non couverts à ce jour par ces documents : immigration, sécurité, justice, santé, institutions, Europe.
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

P = {
    "eco5": (1, PRODUIRE, "Cotisation sur la valeur ajoutée des entreprises (CVAE) : suppression définitive", False),
    "trav2": (-1, TRAVAIL, "« Travaillez moins et vous vivrez mieux » : telle est la fausse promesse faite aux Français", True),
    "trav3": (0.5, PROP, "Refonder le code du travail sur 50 principes, rendre le reste à la négociation collective", True),
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
}
