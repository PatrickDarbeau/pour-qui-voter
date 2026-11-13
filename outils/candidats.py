"""Fiches de profil des candidats retenus (lot 7, étape 3) — BROUILLON à relire.

Source de vérité des fiches : modifier ce fichier, puis lancer
    python outils/candidats.py
qui régénère data/brouillon/candidats.json et docs/fiches_candidats.md.

Règles : faits vérifiables uniquement, formulation neutre, chaque information sourcée.
Couleurs : choisies par l'éditeur le 13/11/2026 pour refléter la tendance politique de chaque candidat
(décision qui remplace la palette neutre initiale).
Profils (naissance, formation, profession) : extraits de Wikipédia en français (article cité dans les sources) ;
portraits : Wikimedia Commons, licences libres, crédits affichés sur la fiche (voir outils/portraits.py).
Liste retenue : docs/candidatures_probables.txt (10 candidats, validée le 12/11/2026).
"""
import json
import sys

from portraits import PORTRAITS
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
CONSULTE = "2026-11-12"

# Couleurs relevées dans le mode Édition le 13/11/2026 (choix de l'éditeur : tendance politique)
COULEURS = {
    "attal": "#0c5a43", "glucksmann": "#f38e86", "lepen": "#605aba", "lisnard": "#bf2ce8", "melenchon": "#c9131c",
    "philippe": "#02dfe3", "retailleau": "#0d69af", "riner": "#0074c2", "roussel": "#f32b2b", "zemmour": "#6a3d9a",
}

WIKI = "https://fr.wikipedia.org/wiki/"
WIKI_CONSULTE = "2026-11-13"
# Profils extraits de Wikipédia (infobox et sections « Études » / « Formation » / « Carrière ») — format uniforme :
#   naissance : (date ISO, « Ville (département ou pays) ») ; formation et profession : courtes, éléments séparés par « ; »
PROFILS = {
    "attal": {"wikipedia": WIKI + "Gabriel_Attal", "naissance": ("1989-03-16", "Clamart (Hauts-de-Seine)"),
              "formation": "Sciences Po Paris (master en affaires publiques, 2013)",
              "profession": "Conseiller en cabinet ministériel (2012-2017)"},
    "glucksmann": {"wikipedia": WIKI + "Raphaël_Glucksmann", "naissance": ("1979-10-15", "Boulogne-Billancourt (Hauts-de-Seine)"),
                   "formation": "Sciences Po Paris",
                   "profession": "Réalisateur de documentaires ; journaliste ; essayiste"},
    "lepen": {"wikipedia": WIKI + "Marine_Le_Pen", "naissance": ("1968-08-05", "Neuilly-sur-Seine (Hauts-de-Seine)"),
              "formation": "Université Panthéon-Assas (droit)",
              "profession": "Avocate"},
    "lisnard": {"wikipedia": WIKI + "David_Lisnard", "naissance": ("1969-02-02", "Limoges (Haute-Vienne)"),
                "formation": "Sciences Po Bordeaux (1992) ; université Paris-Panthéon-Assas (droit public)",
                "profession": "Journaliste pigiste ; commerçant"},
    "melenchon": {"wikipedia": WIKI + "Jean-Luc_Mélenchon", "naissance": ("1951-08-19", "Tanger (Maroc)"),
                  "formation": "Université de Franche-Comté",
                  "profession": "Professeur de français ; journaliste"},
    "philippe": {"wikipedia": WIKI + "Édouard_Philippe", "naissance": ("1970-11-28", "Rouen (Seine-Maritime)"),
                 "formation": "Sciences Po Paris ; École nationale d'administration (ENA)",
                 "profession": "Haut fonctionnaire (Conseil d'État) ; avocat"},
    "retailleau": {"wikipedia": WIKI + "Bruno_Retailleau", "naissance": ("1960-11-20", "Cholet (Maine-et-Loire)"),
                   "formation": "Sciences Po Paris ; Nantes Université",
                   "profession": "Dirigeant de société"},
    "riner": {"wikipedia": WIKI + "Teddy_Riner", "naissance": ("1989-04-07", "Pointe-à-Pitre (Guadeloupe)"),
              "formation": "INSEP ; Sciences Po (certificat pour sportifs de haut niveau, 2011-2015)",
              "profession": "Judoka"},
    "roussel": {"wikipedia": WIKI + "Fabien_Roussel", "naissance": ("1969-04-16", "Béthune (Pas-de-Calais)"),
                "formation": "CFPJ (journaliste reporter d'images)",
                "profession": "Journaliste"},
    "zemmour": {"wikipedia": WIKI + "Éric_Zemmour", "naissance": ("1958-08-31", "Montreuil (Seine)"),
                "formation": "Sciences Po Paris",
                "profession": "Journaliste ; écrivain ; essayiste"},
}

