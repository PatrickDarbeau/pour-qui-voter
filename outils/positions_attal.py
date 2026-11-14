"""Positions de Gabriel Attal (lot 7, étape 5) — BROUILLON à relire.

Source : site de campagne https://attalpresident.fr (édité par Renaissance, directeur de la publication
Gabriel Attal), rubrique « Mes chantiers capitaux » : 4 chantiers, 2 « dettes à résorber » et 96 mesures annoncées
(34 pages archivées le 13/11/2026). Site non trouvé lors du recensement du 12/11 (le domaine
gabrielattal2027.fr redirige vers attalpresident.fr).
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
B = "https://attalpresident.fr/programme"
M = B + "/mesures/"
DETTE, EDU, FRONT, TRAV = B + "/dette-de-letat", B + "/education", B + "/frontieres", B + "/travail-salaires"

P = {
    # Finances publiques et fiscalité
    "eco9": (1, B, "Ramener le déficit sous 3% avant 2032", False),
    "eco10": (-1, DETTE, "L'objectif est clair : zéro déficit en 10 ans maximum", True),
    "eco1": (-1, M + "loi-de-stabilite-fiscale", "La suppression de l'ISF, qui [a] restauré l'attractivité du pays", False),
    "eco5": (1, M + "loi-de-stabilite-fiscale", "La CVAE, impôt qui pèse sur la production et nous désavantage, disparaît", False),
    # Travail et retraites
    "trav1": (-1, M + "test-pme-avant-chaque-loi", "Son programme économique tient en trois mots : débureaucratiser, désmicardiser, déverrouiller", True),
    "trav4": (1, TRAV, "Je porte une réforme de l'assurance chômage qui incite au travail", True),
    "trav5": (-1, TRAV, "Réformer l'assurance chômage et réaliser cinq milliards d'économies", False),
    "retr5": (1, M + "capitalisation-startups", "Introduire un véritable pilier de capitalisation dans le système de retraite, à côté de la répartition", False),
    "retr6": (-1, M + "capitalisation-startups", "La retraite par répartition ne peut plus reposer sur le seul rapport entre actifs et retraités", False),
    "retr4": (-1, B, "Les petites pensions protégées, et l'âge légal remplacé par la durée de cotisation", True),
    "retr1": (-1, M + "aucune-hausse-impots", "Année blanche, réforme de l'assurance chômage, nouvelle réforme des retraites", True),
    # Pouvoir d'achat
    "soli2": (1, M + "aides-directes-plutot-que-baisses-de-taxes", "Une baisse de taxe générale profite d'abord aux plus aisés", False),
    "soli3": (-1, M + "aides-directes-plutot-que-baisses-de-taxes", "Une baisse de taxe générale profite d'abord aux plus aisés et elle finit toujours par être payée plus tard", True),
    "soli1": (-1, M + "aides-directes-plutot-que-baisses-de-taxes", "Des aides directes plutôt que des baisses de taxes [sur les carburants]", True),
    # Éducation et numérique
    "edu2": (0.5, EDU, "200 à 500 euros nets de plus par mois pour les enseignants", False),  # R2 (règles de saisie, 14/11/2026)
    "num1": (1, EDU, "Nous irons au bout de leur interdiction pour les moins de 15 ans", False),
    # Agriculture
    "agri3": (1, B, "Des prix planchers indexés sur les coûts de production", False),
    "agri4": (1, B, "Refuser le traité Mercosur", False),
    "agri5": (-1, B, "Refuser le traité Mercosur", False),
    # Justice et immigration
    "jus6": (0.5, M + "comparution-immediate-mineurs", "Ouvrir la comparution immédiate aux mineurs récidivistes", True),
    "jus7": (-1, M + "comparution-immediate-mineurs", "Les mineurs de 2026 ne sont plus ceux de 1945, mais le droit, lui, n'a pas bougé", True),
    "jus9": (0.5, B, "Instaurer la perpétuité réelle pour les prédateurs sexuels en série", False),
    "imm6": (1, M + "durcir-regroupement-familial", "Durcir les exigences de revenus, de logement et de durée de résidence pour demander le regroupement familial", False),
    # Institutions, Europe, défense
    "ins1": (0.5, M + "journee-referendaire-annuelle", "Une journée par an consacrée à des référendums sur les grands choix du pays", True),
    "eu1": (1, FRONT, "La défense de l'Europe repose en partie sur nos épaules, nous devons les renforcer", True),
    "eu2": (-1, FRONT, "La défense de l'Europe repose en partie sur nos épaules", True),
    "eu6": (0.5, FRONT, "Nous avons commencé notre réarmement avec des hausses historiques en matière de défense depuis 2017", True),
}
