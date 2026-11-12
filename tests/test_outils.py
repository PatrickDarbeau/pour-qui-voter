"""Tests des outils Python (validateur et comparaison de packs).
Lancer : python -m unittest tests/test_outils.py
"""
import copy
import json
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))
import maj  # noqa: E402
import valider  # noqa: E402

PACK = json.loads((RACINE / "data" / "donnees.json").read_text(encoding="utf-8"))


class TestValider(unittest.TestCase):
    def test_pack_de_demo_valide(self):
        erreurs, _ = valider.valider(copy.deepcopy(PACK))
        self.assertEqual(erreurs, [])

    def test_theme_inconnu(self):
        p = copy.deepcopy(PACK)
        p["mesures"][0]["theme"] = "inexistant"
        erreurs, _ = valider.valider(p)
        self.assertTrue(any("thème inconnu" in e for e in erreurs))

    def test_valeur_invalide(self):
        p = copy.deepcopy(PACK)
        p["positions"][0]["valeur"] = 2
        erreurs, _ = valider.valider(p)
        self.assertTrue(any("valeur invalide" in e for e in erreurs))

    def test_source_obligatoire(self):
        p = copy.deepcopy(PACK)
        p["positions"][0]["valeur"] = 1
        p["positions"][0]["source_url"] = None
        erreurs, _ = valider.valider(p)
        self.assertTrue(any("source obligatoire" in e for e in erreurs))

    def test_doublon(self):
        p = copy.deepcopy(PACK)
        p["candidats"].append(copy.deepcopy(p["candidats"][0]))
        erreurs, _ = valider.valider(p)
        self.assertTrue(any("en double" in e for e in erreurs))

    def test_second_tour(self):
        p = copy.deepcopy(PACK)
        p["second_tour"] = {"actif": True, "qualifies": [p["candidats"][0]["id"]]}
        erreurs, _ = valider.valider(p)
        self.assertTrue(any("Second tour" in e for e in erreurs))
        p["second_tour"]["qualifies"].append(p["candidats"][1]["id"])
        erreurs, _ = valider.valider(p)
        self.assertEqual(erreurs, [])


class TestDiff(unittest.TestCase):
    def test_aucune_difference(self):
        self.assertEqual(maj.diff_packs(PACK, copy.deepcopy(PACK)), [])

    def test_changements_detectes(self):
        n = copy.deepcopy(PACK)
        n["positions"][0]["valeur"] = -n["positions"][0]["valeur"] or 1
        n["mesures"].append({"id": "nouvelle", "theme": n["themes"][0]["id"], "intitule": "Nouvelle mesure"})
        retire = n["candidats"].pop()
        types = [t for t, _ in maj.diff_packs(PACK, n)]
        self.assertIn("position", types)
        self.assertIn("ajout", types)
        self.assertIn("retrait", types)
        self.assertTrue(any(retire["nom"] in txt for _, txt in maj.diff_packs(PACK, n)))

    def test_modif_local_ignore(self):
        n = copy.deepcopy(PACK)
        n["mesures"][0]["modif_local"] = True
        self.assertEqual(maj.diff_packs(PACK, n), [])


class TestCollecte(unittest.TestCase):
    def test_urls_sans_doublon(self):
        c = {"site_officiel": "https://a.fr", "pages_programme": ["https://a.fr", "https://a.fr/prog"], "programme_url": None}
        self.assertEqual(maj.urls_candidat(c), ["https://a.fr", "https://a.fr/prog"])

    def test_nom_fichier(self):
        self.assertTrue(maj.nom_fichier("https://a.fr/programme.pdf", "application/pdf").endswith(".pdf"))
        self.assertTrue(maj.nom_fichier("https://a.fr/sante/", "text/html").endswith(".html"))


if __name__ == "__main__":
    unittest.main()
