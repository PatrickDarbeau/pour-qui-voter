"""Outil de mise à jour des données (CDC §9 bis, lot 5).

Usage :
    python outils/maj.py candidats                 Liste les candidats et l'état de leurs sources
    python outils/maj.py collecter [--candidat ID] Archive les pages officielles et signale les changements
    python outils/maj.py diff ANCIEN.json NOUVEAU.json   Compare deux packs
    python outils/maj.py publier --version AAAA.MM.JJ [--journal "texte"]...
                                                   Valide, date et publie un pack dans dist/

Cet outil est réservé au mainteneur. Il se connecte à internet (étape « collecter ») ;
l'application, elle, ne le fait jamais.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent.parent
DONNEES = RACINE / "data" / "donnees.json"
SOURCES = RACINE / "data" / "sources"
DIST = RACINE / "dist"
# Identifiant générique : aucune donnée personnelle dans les requêtes
USER_AGENT = "Mozilla/5.0 (compatible; PourQuiVoter-collecte/1.0)"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import valider  # noqa: E402


def charger(chemin=DONNEES):
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def enregistrer(pack, chemin=DONNEES):
    Path(chemin).write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")


def nom(c):
    return f"{c.get('prenom') or ''} {c['nom']}".strip()


# ---------------------------------------------------------------- candidats
def cmd_candidats(_args):
    pack = charger()
    print(f"Pack {pack['version']} du {pack['date']} — {len(pack['candidats'])} candidats\n")
    print(f"{'ID':<8} {'Candidat':<24} {'Statut':<10} {'Pages':>5}  {'Dernière collecte':<17} Site officiel")
    for c in pack["candidats"]:
        pages = len(urls_candidat(c))
        print(f"{c['id']:<8} {nom(c)[:24]:<24} {c.get('statut') or '?':<10} {pages:>5}  "
              f"{c.get('derniere_collecte') or 'jamais':<17} {c.get('site_officiel') or '⚠ à renseigner'}")
    manquants = [nom(c) for c in pack["candidats"] if not c.get("site_officiel")]
    if manquants:
        print(f"\n⚠ Site officiel manquant pour : {', '.join(manquants)}")


# ---------------------------------------------------------------- collecter
def urls_candidat(c):
    urls = [c.get("site_officiel"), *(c.get("pages_programme") or []), c.get("programme_url")]
    vues, res = set(), []
    for u in urls:
        if u and u.startswith(("http://", "https://")) and u not in vues:
            vues.add(u)
            res.append(u)
    return res


def nom_fichier(url, type_contenu):
    base = re.sub(r"^https?://", "", url).rstrip("/")
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", base)[:120] or "page"
    ext = ".pdf" if "pdf" in (type_contenu or "") or url.lower().endswith(".pdf") else ".html"
    return base if base.endswith(ext) else base + ext


def telecharger(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), r.headers.get("Content-Type", "")


def derniere_collecte_avant(jour):
    if not SOURCES.exists():
        return None
    dossiers = sorted(d for d in SOURCES.iterdir() if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name) and d.name < jour)
    return dossiers[-1] if dossiers else None


def cmd_collecter(args):
    pack = charger()
    jour = date.today().isoformat()
    cible = SOURCES / jour
    precedente = derniere_collecte_avant(jour)
    candidats = [c for c in pack["candidats"] if not args.candidat or c["id"] == args.candidat]
    if not candidats:
        sys.exit(f"Candidat inconnu : {args.candidat}")
    rapport = {"modifiees": [], "nouvelles": [], "disparues": [], "erreurs": [], "identiques": 0}

    for c in candidats:
        urls = urls_candidat(c)
        if not urls:
            print(f"— {nom(c)} : aucune URL (renseignez site_officiel / pages_programme)")
            continue
        dossier = cible / c["id"]
        dossier.mkdir(parents=True, exist_ok=True)
        index = {}
        print(f"— {nom(c)} : {len(urls)} page(s)")
        for url in urls:
            try:
                contenu, type_contenu = telecharger(url)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                rapport["erreurs"].append(f"{nom(c)} : {url} ({e})")
                print(f"   ✗ {url} — {e}")
                continue
            fichier = nom_fichier(url, type_contenu)
            (dossier / fichier).write_bytes(contenu)
            index[url] = {"fichier": fichier, "sha256": hashlib.sha256(contenu).hexdigest(),
                          "type": type_contenu, "consulte_le": jour, "octets": len(contenu)}
            print(f"   ✓ {url}")
        (dossier / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

        # Comparaison avec la collecte précédente
        ancien_index = {}
        if precedente and (precedente / c["id"] / "index.json").exists():
            ancien_index = json.loads((precedente / c["id"] / "index.json").read_text(encoding="utf-8"))
        for url, info in index.items():
            if url not in ancien_index:
                rapport["nouvelles"].append(f"{nom(c)} : {url}")
            elif ancien_index[url]["sha256"] != info["sha256"]:
                rapport["modifiees"].append(f"{nom(c)} : {url}")
            else:
                rapport["identiques"] += 1
        for url in ancien_index:
            if url not in index:
                rapport["disparues"].append(f"{nom(c)} : {url}")
        c["derniere_collecte"] = jour

    enregistrer(pack)
    (cible / "rapport.json").parent.mkdir(parents=True, exist_ok=True)
    (cible / "rapport.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nCollecte archivée dans {cible}")
    print(f"Comparée à : {precedente.name if precedente else 'aucune collecte précédente'}")
    for cle, titre in (("modifiees", "Pages MODIFIÉES — à relire en priorité"),
                       ("nouvelles", "Nouvelles pages"), ("disparues", "Pages disparues"), ("erreurs", "Erreurs")):
        if rapport[cle]:
            print(f"\n{titre} ({len(rapport[cle])}) :")
            for ligne in rapport[cle]:
                print(f"  • {ligne}")
    print(f"\nPages identiques : {rapport['identiques']}")


# ---------------------------------------------------------------- diff
def diff_packs(ancien, nouveau):
    """Retourne la liste des changements lisibles entre deux packs."""
    lignes = []
    for cle, libelle, nom_item in (("themes", "Thème", lambda x: x.get("nom")),
                                   ("mesures", "Mesure", lambda x: x.get("intitule")),
                                   ("candidats", "Candidat", nom)):
        a = {x["id"]: x for x in ancien.get(cle, [])}
        n = {x["id"]: x for x in nouveau.get(cle, [])}
        for i in n.keys() - a.keys():
            lignes.append(("ajout", f"{libelle} ajouté(e) : {nom_item(n[i])}"))
        for i in a.keys() - n.keys():
            lignes.append(("retrait", f"{libelle} retiré(e) : {nom_item(a[i])}"))
        for i in a.keys() & n.keys():
            champs = sorted(k for k in set(a[i]) | set(n[i]) if k != "modif_local" and a[i].get(k) != n[i].get(k))
            if champs:
                lignes.append(("modif", f"{libelle} modifié(e) : {nom_item(n[i])} ({', '.join(champs)})"))
    cands = {c["id"]: nom(c) for c in [*ancien.get("candidats", []), *nouveau.get("candidats", [])]}
    mes = {m["id"]: m.get("intitule") for m in [*ancien.get("mesures", []), *nouveau.get("mesures", [])]}
    pa = {(p["candidat"], p["mesure"]): p for p in ancien.get("positions", [])}
    pn = {(p["candidat"], p["mesure"]): p for p in nouveau.get("positions", [])}
    for k in sorted(pa.keys() | pn.keys()):
        va, vn = (pa.get(k) or {}).get("valeur"), (pn.get(k) or {}).get("valeur")
        if va != vn:
            lignes.append(("position", f"Position {cands.get(k[0], k[0])} / {mes.get(k[1], k[1])} : {va} → {vn}"))
        elif k in pa and k in pn and pa[k].get("source_url") != pn[k].get("source_url"):
            lignes.append(("source", f"Source changée {cands.get(k[0], k[0])} / {mes.get(k[1], k[1])}"))
    return lignes


def cmd_diff(args):
    lignes = diff_packs(charger(args.ancien), charger(args.nouveau))
    if not lignes:
        print("Aucune différence.")
    for _type, texte in lignes:
        print("•", texte)
    print(f"\n{len(lignes)} changement(s).")


# ---------------------------------------------------------------- publier
def cmd_publier(args):
    if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}(-[a-z0-9]+)?", args.version):
        sys.exit("Version attendue au format AAAA.MM.JJ (ex. 2027.01.15)")
    pack = charger()
    ancien = None
    DIST.mkdir(exist_ok=True)
    precedents = sorted(DIST.glob("donnees-*.json"))
    if precedents:
        ancien = charger(precedents[-1])
        if args.version <= ancien.get("version", ""):
            sys.exit(f"La version {args.version} n'est pas plus récente que {ancien['version']}.")

    pack["version"] = args.version
    pack["date"] = date.today().isoformat()
    pack["origine"] = "officiel"
    pack.setdefault("licence", "CC BY-SA 4.0")
    pack.setdefault("source_projet", "https://github.com/PatrickDarbeau/pour-qui-voter")
    pack["demo"] = bool(args.demo)
    pack.pop("date_modification", None)
    for cle in ("themes", "mesures", "candidats", "positions"):
        for x in pack[cle]:
            x.pop("modif_local", None)
    journal = args.journal or []
    if ancien and not journal:
        journal = [t for _, t in diff_packs(ancien, pack)][:200]
    pack["journal"] = journal or ["Publication."]

    erreurs, alertes = valider.valider(pack)
    for a in alertes:
        print("Alerte :", a)
    if erreurs:
        for e in erreurs:
            print("ERREUR :", e)
        sys.exit("Publication annulée : corrigez les erreurs.")

    enregistrer(pack)
    if valider.main(["--publier"]) != 0:
        sys.exit("Échec de la génération de donnees.js")

    nom_pack = f"donnees-{pack['date']}.json"
    sortie = DIST / nom_pack
    shutil.copyfile(DONNEES, sortie)
    empreinte = hashlib.sha256(sortie.read_bytes()).hexdigest()
    (DIST / (nom_pack + ".sha256")).write_text(f"{empreinte}  {nom_pack}\n", encoding="utf-8")

    print(f"\n✓ Pack publié : {sortie}")
    print(f"  SHA-256 : {empreinte}")
    print("\nLigne pour le registre (notice §4) :")
    print(f"| P? | {pack['version']} | {date.today().strftime('%d/%m/%Y')} | {len(pack['candidats'])} | "
          f"{len(pack['mesures'])} | {len(pack['positions'])} | `{empreinte[:16]}` | "
          f"{'; '.join(pack['journal'][:3])[:80]} |")
    print("\nÉtapes suivantes : git commit, git tag pack-" + pack["date"] + ", publier le pack et son .sha256.")


def main():
    p = argparse.ArgumentParser(description="Mise à jour des données « Pour qui voter ? »")
    sp = p.add_subparsers(dest="commande", required=True)
    sp.add_parser("candidats", help="lister les candidats et leurs sources").set_defaults(f=cmd_candidats)
    c = sp.add_parser("collecter", help="archiver les pages officielles")
    c.add_argument("--candidat")
    c.set_defaults(f=cmd_collecter)
    d = sp.add_parser("diff", help="comparer deux packs")
    d.add_argument("ancien")
    d.add_argument("nouveau")
    d.set_defaults(f=cmd_diff)
    pub = sp.add_parser("publier", help="valider et publier un pack")
    pub.add_argument("--version", required=True)
    pub.add_argument("--journal", action="append", help="entrée du journal (répétable)")
    pub.add_argument("--demo", action="store_true", help="marquer le pack comme démonstration")
    pub.set_defaults(f=cmd_publier)
    args = p.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()
