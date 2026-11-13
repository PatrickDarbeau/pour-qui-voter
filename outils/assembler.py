"""Assemble un pack réel à partir des brouillons du lot 7.

Entrées : data/brouillon/catalogue.json, candidats.json, positions.json
          (générés par outils/catalogue.py, outils/candidats.py, outils/positions.py)
Sortie  : data/brouillon/pack_test.json

Usage :
    python outils/assembler.py               assemble le pack de test avec les 10 candidats
                                             (ceux sans positions sont affichés « non encore saisis », hors classement)
    python outils/assembler.py --installer   l'installe aussi dans data/donnees.json + donnees.js
                                             (le pack de démo reste dans data/demo/)
    python outils/assembler.py --installer --version 2026.11.13-test.2   numéro de version imposé
Le pack est marqué « brouillon » : l'application affiche alors un bandeau « données provisoires ».
"""
import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
BR = RACINE / "data" / "brouillon"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import valider  # noqa: E402


def lire(nom):
    return json.loads((BR / nom).read_text(encoding="utf-8"))


def main():
    # --version AAAA.MM.JJ-test.N : numéro imposé (plusieurs préversions le même jour) ; sinon date du jour + « -test »
    version = sys.argv[sys.argv.index("--version") + 1] if "--version" in sys.argv else date.today().strftime("%Y.%m.%d") + "-test"
    cat, cands, pos = lire("catalogue.json"), lire("candidats.json")["candidats"], lire("positions.json")["positions"]
    avec_positions = {p["candidat"] for p in pos}
    candidats = cands
    attente = [c["nom"] for c in cands if c["id"] not in avec_positions]
    pack = {
        "format": 1,
        "version": version,
        "date": date.today().isoformat(),
        "origine": "officiel",
        "demo": False,
        "brouillon": True,
        "auteur": "Pack de test — données réelles en cours de vérification",
        "licence": "CC BY-SA 4.0",
        "source_projet": "https://github.com/PatrickDarbeau/pour-qui-voter",
        "elections": {"tour1": "2027-04-18", "tour2": "2027-05-02"},
        "themes": cat["themes"],
        "mesures": cat["mesures"],
        "candidats": candidats,
        "positions": pos,
        "journal": [f"Pack de test : {len(cat['mesures'])} mesures, {len(candidats)} candidats "
                    f"dont {len(candidats) - len(attente)} avec positions en brouillon à relire ; "
                    f"positions non encore saisies : {', '.join(attente) or 'aucun'}."],
    }
    erreurs, alertes = valider.valider(pack)
    for a in alertes:
        print("Alerte :", a)
    for e in erreurs:
        print("ERREUR :", e)
    if erreurs:
        sys.exit("Pack non valide.")
    texte = json.dumps(pack, ensure_ascii=False, indent=2)
    (BR / "pack_test.json").write_text(texte, encoding="utf-8")
    print(f"Pack de test : {len(candidats)} candidats, {len(pack['mesures'])} mesures, {len(pack['positions'])} positions → data/brouillon/pack_test.json")
    if "--installer" in sys.argv:
        (RACINE / "data" / "donnees.json").write_text(texte, encoding="utf-8")
        valider.main(["--publier"])
        print("Installé dans data/donnees.json et data/donnees.js (le pack de démo reste dans data/demo/).")


if __name__ == "__main__":
    main()
