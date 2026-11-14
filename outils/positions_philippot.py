"""Positions de Florian Philippot — BROUILLON à relire.

Source : relevé d'Hermès du 14/11/2026 (docs/hermes/rapports/2026-11-14_positions-philippot.md).
Chaque citation a été retrouvée mot pour mot dans la source le 14/11/2026 (vérification automatique,
césures et typographie normalisées). « À confirmer » = position déduite d'un principe général
ou d'un passage portant sur une mesure voisine.
Valeurs : 1 soutient · 0.5 soutient en partie · -1 s'oppose ; mesure absente = 0 (non trouvé).
"""
DATE_SOURCE = "2026-11-14"

S0 = 'https://les-patriotes.fr/contre-la-loi-aide-a-mourir-et-pour-une-grande-loi-aide-a-vivre/'
S1 = 'https://les-patriotes.fr/macron-veut-interdire-les-reseaux-sociaux-on-refuse/'
S2 = 'https://les-patriotes.fr/non-a-la-reconnaissance-faciale-et-au-credit-social-en-france/'
S3 = 'https://les-patriotes.fr/notre-charte-des-patriotes/'
S4 = 'https://les-patriotes.fr/wp-content/uploads/2026/09/Projet-pour-la-France-2026-v2.pdf'

P = {
    'agri3': (1, S4, 'Rétablir les prix planchers pour assurer un revenu décent pour nos agriculteurs', False, 'programme_pdf'),
    'agri4': (1, S4, 'Mettre fin aux accords de libre-échange, qui ruinent nos agriculteurs', False, 'programme_pdf'),
    'agri5': (-1, S4, 'Mettre fin aux accords de libre-échange, qui ruinent nos agriculteurs', False, 'programme_pdf'),
    'agri7': (1, S3, "des conditions d'abattage dignes, la fin des fermes-usines", False),
    'ecl1': (-1, S4, 'Investir massivement dans le nucléaire et choisir notre mix énergétique', False, 'programme_pdf'),
    'ecl2': (1, S4, "un plan d'investissement massif dans le nucléaire de nouvelle génération", False, 'programme_pdf'),
    'ecl5': (1, S4, "Quitter le marché européen de l'électricité", False, 'programme_pdf'),
    'ecl6': (-1, S4, "Les règles du marché européen de l'électricité ont été pensées pour nuire à la France", False, 'programme_pdf'),
    'ecl7': (1, S4, "Rétablir le monopole public national d'EDF", False, 'programme_pdf'),
    'ecl8': (-1, S4, "la concurrence artificiellement organisée n'a aucunement fait baisser les prix", False, 'programme_pdf'),
    'ecl9': (1, S4, "un moratoire total et définitif sur cette méthode de production d'électricité", False, 'programme_pdf'),
    'ecl10': (-1, S4, 'En finir avec les éoliennes sur terre et en mer', False, 'programme_pdf'),
    'eco1': (0.5, S3, "ils allégeront l'impôt des classes moyennes et l'augmenteront pour les plus riches, notamment par le rétablissement de l'ISF", False),
    'eco5': (0.5, S4, 'un système fiscal favorable à la production nationale', True, 'programme_pdf'),
    'eco9': (0.5, S4, "une gestion rigoureuse des dépenses de l'Etat accompagnée de la sortie de l'UE et de l'abandon de l'Euro", False, 'programme_pdf'),
    'eco10': (-1, S4, "Pour réaliser ce redressement sans augmenter le niveau d'imposition déjà record subi par les Français", True, 'programme_pdf'),
    'edu2': (0.5, S4, 'leur carrière revalorisée, notamment sur le plan salarial', False, 'programme_pdf'),
    'eu1': (-1, S4, 'La France doit retrouver sa souveraineté nationale en quittant toutes les instances supranationales : UE, Euro, Schengen, CEDH, OTAN, OMS', False, 'programme_pdf'),
    'eu2': (1, S4, "la France retrouvera l'ensemble des compétences qu'elle a transférées", False, 'programme_pdf'),
    'eu3': (0.5, S4, "en exigeant la tenue du référendum en tant que force d'opposition", False, 'programme_pdf'),
    'eu4': (1, S4, "Quitter l'OTAN est l'une des conditions de notre indépendance sur la scène internationale", False, 'programme_pdf'),
    'eu5': (-1, S4, "Quitter l'OTAN est l'une des conditions de notre indépendance sur la scène internationale", False, 'programme_pdf'),
    'eu6': (1, S3, 'Il faut consacrer immédiatement 3 % de notre PIB au budget de la Défense et tendre vers les 4 %', False),
    'eu8': (-1, S4, "Cesser d'entretenir la guerre en Ukraine", False, 'programme_pdf'),
    'eu9': (1, S4, 'la France doit retrouver son rôle historique en faveur de la Paix, par le dialogue et la diplomatie', False, 'programme_pdf'),
    'imm1': (0.5, S4, "Créer le référendum d'initiative citoyenne (RIC) sur tout sujet et l'inscrire dans la Constitution", True, 'programme_pdf'),
    'imm2': (1, S3, "La citoyenneté s'acquiert par filiation ou par naturalisation au mérite", True),
    'imm3': (-1, S3, "La citoyenneté s'acquiert par filiation ou par naturalisation au mérite", True),
    'imm4': (-1, S4, "reconduisant aux frontières ceux qui n'ont rien à faire en France", True, 'programme_pdf'),
    'imm5': (0.5, S4, "mettre un terme à la politique d'immigration massive en revenant à des flux extrêmement limités", True, 'programme_pdf'),
    'imm6': (1, S4, 'remettre en cause le regroupement familial', False, 'programme_pdf'),
    'imm9': (1, S4, 'Renvoyer les clandestins chez eux et appliquer les OQTF', False, 'programme_pdf'),
    'ins1': (1, S4, "Créer le référendum d'initiative citoyenne (RIC) sur tout sujet et l'inscrire dans la Constitution", False, 'programme_pdf'),
    'ins2': (1, S3, "Le mode de scrutin proportionnel sera généralisé pour permettre à tous les courants d'idées d'être représentés", False),
    'ins7': (1, S4, "Mise en place de l'inéligibilité à vie et interdiction de toute charge publique pour les élus et responsables publics condamnés définitivement pour corruption", False, 'programme_pdf'),
    'ins8': (-1, S4, "Mise en place de l'inéligibilité à vie et interdiction de toute charge publique pour les élus et responsables publics condamnés définitivement pour corruption", False, 'programme_pdf'),
    'jus1': (1, S4, 'réinstaurer les peines planchers et de généraliser les sanctions dès la première infraction', False, 'programme_pdf'),
    'jus5': (1, S4, 'Construire les dizaines de milliers de places de prison qui manquent', False, 'programme_pdf'),
    'jus6': (0.5, S4, 'qui tue comme un adulte doit être jugé comme un adulte', False, 'programme_pdf'),
    'jus7': (0.5, S4, "en finir avec l'excuse automatique de minorité", False, 'programme_pdf'),
    'log6': (1, S4, 'Renationaliser les autoroutes', False, 'programme_pdf'),
    'log7': (-1, S4, 'Renationaliser les autoroutes', False, 'programme_pdf'),
    'log8': (0.5, S4, "Chaque Français doit pouvoir bénéficier des mêmes services, où qu'il vive sur le territoire national", True, 'programme_pdf'),
    'num1': (-1, S1, "notre refus ABSOLU d'interdire, de censurer les réseaux sociaux", False),
    'num4': (1, S2, 'Refusons totalement la reconnaissance faciale et le crédit social en France', False),
    'num5': (-1, S2, 'Refusons totalement la reconnaissance faciale et le crédit social en France', False),
    'num7': (1, S4, 'Le code source des outils publics doit être libre et auditable', False, 'programme_pdf'),
    'num9': (1, S4, "Toutes les données stratégiques doivent être hébergées sur des serveurs publics ou contrôlés par l'ANSSI", False, 'programme_pdf'),
    'om2': (-1, S4, "nous refusons catégoriquement la création d'un État de Nouvelle-Calédonie", False, 'programme_pdf'),
    'om6': (0.5, S4, "Un plan d'investissement national est nécessaire pour moderniser les réseaux (eau, électricité, numérique)", False, 'programme_pdf'),
    'om7': (1, S3, "La citoyenneté s'acquiert par filiation ou par naturalisation au mérite", True),
    'om8': (-1, S3, "La citoyenneté s'acquiert par filiation ou par naturalisation au mérite", True),
    'om9': (0.5, S4, 'améliorer la continuité territoriale', True, 'programme_pdf'),
    'retr1': (0.5, S4, "déterminer les conditions d'accession à la retraite et baisser l'âge de départ si les Français le désirent", False, 'programme_pdf'),
    'retr2': (-1, S4, "déterminer les conditions d'accession à la retraite et baisser l'âge de départ si les Français le désirent", True, 'programme_pdf'),
    'retr4': (-1, S4, "déterminer les conditions d'accession à la retraite et baisser l'âge de départ si les Français le désirent", True, 'programme_pdf'),
    'retr6': (1, S3, 'pérenniser la retraite par répartition', False),
    'san5': (1, S3, "L'AME doit être supprimée et remplacée par un dispositif de prise en charge des urgences vitales et des risques épidémiques", False),
    'san6': (-1, S3, "L'AME doit être supprimée et remplacée par un dispositif de prise en charge des urgences vitales et des risques épidémiques", False),
    'san7': (-1, S0, "Nous nous opposons fermement à la proposition de loi sur l'« aide à mourir", False),
    'san8': (1, S0, 'Une société digne se doit de soutenir la vie en renforçant les soins palliatifs', False),
    'sec1': (0.5, S3, 'renforçant la police, la gendarmerie, les douanes, le renseignement', False),
    'sec7': (1, S4, 'Recréer une police de proximité visible et permanente', False, 'programme_pdf'),
    'soli3': (0.5, S3, 'Le retour de la croissance économique se traduira par une baisse de la TVA', True),
    'soli8': (0.5, S4, 'encadrement plus strict des prix des produits de première nécessité', False, 'programme_pdf'),
    'trav4': (-1, S4, "visant à raboter les indemnités chômage, à fermer des lits à l'hôpital ou à arrêter le remboursement des médicaments pourront être supprimées", False, 'programme_pdf'),
    'trav5': (0.5, S4, "visant à raboter les indemnités chômage, à fermer des lits à l'hôpital ou à arrêter le remboursement des médicaments pourront être supprimées", False, 'programme_pdf'),
}
