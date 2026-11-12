/* Graphiques des résultats (CDC F15), en SVG pur : aucune bibliothèque, aucun réseau.
 * - radar : profil de concordance par thème des premiers candidats ;
 * - chaleur : tableau candidats × thèmes coloré selon la concordance.
 */
(function () {
  "use strict";

  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const couleur = (c) => (/^#[0-9a-f]{3,8}$/i.test(c || "") ? c : "#1f3a8a");
  const nom = (c) => `${c.prenom || ""} ${c.nom}`.trim();
  const pct = (v) => (v === null || v === undefined ? "—" : Math.round(v) + " %");

  /* Radar : themes = [{id, nom, icone}], series = résultats de Score.calculer (max 3 conseillé) */
  function radar(themes, series) {
    const axes = themes.filter((t) => series.some((s) => s.themes[t.id] !== undefined));
    if (axes.length < 3) return "";
    const T = 360, C = T / 2, R = 120;
    const point = (i, v) => {
      const a = -Math.PI / 2 + (2 * Math.PI * i) / axes.length;
      return [C + Math.cos(a) * R * v, C + Math.sin(a) * R * v];
    };
    const grille = [0.25, 0.5, 0.75, 1].map((k) =>
      `<polygon points="${axes.map((_, i) => point(i, k).join(",")).join(" ")}" class="radar-grille ${k === 0.5 ? "radar-moitie" : ""}"/>`).join("");
    const rayons = axes.map((t, i) => {
      const [x, y] = point(i, 1);
      const [lx, ly] = point(i, 1.2);
      const ancre = Math.abs(lx - C) < 8 ? "middle" : lx > C ? "start" : "end";
      return `<line x1="${C}" y1="${C}" x2="${x}" y2="${y}" class="radar-rayon"/>
        <text x="${lx}" y="${ly}" text-anchor="${ancre}" dominant-baseline="middle" class="radar-etiquette">${esc(t.icone || "")} ${esc(t.nom)}</text>`;
    }).join("");
    const formes = series.map((s, k) => {
      const pts = axes.map((t, i) => point(i, (s.themes[t.id] ?? 50) / 100).join(",")).join(" ");
      const c = couleur(s.candidat.couleur);
      return `<polygon points="${pts}" fill="${c}" fill-opacity="${k === 0 ? 0.28 : 0.12}" stroke="${c}" stroke-width="${k === 0 ? 3 : 2}" ${k ? 'stroke-dasharray="6 4"' : ""}/>`;
    }).join("");
    const legende = series.map((s, k) => `<li><span class="pastille" style="background:${couleur(s.candidat.couleur)}"></span>
      ${esc(nom(s.candidat))} <span class="doux">(${pct(s.score)})</span>${k === 0 ? "" : ""}</li>`).join("");
    return `<figure class="radar">
      <svg viewBox="-110 -20 580 400" role="img" aria-label="Concordance par thème des ${series.length} premiers candidats">
        ${grille}${rayons}${formes}
        <text x="${C + 4}" y="${C - R / 2 - 4}" class="radar-repere">50 %</text>
        <text x="${C + 4}" y="${C - R - 4}" class="radar-repere">100 %</text>
      </svg>
      <figcaption><ul class="legende">${legende}</ul>
        <span class="doux">Plus la forme est grande, plus le candidat est proche de vous sur ce thème. Le cercle du milieu correspond à 50 %.</span></figcaption>
    </figure>`;
  }

  /* Carte de chaleur : une ligne par candidat, une colonne par thème */
  function chaleur(themes, resultats) {
    const cols = themes.filter((t) => resultats.some((r) => r.themes[t.id] !== undefined));
    if (!cols.length) return "";
    // de rouge (0 %) à gris (50 %) à vert (100 %)
    const fond = (v) => {
      if (v === undefined) return "";
      const d = (v - 50) / 50; // -1..1
      const base = d >= 0 ? "var(--oui)" : "var(--non)";
      return `style="background:color-mix(in srgb, ${base} ${Math.round(Math.abs(d) * 85)}%, var(--carte))"`;
    };
    const entete = cols.map((t) => `<th title="${esc(t.nom)}"><span class="chaleur-ico">${esc(t.icone || "")}</span><span class="chaleur-nom">${esc(t.nom)}</span></th>`).join("");
    const lignes = resultats.map((r) => `<tr><th><span class="pastille" style="background:${couleur(r.candidat.couleur)}"></span>${esc(nom(r.candidat))}</th>
      ${cols.map((t) => { const v = r.themes[t.id]; return `<td ${fond(v)}>${v === undefined ? "—" : Math.round(v)}</td>`; }).join("")}
      <td class="chaleur-total">${pct(r.score)}</td></tr>`).join("");
    return `<div class="chaleur-cadre"><table class="chaleur">
      <thead><tr><th></th>${entete}<th>Total</th></tr></thead><tbody>${lignes}</tbody></table></div>
      <p class="doux"><small>Concordance en % par thème. Vert : proche de vos choix ; rouge : éloigné ; gris : neutre ou sans position.</small></p>`;
  }

  window.Graphiques = { radar, chaleur };
})();
