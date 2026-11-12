"""Génère un pack de données de démonstration (candidats FICTIFS) dans data/donnees.json.

Usage : python outils/demo.py
"""
import json
from datetime import date
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

THEMES = [
    ("economie", "Économie", "💶", "#2f6fb0"),
    ("sante", "Santé", "🩺", "#c0392b"),
    ("education", "Éducation", "🎓", "#8e44ad"),
    ("ecologie", "Écologie", "🌿", "#27ae60"),
    ("securite", "Sécurité et justice", "⚖️", "#34495e"),
    ("institutions", "Institutions et Europe", "🏛️", "#d68910"),
]

# (id, thème, intitulé, description, id de la mesure opposée ou None)
MESURES = [
    ("eco1", "economie", "Abaisser l'âge légal de départ à la retraite à 62 ans", "Revenir sur le recul de l'âge de départ.", "eco2"),
    ("eco2", "economie", "Porter l'âge légal de départ à la retraite à 65 ans", "Allonger la durée d'activité pour financer les retraites.", "eco1"),
    ("eco3", "economie", "Augmenter le SMIC de 10 %", "Revalorisation exceptionnelle du salaire minimum.", None),
    ("eco4", "economie", "Baisser les impôts de production des entreprises", "Réduire la fiscalité pesant sur l'outil productif.", None),
    ("san1", "sante", "Recruter 20 000 soignants à l'hôpital public", "Plan pluriannuel d'embauches.", None),
    ("san2", "sante", "Réguler l'installation des médecins dans les zones surdotées", "Lutter contre les déserts médicaux.", None),
    ("san3", "sante", "Rembourser intégralement les soins dentaires et optiques", "Extension du « 100 % santé ».", None),
    ("edu1", "education", "Limiter les classes à 24 élèves en primaire", "Réduction des effectifs par classe.", None),
    ("edu2", "education", "Augmenter le salaire des enseignants de 15 %", "Revalorisation sur la durée du quinquennat.", None),
    ("edu3", "education", "Rendre l'uniforme obligatoire à l'école", "Tenue commune dans le primaire et le secondaire.", None),
    ("ecl1", "ecologie", "Sortir progressivement du nucléaire", "Fermeture des réacteurs en fin de vie sans remplacement.", "ecl2"),
    ("ecl2", "ecologie", "Construire de nouveaux réacteurs nucléaires", "Programme de nouveaux EPR.", "ecl1"),
    ("ecl3", "ecologie", "Interdire les vols intérieurs lorsqu'un trajet en train de moins de 4 h existe", "Report modal vers le rail.", None),
    ("ecl4", "ecologie", "Taxer le kérosène des vols", "Fin de l'exonération du carburant aérien.", None),
    ("sec1", "securite", "Recruter 10 000 policiers et gendarmes", "Renforcement des effectifs de terrain.", None),
    ("sec2", "securite", "Instaurer des peines planchers", "Peines minimales pour les récidivistes.", None),
    ("sec3", "securite", "Développer les peines alternatives à la prison", "Travaux d'intérêt général, bracelet électronique.", None),
    ("ins1", "institutions", "Instaurer le référendum d'initiative citoyenne", "Référendum déclenché par pétition.", None),
    ("ins2", "institutions", "Introduire une dose de proportionnelle aux législatives", "Modification du mode de scrutin.", None),
    ("ins3", "institutions", "Renforcer l'intégration européenne", "Plus de compétences confiées à l'Union européenne.", None),
]

# Positions par candidat, dans l'ordre de MESURES :
# + soutient, ~ soutient partiellement, 0 ne se prononce pas, - s'oppose
CANDIDATS = [
    ("c1", "Claire", "Durand", "Parti de l'Avenir Social (fictif)", "#e74c3c",
     "Ancienne inspectrice du travail, députée depuis 2017.", "Le progrès pour tous",
     "+-++ +++ ++- +-++ ~-+ +++"),
    ("c2", "Marc", "Lefèvre", "Union Libérale (fictif)", "#3498db",
     "Chef d'entreprise, ancien ministre de l'Économie.", "Libérer l'énergie française",
     "-+-+ +-0 0+~ -+-- +~- 0~+"),
    ("c3", "Inès", "Moreau", "Mouvement Écologiste (fictif)", "#2ecc71",
     "Ingénieure agronome, maire d'une ville moyenne.", "Réparer la planète",
     "+-+- +++ +~- +-++ 0-+ +++"),
    ("c4", "Paul", "Garnier", "Rassemblement National-Populaire (fictif)", "#2c3e50",
     "Avocat, conseiller régional.", "La France d'abord",
     "+-0+ ++~ ~++ -+-- ++- +--"),
]

VAL = {"+": 1, "~": 0.5, "0": 0, "-": -1}


sys.stdout.reconfigure(encoding="utf-8") if hasattr(sys.stdout, "reconfigure") else None


def main():
    themes = [
        {"id": t, "nom": n, "icone": i, "couleur": c, "ordre": k}
        for k, (t, n, i, c) in enumerate(THEMES)
    ]
    mesures = [
        {"id": m, "theme": t, "intitule": it, "description": d,
         "opposee_a": o, "actif": True}
        for (m, t, it, d, o) in MESURES
    ]
    candidats, positions = [], []
    for (cid, prenom, nom, parti, coul, bio, slogan, code) in CANDIDATS:
        candidats.append({
            "id": cid, "prenom": prenom, "nom": nom, "parti": parti,
            "couleur": coul, "biographie": bio, "slogan": slogan,
            "photo": None, "site_officiel": None, "pages_programme": [],
            "programme_url": None, "statut": "fictif", "derniere_collecte": None,
        })
        codes = code.replace(" ", "")
        assert len(codes) == len(MESURES), cid
        for (m, *_), ch in zip(MESURES, codes):
            positions.append({
                "candidat": cid, "mesure": m, "valeur": VAL[ch],
                "source_url": "https://exemple.invalid/programme-fictif",
                "source_type": "site_officiel", "source_date": "2026-11-01",
                "citation": None, "a_confirmer": False,
            })
    pack = {
        "format": 1,
        "version": date.today().strftime("%Y.%m.%d") + "-demo",
        "date": date.today().isoformat(),
        "origine": "officiel",
        "demo": True,
        "auteur": "Jeu de démonstration — candidats fictifs",
        "licence": "CC BY-SA 4.0", "source_projet": "https://github.com/PatrickDarbeau/pour-qui-voter",
        "elections": {"tour1": "2027-04-18", "tour2": "2027-05-02"},
        "themes": themes, "mesures": mesures,
        "candidats": candidats, "positions": positions,
        "journal": ["Création du jeu de démonstration."],
    }
    sortie = RACINE / "data" / "donnees.json"
    sortie.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Écrit : {sortie}")


if __name__ == "__main__":
    main()
