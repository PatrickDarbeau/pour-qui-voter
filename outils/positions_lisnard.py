"""Positions de David Lisnard (lot 7, étape 5) — BROUILLON à relire.

Source : programme de Nouvelle Énergie pour 2027, https://www.unenouvelleenergie.fr/notre-programme/
(3 axes et 5 pages thématiques, archivés le 12/11/2026).
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
B = "https://www.unenouvelleenergie.fr/notre-programme/"
DESTIN, AMBITION, CIVIQUE = B + "etre-maitre-de-notre-destin/", B + "reussir-une-nouvelle-ambition-francaise/", B + "generer-un-renouveau-civique/"
AGRI, EDU, IMM, SANTE, SECU = B + "agriculture/", B + "education/", B + "immigration/", B + "sante/", B + "securite/"

P = {
    "eco5": (1, AMBITION, "La baisse de la fiscalité de production doit être intensifiée", False),
    "eco9": (0.5, DESTIN, "Pour un plan de réduction des déficits et de la dette publics", True),  # R2 (règles de saisie, 14/11/2026)
    "eco10": (-1, DESTIN, "Cette « règle d'or » s'appliquerait aux dépenses de fonctionnement mais pas à l'investissement", True),
    "trav2": (-1, AMBITION, "Les incitations à travailler davantage doivent stimuler la capacité de croissance française", True),
    "trav3": (0.5, AMBITION, "La simplification et l'assouplissement des règles du code du Travail", True),
    "retr1": (-1, AMBITION, "La norme de l'âge légal de 65 ans est un impératif national urgent", False),
    "retr2": (1, AMBITION, "La norme de l'âge légal de 65 ans est un impératif national urgent", False),
    "retr3": (-1, AMBITION, "La norme de l'âge légal de 65 ans est un impératif national urgent", False),
    "retr4": (-1, AMBITION, "La norme de l'âge légal de 65 ans est un impératif national urgent", True),
    "retr5": (1, AMBITION, "Faire évoluer tous les autres régimes vers la capitalisation", False),
    "retr6": (-1, AMBITION, "Faire évoluer tous les autres régimes vers la capitalisation", False),
    "san2": (-1, SANTE, "Cela ne passe ni par la contrainte, ni par les injonctions administratives", False),
    "san3": (1, SANTE, "La Sécurité sociale rembourse mieux les actes dans les zones sous-dotées que dans les zones saturées", False),
    "san5": (1, IMM, "Supprimer l'Aide Médicale d'État (AME) et la remplacer par une aide d'urgence", False),
    "san6": (-1, IMM, "Supprimer l'Aide Médicale d'État (AME) et la remplacer par une aide d'urgence", False),
    "edu2": (1, EDU, "Une augmentation de 20 % des rémunérations en cinq ans, conditionnée à une réorganisation profonde", False),
    "edu4": (0.5, SANTE, "Supprimer Parcoursup", True),
    "edu7": (-1, EDU, "L'enseignement privé n'est pas le problème", False),
    "edu8": (1, EDU, "Un chèque-éducation : un financement public équivalent, que la famille choisisse l'enseignement public ou privé", False),
    "ecl1": (-1, CIVIQUE, "Favoriser la production d'énergie décarbonée en s'appuyant sur le nucléaire", False),
    "ecl2": (1, CIVIQUE, "Construction d'EPR de nouvelle génération, déploiement de mini-réacteurs nucléaires", False),
    "ecl10": (-1, CIVIQUE, "« Énergies renouvelables » dérogatoires aux prix du marché […] Il faut mettre un terme à cette gabegie", True),
    "agri1": (-1, AGRI, "L'usage raisonné des phytosanitaires sur base scientifique", True),
    "agri2": (1, AGRI, "En finir avec les surtranspositions françaises, l'alignement réglementaire avec le marché commun", False),
    "agri8": (1, AGRI, "Oui aux bassines, lorsqu'elles sont techniquement justifiées et localement décidées", False),
    "agri9": (-1, AGRI, "Oui aux bassines, lorsqu'elles sont techniquement justifiées et localement décidées", False),
    "log4": (1, AMBITION, "La suppression de l'article 55 de la loi SRU […] obligeant les communes à disposer de 20 % et bientôt 25 % de logements sociaux", False),
    "log5": (-1, AMBITION, "La suppression de l'article 55 de la loi SRU", False),
    "sec1": (0.5, AMBITION, "Un plan massif de remise à niveau de la police nationale", False),
    "jus1": (1, SECU, "Rétablir les peines planchers pour les récidivistes", False),
    "jus2": (0.5, AMBITION, "Le recours plus effectif des peines alternatives à la prison", False),
    "jus5": (0.5, AMBITION, "L'augmentation des places de prison", False),  # R2 (règles de saisie, 14/11/2026)
    "jus6": (1, SECU, "Abaisser la majorité pénale à 16 ans", False),
    "jus7": (-1, SECU, "Inverser le principe de l'excuse de minorité dès 13 ans", False),
    "jus8": (0.5, AMBITION, "Donner un budget décent à la justice […] Il faut rattraper la moyenne européenne", False),
    "imm1": (1, AMBITION, "Un référendum sera nécessaire", False),
    "imm2": (0.5, IMM, "Mettre fin à l'automaticité du droit du sol", False),
    "imm3": (-1, IMM, "Mettre fin à l'automaticité du droit du sol", False),
    "imm4": (-1, AMBITION, "Supprimer toute possibilité d'être régularisé après être entré clandestinement sur le territoire", False),
    "imm5": (1, AMBITION, "Supprimer toute possibilité d'être régularisé après être entré clandestinement sur le territoire", False),
    "imm6": (1, IMM, "Conditionner le regroupement familial à des critères de ressources et des tests d'intégration", False),
    "imm7": (0.5, IMM, "Conditionner les prestations sociales non contributives aux étrangers résidant régulièrement […] depuis au moins cinq ans", True),
    "imm9": (0.5, IMM, "Expulser systématiquement les étrangers condamnés pour délits graves et les fichés S étrangers", True),
    "eu2": (1, DESTIN, "Redéfinir les compétences […] et les compétences qui doivent rester de niveau national ou régional", False),
    "eu3": (-1, DESTIN, "L'Europe institutionnelle est une conquête et un outil nécessaire", True),
}
