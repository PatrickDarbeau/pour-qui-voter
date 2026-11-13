"""Positions de Marine Le Pen (lot 7, étape 5) — BROUILLON à relire.

Recherche confiée à Hermès le 13/11/2026 (rapport : docs/recherche_hermes_2026-11-13_lepen_riner.md),
citations vérifiées par Claude le même jour.
Sources :
  - site de campagne https://marinelepen.com (officiel, édité par le RN) : formulaire de soutien seulement, aucun programme ;
  - site du parti https://rassemblementnational.fr : bandeaux de la page d'accueil (vérifiés le 13/11/2026) ;
  - à défaut de programme publié, presse reconnue rapportant les annonces de la candidate (contre-budget du 06/10/2026,
    retraites le 14/10/2026) → positions marquées « à confirmer ».
Réforme des retraites détaillée annoncée pour le 17/11/2026 : à revérifier.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
RN = "https://rassemblementnational.fr/"
FI = ("https://www.franceinfo.fr/elections/presidentielle/"
      "marine-le-pen-presentera-de-maniere-extremement-precise-sa-reforme-des-retraites-le-17-novembre_8237821.html")
LM = ("https://www.lemonde.fr/politique/article/2026/10/06/"
      "presidentielle-2027-marine-le-pen-promet-140-milliards-d-euros-nets-d-economies-d-ici-2032_6788959_823448.html")

P = {
    # Bandeaux du site du Rassemblement national
    "soli3": (1, RN, "Pour la réduction de la TVA de 20% à 5,5% sur l'énergie", False),
    "ins1": (1, RN, "Pour le RIC le référendum initiative citoyenne", False),
    "ecl2": (1, RN, "Pour investir dans le nucléaire", True),
    "ecl1": (-1, RN, "Pour investir dans le nucléaire", True),
    "retr3": (0.5, RN, "Pour la retraite à 60 ans pour ceux qui commencent à travailler tôt", False),
    # Retraites (franceinfo/AFP, 14/10/2026)
    "retr1": (1, FI, "L'objectif sera « d'augmenter le taux d'activité » pour ramener l'âge de départ à 62 voire 60 ans", True),
    "retr2": (-1, FI, "Ramener l'âge de départ à 62 voire 60 ans", True),
    "retr4": (-1, FI, "Ramener l'âge de départ à 62 voire 60 ans", True),
    # Contre-budget (Le Monde, 06/10/2026)
    "retr5": (1, LM, "Elle a également annoncé « la création d'un véritable pilier de capitalisation »", True),
    "retr6": (-1, LM, "« La création d'un véritable pilier de capitalisation »", True),
    "imm7": (1, LM, "« Reprise en main de [la] politique migratoire et l'instauration de la priorité nationale »", True),
    "imm8": (-1, LM, "L'instauration de la priorité nationale", True),
    "om4": (1, LM, "Appelé à mettre fin à l'octroi de mer", True),
    "om5": (-1, LM, "Appelé à mettre fin à l'octroi de mer", True),
    "eco2": (-1, LM, "Remplacer l'impôt sur la fortune immobilière (IFI) par un « impôt sur la fortune financière »", True),
}