CANDIDATS = [
    {
        "id": "attal", "prenom": "Gabriel", "nom": "Attal", "parti": "Renaissance",
        "biographie": "Ancien Premier ministre (2024). Secrétaire général de Renaissance. Candidature annoncée le 22 mai 2026.",
        "slogan": "La force d'agir",
        "site_officiel": "https://attalpresident.fr", "site_type": "campagne",
        "sources": ["https://lcp.fr/actualites/presidentielle-2027-gabriel-attal-officialise-sa-candidature-436721",
                    "https://attalpresident.fr/mentions-legales"],
        "a_verifier": ["Site de campagne attalpresident.fr trouvé le 13/11/2026 (édité par Renaissance) : programme publié mesure par mesure"],
    },
    {
        "id": "glucksmann", "prenom": "Raphaël", "nom": "Glucksmann", "parti": "Place publique",
        "biographie": "Député européen, cofondateur de Place publique. Candidature annoncée le 23 août 2026 ; désigné par la primaire sociale-démocrate du 11 octobre 2026 (66,17 % des voix).",
        "pages_programme": ["https://glucks2027.fr/revolution-ecologique/", "https://glucks2027.fr/wp-content/uploads/2026/11/livret_progr_revolution_ecologique_2027.pdf", "https://place-publique.eu/pages/69jA2SKIG5udlNX7wI3dmc/le-projet", "https://place-publique.eu/document/6J8wjk3EW8dBCLwKxa7J96/projet-placepublique-acte1.pdf", "https://place-publique.eu/pages/59EfFYTpFlj2lJhQ92PXsy/les-combats", "https://place-publique.eu/posts/2fgDdljEIy36rgxBjRyiQZ/raphael-glucksmann-sa-lettre-aux-francais", "https://place-publique.eu/posts/5hZ1DizFpQdRh9GXoUHhGJ/les-5-prochains-mois-nous-les-vivrons-a-credit", "https://place-publique.eu/posts/5alHI42mxxIp7GNFA9ImFX/franchises-medicales-s-lecornu-envoie-la-facture-du-deficit-aux-malades"],
        "slogan": None,
        "site_officiel": "https://glucks2027.fr", "site_type": "campagne",
        "sources": ["https://lcp.fr/actualites/gagner-en-2027-raphael-glucksmann-lance-sa-campagne-et-veut-ramener-la-gauche-au-pouvoir",
                    "https://es.euronews.com/2026/08/23/presidencial-francesa-2027-raphael-glucksmann-entra-en-liza"],
        "a_verifier": ["Programme complet (le plan « Révolution écologique » est présenté comme la première partie)"],
    },
    {
        "id": "lepen", "prenom": "Marine", "nom": "Le Pen", "parti": "Rassemblement national",
        "biographie": "Députée, ancienne présidente du Rassemblement national, candidate en 2012, 2017 et 2022. Candidature annoncée le 7 juillet 2026, après sa condamnation en appel ; pourvoi en cassation en cours.",
        "slogan": None,
        "site_officiel": "https://marinelepen.com", "site_type": "campagne",
        "sources": ["https://www.publicsenat.fr/actualites/politique/presidentielle-marine-le-pen-est-candidate-et-se-pourvoit-en-cassation",
                    "https://www.leclubdesjuristes.com/en-bref/marine-le-pen-candidate-a-la-presidentielle-de-2027-malgre-sa-condamnation-en-appel-16843/"],
        "a_verifier": ["Site de campagne marinelepen.com trouvé le 13/11/2026 (par Hermès) : aucun programme publié ; réforme des retraites détaillée annoncée pour le 17/11/2026"],
    },
    {
        "id": "lisnard", "prenom": "David", "nom": "Lisnard", "parti": "Nouvelle Énergie",
        "biographie": "Maire de Cannes. A quitté Les Républicains pour se présenter sous l'étiquette de son mouvement, Nouvelle Énergie.",
        "pages_programme": ["https://www.unenouvelleenergie.fr/notre-programme/", "https://www.unenouvelleenergie.fr/notre-programme/etre-maitre-de-notre-destin/", "https://www.unenouvelleenergie.fr/notre-programme/reussir-une-nouvelle-ambition-francaise/", "https://www.unenouvelleenergie.fr/notre-programme/generer-un-renouveau-civique/", "https://www.unenouvelleenergie.fr/notre-programme/agriculture/", "https://www.unenouvelleenergie.fr/notre-programme/education/", "https://www.unenouvelleenergie.fr/notre-programme/immigration/", "https://www.unenouvelleenergie.fr/notre-programme/sante/", "https://www.unenouvelleenergie.fr/notre-programme/securite/"],
        "slogan": None,
        "site_officiel": "https://www.unenouvelleenergie.fr", "site_type": "mouvement",
        "sources": ["https://lcp.fr/actualites/je-suis-candidat-david-lisnard-quitte-lr-et-relance-le-debat-sur-une-primaire-a-droite"],
        "a_verifier": ["Date exacte de la déclaration de candidature"],
    },
    {
        "id": "melenchon", "prenom": "Jean-Luc", "nom": "Mélenchon", "parti": "La France insoumise",
        "biographie": "Fondateur de La France insoumise, ancien député et ancien ministre, candidat en 2012, 2017 et 2022. Programme : « L'Avenir en commun » (nouvelle version 2026).",
        "pages_programme": ["https://melenchon2027.fr/programme/livre/", "https://melenchon2027.fr/programme/livre/fonder-la-6e-republique", "https://melenchon2027.fr/programme/livre/fonder-la-6e-republique/chapitre1", "https://melenchon2027.fr/programme/livre/fonder-la-6e-republique/chapitre2", "https://melenchon2027.fr/programme/livre/fonder-la-6e-republique/chapitre3", "https://melenchon2027.fr/programme/livre/introduction", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre1", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre2", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre3", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre4", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre5", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre6", "https://melenchon2027.fr/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre7", "https://melenchon2027.fr/programme/livre/mettre-en-securite-sociale", "https://melenchon2027.fr/programme/livre/mettre-en-securite-sociale/chapitre1", "https://melenchon2027.fr/programme/livre/mettre-en-securite-sociale/chapitre2", "https://melenchon2027.fr/programme/livre/mettre-en-securite-sociale/chapitre3", "https://melenchon2027.fr/programme/livre/mettre-en-securite-sociale/chapitre4", "https://melenchon2027.fr/programme/livre/pour-une-bifurcation-ecologique-et-sociale", "https://melenchon2027.fr/programme/livre/pour-une-bifurcation-ecologique-et-sociale/chapitre1", "https://melenchon2027.fr/programme/livre/pour-une-bifurcation-ecologique-et-sociale/chapitre2", "https://melenchon2027.fr/programme/livre/pour-une-bifurcation-ecologique-et-sociale/chapitre3", "https://melenchon2027.fr/programme/livre/un-monde-ordonne", "https://melenchon2027.fr/programme/livre/un-monde-ordonne/chapitre1", "https://melenchon2027.fr/programme/livre/un-monde-ordonne/chapitre2", "https://melenchon2027.fr/programme/livre/un-monde-ordonne/chapitre3", "https://melenchon2027.fr/programme/livre/une-economie-au-service-des-besoins", "https://melenchon2027.fr/programme/livre/une-economie-au-service-des-besoins/chapitre1", "https://melenchon2027.fr/programme/livre/une-economie-au-service-des-besoins/chapitre2", "https://melenchon2027.fr/programme/livre/une-economie-au-service-des-besoins/chapitre3", "https://melenchon2027.fr/programme/plans-thematiques/", "https://melenchon2027.fr/programme/plans-thematiques/sante/", "https://melenchon2027.fr/programme/plans-thematiques/esr/", "https://melenchon2027.fr/programme/plans-thematiques/ruralite/"],
        "slogan": None,
        "site_officiel": "https://melenchon2027.fr", "site_type": "campagne",
        "sources": ["https://lcp.fr/actualites/presidentielle-2027-ce-qui-change-dans-le-nouveau-programme-de-jean-luc-melenchon-444841",
                    "https://melenchon2027.fr/"],
        "a_verifier": [],
    },
    {
        "id": "philippe", "prenom": "Édouard", "nom": "Philippe", "parti": "Horizons",
        "biographie": "Ancien Premier ministre (2017-2020), maire du Havre, président d'Horizons. Candidat déclaré depuis septembre 2024.",
        "pages_programme": ["https://www.edouardphilippe.fr/programme", "https://www.edouardphilippe.fr/programme/adaptation-climatique", "https://www.edouardphilippe.fr/programme/comptes-publics", "https://www.edouardphilippe.fr/programme/defense", "https://www.edouardphilippe.fr/programme/ecole", "https://www.edouardphilippe.fr/programme/energie", "https://www.edouardphilippe.fr/programme/entreprises", "https://www.edouardphilippe.fr/programme/famille", "https://www.edouardphilippe.fr/programme/immigration", "https://www.edouardphilippe.fr/programme/intelligence-artificielle", "https://www.edouardphilippe.fr/programme/justice", "https://www.edouardphilippe.fr/programme/outre-mer", "https://www.edouardphilippe.fr/programme/protection-de-l-enfance", "https://www.edouardphilippe.fr/programme/retraites", "https://www.edouardphilippe.fr/programme/securite", "https://www.edouardphilippe.fr/programme/travail", "https://horizonsleparti.fr/le-plan-dedouard-philippe-contre-le-narcotrafic/"],
        "slogan": None,
        "site_officiel": "https://www.edouardphilippe.fr", "site_type": "campagne",
        "sources": ["https://connexionfrance.com/news/former-french-pm-edouard-philippe-announces-presidential-candidacy/676922"],
        "a_verifier": [],
    },
    {
        "id": "retailleau", "prenom": "Bruno", "nom": "Retailleau", "parti": "Les Républicains",
        "biographie": "Président des Républicains, ancien ministre de l'Intérieur. Candidature annoncée le 12 février 2026 ; désigné par son parti en avril 2026.",
        "pages_programme": ["https://republicains.fr/nos-propositions/", "https://republicains.fr/actualites/2026/09/23/je-veux-sauver-notre-systeme-de-retraite/", "https://republicains.fr/actualites/2026/09/15/ce-que-je-veux-faire-pour-le-pouvoir-dachat/", "https://republicains.fr/actualites/2026/09/06/on-est-dans-un-gouvernement-des-juges/", "https://republicains.fr/actualites/2026/09/02/en-france-la-seule-cour-supreme-cest-le-peuple-je-lui-donnerai-le-dernier-mot/", "https://republicains.fr/actualites/2026/08/26/je-serai-le-president-qui-baissera-les-impots-de-succession/", "https://republicains.fr/actualites/2026/08/09/face-au-rechauffement-climatique-adapter-la-france-plutot-que-punir/", "https://republicains.fr/actualites/2026/08/02/lespace-schengen-doit-etre-reserve-aux-europeens/", "https://republicains.fr/actualites/2026/07/15/une-grande-nation-ne-repond-pas-a-la-souffrance-par-la-mort/", "https://republicains.fr/actualites/2026/07/08/je-veux-rendre-la-parole-aux-francais/", "https://republicains.fr/actualites/2026/07/01/la-prochaine-catastrophe-sera-budgetaire/", "https://republicains.fr/actualites/2026/06/09/mettre-fin-au-corporatisme-judiciaire/", "https://republicains.fr/actualites/2026/06/06/il-faut-creer-une-cour-disciplinaire-de-la-magistrature/", "https://republicains.fr/actualites/2026/06/01/les-zones-demeutes-correspondent-aux-zones-dimmigration-importante/", "https://republicains.fr/actualites/2026/05/02/priorite-travail-france-35h-salaires-retraites/", "https://republicains.fr/actualites/2026/04/29/algerie-ma-lettre-a-emmanuel-macron/", "https://republicains.fr/actualites/2026/03/01/la-dissuasion-nucleaire-francaise-ne-se-partage-pas/", "https://republicains.fr/actualites/2026/01/05/refuser-la-dependance-numerique-culturelle-defendre-lindependance-europeenne/", "https://republicains.fr/actualites/2025/12/18/ce-que-jai-dit-a-la-droite-europeenne/", "https://republicains.fr/wp-content/uploads/2026/01/51705_LesRepublicains_Brochures_A5-40P_DEF.pdf", "https://republicains.fr/wp-content/uploads/2026/02/LR_Produire_Plus_LIVRET.pdf", "https://republicains.fr/wp-content/uploads/2026/03/LR_Agriculture.pdf", "https://republicains.fr/wp-content/uploads/2026/05/LR_Electricite_vFF070626.pdf", "https://republicains.fr/wp-content/uploads/2026/05/LR_Famille_vFinale.pdf", "https://republicains.fr/wp-content/uploads/2026/05/LR_Logement.pdf", "https://republicains.fr/wp-content/uploads/2026/07/LR_IA.pdf", "https://republicains.fr/wp-content/uploads/2026/09/LR_Ecole_vF.pdf"],
        "slogan": None,
        "site_officiel": "https://republicains.fr", "site_type": "parti",
        "sources": ["https://www.publicsenat.fr/actualites/politique/je-suis-pret-bruno-retailleau-se-declare-candidat-a-lelection-presidentielle-2027",
                    "https://www.franceinfo.fr/elections/presidentielle/portraits-qui-sont-les-candidats-declares-a-l-election-presidentielle-de-2027_8208032.html"],
        "a_verifier": ["Site de campagne propre au candidat"],
    },
    {
        "id": "riner", "prenom": "Teddy", "nom": "Riner", "parti": "Sans étiquette",
        "biographie": "Judoka, quintuple champion olympique. Candidature annoncée le 9 novembre 2026, sans étiquette (« ni de droite, ni de gauche »).",
        "slogan": "La France qu'on veut",
        "site_officiel": None, "site_type": None,
        "sources": ["https://lcp.fr/actualites/le-judoka-teddy-riner-annonce-sa-candidature-a-l-election-presidentielle-de-2027-444920"],
        "a_verifier": ["Site « La France qu'on veut » : adresse probable riner2027.fr (adresse de contact du candidat), hors service le 13/11/2026 ; seules trois pistes de programme rapportées par la presse (09/11/2026)"],
    },
    {
        "id": "roussel", "prenom": "Fabien", "nom": "Roussel", "parti": "Parti communiste français",
        "biographie": "Secrétaire national du Parti communiste français, candidat en 2022. Candidature validée par les adhérents et officialisée en septembre 2026.",
        "slogan": None,
        "site_officiel": "https://www.fabienroussel2027.fr", "site_type": "campagne",
        "pages_programme": ["https://www.fabienroussel2027.fr/materiel"],
        "sources": ["https://lcp.fr/actualites/fabien-roussel-officiellement-candidat-du-pcf-a-l-election-presidentielle-de-2027-441389",
                    "https://www.fabienroussel2027.fr"],
        "a_verifier": ["Programme détaillé (le site présente un manifeste, « VIVRE ! »)"],
    },
    {
        "id": "zemmour", "prenom": "Éric", "nom": "Zemmour", "parti": "Reconquête",
        "biographie": "Président de Reconquête, candidat en 2022. Candidature confirmée à l'automne 2026.",
        "slogan": None,
        "site_officiel": "https://www.ericzemmour.fr", "site_type": "campagne",
        "pages_programme": ["https://www.ericzemmour.fr/priorites"],
        "sources": ["https://lcp.fr/actualites/presidentielle-2027-eric-zemmour-officialise-sa-candidature-441871",
                    "https://fr.euronews.com/2026/11/10/eric-zemmour-annonce-sa-candidature-a-la-presidentielle"],
        "a_verifier": ["Date de la déclaration officielle (17/09 ou 10/11/2026 selon les sources)", "Programme détaillé (page « Priorités » seulement)"],
    },
]


