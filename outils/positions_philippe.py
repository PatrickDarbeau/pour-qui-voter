"""Positions d'Édouard Philippe (lot 7, étape 5) — BROUILLON à relire.

Source : programme du site de campagne https://www.edouardphilippe.fr/programme
(15 pages thématiques « mises à jour le 12 novembre 2026 », archivées le même jour).
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
B = "https://www.edouardphilippe.fr/programme/"
CP, DEF, ECOLE, ENER, ENTR, FAM = B + "comptes-publics", B + "defense", B + "ecole", B + "energie", B + "entreprises", B + "famille"
IMM, JUS, OM, RET, SEC, TRAV, ADA = B + "immigration", B + "justice", B + "outre-mer", B + "retraites", B + "securite", B + "travail", B + "adaptation-climatique"

P = {
    "eco1": (-1, CP, "Ne créer aucun nouvel impôt pendant cinq ans", True),
    "eco5": (1, ENTR, "50 milliards d'euros d'impôts de production en moins contre 50 milliards d'euros d'aides en moins", False),
    "eco9": (1, CP, "Ramener le déficit de plus de 5 % à 2 % de la richesse nationale à la fin du mandat", False),
    "eco10": (-1, CP, "Une règle inscrite dans la Constitution qui interdira aux parlementaires de creuser le déficit", True),
    "trav2": (-1, TRAV, "Permettre aux entreprises de fixer librement leur temps de travail […] pour sortir des 35 heures", False),
    "trav3": (1, TRAV, "Permettre aux entreprises de fixer librement leur temps de travail, par accord d'entreprise", False),
    "trav4": (1, TRAV, "Limiter l'indemnisation chômage à 12 mois au maximum, contre 18 mois aujourd'hui", False),
    "trav5": (-1, TRAV, "Limiter à 12 mois l'indemnisation chômage des moins de 50 ans", False),
    "trav8": (1, TRAV, "Les heures au-dessus de 35 h seront exonérées de cotisations sociales et d'impôt sur le revenu", False),
    "retr1": (-1, RET, "Porter progressivement l'âge de départ à 65 ans et la durée de cotisation à 45 ans", False),
    "retr2": (1, RET, "Porter progressivement l'âge de départ à 65 ans et la durée de cotisation à 45 ans en moins de dix ans", False),
    "retr3": (-1, RET, "Pourquoi Édouard Philippe refuse-t-il la retraite à 60 ans ?", False),
    "retr4": (-1, RET, "Porter progressivement l'âge de départ à 65 ans", False),
    "retr5": (1, RET, "Généraliser la capitalisation collective à tous les salariés et ouvrir un plan d'épargne retraite à chaque Français", False),
    "retr6": (-1, RET, "Généraliser la capitalisation collective à tous les salariés", False),
    "retr8": (0.5, RET, "Que la définition des critères de pénibilité soit négociée avec les partenaires sociaux", True),
    "soli9": (1, FAM, "Verser une allocation familiale de 350 € par mois dès le premier enfant", False),
    "edu1": (0.5, ECOLE, "Diminuer la taille des classes en maternelle et en primaire", True),
    "edu2": (1, ECOLE, "Augmenter de 20 % en moyenne le salaire des enseignants pendant le quinquennat", False),
    "num8": (1, ECOLE, "Interdire strictement le téléphone portable à l'école primaire, au collège et au lycée", False),
    "ecl1": (-1, ENER, "Relancer le nucléaire", False),
    "ecl2": (1, ENER, "Le lancement de 8 réacteurs EPR supplémentaires en plus des 6 déjà prévus", False),
    "ecl10": (0.5, ENER, "Développer les renouvelables là où elles sont efficaces", False),
    "agri2": (1, ADA, "Zéro surtransposition normative pour l'agriculture française", False),
    "agri8": (1, ADA, "Édouard Philippe est-il pour les réserves d'eau agricoles, les bassines ? Oui.", False),
    "agri9": (-1, ADA, "Accélérer le stockage de l'eau par les agriculteurs, en plaçant « la protection avant la procédure »", False),
    "om4": (-1, OM, "Édouard Philippe veut-il supprimer l'octroi de mer ? Non, il veut le moderniser", False),
    "om5": (0.5, OM, "Il reconnaît les avantages de cet impôt ancien […] Mais il manque de transparence", False),
    "om6": (0.5, OM, "Garantir dans la durée, jusqu'en 2032, les financements de l'eau à Mayotte", False),
    "om7": (0.5, OM, "La suspension totale du droit du sol à Mayotte pendant plusieurs années", False),
    "om8": (-1, OM, "La suspension totale du droit du sol à Mayotte pendant plusieurs années", False),
    "num4": (-1, SEC, "Édouard Philippe est-il pour la reconnaissance faciale ? Oui, de façon ciblée", False),
    "num5": (0.5, SEC, "[Reconnaissance faciale] dans le cadre de l'état d'urgence contre le narcotrafic et en cas d'émeutes", False),
    "sec8": (-1, SEC, "Édouard Philippe veut-il punir les consommateurs de drogue ? Oui", False),
    "sec9": (1, SEC, "Des amendes réellement payées, au besoin prélevées sur les prestations sociales", False),
    "jus1": (1, JUS, "Le rétablissement des peines planchers", False),
    "jus5": (1, JUS, "Une loi d'accélération de la construction de prisons", False),
    "jus6": (0.5, JUS, "Lever l'excuse de minorité pour les faits liés au narcotrafic et créer la comparution immédiate des mineurs", True),
    "jus7": (-1, JUS, "Lever l'excuse de minorité pour les faits liés au narcotrafic", True),
    "imm4": (-1, IMM, "Pas de régularisation massive […] il préfère […] des quotas pour choisir notre immigration économique", True),
    "imm5": (1, IMM, "Pas de régularisation massive", True),
    "imm6": (1, IMM, "Un moratoire sur le regroupement familial", False),
    "imm7": (0.5, IMM, "Aligner les aides sociales versées aux étrangers sur la moyenne européenne", True),
    "imm9": (1, IMM, "Utiliser les centres de retour […] pour que les décisions d'éloignement soient enfin exécutées", False),
    "eu7": (-1, DEF, "Édouard Philippe mise d'abord sur l'engagement […] service militaire volontaire de 3 000 à 50 000 places", True),
    "eu8": (1, DEF, "Un soutien plein à l'Ukraine", False),
}
