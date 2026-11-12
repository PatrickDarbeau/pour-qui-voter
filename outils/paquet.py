"""Construit l'archive ZIP distribuée aux utilisateurs (CDC F24, F25).

Usage : python outils/paquet.py
Sortie : dist/pour-qui-voter-<version>.zip (+ empreinte .sha256)

L'archive ne contient que ce qui sert à l'utilisateur : pas d'outils, de tests ni de sources archivées.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
DIST = RACINE / "dist"
DOSSIER = "pour-qui-voter"  # dossier racine dans l'archive

FICHIERS = ["index.html", "data/donnees.js", "data/donnees.json"]
DOSSIERS = ["assets"]

LISEZMOI = """POUR QUI VOTER ? — Présidentielle 2027
=====================================

Comparateur de programmes gratuit, neutre et hors ligne.
Version des données : {version} du {date}

UTILISATION
-----------
1. Décompressez cette archive (clic droit > « Extraire tout… »).
2. Ouvrez le dossier « pour-qui-voter ».
3. Double-cliquez sur « index.html » : l'application s'ouvre dans votre navigateur.

Aucune installation n'est nécessaire. Aucune connexion internet n'est utilisée
(sauf si vous cliquez sur un lien « source » vers le site d'un candidat).
Vos réponses restent sur votre ordinateur.

Si la page ne s'affiche pas correctement par double-clic, lancez « lancer.bat »
(Windows) ou « lancer.sh » (macOS / Linux) : ils démarrent un petit serveur local
et ouvrent l'application. Python 3 doit être installé.

METTRE À JOUR LES DONNÉES
-------------------------
Téléchargez le dernier pack (fichier donnees-AAAA-MM-JJ.json), puis dans
l'application : Édition > Import / export > Importer un pack.

Avant d'importer, vous pouvez vérifier que le fichier n'a pas été modifié :
l'empreinte SHA-256 affichée par l'application doit être identique à celle
publiée à côté du pack.

AVERTISSEMENT
-------------
Outil non officiel et indépendant. C'est une aide à la réflexion, pas une
consigne de vote. Il ne remplace pas la lecture des programmes des candidats.

Premier tour : 18 avril 2027 — Second tour : 2 mai 2027.

Téléchargements et mises à jour : {telechargement}
"""

LANCER_BAT = """@echo off
rem Lance l'application via un petit serveur local (facultatif).
cd /d "%~dp0"
echo Ouverture de « Pour qui voter ? » sur http://localhost:8765 ...
echo Fermez cette fenetre pour arreter.
start "" http://localhost:8765/
python -m http.server 8765 --bind 127.0.0.1 || py -m http.server 8765 --bind 127.0.0.1
pause
"""

LANCER_SH = """#!/bin/sh
# Lance l'application via un petit serveur local (facultatif).
cd "$(dirname "$0")"
echo "Ouverture de « Pour qui voter ? » sur http://localhost:8765 — Ctrl+C pour arrêter."
( sleep 1; (xdg-open http://localhost:8765/ || open http://localhost:8765/) >/dev/null 2>&1 ) &
python3 -m http.server 8765 --bind 127.0.0.1
"""


def main():
    pack = json.loads((RACINE / "data" / "donnees.json").read_text(encoding="utf-8"))
    version = pack.get("version", "dev")
    config = (RACINE / "assets" / "js" / "config.js").read_text(encoding="utf-8")
    telechargement = next((l.split('"')[1] for l in config.splitlines() if "telechargement:" in l), "")

    DIST.mkdir(exist_ok=True)
    sortie = DIST / f"pour-qui-voter-{version}.zip"
    with zipfile.ZipFile(sortie, "w", zipfile.ZIP_DEFLATED) as z:
        for f in FICHIERS:
            z.write(RACINE / f, f"{DOSSIER}/{f}")
        for d in DOSSIERS:
            for f in sorted((RACINE / d).rglob("*")):
                if f.is_file():
                    z.write(f, f"{DOSSIER}/{f.relative_to(RACINE).as_posix()}")
        z.writestr(f"{DOSSIER}/LISEZMOI.txt", LISEZMOI.format(version=version, date=pack.get("date", "?"),
                                                              telechargement=telechargement).replace("\n", "\r\n"))
        z.writestr(f"{DOSSIER}/lancer.bat", LANCER_BAT.replace("\n", "\r\n"))
        info = zipfile.ZipInfo(f"{DOSSIER}/lancer.sh")
        info.external_attr = 0o755 << 16  # exécutable sous macOS / Linux
        z.writestr(info, LANCER_SH)
        noms = z.namelist()

    empreinte = hashlib.sha256(sortie.read_bytes()).hexdigest()
    (DIST / (sortie.name + ".sha256")).write_text(f"{empreinte}  {sortie.name}\n", encoding="utf-8")
    print(f"✓ Archive : {sortie} ({sortie.stat().st_size // 1024} Ko, {len(noms)} fichiers)")
    print(f"  SHA-256 : {empreinte}")
    for n in noms:
        print("   ", n)


if __name__ == "__main__":
    main()
