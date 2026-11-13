"""Portraits des candidats (lot 7) — Wikimedia Commons, licences libres.

Usage : python outils/portraits.py
Télécharge chaque portrait (vignette Commons de 960 px), le recadre au format uniforme 3:4
(cadrage haut : tête et épaules) et l'enregistre en 300 × 400 px dans assets/img/candidats/<id>.jpg.

Le crédit (auteur, licence, page du fichier) est repris dans la fiche par outils/candidats.py
et affiché sous la photo dans l'application. Fichiers choisis le 13/11/2026 : portrait de face ou de trois quarts,
le plus récent disponible sous licence libre.
"""
import io
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = Path(__file__).resolve().parent.parent
DOSSIER = RACINE / "assets" / "img" / "candidats"
TAILLE = (300, 400)  # format uniforme 3:4
C = "https://commons.wikimedia.org/wiki/File:"
CC_BY4, CC_BYSA4, CC_BYSA3 = ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/"), \
    ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0/"), ("CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0/")
CC0 = ("CC0 (domaine public)", "https://creativecommons.org/publicdomain/zero/1.0/")


def _p(fichier, vignette, auteur, licence, haut=0.0):
    return {"page": C + fichier, "vignette": vignette, "auteur": auteur,
            "licence": licence[0], "licence_url": licence[1], "haut": haut}


T = "https://upload.wikimedia.org/wikipedia/commons/thumb/"
U = "https://upload.wikimedia.org/wikipedia/commons/"
PORTRAITS = {
    "attal": _p("Gabriel_Attal_2025_(close_crop).jpg",
                T + "c/c4/Gabriel_Attal_2025_%28close_crop%29.jpg/960px-Gabriel_Attal_2025_%28close_crop%29.jpg",
                "Ismail Aissoub (2025)", CC_BY4),
    "glucksmann": _p("1720448398743_20240708_GLUCKSMANN_Raphael_FR_006.jpg",
                     T + "1/1f/1720448398743_20240708_GLUCKSMANN_Raphael_FR_006.jpg/960px-1720448398743_20240708_GLUCKSMANN_Raphael_FR_006.jpg",
                     "© Union européenne 2024 – Source : Parlement européen",
                     ("Réutilisation autorisée avec mention de la source (Parlement européen)", "https://www.europarl.europa.eu/legal-notice/")),
    "lepen": _p("Marine_Le_Pen_2025_(cropped).jpg",
                T + "8/81/Marine_Le_Pen_2025_%28cropped%29.jpg/960px-Marine_Le_Pen_2025_%28cropped%29.jpg",
                "Vox España (2025)", CC0),
    "lisnard": _p("David_Lisnard_en_2026.jpg",
                  T + "c/ce/David_Lisnard_en_2026.jpg/960px-David_Lisnard_en_2026.jpg",
                  "Grégor Sauvagère (2026)", CC_BYSA4),
    "melenchon": _p("Jean_Luc_Mélenchon_en_mai_2026-_55261894422_(cropped).jpg",
                    U + "3/3e/Jean_Luc_M%C3%A9lenchon_en_mai_2026-_55261894422_%28cropped%29.jpg",
                    "jlm2017.fr (2026)", CC_BY4),
    "philippe": _p("Edouard_Philippe_3x4_crop.jpg", U + "a/a3/Edouard_Philippe_3x4_crop.jpg", "Wasasaq8 (2024)", CC0),
    "retailleau": _p("Bruno_Retailleau_-_Ministre_de_l'Intérieur_français_(cropped).jpg",
                     T + "6/61/Bruno_Retailleau_-_Ministre_de_l%27Int%C3%A9rieur_fran%C3%A7ais_%28cropped%29.jpg/"
                         "960px-Bruno_Retailleau_-_Ministre_de_l%27Int%C3%A9rieur_fran%C3%A7ais_%28cropped%29.jpg",
                     "Anthonymontardyfr (2025)", CC_BY4),
    "riner": _p("Teddy_Riner_Cannes_2016.jpg", U + "7/7f/Teddy_Riner_Cannes_2016.jpg", "Georges Biard (2016)", CC_BYSA3),
    "roussel": _p("Roussel_Fabien_1.jpg", U + "a/ae/Roussel_Fabien_1.jpg", "Zouhair Nakara (2018)", CC_BYSA4),
    "zemmour": _p("Portrait_d'Éric_Zemmour,_avril_2022.jpg",
                  T + "8/8c/Portrait_d%27%C3%89ric_Zemmour%2C_avril_2022.jpg/960px-Portrait_d%27%C3%89ric_Zemmour%2C_avril_2022.jpg",
                  "Anh De France (2022)", CC0),
}


def recadrer(img, haut=0.0):
    """Recadre au format 3:4 : largeur conservée si l'image est plus haute que 3:4 (cadrage depuis le haut)."""
    l, h = img.size
    if h * 3 > l * 4:                       # trop haute : on coupe en bas
        nh = l * 4 // 3
        y = int((h - nh) * haut)
        img = img.crop((0, y, l, y + nh))
    else:                                   # trop large : on coupe sur les côtés
        nl = h * 3 // 4
        x = (l - nl) // 2
        img = img.crop((x, 0, x + nl, h))
    return img.resize(TAILLE)


def main():
    from PIL import Image
    DOSSIER.mkdir(parents=True, exist_ok=True)
    forcer = "--forcer" in sys.argv
    for cid, p in PORTRAITS.items():
        sortie = DOSSIER / f"{cid}.jpg"
        if sortie.exists() and not forcer:
            print(f"{cid} : déjà présent (--forcer pour retélécharger)")
            continue
        req = urllib.request.Request(p["vignette"], headers={"User-Agent": "pour-qui-voter-outils/1.0"})
        for essai in range(5):              # Commons limite le débit (HTTP 429) : on patiente puis on réessaie
            try:
                donnees = urllib.request.urlopen(req, timeout=60).read()
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or essai == 4:
                    raise
                time.sleep(15 * (essai + 1))
        img = Image.open(io.BytesIO(donnees)).convert("RGB")
        recadrer(img, p["haut"]).save(sortie, "JPEG", quality=85, optimize=True, progressive=True)
        print(f"{cid} : {sortie.relative_to(RACINE)} ({sortie.stat().st_size // 1024} Ko) — {p['auteur']}, {p['licence']}")
        time.sleep(3)


if __name__ == "__main__":
    main()
