"""Rapatrie les rapports d'Hermès enregistrés sur la VM (rattrapage après une déconnexion).

Usage : python outils/hermes_rapports.py [--etat]
    Copie dans docs/hermes/rapports/ tout livrable du dossier de travail de la VM qui manque en local ou qui a changé
    (comparaison par empreinte SHA-256), puis affiche l'état de la file GLM et la fin du journal de la veille hebdomadaire.
    --etat : affiche seulement ce qui serait rapatrié, sans rien copier.
    Met aussi à jour le journal de suivi docs/hermes/journal_suivi.md : chaque tâche de veille (semaine, candidat, mode,
    tâche, statut chez Hermès, livrable, rapatriement, suite donnée). La colonne « Suite donnée » vient de
    docs/hermes/rapports_traites.txt, tenu à la main (« livrable | date | suite donnée »).

Les livrables restent toujours sur la VM (sauvegarde) : si Hermès est injoignable, rien n'est perdu ;
relancer simplement l'outil plus tard. À lancer au début de chaque session de travail sur les positions.
Prérequis : alias SSH « hermes » (clé installée).
"""
import hashlib
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
LOCAL = RACINE / "docs" / "hermes" / "rapports"
DISTANT = "/home/patrick/workspace/Projets/pour-qui-voter"
MOTIFS = ["*_positions-*.md", "*_veille-*.md", "*_sources-*.md"]
H = RACINE / "docs" / "hermes"
# Lecture groupée de l'état de la veille sur la VM (états par semaine, échéances, file GLM, livrables)
ETAT_VM = r"""python3 - <<'PY'
import json, glob, os
d = {"semaines": {}, "echeances": [], "fait": [], "livrables": {}}
for f in sorted(glob.glob(os.path.expanduser("~/.hermes/state/pqv_hebdo/*.txt"))):
    d["semaines"][os.path.basename(f)[:-4]] = open(f, encoding="utf-8").read().splitlines()
for n, k in (("pqv_echeances.txt", "echeances"), ("pqv_echeances.fait", "fait")):
    f = os.path.expanduser("~/.hermes/state/" + n)
    if os.path.exists(f): d[k] = open(f, encoding="utf-8").read().splitlines()
q = json.load(open(os.path.expanduser("~/.hermes/glm_file.json"), encoding="utf-8"))
d["file"] = [x["id"] for x in q.get("file", [])]
d["en_cours"] = (q.get("en_cours") or {}).get("id")
d["historique"] = {x["id"]: [x.get("statut"), x.get("fin_a")] for x in q.get("historique", [])}
for f in glob.glob("/home/patrick/workspace/Projets/pour-qui-voter/*_*-*.md"):
    s = os.stat(f); d["livrables"][os.path.basename(f)] = [s.st_size, s.st_mtime]
print(json.dumps(d))
PY"""


def ssh(commande, timeout=30):
    r = subprocess.run(["ssh", "-o", "ConnectTimeout=10", "-o", "BatchMode=yes", "hermes", commande],
                       capture_output=True, text=True, encoding="utf-8", timeout=timeout)
    if r.returncode != 0:
        raise ConnectionError(r.stderr.strip() or f"code {r.returncode}")
    return r.stdout


def main():
    essai = "--etat" in sys.argv
    try:
        sortie = ssh(f"cd {DISTANT} && sha256sum {' '.join(MOTIFS)} 2>/dev/null || true")
    except (ConnectionError, subprocess.TimeoutExpired) as e:
        print(f"Hermès injoignable ({e}). Rien n'est perdu : les livrables restent sur la VM. Relancer plus tard.")
        sys.exit(2)
    distants = dict(reversed(l.split(None, 1)) for l in sortie.splitlines() if l.strip())
    LOCAL.mkdir(parents=True, exist_ok=True)
    a_copier = []
    for nom, empreinte in sorted(distants.items()):
        nom = nom.lstrip("*")
        f = LOCAL / nom
        if not f.exists():
            a_copier.append((nom, "nouveau"))
        elif hashlib.sha256(f.read_bytes()).hexdigest() != empreinte:
            a_copier.append((nom, "modifié"))
    print(f"{len(distants)} livrable(s) sur la VM, {len(a_copier)} à rapatrier.")
    for nom, motif in a_copier:
        if essai:
            print(f"  [état] {nom} ({motif})")
            continue
        r = subprocess.run(["scp", "-q", "-o", "ConnectTimeout=10", f"hermes:{DISTANT}/{nom}", str(LOCAL / nom)])
        print(f"  {'✓' if r.returncode == 0 else '✗ échec :'} {nom} ({motif})")
    try:
        print("\nFile GLM :")
        print(ssh("export PATH=$HOME/.local/bin:$PATH; ~/.hermes/scripts/glm_file.py liste 2>&1 | grep -v 'Flux arrêtés'").rstrip())
        print("\nVeille hebdomadaire (fin du journal) :")
        print(ssh("tail -n 12 ~/.hermes/logs/pqv_hebdo.log 2>/dev/null || echo '(aucune exécution pour l instant)'").rstrip())
        journal_suivi()
    except (ConnectionError, subprocess.TimeoutExpired) as e:
        print(f"(état de la file ou journal de suivi indisponible : {e})")


