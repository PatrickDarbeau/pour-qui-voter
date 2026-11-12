"""Assemble les positions des candidats (lot 7, étape 5) et génère les fiches de relecture.

Chaque candidat a son fichier source : outils/positions_<id>.py (dictionnaire P).
Usage : python outils/positions.py
Génère : data/brouillon/positions.json et docs/positions_<id>.md (relecture).
"""
import importlib
import json
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalogue  # noqa: E402

DATE_SOURCE = "2026-11-12"
LIBELLE = {1: "Soutient", 0.5: "Soutient en partie", 0: "Ne se prononce pas", -1: "S'oppose"}


def main():
    cands = json.loads((RACINE / "data" / "brouillon" / "candidats.json").read_text(encoding="utf-8"))["candidats"]
    mesures = {m[0]: m for m in catalogue.M}
    toutes, bilan = [], []
    for c in cands:
        try:
            mod = importlib.import_module(f"positions_{c['id']}")
        except ModuleNotFoundError:
            continue
        P = mod.P
        inconnues = set(P) - set(mesures)
        assert not inconnues, f"{c['id']} : mesures inconnues {inconnues}"
        for mid, (v, src, cit, conf) in P.items():
            assert v in (-1, 0, 0.5, 1), (c["id"], mid, v)
            toutes.append({"candidat": c["id"], "mesure": mid, "valeur": v, "source_url": src,
                           "source_type": "site_officiel", "source_date": DATE_SOURCE,
                           "citation": cit, "a_confirmer": conf})
        n = Counter(v for v, *_ in P.values())
        bilan.append((c, len(P), n, sum(1 for *_, conf in P.values() if conf)))

        # Fiche de relecture par candidat
        L = [f"# Positions de {c['prenom']} {c['nom']} — brouillon à relire", "",
             f"*Générée par `python outils/positions.py` depuis `outils/positions_{c['id']}.py`. "
             f"Sources consultées le {DATE_SOURCE}.*", "",
             f"**{len(P)} positions renseignées sur {len(mesures)} mesures** "
             f"({n[1]} soutient, {n[0.5]} en partie, {n[-1]} s'oppose) ; "
             f"les {len(mesures) - len(P)} autres valent « ne se prononce pas » (aucun passage trouvé). "
             f"{bilan[-1][3]} position(s) marquée(s) « à confirmer » ⚠.", ""]
        for t, nom_t, ico, _ in catalogue.THEMES:
            lignes = [m for m in catalogue.M if m[1] == t]
            L += [f"## {ico} {nom_t}", "", "| Mesure | Position | Extrait du programme |", "|---|---|---|"]
            for m in lignes:
                if m[0] in P:
                    v, src, cit, conf = P[m[0]]
                    L.append(f"| {m[2]} | **{LIBELLE[v]}**{' ⚠' if conf else ''} | « {cit} » ([source]({src})) |")
                else:
                    L.append(f"| {m[2]} | · | — |")
            L.append("")
        (RACINE / "docs" / f"positions_{c['id']}.md").write_text("\n".join(L), encoding="utf-8")

    sortie = RACINE / "data" / "brouillon" / "positions.json"
    sortie.write_text(json.dumps({"statut": "brouillon à relire", "positions": toutes}, ensure_ascii=False, indent=2), encoding="utf-8")
    for c, nb, n, conf in bilan:
        print(f"{c['prenom']} {c['nom']} : {nb} positions ({n[1]} +, {n[0.5]} ½, {n[-1]} −), {conf} à confirmer")
    print(f"Écrit : {sortie}")


if __name__ == "__main__":
    main()
