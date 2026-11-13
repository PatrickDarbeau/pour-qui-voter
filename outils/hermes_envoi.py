"""Prépare et envoie sur la VM d'Hermès les fichiers de la veille hebdomadaire.

Usage : python outils/hermes_envoi.py [--local]
    1. Génère docs/hermes/positions_actuelles.md : positions déjà saisies dans le comparateur, par candidat
       (référence, valeur, « à confirmer », source), pour le mode « complément » de la consigne.
    2. Copie sur la VM : consigne hebdomadaire, listes des candidats, liste des mesures, positions actuelles,
       et les scripts pqv_hebdo.sh et pqv_echeances.sh.
    --local : génère seulement le fichier, sans rien envoyer.

À relancer après chaque saisie de positions, chaque révision du catalogue et toute modification de la veille
(demandée par l'éditeur). Si Hermès est injoignable, relancer plus tard : la VM garde les anciens fichiers.
"""
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
H = RACINE / "docs" / "hermes"
DISTANT = "/home/patrick/workspace/Projets/pour-qui-voter"
VALEUR = {1: "soutient", 0.5: "en partie", -1: "s'oppose"}


def positions_actuelles():
    pack = json.loads((RACINE / "data" / "donnees.json").read_text(encoding="utf-8"))
    mes = {m["id"]: m["intitule"] for m in pack["mesures"]}
    L = ["# Positions déjà saisies dans le comparateur", "",
         f"*Généré par `python outils/hermes_envoi.py` le {date.today().strftime('%d/%m/%Y')} (données {pack['version']}). "
         "Sert au mode « complément » : ne pas recopier ces positions, chercher ce qui manque.*", ""]
    for c in sorted(pack["candidats"], key=lambda x: x["nom"]):
        ps = sorted((p for p in pack["positions"] if p["candidat"] == c["id"] and p["valeur"] != 0), key=lambda p: p["mesure"])
        L += [f"## {c['id']} — {c['prenom']} {c['nom']} ({len(ps)} positions sur {len(mes)} mesures)", ""]
        if not ps:
            L += ["Aucune position saisie.", ""]
            continue
        L += ["| Réf. | Mesure | Position | À confirmer | Source |", "|---|---|---|---|---|"]
        for p in ps:
            L.append(f"| {p['mesure']} | {mes.get(p['mesure'], '?')} | {VALEUR.get(p['valeur'], p['valeur'])} "
                     f"| {'oui' if p.get('a_confirmer') else ''} | {p.get('source_url') or ''} |")
        L.append("")
    f = H / "positions_actuelles.md"
    f.write_text("\n".join(L), encoding="utf-8")
    print(f"Généré : {f.relative_to(RACINE)}")
    return f


def main():
    pa = positions_actuelles()
    if "--local" in sys.argv:
        return
    vers_dossier = [H / "consigne_positions_hebdo.md", H / "candidats_hebdo.txt", H / "candidats_rotation.txt",
                    RACINE / "docs" / "candidats" / "mesures_par_theme.md", pa]
    scripts = [H / "pqv_hebdo.sh", H / "pqv_echeances.sh"]
    try:
        for liste, cible in ((vers_dossier, DISTANT + "/"), (scripts, ".hermes/scripts/")):
            subprocess.run(["scp", "-q", "-o", "ConnectTimeout=10", *map(str, liste), "hermes:" + cible], check=True, timeout=120)
        # fins de ligne Unix et droits d'exécution sur la VM
        subprocess.run(["ssh", "-o", "ConnectTimeout=10", "hermes",
                        f"sed -i 's/\\r$//' {DISTANT}/candidats_*.txt ~/.hermes/scripts/pqv_*.sh && chmod +x ~/.hermes/scripts/pqv_*.sh "
                        "&& bash -n ~/.hermes/scripts/pqv_hebdo.sh && bash -n ~/.hermes/scripts/pqv_echeances.sh"], check=True, timeout=60)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"Envoi impossible ({e}) : Hermès injoignable ? La VM garde les fichiers précédents ; relancer plus tard.")
        sys.exit(2)
    print(f"Envoyé sur la VM : {len(vers_dossier)} fichiers de travail et {len(scripts)} scripts.")


if __name__ == "__main__":
    main()
