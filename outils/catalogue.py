"""Catalogue des thèmes et mesures réels (lot 7, étape 2) — BROUILLON à relire.

Génère :
  - data/brouillon/catalogue.json : thèmes + mesures, sans candidats (à fusionner au pack réel à l'étape 5) ;
  - docs/catalogue_mesures.md     : version lisible pour la relecture de neutralité.

Usage : python outils/catalogue.py

Règles (docs/lot_7_pas_a_pas.md §3) : neutre, concrète, une idée par mesure, contrepoints reliés (opposee_a).
Colonne « origine » : demo = reprise du jeu de démonstration, contrepoint = ajoutée pour l'équilibre,
nouveau = rédigée pour le catalogue.
"""
import json
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent

THEMES = [
    ("eco", "Économie et fiscalité", "💶", "#2f6fb0"),
    ("trav", "Travail et emploi", "👷", "#5d6d7e"),
    ("retr", "Retraites", "👵", "#8e6c3a"),
    ("sante", "Santé", "🩺", "#c0392b"),
    ("soli", "Solidarités et pouvoir d'achat", "🤝", "#d35400"),
    ("edu", "Éducation et jeunesse", "🎓", "#8e44ad"),
    ("cult", "Culture", "🎭", "#b03a6e"),
    ("ecol", "Écologie et énergie", "🌿", "#27ae60"),
    ("agri", "Agriculture et alimentation", "🚜", "#7d8f2a"),
    ("loge", "Logement et territoires", "🏠", "#a0522d"),
    ("om", "Outre-mer", "🌴", "#16a085"),
    ("num", "Numérique et libertés", "💻", "#2c7fb8"),
    ("secu", "Sécurité", "🛡️", "#34495e"),
    ("just", "Justice", "⚖️", "#6c3483"),
    ("immi", "Immigration", "🧭", "#7f8c8d"),
    ("euro", "Europe et international", "🇪🇺", "#1f3a8a"),
    ("inst", "Institutions et démocratie", "🏛️", "#d68910"),
]

