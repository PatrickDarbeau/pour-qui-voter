"""Questionnaire de réponse destiné aux candidats (accompagne docs/candidats/note_aux_candidats.md).

Usage : python outils/questionnaire.py
Sortie :
    docs/candidats/questionnaire_mesures.csv   à remplir (une ligne par mesure, séparateur « ; », UTF-8 avec BOM pour Excel)
    docs/candidats/mesures_par_theme.md        même liste, lisible et imprimable

Les mesures sont lues dans data/donnees.json (mesures actives uniquement) : relancer l'outil après chaque
révision du catalogue, pour que le questionnaire corresponde toujours aux mesures du comparateur.
"""
import csv
import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "docs" / "candidats"
REPONSES = "soutient / soutient en partie / ne se prononce pas / s'oppose"


def main():
    pack = json.loads((RACINE / "data" / "donnees.json").read_text(encoding="utf-8"))
    themes = sorted(pack["themes"], key=lambda t: t.get("ordre", 0))
    mesures = [m for m in pack["mesures"] if m.get("actif", True)]
    intitule = {m["id"]: m["intitule"] for m in mesures}
    SORTIE.mkdir(parents=True, exist_ok=True)

    with (SORTIE / "questionnaire_mesures.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id_mesure", "theme", "intitule", "description", "mesure_opposee",
                    f"position ({REPONSES})", "extrait_du_programme", "lien_ou_page_du_document", "commentaire"])
        for t in themes:
            for m in (x for x in mesures if x["theme"] == t["id"]):
                w.writerow([m["id"], t["nom"], m["intitule"], m.get("description", ""),
                            m.get("opposee_a") or "", "", "", "", ""])

    L = ["# Mesures retenues dans le comparateur", "",
         f"*Liste générée par `python outils/questionnaire.py` le {date.today().strftime('%d/%m/%Y')} "
         f"à partir des données version {pack['version']} : {len(mesures)} mesures, {len(themes)} thèmes.*", "",
         "Version à remplir : [questionnaire_mesures.csv](questionnaire_mesures.csv). "
         f"Pour chaque mesure, indiquer : **{REPONSES}**, avec un extrait du programme et sa source.", ""]
    for t in themes:
        ms = [x for x in mesures if x["theme"] == t["id"]]
        L += [f"## {t.get('icone', '')} {t['nom']} ({len(ms)} mesures)".replace("##  ", "## "), "",
              "| Réf. | Mesure | Précision |", "|---|---|---|"]
        for m in ms:
            prec = m.get("description", "")
            if m.get("opposee_a") in intitule:
                prec += f" *(mesure opposée : {m['opposee_a']})*"
            L.append(f"| {m['id']} | {m['intitule']} | {prec.strip()} |")
        L.append("")
    (SORTIE / "mesures_par_theme.md").write_text("\n".join(L), encoding="utf-8")
    print(f"{len(mesures)} mesures, {len(themes)} thèmes → {SORTIE / 'questionnaire_mesures.csv'} et mesures_par_theme.md")


if __name__ == "__main__":
    main()