def main():
    ids = [c["id"] for c in CANDIDATS]
    assert len(set(ids)) == len(ids), "identifiants en double"
    # Conserver la date de dernière collecte écrite par « maj.py collecter »
    sortie = RACINE / "data" / "brouillon" / "candidats.json"
    anciens = {}
    if sortie.exists():
        anciens = {x["id"]: x for x in json.loads(sortie.read_text(encoding="utf-8")).get("candidats", [])}
    fiches = []
    assert set(COULEURS) == set(PROFILS) == set(PORTRAITS) == set(ids), "couleur, profil ou portrait manquant"
    for c in sorted(CANDIDATS, key=lambda x: x["nom"]):
        pr, ph = PROFILS[c["id"]], PORTRAITS[c["id"]]
        fiches.append({
            "id": c["id"], "prenom": c["prenom"], "nom": c["nom"], "parti": c["parti"],
            "couleur": COULEURS[c["id"]], "biographie": c["biographie"], "slogan": c["slogan"],
            "date_naissance": pr["naissance"][0], "lieu_naissance": pr["naissance"][1],
            "formation": pr["formation"], "profession": pr["profession"],
            "wikipedia": pr["wikipedia"], "wikipedia_consulte": WIKI_CONSULTE,
            "photo": f"assets/img/candidats/{c['id']}.jpg",
            "photo_credit": {"auteur": ph["auteur"], "licence": ph["licence"], "licence_url": ph["licence_url"], "source": ph["page"]},
            "site_officiel": c["site_officiel"],
            "pages_programme": c.get("pages_programme", []), "programme_url": None, "statut": "declare",
            "derniere_collecte": anciens.get(c["id"], {}).get("derniere_collecte"), "sources_profil": c["sources"] + [pr["wikipedia"]], "consulte_le": CONSULTE,
            "a_verifier": c["a_verifier"],
        })
    sortie = RACINE / "data" / "brouillon" / "candidats.json"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps({"statut": "brouillon à relire", "candidats": fiches}, ensure_ascii=False, indent=2), encoding="utf-8")

    L = ["# Fiches de profil des candidats — brouillon à relire (lot 7, étape 3)", "",
         f"*Généré par `python outils/candidats.py` le {date.today().strftime('%d/%m/%Y')}. Sources consultées le {CONSULTE}. "
         "Liste retenue : `docs/candidatures_probables.txt`.*", "",
         f"**{len(fiches)} candidats.** Biographies limitées à des faits vérifiables et sourcés ; couleurs choisies par l'éditeur (tendance politique). "
         f"Naissance, formation et profession : Wikipédia, consulté le {WIKI_CONSULTE}.", "",
         "| Candidat | Parti | Naissance | Formation | Profession | Biographie | Site | Points à vérifier |", "|---|---|---|---|---|---|---|---|"]
    for f in fiches:
        c = next(x for x in CANDIDATS if x["id"] == f["id"])
        site = f"[{c['site_type']}]({f['site_officiel']})" if f["site_officiel"] else "—"
        j = date.fromisoformat(f["date_naissance"])
        L.append(f"| **{f['prenom']} {f['nom']}** | {f['parti']} | {j.strftime('%d/%m/%Y')}, {f['lieu_naissance']} "
                 f"| {f['formation']} | {f['profession']} | {f['biographie']}"
                 + (f" Slogan : « {f['slogan']} »." if f["slogan"] else "")
                 + f" | {site} | {'<br>'.join('☐ ' + v for v in f['a_verifier']) or '—'} |")
    L += ["", "## Sources des fiches", ""]
    for f in fiches:
        L.append(f"- **{f['prenom']} {f['nom']}** : " + " · ".join(f"<{u}>" for u in f["sources_profil"]))
    L += ["", "## Portraits (Wikimedia Commons)", "", "| Candidat | Auteur | Licence | Fichier |", "|---|---|---|---|"]
    for f in fiches:
        pc = f["photo_credit"]
        L.append(f"| {f['prenom']} {f['nom']} | {pc['auteur']} | [{pc['licence']}]({pc['licence_url']}) | <{pc['source']}> |")
    L += ["", "Type de site : *campagne* = site de campagne du candidat ; *parti* ou *mouvement* = site de sa formation, "
          "en attendant un site de campagne. Tous les sites ont été vérifiés accessibles le 12/11/2026.", ""]
    (RACINE / "docs" / "fiches_candidats.md").write_text("\n".join(L), encoding="utf-8")
    print(f"{len(fiches)} fiches — écrit : {sortie} et docs/fiches_candidats.md")


if __name__ == "__main__":
    main()
