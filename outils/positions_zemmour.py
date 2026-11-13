"""Positions d'Éric Zemmour (lot 7, étape 5) — BROUILLON à relire.

Source : site de campagne https://www.ericzemmour.fr, page « Nos priorités pour les Français » (5 priorités),
archivée les 12 et 13/11/2026. Pas de programme détaillé publié : le site du parti renvoie vers une plateforme
participative (« Le programme pour la France ») qui recueille des contributions, sans engagement du candidat.
Couverture volontairement limitée à ce qui est écrit dans les priorités.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
PR = "https://www.ericzemmour.fr/priorites"

P = {
    # #1 L'immigration négative, maintenant !
    "imm4": (-1, PR, "Arrêter l'immigration légale et illégale en reprenant le contrôle de nos frontières", False),
    "imm5": (1, PR, "Remigrer les étrangers en situation irrégulière, délinquants et chômeurs de longue durée", True),
    "imm6": (1, PR, "Arrêter l'immigration légale et illégale", True),
    "imm9": (1, PR, "Remigrer les étrangers en situation irrégulière, délinquants et chômeurs de longue durée", True),
    # #2 Préférence nationale
    "imm7": (1, PR, "Réserver les aides sociales non-contributives, les allocations familiales et le logement social aux Français", False),
    "imm8": (-1, PR, "Réserver les aides sociales non-contributives, les allocations familiales et le logement social aux Français", False),
    "san5": (1, PR, "Supprimer l'AME qui soigne les clandestins avec votre argent", True),
    "san6": (-1, PR, "Supprimer l'AME", False),
    # #3 Fin du laxisme
    "jus1": (1, PR, "Peines plancher et loi anti-casseurs", False),
    "jus2": (-1, PR, "Fin des aménagements de peine", True),
    "jus5": (1, PR, "Construction de 100 000 places de prison en 24 mois", False),
    "jus7": (-1, PR, "Fin des aménagements de peine et de l'excuse de minorité", False),
    # #4 Dépenser moins pour taxer moins
    "eco1": (-1, PR, "La fin des droits de succession et de l'impôt sur la fortune", False),
    "eco2": (-1, PR, "La fin des droits de succession et de l'impôt sur la fortune", True),
    "soli3": (0.5, PR, "40 centimes de baisse de taxes sur les carburants", True),
}
