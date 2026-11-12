"""Valide un pack de données et génère data/donnees.js (chargeable en file://).

Usage :
    python outils/valider.py [chemin_du_pack.json]     # contrôle seul
    python outils/valider.py --publier                  # contrôle + génère donnees.js
Code de sortie 0 si aucune erreur.
"""
import hashlib
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
VALEURS = {-1, 0, 0.5, 1}
TYPES_SOURCE = {"site_officiel", "programme_pdf", "presse", "interview", "vote"}


def valider(pack):
    erreurs, alertes = [], []
    for cle in ("format", "version", "date", "origine", "themes", "mesures", "candidats", "positions"):
        if cle not in pack:
            erreurs.append(f"Champ obligatoire manquant : {cle}")
    if erreurs:
        return erreurs, alertes

    def uniques(liste, nom):
        ids = [x.get("id") for x in liste]
        doublons = {i for i in ids if ids.count(i) > 1}
        if doublons:
            erreurs.append(f"{nom} : identifiants en double {sorted(doublons)}")
        return set(ids)

    themes = uniques(pack["themes"], "Thèmes")
    mesures = uniques(pack["mesures"], "Mesures")
    candidats = uniques(pack["candidats"], "Candidats")

    for m in pack["mesures"]:
        if m.get("theme") not in themes:
            erreurs.append(f"Mesure {m['id']} : thème inconnu {m.get('theme')}")
        if not m.get("intitule"):
            erreurs.append(f"Mesure {m['id']} : intitulé vide")
        o = m.get("opposee_a")
        if o and o not in mesures:
            erreurs.append(f"Mesure {m['id']} : mesure opposée inconnue {o}")
    for c in pack["candidats"]:
        if not c.get("nom"):
            erreurs.append(f"Candidat {c['id']} : nom vide")

    vues = set()
    for p in pack["positions"]:
        cle = (p.get("candidat"), p.get("mesure"))
        if cle in vues:
            erreurs.append(f"Position en double : {cle}")
        vues.add(cle)
        if p.get("candidat") not in candidats:
            erreurs.append(f"Position {cle} : candidat inconnu")
        if p.get("mesure") not in mesures:
            erreurs.append(f"Position {cle} : mesure inconnue")
        if p.get("valeur") not in VALEURS:
            erreurs.append(f"Position {cle} : valeur invalide {p.get('valeur')}")
        if p.get("valeur") != 0 and not p.get("source_url"):
            erreurs.append(f"Position {cle} : source obligatoire")
        if p.get("source_type") and p["source_type"] not in TYPES_SOURCE:
            alertes.append(f"Position {cle} : type de source inconnu {p['source_type']}")

    # Couverture : chaque candidat devrait se prononcer sur chaque mesure active
    actives = {m["id"] for m in pack["mesures"] if m.get("actif", True)}
    for c in candidats:
        exprimees = {p["mesure"] for p in pack["positions"] if p["candidat"] == c and p["valeur"] != 0}
        taux = len(exprimees & actives) / len(actives) if actives else 0
        if taux < 0.5:
            alertes.append(f"Candidat {c} : couverture faible ({taux:.0%})")
    st = pack.get("second_tour")
    if st and st.get("actif"):
        q = st.get("qualifies") or []
        if len(q) != 2 or len(set(q)) != 2 or not set(q) <= candidats:
            erreurs.append("Second tour actif : il faut exactement deux candidats qualifiés, différents et existants")
    for t in themes:
        n = sum(1 for m in pack["mesures"] if m["theme"] == t)
        if n < 2:
            alertes.append(f"Thème {t} : moins de 2 mesures")
    return erreurs, alertes


sys.stdout.reconfigure(encoding="utf-8") if hasattr(sys.stdout, "reconfigure") else None


def main(argv):
    publier = "--publier" in argv
    args = [a for a in argv if not a.startswith("--")]
    chemin = Path(args[0]) if args else RACINE / "data" / "donnees.json"
    brut = chemin.read_bytes()
    try:
        pack = json.loads(brut.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        print(f"ERREUR : JSON illisible ({e})")
        return 1
    erreurs, alertes = valider(pack)
    for a in alertes:
        print(f"Alerte : {a}")
    for e in erreurs:
        print(f"ERREUR : {e}")
    print(f"{len(pack.get('candidats', []))} candidats, {len(pack.get('mesures', []))} mesures, "
          f"{len(pack.get('positions', []))} positions — SHA-256 {hashlib.sha256(brut).hexdigest()}")
    if erreurs:
        return 1
    if publier:
        js = RACINE / "data" / "donnees.js"
        js.write_text("// Fichier généré par outils/valider.py --publier : ne pas modifier.\n"
                      "window.DONNEES = " + json.dumps(pack, ensure_ascii=False) + ";\n",
                      encoding="utf-8")
        print(f"Généré : {js}")
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
