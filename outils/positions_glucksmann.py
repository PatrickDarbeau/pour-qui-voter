"""Positions de Raphaël Glucksmann (lot 7, étape 5) — BROUILLON à relire.

Sources (archivées le 12/11/2026) :
  - site de campagne https://glucks2027.fr : livret « Révolution écologique — les premiers 100 jours » (novembre 2026) ;
  - Place publique, son parti : projet « Acte I » (42 chantiers), page des combats, lettre aux Français, prises de position.
L'Acte I est le projet du parti, antérieur à la campagne : le livret de campagne est présenté comme une « première partie ».
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
LIVRET = "https://glucks2027.fr/wp-content/uploads/2026/11/livret_progr_revolution_ecologique_2027.pdf"
ACTE1 = "https://place-publique.eu/document/6J8wjk3EW8dBCLwKxa7J96/projet-placepublique-acte1.pdf"
FRANCHISES = "https://place-publique.eu/posts/5alHI42mxxIp7GNFA9ImFX/franchises-medicales-s-lecornu-envoie-la-facture-du-deficit-aux-malades"

P = {
    "eco1": (0.5, LIVRET, "Notre contribution exceptionnelle pour l'investissement climatique sur les plus hauts patrimoines […] rapportera 50 milliards d'euros", True),
    "eco7": (1, ACTE1, "L'absence de conditionnement des aides publiques aux entreprises", True),
    "trav1": (0.5, ACTE1, "Augmenter le SMIC à 1600 euros net dans les deux ans qui suivent notre accession au pouvoir", True),
    "trav4": (-1, ACTE1, "Abroger la réforme Macron de l'assurance chômage, injuste et inefficace", False),
    "trav5": (1, ACTE1, "Abroger la réforme Macron de l'assurance chômage, injuste et inefficace", False),
    "trav7": (0.5, ACTE1, "Intégrer davantage les représentants des salariés dans les conseils d'administration des entreprises, dès 100 salariés", False),
    "trav9": (0.5, ACTE1, "Travailler à limiter les écarts de salaires dans une même entreprise", False),
    "retr1": (0.5, ACTE1, "La réforme de 2023 […] est injuste. Elle doit être abrogée. Mais cette abrogation n'est pas un horizon en soi", True),
    "retr2": (-1, ACTE1, "La réforme de 2023 […] est injuste. Elle doit être abrogée", False),
    "retr4": (-1, ACTE1, "La réforme de 2023 […] est injuste. Elle doit être abrogée", False),
    "san9": (1, FRANCHISES, "Place publique s'oppose avec force à ce type de mesures [hausse des franchises médicales]", True),
    "edu2": (0.5, ACTE1, "Revaloriser le salaire de tous les enseignants de manière continue et planifiée sur 5 ans", False),
    "edu4": (0.5, ACTE1, "Repenser en profondeur Parcoursup à travers une concertation", True),
    "cult6": (0.5, ACTE1, "Supprimer la part individuelle du pass Culture au profit du financement d'artistes intervenant en milieu scolaire", False),
    "cult7": (-1, ACTE1, "Supprimer la part individuelle du pass Culture", False),
    "cult9": (1, ACTE1, "Renforcer le statut des artistes-auteurs par une loi garantissant continuité de revenus et droits sociaux adaptés", False),
    "ecl1": (-1, LIVRET, "Le mix s'appuiera sur un déploiement massif des énergies renouvelables et la pérennisation de l'énergie nucléaire", False),
    "ecl10": (1, LIVRET, "Plus que doubler la production d'énergie renouvelable d'ici 2035", False),
    "ecl3": (1, ACTE1, "Étendre l'interdiction des vols intérieurs avec alternative ferroviaire viable", False),
    "ecl4": (1, LIVRET, "Dès les 100 premiers jours, nous mettrons fin aux exonérations fiscales sur le carburant pour les vols intérieurs", False),
    "agri1": (1, ACTE1, "Interdisant les pesticides les plus néfastes, glyphosate, néonicotinoïdes", False),
    "agri2": (-1, ACTE1, "Interdisant les pesticides les plus néfastes, glyphosate, néonicotinoïdes", True),
    "agri3": (1, ACTE1, "Garantir le revenu des agriculteurs par la mise en place de prix planchers rémunérateurs", False),
    "agri4": (1, ACTE1, "S'opposer aux traités comme le Mercosur", False),
    "agri5": (-1, ACTE1, "S'opposer aux traités comme le Mercosur", False),
    "agri6": (0.5, ACTE1, "Faire de la cantine le lieu d'accès universel à une alimentation saine, locale et bio", True),
    "agri8": (-1, ACTE1, "Refuser les méga-bassines au profit de solutions locales réfléchies avec les agriculteurs", False),
    "agri9": (1, ACTE1, "Refuser les méga-bassines", False),
    "log1": (1, ACTE1, "Encadrer les loyers dans les zones en grande tension", False),
    "log2": (-1, ACTE1, "Encadrer les loyers dans les zones en grande tension", False),
    "log3": (0.5, ACTE1, "Accélérer la construction de logements sociaux en réhaussant les objectifs nationaux annuels", False),
    "om4": (-1, ACTE1, "Flécher une part des revenus de l'octroi de mer vers des projets d'investissements locaux", True),
    "om5": (1, ACTE1, "Flécher une part des revenus de l'octroi de mer vers des projets d'investissements locaux", True),
    "om1": (0.5, ACTE1, "Plafonner les prix des biens de première nécessité et des produits essentiels", True),
    "num1": (1, ACTE1, "Interdire les réseaux sociaux pour les moins de 15 ans", False),
    "num6": (1, ACTE1, "Une hausse ciblée de la taxe GAFAM", False),
    "num7": (0.5, ACTE1, "Un plan national d'investissement dans les infrastructures algorithmiques d'intérêt général : logiciels libres", True),
    "sec7": (1, ACTE1, "Faire renaître une police de proximité moderne, ancrée localement", False),
    "sec8": (0.5, ACTE1, "Organiser une convention citoyenne sur la politique vis-à-vis des drogues, notamment la question de la légalisation du cannabis", True),
    "jus2": (1, ACTE1, "Déployer massivement la justice restaurative et les travaux d'intérêt général (TIG)", False),
    "imm4": (1, ACTE1, "Faciliter les démarches de régularisation des travailleurs sans papiers", False),
    "imm5": (-1, ACTE1, "Faciliter les démarches de régularisation des travailleurs sans papiers", False),
    "imm9": (0.5, ACTE1, "Mettre fin au système de la politique du chiffre sur les OQTF, et appliquer celles délivrées", True),
    "eu1": (1, ACTE1, "Prendre la tête de l'effort commun pour construire une puissance européenne digne de ce nom", False),
    "eu2": (-1, ACTE1, "Construire une puissance européenne digne de ce nom", True),
    "eu7": (-1, ACTE1, "Recréer un rite de passage républicain et universel autour de la majorité pour remplacer le service militaire", True),
    "ins1": (0.5, ACTE1, "Instaurer un droit d'initiative citoyenne, permettant de déclencher […] des référendums à l'échelle locale et nationale", True),
    "ins2": (1, ACTE1, "Instaurer immédiatement la proportionnelle", False),
    "ins10": (0.5, ACTE1, "Agir contre le pantouflage", True),
    "ins12": (1, ACTE1, "Instaurer la motion de censure « constructive » […] ce qui permettra de mettre fin au 49.3", False),
}
