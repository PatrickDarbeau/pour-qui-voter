"""Positions de François Asselineau — BROUILLON à relire.

Source : relevé d'Hermès du 14/11/2026 (docs/hermes/rapports/2026-11-14_positions-asselineau.md).
Chaque citation a été retrouvée mot pour mot dans la source le 14/11/2026 (vérification automatique,
césures et typographie normalisées). « À confirmer » = position déduite d'un principe général
ou d'un passage portant sur une mesure voisine.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
DATE_SOURCE = "2026-11-14"

S0 = 'https://upr.fr/communiques-de-presse/accords-de-libre-echange-ue-mercosur-et-ceta-lupr-denonce-une-attaque-de-grande-ampleur-contre-la-democratie-et-contre-lecologie'
S1 = 'https://upr.fr/drp/reunion-publique-en-charente-retrouvons-notre-liberte-et-lindependance-de-la-france'
S2 = 'https://upr.fr/essentiels/lincroyable-histoire-de-larenh-liee-au-demantelement-du-service-public-dedf'
S3 = 'https://upr.fr/faq'
S4 = 'https://upr.fr/le-frexit'
S5 = 'https://upr.fr/nos-fondamentaux'
S6 = 'https://upr.fr/universites/discours-de-rentree-2026-de-francois-asselineau-la-liberation-nationale'

P = {
    'agri3': (0.5, S4, "protéger les productions qui le nécessitent, d'assurer des prix rémunérateurs", False),
    'agri4': (1, S0, 'Ces accords de libre-échange européens sont une attaque de grande ampleur contre la démocratie', False),
    'agri5': (-1, S0, 'Ces accords de libre-échange européens sont une attaque de grande ampleur contre la démocratie', False),
    'cult2': (-1, S4, "renationaliser certains (gestion des sociétés d'autoroutes et d'adduction d'eau, Orange, TF1)", True),
    'cult3': (0.5, S4, 'mettre un terme à la privatisation rampante de nos services publics (EDF, GDF, SNCF, La Poste)', True),
    'ecl7': (1, S2, "si les demandes de l'Union européenne étaient acceptées par la France, il s'agirait ni plus ni moins d'un démantèlement pur et simple d'EDF", False),
    'ecl8': (-1, S2, 'EDF ne peut que perdre et les sociétés concurrentes ne peuvent que gagner', True),
    'eu1': (-1, S1, "D'où sa proposition de sortir de l'Union européenne, de l'euro et de l'OTAN", False),
    'eu2': (0.5, S3, "Le mouvement privilégie donc une sortie juridique et politique assumée plutôt qu'une promesse de transformation interne de l'Union", True),
    'eu3': (-1, S6, "Il refuse l'idée d'un référendum préalable sur le sujet, estimant que son élection vaudra mandat", False),
    'eu4': (1, S6, "notification immédiate au Département d'État américain via l'article 13 pour faire sortir la France de l'alliance sous un an", False),
    'eu5': (-1, S6, "notification immédiate au Département d'État américain via l'article 13 pour faire sortir la France de l'alliance sous un an", False),
    'eu8': (-1, S6, "arrêt immédiat de tout versement d'aides financières et militaires à l'Ukraine dès sa prise de fonction", False),
    'eu9': (1, S6, "arrêt immédiat de tout versement d'aides financières et militaires à l'Ukraine dès sa prise de fonction", False),
    'imm1': (1, S5, 'Grands référendums : immigration, dette, nucléaire', False),
    'ins1': (1, S6, "instauration du Référendum d'Initiative Citoyenne (RIC)", False),
    'ins4': (0.5, S4, 'reconnaître pleinement et entièrement le vote blanc', False),
    'log6': (1, S4, "renationaliser certains (gestion des sociétés d'autoroutes et d'adduction d'eau, Orange, TF1)", False),
    'log7': (-1, S4, "renationaliser certains (gestion des sociétés d'autoroutes et d'adduction d'eau, Orange, TF1)", False),
    'retr5': (-1, S4, 'protéger constitutionnellement les services publics et la retraite par répartition', True),
    'retr6': (1, S4, 'protéger constitutionnellement les services publics et la retraite par répartition', False),
    'retr7': (0.5, S4, 'assurer un minimum vieillesse équivalant à 950 € par mois', False),
    'trav1': (0.5, S4, 'augmenter substantiellement le SMIC tout en abaissant les charges patronales pour les TPE et les PME', False),
}
