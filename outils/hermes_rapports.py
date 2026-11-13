"""Rapatrie les rapports d'Hermès enregistrés sur la VM (rattrapage après une déconnexion).

Usage : python outils/hermes_rapports.py [--etat]
    Copie dans docs/hermes/rapports/ tout livrable du dossier de travail de la VM qui manque en local ou qui a changé
    (comparaison par empreinte SHA-256), puis affiche l'état de la file GLM et la fin du journal de la veille hebdomadaire.
    --etat : affiche seulement ce qui serait rapatrié, sans rien copier.

Les livrables restent toujours sur la VM (sauvegarde) : si Hermès est injoignable, rien n'est perdu ;
relancer simplement l'outil plus tard. À lancer au début de chaque session de travail sur les positions.
Prérequis : alias SSH « hermes » (clé installée).
"""
import subprocess
import sys
import hashlib
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
LOCAL = RACINE / "docs" / "hermes" / "rapports"
DISTANT = "/home/patrick/workspace/Projets/pour-qui-voter"
MOTIFS = ["*_positions-*.md", "*_veille-*.md", "*_sources-*.md"]


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
    except (ConnectionError, subprocess.TimeoutExpired) as e:
        print(f"(état de la file indisponible : {e})")


if __name__ == "__main__":
    main()
