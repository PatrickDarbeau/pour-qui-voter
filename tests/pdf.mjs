// Génère le PDF de la page de résultats avec Chrome sans interface, pour vérifier la mise en page d'impression.
// Prérequis : serveur local lancé (python -m http.server 8765).
// Usage : node tests/pdf.mjs [fichier_sortie.pdf]
import { spawn } from "node:child_process";
import { writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe";
const SORTIE = process.argv[2] || "resultats.pdf";
const BASE = "http://localhost:8765/";
const PORT = 9900 + Math.floor(Math.random() * 90);
const pause = (ms) => new Promise((r) => setTimeout(r, ms));

const profil = mkdtempSync(join(tmpdir(), "pqv-pdf-"));
const chrome = spawn(CHROME, ["--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${profil}`, "--no-first-run", "about:blank"]);

try {
  let cible;
  for (let i = 0; i < 40 && !cible; i++) {
    await pause(250);
    try { cible = (await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json()).find((t) => t.type === "page"); } catch (_) { /* pas prêt */ }
  }
  if (!cible) throw new Error("Chrome n'a pas démarré");
  const ws = new WebSocket(cible.webSocketDebuggerUrl);
  await new Promise((r) => ws.addEventListener("open", r, { once: true }));
  let n = 0;
  const attente = new Map();
  ws.addEventListener("message", (e) => { const m = JSON.parse(e.data); if (attente.has(m.id)) { attente.get(m.id)(m); attente.delete(m.id); } });
  const cmd = (method, params = {}) => new Promise((r) => { const id = ++n; attente.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
  const evaluer = async (expr) => (await cmd("Runtime.evaluate", { expression: expr, awaitPromise: true, returnByValue: true })).result?.result?.value;

  await cmd("Page.navigate", { url: BASE });
  await pause(1000);
  // Réponses de test : pour sur les mesures paires, contre sur les impaires, une essentielle, un thème prioritaire
  await evaluer(`(() => {
    const rep = {};
    DONNEES.mesures.forEach((m, i) => { rep[m.id] = { avis: i % 2 ? -1 : 1, essentielle: i === 0 }; });
    localStorage.setItem("pqv.reponses.v1", JSON.stringify({ reponses: rep, prioritaires: [DONNEES.themes[1].id], ordre: {} }));
    localStorage.setItem("pqv.avertissement.masque", "1");
  })()`);
  await cmd("Page.navigate", { url: BASE + "#/resultats" });
  await cmd("Page.reload", { ignoreCache: true });
  await pause(1500);
  // Même logique que le bouton « Imprimer / PDF »
  await evaluer(`document.querySelectorAll("details").forEach((d) => (d.open = !!d.closest(".premier") || d.classList.contains("carte")))`);
  await pause(300);
  const pdf = await cmd("Page.printToPDF", { printBackground: true, preferCSSPageSize: true });
  if (!pdf.result) throw new Error(JSON.stringify(pdf.error));
  writeFileSync(SORTIE, Buffer.from(pdf.result.data, "base64"));
  console.log("PDF écrit :", SORTIE);
  ws.close();
} finally {
  chrome.kill();
}
