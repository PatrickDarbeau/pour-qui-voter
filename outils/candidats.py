"""Fiches de profil des candidats retenus (lot 7, étape 3) — BROUILLON à relire.

Source de vérité des fiches : modifier ce fichier, puis lancer
    python outils/candidats.py
qui régénère data/brouillon/candidats.json et docs/fiches_candidats.md.

Règles : faits vérifiables uniquement, formulation neutre, chaque information sourcée.
Couleurs : palette neutre (pas de couleurs partisanes, CDC §5 « neutralité »).
Liste retenue : docs/candidatures_probables.txt (10 candidats, validée le 12/11/2026).
"""
import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
CONSULTE = "2026-11-12"

# Palette neutre, attribuée dans l'ordre alphabétique
PALETTE = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#1f78b4", "#b15928", "#6a3d9a"]

CANDIDATS = [
    {
        "id": "attal", "prenom": "Gabriel", "nom": "Attal", "parti": "Renaissance",
        "biographie": "Ancien Premier ministre (2024). Secrétaire général de Renaissance. Candidature annoncée le 22 mai 2026.",
        "slogan": None,
        "site_officiel": "https://parti-renaissance.fr", "site_type": "parti",
        "sources": ["https://lcp.fr/actualites/presidentielle-2027-gabriel-attal-officialise-sa-candidature-436721"],
        "a_verifier": ["Site de campagne 2027 (gabrielattal.fr est son site des législatives 2024) et programme (non trouvés au 12/11/2026)"],
    },
    {
        "id": "glucksmann", "prenom": "Raphaël", "nom": "Glucksmann", "parti": "Place publique",
        "biographie": "Député européen, cofondateur de Place publique. Candidature annoncée le 23 août 2026 ; participant à la primaire sociale-démocrate d'octobre 2026.",
        "pages_programme": ["https://place-publique.eu/pages/69jA2SKIG5udlNX7wI3dmc/le-projet"],
        "slogan": None,
        "site_officiel": "https://place-publique.eu", "site_type": "parti",
        "sources": ["https://lcp.fr/actualites/gagner-en-2027-raphael-glucksmann-lance-sa-campagne-et-veut-ramener-la-gauche-au-pouvoir",
                    "https://es.euronews.com/2026/08/23/presidencial-francesa-2027-raphael-glucksmann-entra-en-liza"],
        "a_verifier": ["Résultat de la primaire sociale-démocrate du 11/10/2026", "Site de campagne propre au candidat"],
    },
    {
        "id": "lepen", "prenom": "Marine", "nom": "Le Pen", "parti": "Rassemblement national",
        "biographie": "Députée, ancienne présidente du Rassemblement national, candidate en 2012, 2017 et 2022. Candidature annoncée le 7 juillet 2026, après sa condamnation en appel ; pourvoi en cassation en cours.",
        "slogan": None,
        "site_officiel": "https://rassemblementnational.fr", "site_type": "parti",
        "sources": ["https://www.publicsenat.fr/actualites/politique/presidentielle-marine-le-pen-est-candidate-et-se-pourvoit-en-cassation",
                    "https://www.leclubdesjuristes.com/en-bref/marine-le-pen-candidate-a-la-presidentielle-de-2027-malgre-sa-condamnation-en-appel-16843/"],
        "a_verifier": ["Site de campagne et programme 2027 (non trouvés ; le site du RN bloque la collecte automatique)", "Mandat actuel (députée) à confirmer", "Issue du pourvoi en cassation (éligibilité)", "Candidature éventuelle de Jordan Bardella", "Site de campagne propre à la candidate"],
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
        "pages_programme": ["https://horizonsleparti.fr/le-pole-idees/"],
        "slogan": None,
        "site_officiel": "https://horizonsleparti.fr", "site_type": "parti",
        "sources": ["https://connexionfrance.com/news/former-french-pm-edouard-philippe-announces-presidential-candidacy/676922"],
        "a_verifier": ["Site de campagne propre au candidat"],
    },
    {
        "id": "retailleau", "prenom": "Bruno", "nom": "Retailleau", "parti": "Les Républicains",
        "biographie": "Président des Républicains, ancien ministre de l'Intérieur. Candidature annoncée le 12 février 2026 ; désigné par son parti en avril 2026.",
        "pages_programme": ["https://republicains.fr/nos-propositions/", "https://republicains.fr/wp-content/uploads/2026/01/51705_LesRepublicains_Brochures_A5-40P_DEF.pdf", "https://republicains.fr/wp-content/uploads/2026/02/LR_Produire_Plus_LIVRET.pdf", "https://republicains.fr/wp-content/uploads/2026/03/LR_Agriculture.pdf", "https://republicains.fr/wp-content/uploads/2026/05/LR_Electricite_vFF070626.pdf", "https://republicains.fr/wp-content/uploads/2026/05/LR_Famille_vFinale.pdf", "https://republicains.fr/wp-content/uploads/2026/05/LR_Logement.pdf", "https://republicains.fr/wp-content/uploads/2026/07/LR_IA.pdf", "https://republicains.fr/wp-content/uploads/2026/09/LR_Ecole_vF.pdf"],
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
        "a_verifier": ["Site de campagne « La France qu'on veut » annoncé par la presse, adresse non trouvée au 12/11/2026", "Programme (annoncé, non publié)"],
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
    for k, c in enumerate(sorted(CANDIDATS, key=lambda x: x["nom"])):
        fiches.append({
            "id": c["id"], "prenom": c["prenom"], "nom": c["nom"], "parti": c["parti"],
            "couleur": PALETTE[k % len(PALETTE)], "biographie": c["biographie"], "slogan": c["slogan"],
            "photo": None, "site_officiel": c["site_officiel"],
            "pages_programme": c.get("pages_programme", []), "programme_url": None, "statut": "declare",
            "derniere_collecte": anciens.get(c["id"], {}).get("derniere_collecte"), "sources_profil": c["sources"], "consulte_le": CONSULTE,
            "a_verifier": c["a_verifier"],
        })
    sortie = RACINE / "data" / "brouillon" / "candidats.json"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps({"statut": "brouillon à relire", "candidats": fiches}, ensure_ascii=False, indent=2), encoding="utf-8")

    L = ["# Fiches de profil des candidats — brouillon à relire (lot 7, étape 3)", "",
         f"*Généré par `python outils/candidats.py` le {date.today().strftime('%d/%m/%Y')}. Sources consultées le {CONSULTE}. "
         "Liste retenue : `docs/candidatures_probables.txt`.*", "",
         f"**{len(fiches)} candidats.** Biographies limitées à des faits vérifiables et sourcés ; couleurs neutres (pas de couleurs partisanes).", "",
         "| Candidat | Parti | Biographie | Site | Points à vérifier |", "|---|---|---|---|---|"]
    for f in fiches:
        c = next(x for x in CANDIDATS if x["id"] == f["id"])
        site = f"[{c['site_type']}]({f['site_officiel']})" if f["site_officiel"] else "—"
        L.append(f"| **{f['prenom']} {f['nom']}** | {f['parti']} | {f['biographie']}"
                 + (f" Slogan : « {f['slogan']} »." if f["slogan"] else "")
                 + f" | {site} | {'<br>'.join('☐ ' + v for v in f['a_verifier']) or '—'} |")
    L += ["", "## Sources des fiches", ""]
    for f in fiches:
        L.append(f"- **{f['prenom']} {f['nom']}** : " + " · ".join(f"<{u}>" for u in f["sources_profil"]))
    L += ["", "Type de site : *campagne* = site de campagne du candidat ; *parti* ou *mouvement* = site de sa formation, "
          "en attendant un site de campagne. Tous les sites ont été vérifiés accessibles le 12/11/2026.", ""]
    (RACINE / "docs" / "fiches_candidats.md").write_text("\n".join(L), encoding="utf-8")
    print(f"{len(fiches)} fiches — écrit : {sortie} et docs/fiches_candidats.md")


if __name__ == "__main__":
    main()