# (id, thème, intitulé, description, id opposé ou None, origine)
M = [
    # ---- Économie et fiscalité
    ("eco1", "eco", "Rétablir un impôt sur la fortune, avec un crédit d'impôt pour l'investissement dans les PME", "Retour d'un impôt sur l'ensemble du patrimoine, y compris financier.", "eco2", "nouveau"),
    ("eco2", "eco", "Conserver l'impôt sur la fortune immobilière (IFI) sans l'étendre au patrimoine financier", "Statu quo depuis 2018.", "eco1", "contrepoint"),
    ("eco3", "eco", "Créer un impôt lié à la nationalité pour imposer en France les très hauts patrimoines partis à l'étranger", "Lutte contre l'exil fiscal par un impôt nouveau.", "eco4", "nouveau"),
    ("eco4", "eco", "Lutter contre l'exil fiscal par des conventions internationales plutôt que par un nouvel impôt", "Coopération fiscale entre États.", "eco3", "contrepoint"),
    ("eco5", "eco", "Baisser les impôts de production des entreprises", "Réduction de la fiscalité pesant sur l'outil productif.", None, "demo"),
    ("eco6", "eco", "Publier la liste et le montant des aides publiques reçues par chaque entreprise", "Transparence des aides aux entreprises.", None, "nouveau"),
    ("eco7", "eco", "Conditionner les aides publiques aux entreprises à des engagements d'emploi et d'investissement", "Remboursement des aides en cas de non-respect.", "eco8", "nouveau"),
    ("eco8", "eco", "Simplifier les aides aux entreprises sans leur ajouter de conditions", "Moins de démarches, mêmes critères d'attribution.", "eco7", "contrepoint"),
    ("eco9", "eco", "Ramener le déficit public sous 3 % du PIB avant la fin du quinquennat", "Priorité à la réduction du déficit.", "eco10", "nouveau"),
    ("eco10", "eco", "Augmenter l'investissement public, même au prix d'un déficit plus élevé", "Priorité à la relance et à la transition.", "eco9", "nouveau"),
    # ---- Travail et emploi
    ("trav1", "trav", "Augmenter le SMIC de 10 %", "Revalorisation exceptionnelle du salaire minimum.", None, "demo"),
    ("trav2", "trav", "Réduire la durée légale du travail à 32 heures par semaine", "Semaine de quatre jours, sans baisse de salaire.", "trav3", "nouveau"),
    ("trav3", "trav", "Permettre aux entreprises de fixer la durée du travail par accord, au-delà de 35 heures", "Assouplissement de la durée légale.", "trav2", "nouveau"),
    ("trav4", "trav", "Réduire la durée d'indemnisation du chômage lorsque le marché de l'emploi est favorable", "Règles d'assurance chômage plus strictes.", "trav5", "nouveau"),
    ("trav5", "trav", "Allonger la durée d'indemnisation du chômage et annuler les dernières réformes", "Retour à des droits plus protecteurs.", "trav4", "nouveau"),
    ("trav6", "trav", "Indexer automatiquement les salaires sur l'inflation", "Hausse des salaires au même rythme que les prix.", None, "nouveau"),
    ("trav7", "trav", "Réserver un tiers des sièges des conseils d'administration aux représentants des salariés", "Dans les grandes entreprises.", None, "nouveau"),
    ("trav8", "trav", "Supprimer les cotisations salariales sur les heures supplémentaires", "Heures supplémentaires mieux rémunérées en net.", None, "nouveau"),
    ("trav9", "trav", "Limiter l'écart entre le salaire le plus bas et le plus haut d'une entreprise à 1 pour 20", "Plafonnement des hautes rémunérations.", None, "nouveau"),
    # ---- Retraites
    ("retr1", "retr", "Abaisser l'âge légal de départ à la retraite à 62 ans", "Retour sur la réforme de 2023.", "retr2", "demo"),
    ("retr2", "retr", "Porter l'âge légal de départ à la retraite à 65 ans", "Allongement de la durée d'activité.", "retr1", "demo"),
    ("retr3", "retr", "Fixer l'âge légal de départ à 60 ans avec 40 années de cotisation", "Retour à un départ plus précoce.", "retr2", "nouveau"),
    ("retr4", "retr", "Conserver l'âge légal de départ à 64 ans prévu par la réforme de 2023", "Application de la réforme existante.", None, "nouveau"),
    ("retr5", "retr", "Introduire une part de capitalisation dans le financement des retraites", "Épargne retraite collective obligatoire en complément.", "retr6", "nouveau"),
    ("retr6", "retr", "Financer les retraites uniquement par répartition, en augmentant les cotisations si nécessaire", "Pas de capitalisation.", "retr5", "nouveau"),
    ("retr7", "retr", "Porter le minimum de pension au niveau du SMIC net pour une carrière complète", "Revalorisation des petites pensions.", None, "nouveau"),
    ("retr8", "retr", "Réintégrer le port de charges lourdes et les postures pénibles dans le compte pénibilité", "Départs anticipés pour les métiers pénibles.", None, "nouveau"),
    ("retr9", "retr", "Créer un régime de retraite universel par points", "Mêmes règles pour tous les actifs.", None, "nouveau"),
    # ---- Santé
    ("san1", "sante", "Recruter 20 000 soignants à l'hôpital public", "Plan pluriannuel d'embauches.", None, "demo"),
    ("san2", "sante", "Réguler l'installation des médecins dans les zones déjà bien dotées", "Lutte contre les déserts médicaux par la contrainte.", "san3", "demo"),
    ("san3", "sante", "Inciter financièrement les médecins à s'installer dans les déserts médicaux, sans contrainte", "Primes et aides à l'installation.", "san2", "contrepoint"),
    ("san4", "sante", "Rembourser intégralement les soins dentaires et optiques", "Extension du « 100 % santé ».", None, "demo"),
    ("san5", "sante", "Remplacer l'aide médicale d'État (AME) par une aide limitée aux soins urgents", "Restriction des soins des étrangers en situation irrégulière.", "san6", "nouveau"),
    ("san6", "sante", "Maintenir l'aide médicale d'État (AME) dans sa forme actuelle", "Statu quo.", "san5", "nouveau"),
    ("san7", "sante", "Légaliser une aide active à mourir strictement encadrée", "Pour les malades en fin de vie qui le demandent.", "san8", "nouveau"),
    ("san8", "sante", "Développer les soins palliatifs sans légaliser l'aide active à mourir", "Priorité à l'accompagnement.", "san7", "nouveau"),
    ("san9", "sante", "Supprimer les franchises médicales restant à la charge des patients", "Sur les médicaments et consultations.", None, "nouveau"),
    # ---- Solidarités et pouvoir d'achat
    ("soli1", "soli", "Bloquer les prix des carburants en période de forte inflation", "Plafonnement temporaire des prix à la pompe.", "soli2", "nouveau"),
    ("soli2", "soli", "Aider de façon ciblée les ménages modestes plutôt que bloquer les prix", "Chèques ou aides sous conditions de ressources.", "soli1", "contrepoint"),
    ("soli3", "soli", "Baisser la TVA sur l'énergie et les produits de première nécessité", "Baisse générale des prix.", None, "nouveau"),
    ("soli4", "soli", "Conditionner le RSA à 15 heures d'activité par semaine", "Formation, insertion ou bénévolat.", "soli5", "nouveau"),
    ("soli5", "soli", "Verser le RSA sans obligation d'activité", "Droit inconditionnel au minimum social.", "soli4", "nouveau"),
    ("soli6", "soli", "Ouvrir le RSA aux jeunes de 18 à 25 ans", "Revenu minimum pour les jeunes adultes.", None, "nouveau"),
    ("soli7", "soli", "Porter l'allocation aux adultes handicapés (AAH) au niveau du seuil de pauvreté", "Revalorisation de l'AAH.", None, "nouveau"),
    ("soli8", "soli", "Encadrer les prix d'un panier de produits alimentaires de base", "Prix maximaux fixés par l'État.", None, "nouveau"),
    ("soli9", "soli", "Verser les allocations familiales dès le premier enfant", "Aujourd'hui à partir du deuxième.", None, "nouveau"),
    # ---- Éducation et jeunesse
    ("edu1", "edu", "Limiter les classes à 24 élèves en primaire", "Réduction des effectifs par classe.", None, "demo"),
    ("edu2", "edu", "Augmenter le salaire des enseignants de 15 %", "Revalorisation sur la durée du quinquennat.", None, "demo"),
    ("edu3", "edu", "Rendre l'uniforme obligatoire à l'école", "Tenue commune dans le primaire et le secondaire.", None, "demo"),
    ("edu4", "edu", "Supprimer Parcoursup et rétablir un accès de droit à l'université après le baccalauréat", "Fin de la sélection à l'entrée.", "edu5", "nouveau"),
    ("edu5", "edu", "Renforcer la sélection à l'entrée de l'université", "Prérequis par filière.", "edu4", "nouveau"),
    ("edu6", "edu", "Rendre le service national universel obligatoire", "Pour tous les jeunes d'une classe d'âge.", None, "nouveau"),
    ("edu7", "edu", "Réduire le financement public des écoles privées sous contrat", "Redéploiement vers le public.", "edu8", "nouveau"),
    ("edu8", "edu", "Maintenir le financement public de l'enseignement privé sous contrat", "Statu quo.", "edu7", "nouveau"),
    ("edu9", "edu", "Rendre la cantine scolaire gratuite pour tous les élèves", "Prise en charge par l'État et les collectivités.", None, "nouveau"),
    # ---- Culture
    ("cult1", "cult", "Porter le budget de la culture à 1 % du budget de l'État", "Hausse des moyens du ministère.", None, "nouveau"),
    ("cult2", "cult", "Privatiser une partie de l'audiovisuel public", "Cession de chaînes ou de stations.", "cult3", "nouveau"),
    ("cult3", "cult", "Maintenir l'audiovisuel public entièrement public, avec un financement dédié", "Garantie d'indépendance et de moyens.", "cult2", "nouveau"),
    ("cult4", "cult", "Limiter à un seul grand média (télévision, radio ou presse nationale) le nombre de médias détenus par une même personne", "Lutte contre la concentration des médias.", "cult5", "nouveau"),
    ("cult5", "cult", "Assouplir les règles anti-concentration pour renforcer les groupes de médias français", "Face à la concurrence des plateformes.", "cult4", "contrepoint"),
    ("cult6", "cult", "Supprimer le pass Culture", "Redéploiement des crédits.", "cult7", "nouveau"),
    ("cult7", "cult", "Maintenir et étendre le pass Culture", "Aide à l'accès des jeunes à la culture.", "cult6", "nouveau"),
    ("cult8", "cult", "Rendre gratuite l'entrée des musées nationaux", "Pour tous les publics.", None, "nouveau"),
    ("cult9", "cult", "Créer un régime de protection sociale propre aux artistes-auteurs", "Sur le modèle de l'intermittence.", None, "nouveau"),
    # ---- Écologie et énergie
    ("ecl1", "ecol", "Sortir progressivement du nucléaire", "Fermeture des réacteurs en fin de vie sans remplacement.", "ecl2", "demo"),
    ("ecl2", "ecol", "Construire de nouveaux réacteurs nucléaires", "Programme de nouveaux EPR.", "ecl1", "demo"),
    ("ecl3", "ecol", "Interdire les vols intérieurs lorsqu'un trajet en train de moins de 4 heures existe", "Report vers le rail.", None, "demo"),
    ("ecl4", "ecol", "Taxer le kérosène des vols", "Fin de l'exonération du carburant aérien.", None, "demo"),
    ("ecl5", "ecol", "Sortir du marché européen de l'électricité pour fixer les prix au niveau national", "Prix fondés sur les coûts de production français.", "ecl6", "nouveau"),
    ("ecl6", "ecol", "Rester dans le marché européen de l'électricité en réformant le calcul des prix", "Réforme au niveau européen.", "ecl5", "contrepoint"),
    ("ecl7", "ecol", "Faire d'EDF une entreprise publique en monopole sur la production et la fourniture d'électricité", "Fin de la concurrence des fournisseurs.", "ecl8", "nouveau"),
    ("ecl8", "ecol", "Maintenir l'ouverture à la concurrence des fournisseurs d'électricité", "Statu quo.", "ecl7", "contrepoint"),
    ("ecl9", "ecol", "Instaurer un moratoire sur les nouvelles éoliennes", "Arrêt des nouveaux projets.", "ecl10", "nouveau"),
    ("ecl10", "ecol", "Accélérer le développement de l'éolien et du solaire", "Objectifs et procédures accélérées.", "ecl9", "nouveau"),
    # ---- Agriculture et alimentation
    ("agri1", "agri", "Interdire le glyphosate en France", "Sortie de l'herbicide.", "agri2", "nouveau"),
    ("agri2", "agri", "Aligner les règles françaises sur les pesticides sur celles de l'Union européenne", "Fin des interdictions plus strictes qu'en Europe.", "agri1", "nouveau"),
    ("agri3", "agri", "Garantir aux agriculteurs des prix planchers couvrant leurs coûts de production", "Prix minimum fixé par filière.", None, "nouveau"),
    ("agri4", "agri", "S'opposer à l'accord de libre-échange entre l'Union européenne et le Mercosur", "Protection des filières agricoles.", "agri5", "nouveau"),
    ("agri5", "agri", "Soutenir les accords de libre-échange, dont celui avec le Mercosur", "Ouverture de débouchés à l'export.", "agri4", "nouveau"),
    ("agri6", "agri", "Imposer 50 % de produits bio et locaux dans la restauration collective publique", "Cantines, hôpitaux, administrations.", None, "nouveau"),
    ("agri7", "agri", "Interdire la création de nouveaux élevages industriels intensifs", "Fermes-usines.", None, "nouveau"),
    ("agri8", "agri", "Faciliter la construction de réserves d'eau pour l'irrigation", "Retenues de substitution.", "agri9", "nouveau"),
    ("agri9", "agri", "Instaurer un moratoire sur les grandes réserves d'eau (« bassines »)", "Partage de l'eau en priorité.", "agri8", "nouveau"),
    # ---- Logement et territoires
    ("log1", "loge", "Généraliser l'encadrement des loyers dans les zones tendues", "Plafonnement des loyers.", "log2", "nouveau"),
    ("log2", "loge", "Supprimer l'encadrement des loyers", "Liberté de fixation des loyers.", "log1", "nouveau"),
    ("log3", "loge", "Construire 150 000 logements sociaux par an", "Plan national de construction.", None, "nouveau"),
    ("log4", "loge", "Supprimer l'obligation de 25 % de logements sociaux par commune (loi SRU)", "Liberté laissée aux maires.", "log5", "nouveau"),
    ("log5", "loge", "Renforcer les sanctions contre les communes qui ne respectent pas la loi SRU", "Plus de logements sociaux partout.", "log4", "nouveau"),
    ("log6", "loge", "Faire revenir les autoroutes concédées dans le giron de l'État", "Fin anticipée des concessions.", "log7", "nouveau"),
    ("log7", "loge", "Maintenir les concessions autoroutières jusqu'à leur terme en encadrant mieux les péages", "Statu quo amélioré.", "log6", "contrepoint"),
    ("log8", "loge", "Garantir un service public de base à moins de 30 minutes de chaque habitant", "École, santé, poste, services de l'État.", None, "nouveau"),
    ("log9", "loge", "Rendre gratuits les transports en commun locaux", "Bus, tramways, métros.", None, "nouveau"),
    # ---- Outre-mer
    ("om1", "om", "Aligner le prix des produits de première nécessité des outre-mer sur celui de l'Hexagone", "Lutte contre la vie chère.", None, "nouveau"),
    ("om2", "om", "Permettre aux territoires d'outre-mer qui le demandent une autonomie élargie, validée par référendum local", "Évolution institutionnelle à la carte.", "om3", "nouveau"),
    ("om3", "om", "Maintenir les statuts actuels des territoires d'outre-mer", "Pas de nouvelle évolution institutionnelle.", "om2", "nouveau"),
    ("om4", "om", "Supprimer l'octroi de mer", "Taxe locale sur les importations.", "om5", "nouveau"),
    ("om5", "om", "Maintenir l'octroi de mer, ressource des collectivités d'outre-mer", "Statu quo.", "om4", "nouveau"),
    ("om6", "om", "Lancer un plan d'urgence pour l'accès à l'eau potable outre-mer", "Notamment en Guadeloupe et à Mayotte.", None, "nouveau"),
    ("om7", "om", "Supprimer le droit du sol à Mayotte", "Nationalité par filiation uniquement.", "om8", "nouveau"),
    ("om8", "om", "Maintenir le droit du sol à Mayotte dans les conditions actuelles", "Statu quo.", "om7", "nouveau"),
    ("om9", "om", "Renforcer l'aide aux billets d'avion entre les outre-mer et l'Hexagone", "Continuité territoriale.", None, "nouveau"),
    # ---- Numérique et libertés
    ("num1", "num", "Interdire l'accès aux réseaux sociaux aux moins de 15 ans", "Vérification de l'âge obligatoire.", None, "nouveau"),
    ("num2", "num", "Obliger les utilisateurs de réseaux sociaux à vérifier leur identité", "Fin de l'anonymat vis-à-vis des plateformes.", "num3", "nouveau"),
    ("num3", "num", "Garantir le droit à l'anonymat en ligne", "Pas d'identification obligatoire.", "num2", "nouveau"),
    ("num4", "num", "Interdire la reconnaissance faciale dans l'espace public", "Protection de la vie privée.", "num5", "nouveau"),
    ("num5", "num", "Autoriser la reconnaissance faciale dans l'espace public pour la sécurité", "Sous contrôle d'une autorité.", "num4", "nouveau"),
    ("num6", "num", "Augmenter la taxe sur les grandes entreprises du numérique", "Taxe sur les services numériques.", None, "nouveau"),
    ("num7", "num", "Privilégier les logiciels libres dans les administrations", "Souveraineté et économies.", None, "nouveau"),
    ("num8", "num", "Interdire l'usage du téléphone portable au collège et au lycée", "Pendant toute la journée scolaire.", None, "nouveau"),
    ("num9", "num", "Héberger les données publiques sensibles uniquement chez des prestataires européens", "Cloud souverain.", None, "nouveau"),
    # ---- Sécurité
    ("sec1", "secu", "Recruter 10 000 policiers et gendarmes", "Renforcement des effectifs de terrain.", None, "demo"),
    ("sec2", "secu", "Confier le contrôle de la police à une autorité indépendante du ministère de l'Intérieur", "À la place de l'IGPN actuelle.", "sec3", "nouveau"),
    ("sec3", "secu", "Maintenir le contrôle interne de la police (IGPN) en renforçant ses moyens", "Statu quo amélioré.", "sec2", "contrepoint"),
    ("sec4", "secu", "Instaurer une présomption de légitime défense pour les policiers et gendarmes", "Renversement de la charge de la preuve.", "sec5", "nouveau"),
    ("sec5", "secu", "Conserver le régime actuel de la légitime défense, apprécié au cas par cas par le juge", "Statu quo.", "sec4", "contrepoint"),
    ("sec6", "secu", "Rendre obligatoire le déclenchement de la caméra-piéton lors des interventions de police", "Traçabilité des interventions.", None, "nouveau"),
    ("sec7", "secu", "Recréer une police de proximité", "Policiers affectés durablement à un quartier.", None, "nouveau"),
    ("sec8", "secu", "Légaliser le cannabis avec une production et une vente encadrées par l'État", "Fin de la prohibition.", "sec9", "nouveau"),
    ("sec9", "secu", "Durcir les sanctions contre la consommation de stupéfiants", "Amendes et peines alourdies.", "sec8", "nouveau"),
    # ---- Justice
    ("jus1", "just", "Instaurer des peines planchers", "Peines minimales pour les récidivistes.", "jus2", "demo"),
    ("jus2", "just", "Développer les peines alternatives à la prison", "Travaux d'intérêt général, bracelet électronique.", "jus1", "demo"),
    ("jus3", "just", "Calculer le montant des amendes routières en fonction des revenus", "Amendes proportionnelles.", "jus4", "nouveau"),
    ("jus4", "just", "Maintenir des amendes routières forfaitaires identiques pour tous", "Statu quo.", "jus3", "contrepoint"),
    ("jus5", "just", "Construire 20 000 places de prison supplémentaires", "Contre la surpopulation carcérale.", None, "nouveau"),
    ("jus6", "just", "Abaisser la majorité pénale à 16 ans", "Mineurs de 16 ans jugés comme des majeurs.", "jus7", "nouveau"),
    ("jus7", "just", "Maintenir la justice spécifique des mineurs et l'excuse de minorité", "Statu quo.", "jus6", "nouveau"),
    ("jus8", "just", "Doubler le budget de la justice sur le quinquennat", "Recrutement de magistrats et de greffiers.", None, "nouveau"),
    ("jus9", "just", "Créer une peine de perpétuité réelle, sans possibilité de libération", "Pour les crimes les plus graves.", None, "nouveau"),
    # ---- Immigration
    ("imm1", "immi", "Organiser un référendum sur l'immigration", "Consultation directe des Français.", None, "nouveau"),
    ("imm2", "immi", "Supprimer le droit du sol sur l'ensemble du territoire", "Nationalité par filiation ou naturalisation.", "imm3", "nouveau"),
    ("imm3", "immi", "Maintenir le droit du sol dans les conditions actuelles", "Statu quo.", "imm2", "nouveau"),
    ("imm4", "immi", "Régulariser les travailleurs sans papiers dans les métiers en tension", "Titre de séjour lié à l'emploi.", "imm5", "nouveau"),
    ("imm5", "immi", "Limiter les régularisations de sans-papiers aux cas exceptionnels", "Durcissement des conditions.", "imm4", "nouveau"),
    ("imm6", "immi", "Durcir les conditions du regroupement familial", "Ressources, logement, langue.", None, "nouveau"),
    ("imm7", "immi", "Réserver certaines prestations sociales aux Français (« priorité nationale »)", "Logement social, aides, emplois.", "imm8", "nouveau"),
    ("imm8", "immi", "Maintenir l'égalité d'accès aux prestations pour les étrangers en situation régulière", "Statu quo.", "imm7", "nouveau"),
    ("imm9", "immi", "Faire exécuter systématiquement les obligations de quitter le territoire (OQTF)", "Moyens et accords de retour.", None, "nouveau"),
    # ---- Europe et international
    ("eu1", "euro", "Renforcer l'intégration européenne", "Plus de compétences confiées à l'Union européenne.", "eu2", "demo"),
    ("eu2", "euro", "Rendre des compétences aux États membres de l'Union européenne", "Europe des nations.", "eu1", "contrepoint"),
    ("eu3", "euro", "Organiser un référendum sur la sortie de l'Union européenne", "Consultation sur l'appartenance à l'UE.", None, "nouveau"),
    ("eu4", "euro", "Sortir du commandement intégré de l'OTAN", "Indépendance militaire.", "eu5", "nouveau"),
    ("eu5", "euro", "Maintenir la pleine participation de la France à l'OTAN", "Statu quo.", "eu4", "nouveau"),
    ("eu6", "euro", "Porter le budget de la défense à 3 % du PIB", "Hausse des dépenses militaires.", None, "nouveau"),
    ("eu7", "euro", "Rétablir un service militaire obligatoire", "Pour les jeunes d'une classe d'âge.", None, "nouveau"),
    ("eu8", "euro", "Maintenir ou augmenter l'aide militaire à l'Ukraine", "Livraisons d'armes et soutien financier.", "eu9", "nouveau"),
    ("eu9", "euro", "Cesser les livraisons d'armes à l'Ukraine et privilégier la négociation", "Priorité à la diplomatie.", "eu8", "nouveau"),
    # ---- Institutions et démocratie
    ("ins1", "inst", "Instaurer le référendum d'initiative citoyenne (RIC)", "Référendum déclenché par pétition.", None, "demo"),
    ("ins2", "inst", "Introduire une dose de proportionnelle aux élections législatives", "Modification du mode de scrutin.", None, "demo"),
    ("ins3", "inst", "Prendre en compte le vote blanc, avec annulation de l'élection s'il arrive en tête", "Nouvelle élection avec d'autres candidats.", "ins4", "nouveau"),
    ("ins4", "inst", "Compter le vote blanc à part, sans effet sur le résultat", "Statu quo amélioré.", "ins3", "contrepoint"),
    ("ins5", "inst", "Permettre de révoquer le président de la République par référendum d'initiative citoyenne", "En cours de mandat.", "ins6", "nouveau"),
    ("ins6", "inst", "Conserver la durée fixe du mandat présidentiel, sans révocation", "Statu quo.", "ins5", "contrepoint"),
    ("ins7", "inst", "Rendre inéligible à vie un élu condamné pour corruption ou enrichissement personnel", "Sanction définitive.", "ins8", "nouveau"),
    ("ins8", "inst", "Maintenir des peines d'inéligibilité limitées dans le temps, fixées par le juge", "Statu quo.", "ins7", "contrepoint"),
    ("ins9", "inst", "Rendre publiques les rémunérations des hauts fonctionnaires", "Transparence.", None, "nouveau"),
    ("ins10", "inst", "Interdire aux hauts fonctionnaires de rejoindre une entreprise qu'ils ont contrôlée (« pantouflage »)", "Prévention des conflits d'intérêts.", "ins11", "nouveau"),
    ("ins11", "inst", "Encadrer le pantouflage par un délai et un avis déontologique, sans l'interdire", "Statu quo renforcé.", "ins10", "contrepoint"),
    ("ins12", "inst", "Supprimer l'article 49.3 de la Constitution", "Fin de l'adoption d'un texte sans vote.", None, "nouveau"),
]


