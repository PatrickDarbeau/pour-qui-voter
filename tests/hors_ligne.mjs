// Test d'acceptation (CDC §11) : l'application extraite du ZIP fonctionne en file:// (double-clic),
// sans aucune requête réseau, y compris le parcours complet, l'édition locale et le mode second tour.
// Prérequis : python outils/paquet.py (crée l'archive dans dist/).
// Usage : node tests/hors_ligne.mjs
import { spawn, execFileSync } from "node:child_process";
import { mkdtempSync, readdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import assert from "node:assert";

const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe";
const PORT = 9334;
const pause = (ms) => new Promise((r) => setTimeout(r, ms));

// 1. Extraction de la dernière archive
const zip = readdirSync("dist").filter((f) => f.endsWith(".zip")).sort().pop();
assert.ok(zip, "Aucune archive dans dist/ : lancez python outils/paquet.py");
const dossier = mkdtempSync(join(tmpdir(), "pqv-zip-"));
execFileSync("python", ["-c", `import zipfile,sys; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])`, join("dist", zip), dossier]);
const URL_APP = pathToFileURL(join(dossier, "pour-qui-voter", "index.html")).href;
console.log("Archive :", zip, "\nOuverte en :", URL_APP);

// 2. Chrome sans interface
const profil = mkdtempSync(join(tmpdir(), "pqv-chrome-"));
const chrome = spawn(CHROME, ["--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${profil}`, "--no-first-run", "about:blank"]);
let echecs = 0;
const ok = (cond, msg) => { console.log(`${cond ? "✓" : "✗"} ${msg}`); if (!cond) echecs++; };

try {
  let cible;
  for (let i = 0; i < 40 && !cible; i++) {
    await pause(250);
    try { cible = (await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json()).find((t) => t.type === "page"); } catch (_) { /* pas prêt */ }
  }
  const ws = new WebSocket(cible.webSocketDebuggerUrl);
  await new Promise((r) => ws.addEventListener("open", r, { once: true }));
  let n = 0;
  const attente = new Map();
  const requetes = [];
  const erreurs = [];
  ws.addEventListener("message", (e) => {
    const m = JSON.parse(e.data);
    if (attente.has(m.id)) { attente.get(m.id)(m); attente.delete(m.id); }
    if (m.method === "Network.requestWillBeSent") requetes.push(m.params.request.url);
    if (m.method === "Runtime.exceptionThrown") erreurs.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
  });
  const cmd = (method, params = {}) => new Promise((r) => { const id = ++n; attente.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
  const js = async (expr) => (await cmd("Runtime.evaluate", { expression: expr, awaitPromise: true, returnByValue: true })).result?.result?.value;
  const aller = async (hash) => { await js(`location.hash = ${JSON.stringify(hash)}`); await pause(300); };

  await cmd("Network.enable");
  await cmd("Runtime.enable");
  await cmd("Page.navigate", { url: URL_APP });
  await pause(1500);

  // Démarrage
  ok(await js("typeof DONNEES === 'object' && DONNEES.candidats.length > 0"), "Données chargées en file://");
  ok(await js("document.getElementById('avertissement').open"), "Avertissement affiché au démarrage");
  await js("document.querySelector('#avertissement button[value=ok]').click()");
  ok((await js("document.title")).includes("Pour qui voter"), "Titre de l'onglet mis à jour");

  // Parcours complet : un avis sur chaque mesure de chaque thème
  const themes = await js("DONNEES.themes.map((t) => t.id)");
  await aller("#/priorites");
  await js("document.querySelector('.tuile').click()");
  for (const [i, t] of themes.entries()) {
    await aller(`#/questionnaire/${t}`);
    await js(`document.querySelectorAll('[data-avis]').forEach((b, k) => { if (k % 3 === ${i % 3}) b.click(); })`);
  }
  await js("document.querySelector('[data-avis]')?.click(); document.querySelector('[data-etoile]:not([disabled])')?.click()");
  await aller("#/resultats");
  ok(await js("!!document.querySelector('.tampon') && !!document.querySelector('.radar svg') && !!document.querySelector('table.chaleur')"),
    "Résultats : classement, radar et tableau par thème");
  const nbCand = await js("document.querySelectorAll('section.bulletin').length");
  const nbSaisis = await js("new Set(DONNEES.positions.filter((p) => p.valeur !== 0).map((p) => p.candidat)).size");
  const nbTotal = await js("DONNEES.candidats.length");
  ok(nbCand === nbSaisis, `Candidats ayant des positions classés (${nbCand}/${nbTotal})`);
  ok(nbTotal === nbSaisis || await js("!!document.querySelector('.en-attente')"), "Candidats sans positions signalés à part");

  // Persistance après rechargement
  await cmd("Page.reload");
  await pause(1200);
  ok(await js("Object.keys(JSON.parse(localStorage.getItem('pqv.reponses.v1')).reponses).length > 0"), "Réponses conservées après rechargement");

  // Édition locale + mode second tour
  await js(`(() => {
    const d = JSON.parse(JSON.stringify(DONNEES));
    const saisis = [...new Set(d.positions.filter((p) => p.valeur !== 0).map((p) => p.candidat))];
    d.second_tour = { actif: true, qualifies: [saisis[0], saisis[1]] };
    d.origine = "local";
    localStorage.setItem("pqv.donnees.v1", JSON.stringify(d));
  })()`);
  await cmd("Page.reload");
  await pause(1200);
  await js("document.getElementById('avertissement').open && document.getElementById('avertissement').close()");
  await aller("#/resultats");
  ok(await js("document.querySelectorAll('section.bulletin').length") === 2, "Second tour : seuls les 2 qualifiés sont comparés");
  ok(await js("!!document.querySelector('.t2')"), "Second tour : bandeau affiché");
  await aller("#/resultats/tous");
  ok(await js("document.querySelectorAll('section.bulletin').length") === nbCand, "Second tour : « voir tous les candidats » fonctionne");
  await aller("#/candidats");
  ok(await js("document.querySelectorAll('a.carte.elimine').length") === nbTotal - 2, "Second tour : non-qualifiés grisés");
  await aller("#/edition/positions");
  ok(await js("document.querySelectorAll('.ed-cellule').length > 0"), "Mode Édition disponible en local");

  // Pages d'information
  await aller("#/mentions");
  ok(await js("document.querySelector('main h1').textContent") === "Mentions légales", "Page Mentions légales (licences, responsabilité, confidentialité)");
  ok(await js("document.querySelector('.pied').textContent.includes('EUPL')"), "Licences indiquées dans le pied de page");

  // Démo en ligne simulée (?demo) : édition d'essai, candidats verrouillés
  await js(`(() => {
    const d = JSON.parse(localStorage.getItem("pqv.donnees.v1") || JSON.stringify(DONNEES));
    d.candidats.push({ id: "intrus", nom: "Candidat ajouté", parti: "?" });
    localStorage.setItem("pqv.donnees.v1", JSON.stringify(d));
  })()`);
  await cmd("Page.navigate", { url: URL_APP + "?demo#/candidats" });
  await pause(1500);
  await js("document.getElementById('avertissement').open && document.getElementById('avertissement').close()");
  ok(await js("!!document.querySelector('.bandeau-demo')"), "Démo en ligne : bandeau de téléchargement");
  ok(await js("document.querySelectorAll('main a.carte').length === DONNEES.candidats.length"), "Démo en ligne : candidat ajouté localement ignoré (liste verrouillée)");
  await aller("#/edition/candidats");
  ok(await js("!!document.querySelector('.ed-verrou') && !document.querySelector('[data-ed=modifier]') && !document.querySelector('[data-ed=ajouter]')"),
    "Démo en ligne : candidats non modifiables dans l'édition");
  await aller("#/edition/mesures");
  ok(await js("document.querySelectorAll('[data-ed=modifier]').length > 0"), "Démo en ligne : mesures modifiables (mode essai)");
  await aller("#/edition/fichiers");
  ok(await js("!document.querySelector('[data-ed-fichier]')"), "Démo en ligne : import de packs désactivé");

  // Aucune requête réseau
  const externes = requetes.filter((u) => !u.startsWith("file:") && !u.startsWith("data:") && !u.startsWith("blob:"));
  ok(externes.length === 0, `Aucune requête réseau (${requetes.length} chargements locaux${externes.length ? ` ; externes : ${externes.join(", ")}` : ""})`);
  ok(erreurs.length === 0, `Aucune erreur JavaScript${erreurs.length ? " : " + erreurs.join(" | ") : ""}`);
  ws.close();
} finally {
  chrome.kill();
}
console.log(echecs ? `\n${echecs} échec(s).` : "\nTous les contrôles hors ligne passent.");
process.exit(echecs ? 1 : 0);