def lire_liste(nom):
    f = H / nom
    if not f.exists():
        return []
    return [l.split()[0] for l in f.read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#")]


def journal_suivi():
    """Régénère docs/hermes/journal_suivi.md à partir de l'état de la VM et des fichiers locaux."""
    d = json.loads(ssh(ETAT_VM, timeout=60))
    hebdo, rotation = set(lire_liste("candidats_hebdo.txt")), set(lire_liste("candidats_rotation.txt"))
    traites = {}
    f = H / "rapports_traites.txt"
    if f.exists():
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip() and not l.startswith("#") and l.count("|") >= 2:
                nom, date_t, suite = (x.strip() for x in l.split("|", 2))
                traites[nom] = f"{date_t} : {suite}"

    def statut(job, livrable):
        if livrable in d["livrables"]:
            t, k = d["livrables"][livrable]
            return f"✅ livré le {datetime.fromtimestamp(k).strftime('%d/%m %H:%M')} ({t // 1024} Ko)"
        if job == d["en_cours"]:
            return "⏳ en cours"
        if job in d["file"]:
            n = d['file'].index(job) + 1
            return f"🕒 en file ({n}{'ʳᵉ' if n == 1 else 'ᵉ'})"
        if job in d["historique"]:
            s, fin = d["historique"][job]
            return f"⚠️ terminé ({s}) le {fin[8:10]}/{fin[5:7]} {fin[11:16]}, **sans livrable**" if fin else f"⚠️ {s}, sans livrable"
        return "❓ inconnu de la file"

    def ligne(semaine, cand, mode, job, livrable):
        rap = "oui" if (LOCAL / livrable).exists() else "non"
        return f"| {semaine} | {cand} | {mode} | `{job}` | {statut(job, livrable)} | `{livrable}` | {rap} | {traites.get(livrable, '—')} |"

    L = ["# Journal de suivi de la veille d'Hermès", "",
         f"*Généré par `python outils/hermes_rapports.py` le {datetime.now().strftime('%d/%m/%Y à %H:%M')}. "
         "Ne pas modifier à la main : la colonne « Suite donnée » se tient dans `rapports_traites.txt`.*", "",
         "Statuts : ✅ livré sur la VM · ⏳ en cours · 🕒 en file d'attente GLM · ⚠️ terminé sans livrable (à relancer) · "
         "❓ tâche absente de la file. « Rapatrié » : copie présente dans `docs/hermes/rapports/`.", "",
         "## Veille hebdomadaire (samedi 07:00, avec rattrapage)", "",
         "| Semaine du | Candidat | Mode | Tâche | Statut chez Hermès | Livrable | Rapatrié | Suite donnée |",
         "|---|---|---|---|---|---|---|---|"]
    vus = set()
    for semaine in sorted(d["semaines"], reverse=True):
        for l in d["semaines"][semaine]:
            x = l.split()
            if len(x) < 3 or x[1] == "-" or (x[0], x[1]) in vus:
                continue
            vus.add((x[0], x[1]))
            mode = "complément" if x[0] in rotation else "relevé"
            L.append(ligne(semaine, x[0], mode, x[1], x[2]))
    L += ["", "## Veilles ponctuelles", "", "| Échéance | Tâche | Libellé | Mise en file | Livrable(s) | Suite donnée |", "|---|---|---|---|---|---|"]
    fait = {l.split()[1]: l.split()[0] for l in d["fait"] if len(l.split()) > 1}
    for l in d["echeances"]:
        if not l.strip() or l.startswith("#"):
            continue
        quand, job, libelle = (l.split(None, 2) + [""])[:3]
        livs = [n for n in d["livrables"] if n.startswith(quand[:10] + "_veille")]
        mise = fait.get(job, "pas encore")
        attente = "⏸ en attente de l'échéance" if job not in fait else statut(job, "-")
        L.append(f"| {quand.replace('T', ' ')} | `{job}` | {libelle} | {mise.replace('T', ' ')} | "
                 f"{', '.join(f'`{n}`' for n in livs) or attente} | {'; '.join(traites.get(n, '—') for n in livs) or '—'} |")
    couverts = {x.split()[2] for s in d["semaines"].values() for x in s if len(x.split()) > 2}
    autres = sorted(n for n in d["livrables"] if n not in couverts and "_veille-" not in n and not n.startswith("consigne"))
    if autres:
        L += ["", "## Autres rapports (recherches ponctuelles)", "", "| Livrable | Rapatrié | Suite donnée |", "|---|---|---|"]
        L += [f"| `{n}` | {'oui' if (LOCAL / n).exists() else 'non'} | {traites.get(n, '—')} |" for n in autres]
    sortie = H / "journal_suivi.md"
    sortie.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\nJournal de suivi mis à jour : {sortie.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