def main():
    ids = {m[0] for m in M}
    assert len(ids) == len(M), "identifiants en double"
    themes_ids = {t[0] for t in THEMES}
    for m in M:
        assert m[1] in themes_ids, m
        assert m[4] is None or m[4] in ids, m
    themes = [{"id": t, "nom": n, "icone": i, "couleur": c, "ordre": k} for k, (t, n, i, c) in enumerate(THEMES)]
    mesures = [{"id": i, "theme": t, "intitule": it, "description": d, "opposee_a": o, "actif": True, "origine": org}
               for (i, t, it, d, o, org) in M]
    sortie = RACINE / "data" / "brouillon" / "catalogue.json"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps({"statut": "brouillon à relire", "themes": themes, "mesures": mesures},
                                 ensure_ascii=False, indent=2), encoding="utf-8")

    par_theme = Counter(m[1] for m in M)
    origines = Counter(m[5] for m in M)
    lignes = ["# Catalogue des mesures — brouillon à relire (lot 7, étape 2)", "",
              "*Généré par `python outils/catalogue.py` à partir de `outils/catalogue.py` : modifiez ce dernier, puis relancez.*", "",
              f"**{len(M)} mesures, {len(THEMES)} thèmes.** Origine : "
              + ", ".join(f"{k} {v}" for k, v in sorted(origines.items()))
              + " (demo = jeu de démonstration ; contrepoint = ajoutée pour l'équilibre ; nouveau = rédigée pour le catalogue).", "",
              "↔ indique la mesure opposée reliée. Points à vérifier : neutralité, exactitude des faits (statu quo cité), équilibre entre sensibilités.", ""]
    for t, n, i, _ in THEMES:
        lignes += [f"## {i} {n} ({par_theme[t]})", "", "| Id | Mesure | Précision | ↔ | Origine |", "|---|---|---|---|---|"]
        for (mid, th, it, d, o, org) in M:
            if th == t:
                lignes.append(f"| {mid} | {it} | {d} | {o or ''} | {org} |")
        lignes.append("")
    (RACINE / "docs" / "catalogue_mesures.md").write_text("\n".join(lignes), encoding="utf-8")
    ecrire_bilan(par_theme, origines)
    print(f"{len(M)} mesures, {len(THEMES)} thèmes — {dict(origines)}")
    print("Par thème :", dict(par_theme))
    print(f"Écrit : {sortie}, docs/catalogue_mesures.md et docs/bilan_catalogue.md")


