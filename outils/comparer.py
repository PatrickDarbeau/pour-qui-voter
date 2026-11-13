"""Analyse comparative des programmes à partir des positions saisies (lot 7).

Usage : python outils/comparer.py [suffixe]   (ex. « 2 » → AAAA-MM-JJ_analyse_comparative_2.md)
Sortie : docs/enseignements/AAAA-MM-JJ_analyse_comparative.md (chiffres bruts, sans commentaire politique)

Contenu : couverture par candidat et par thème, proximité entre candidats, mesures clivantes,
mesures consensuelles, mesures orphelines, qualité des sources (positions « à confirmer »).
À commenter de façon neutre dans la note d'enseignements correspondante.
"""
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from itertools import combinations
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalogue  # noqa: E402


def main():
    br = RACINE / "data" / "brouillon"
    cands = json.loads((br / "candidats.json").read_text(encoding="utf-8"))["candidats"]
    pos = json.loads((br / "positions.json").read_text(encoding="utf-8"))["positions"]
    nom = {c["id"]: f"{c['prenom']} {c['nom']}" for c in cands}
    P = defaultdict(dict)  # candidat -> mesure -> valeur
    conf = Counter()
    for p in pos:
        if p["valeur"] != 0:
            P[p["candidat"]][p["mesure"]] = p["valeur"]
        if p.get("a_confirmer"):
            conf[p["candidat"]] += 1
    saisis = sorted(P, key=lambda c: nom[c].split()[-1])
    attente = [c["id"] for c in cands if c["id"] not in P]
    mes = {m[0]: m for m in catalogue.M}
    themes = catalogue.THEMES
    n_mes = len(mes)
    L = [f"# Analyse comparative des programmes — {date.today().strftime('%d/%m/%Y')}", "",
         "*Générée par `python outils/comparer.py` à partir des positions en brouillon. Chiffres bruts, sans jugement ; "
         "le commentaire figure dans la note d'enseignements du même jour.*", "",
         f"**Candidats analysés** : {len(saisis)} ({', '.join(nom[c] for c in saisis)}). "
         f"**En attente** : {len(attente)} ({', '.join(nom[c] for c in attente) or '—'}).", ""]

    # 1. Couverture
    L += ["## 1. Couverture des programmes", "",
          "| Candidat | Positions | Couverture | Soutient | En partie | S'oppose | À confirmer |", "|---|---:|---:|---:|---:|---:|---:|"]
    for c in saisis:
        v = Counter(P[c].values())
        L.append(f"| {nom[c]} | {len(P[c])} | {len(P[c]) / n_mes:.0%} | {v[1]} | {v[0.5]} | {v[-1]} | {conf[c]} |")
    L += ["", "### Couverture par thème (nombre de mesures sur lesquelles le candidat se prononce)", "",
          "| Thème | Mesures | " + " | ".join(nom[c].split()[-1] for c in saisis) + " |",
          "|---|---:|" + "---:|" * len(saisis)]
    for t, n, i, _ in themes:
        ids = [m for m in mes if mes[m][1] == t]
        L.append(f"| {i} {n} | {len(ids)} | " + " | ".join(str(sum(1 for m in ids if m in P[c])) for c in saisis) + " |")

    # 2. Proximité
    L += ["", "## 2. Proximité entre candidats", "",
          "Taux d'accord sur les mesures où **les deux** candidats se prononcent (même sens = accord). "
          "Entre parenthèses : nombre de mesures communes. Un faible nombre de mesures communes rend le taux peu significatif.", "",
          "| | " + " | ".join(nom[c].split()[-1] for c in saisis) + " |", "|---|" + "---|" * len(saisis)]
    for a in saisis:
        ligne = []
        for b in saisis:
            if a == b:
                ligne.append("—")
                continue
            com = [m for m in P[a] if m in P[b]]
            acc = sum(1 for m in com if (P[a][m] > 0) == (P[b][m] > 0))
            ligne.append(f"{acc / len(com):.0%} ({len(com)})" if com else "· (0)")
        L.append(f"| **{nom[a].split()[-1]}** | " + " | ".join(ligne) + " |")

    # 3. Mesures clivantes / consensuelles / orphelines
    expr = {m: {c: P[c][m] for c in saisis if m in P[c]} for m in mes}
    clivantes = [(m, e) for m, e in expr.items() if any(v > 0 for v in e.values()) and any(v < 0 for v in e.values())]
    consens = [(m, e) for m, e in expr.items() if len(e) >= 3 and (all(v > 0 for v in e.values()) or all(v < 0 for v in e.values()))]
    orphelines = [m for m, e in expr.items() if not e]
    fmt = lambda e: ", ".join(f"{nom[c].split()[-1]} {'+' if v > 0 else '−'}" for c, v in e.items())
    L += ["", f"## 3. Mesures clivantes ({len(clivantes)})", "", "Au moins un candidat pour et un candidat contre.", "",
          "| Thème | Mesure | Positions |", "|---|---|---|"]
    for m, e in sorted(clivantes, key=lambda x: (-len(x[1]), x[0])):
        L.append(f"| {mes[m][1]} | {mes[m][2]} | {fmt(e)} |")
    L += ["", f"## 4. Mesures consensuelles ({len(consens)})", "", "Au moins trois candidats, tous dans le même sens.", "",
          "| Thème | Mesure | Positions |", "|---|---|---|"]
    for m, e in sorted(consens, key=lambda x: (-len(x[1]), x[0])):
        L.append(f"| {mes[m][1]} | {mes[m][2]} | {fmt(e)} |")
    L += ["", f"## 5. Mesures orphelines ({len(orphelines)} sur {n_mes})", "",
          "Aucun candidat analysé ne se prononce : elles ne départagent personne (à revoir dans le catalogue).", ""]
    par_t = defaultdict(list)
    for m in orphelines:
        par_t[mes[m][1]].append(mes[m][2])
    for t, n, i, _ in themes:
        if par_t[t]:
            L.append(f"- **{i} {n}** ({len(par_t[t])}) : " + " ; ".join(par_t[t]))
    sortie = RACINE / "docs" / "enseignements" / f"{date.today().isoformat()}_analyse_comparative{'_' + sys.argv[1] if len(sys.argv) > 1 else ''}.md"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Clivantes {len(clivantes)}, consensuelles {len(consens)}, orphelines {len(orphelines)} → {sortie}")


if __name__ == "__main__":
    main()