def ecrire_bilan(par_theme, origines):
    """Bilan chiffré du catalogue, régénéré à chaque exécution (donc à chaque modification)."""
    from datetime import datetime
    paires = {t: sum(1 for m in M if m[1] == t and m[4]) // 2 for t, *_ in THEMES}
    seules = {t: sum(1 for m in M if m[1] == t and not m[4]) for t, *_ in THEMES}
    org_theme = {t: Counter(m[5] for m in M if m[1] == t) for t, *_ in THEMES}
    hors_cible = [n for t, n, *_ in THEMES if not 8 <= par_theme[t] <= 10]
    sans_paire = [n for t, n, *_ in THEMES if paires[t] == 0]
    L = ["# Bilan du catalogue des mesures", "",
         f"*Mis à jour automatiquement le {datetime.now().strftime('%d/%m/%Y à %H:%M')} par `python outils/catalogue.py`.*",
         "*À chaque modification du catalogue (`outils/catalogue.py`), relancer la commande : ce bilan est régénéré.*", "",
         f"**{sum(par_theme.values())} mesures** réparties sur **{len(THEMES)} thèmes** "
         f"(cible : 8 à 10 par thème, soit {8 * len(THEMES)} à {10 * len(THEMES)}).", "",
         "| Thème | Mesures | Paires opposées ↔ | Sans contrepoint | Démo | Contrepoints | Nouvelles |",
         "|---|---:|---:|---:|---:|---:|---:|"]
    for t, n, i, _ in THEMES:
        o = org_theme[t]
        L.append(f"| {i} {n} | {par_theme[t]} | {paires[t]} | {seules[t]} | {o['demo']} | {o['contrepoint']} | {o['nouveau']} |")
    L.append(f"| **Total** | **{sum(par_theme.values())}** | **{sum(paires.values())}** | **{sum(seules.values())}** | "
             f"**{origines['demo']}** | **{origines['contrepoint']}** | **{origines['nouveau']}** |")
    L += ["", "## Points d'attention", ""]
    L.append(f"- Thèmes hors de la cible de 8 à 10 mesures : {', '.join(hors_cible) if hors_cible else 'aucun'}.")
    L.append(f"- Thèmes sans aucune paire de mesures opposées : {', '.join(sans_paire) if sans_paire else 'aucun'}.")
    L.append("- Statut : **brouillon à relire** (neutralité, faits cités, confrontation aux programmes réels).")
    L += ["", "Détail des mesures : [catalogue_mesures.md](catalogue_mesures.md) · Méthode : [methode_choix_mesures.md](methode_choix_mesures.md)", ""]
    (RACINE / "docs" / "bilan_catalogue.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
