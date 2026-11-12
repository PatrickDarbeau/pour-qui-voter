/* Application « Pour qui voter ? » — parcours électeur (CDC §4.3 à §4.5).
 * Routage par hash, aucun appel réseau, réponses conservées dans localStorage.
 */
(function () {
  "use strict";

  const D = window.DONNEES;
  const app = document.getElementById("app");
  const CLE = "pqv.reponses.v1";

  if (!D) {
    app.innerHTML = "<p>Les données sont introuvables (data/donnees.js).</p>";
    return;
  }

  // ---------- Outils ----------
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const themes = [...D.themes].sort((a, b) => a.ordre - b.ordre);
  const themeParId = Object.fromEntries(themes.map((t) => [t.id, t]));
  const candParId = Object.fromEntries(D.candidats.map((c) => [c.id, c]));
  const mesuresActives = D.mesures.filter((m) => m.actif !== false);
  const mesuresDuTheme = (t) => mesuresActives.filter((m) => m.theme === t);
  const nomComplet = (c) => `${c.prenom || ""} ${c.nom}`.trim();
  const pct = (v) => (v === null || v === undefined ? "—" : v.toLocaleString("fr-FR") + " %");
  const pluriel = (n, mot) => `${n} ${mot}${n > 1 ? "s" : ""}`;
  const LIBELLE_POS ={ "1": "Soutient", "0.5": "Soutient partiellement", "0": "Ne se prononce pas", "-1": "S'oppose" };

  // ---------- État (F18) ----------
  function charger() {
    try {
      const e = JSON.parse(localStorage.getItem(CLE));
      if (e && e.reponses) return e;
    } catch (_) { /* stockage indisponible */ }
    return { reponses: {}, prioritaires: [], ordre: {} };
  }
  let etat = charger();
  function sauver() {
    try { localStorage.setItem(CLE, JSON.stringify(etat)); } catch (_) { /* ignoré */ }
  }

  // F12 : ordre aléatoire des mesures, figé pour la session de l'utilisateur
  function ordreMesures(themeId) {
    const ids = mesuresDuTheme(themeId).map((m) => m.id);
    let o = etat.ordre[themeId];
    if (!o || o.length !== ids.length || !o.every((i) => ids.includes(i))) {
      o = [...ids];
      for (let i = o.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [o[i], o[j]] = [o[j], o[i]];
      }
      etat.ordre[themeId] = o;
      sauver();
    }
    return o.map((id) => D.mesures.find((m) => m.id === id));
  }

  const nbRepondues = () => Object.values(etat.reponses).filter((r) => r.avis !== undefined).length;
  const themeFait = (t) => mesuresDuTheme(t).every((m) => etat.reponses[m.id]);

  // ---------- Dates du scrutin ----------
  const TOUR1 = new Date((D.elections?.tour1 || "2027-04-18") + "T08:00:00");
  const TOUR2 = new Date((D.elections?.tour2 || "2027-05-02") + "T08:00:00");
  function decompte() {
    const now = new Date();
    const cible = now < TOUR1 ? ["premier tour", TOUR1] : now < TOUR2 ? ["second tour", TOUR2] : null;
    if (!cible) return "";
    const jours = Math.ceil((cible[1] - now) / 86400000);
    return `<div><strong>${jours}</strong> jours avant le ${cible[0]}<br>
      <span class="doux">${cible[1].toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long", year: "numeric" })}</span></div>`;
  }

  // ---------- Bandeau origine des données (F28, F39) ----------
  function bandeau() {
    const b = document.getElementById("bandeau-donnees");
    const msgs = [];
    if (D.demo) msgs.push("Données de démonstration : les candidats sont fictifs.");
    const age = (Date.now() - new Date(D.date)) / 86400000;
    const limite = Date.now() >= new Date("2027-02-01") ? 7 : 30;
    if (age > limite) msgs.push(`Données datées du ${new Date(D.date).toLocaleDateString("fr-FR")} : pensez à importer un pack plus récent.`);
    b.hidden = !msgs.length;
    b.textContent = msgs.join(" ");
  }

  // ---------- Vues ----------
  function vueAccueil() {
    const n = nbRepondues();
    return `
      <section class="hero">
        <div>
          <span class="surtitre">Présidentielle 2027</span>
          <h1>Votre bulletin, vos priorités.</h1>
          <p class="chapo">Indiquez, thème par thème, les mesures que vous soutenez ou rejetez.
          L'outil calcule votre concordance avec chaque candidat.</p>
        </div>
        <svg class="urne" viewBox="0 0 200 200" role="img" aria-label="Urne transparente">
          <rect class="fente-bulletin" x="72" y="20" width="56" height="40" rx="2" fill="var(--carte)" stroke="currentColor" stroke-width="3"/>
          <rect x="30" y="70" width="140" height="18" rx="3" fill="var(--papier-2)" stroke="currentColor" stroke-width="3"/>
          <rect x="70" y="76" width="60" height="5" rx="2" fill="currentColor"/>
          <rect x="38" y="88" width="124" height="96" rx="4" fill="color-mix(in srgb, var(--bleu) 8%, transparent)" stroke="currentColor" stroke-width="3"/>
          <path d="M60 170 l12 -14 l12 10 l14 -18" fill="none" stroke="var(--rouge)" stroke-width="3" stroke-linecap="round" opacity=".7"/>
        </svg>
      </section>
      <div class="decompte">${decompte()}
        <div><strong>${D.candidats.length}</strong> candidats<br><span class="doux">${mesuresActives.length} mesures, ${themes.length} thèmes</span></div>
      </div>
      <ol class="etapes">
        <li>Choisissez vos thèmes prioritaires (facultatif).</li>
        <li>Donnez votre avis sur chaque mesure ; marquez d'une ★ celles qui vous sont essentielles.</li>
        <li>Découvrez le classement et le détail des accords et désaccords, sources à l'appui.</li>
      </ol>
      <p class="doux">Rien n'est envoyé sur internet : vos réponses restent sur cet appareil.</p>
      <div class="actions">
        <a class="btn" href="#/priorites">${n ? "Reprendre" : "Commencer"}</a>
        ${n ? `<a class="btn secondaire" href="#/resultats">Voir mes résultats (${n} réponses)</a>` : ""}
      </div>
      <p class="doux" style="margin-top:2rem">Données : version ${esc(D.version)} du ${new Date(D.date).toLocaleDateString("fr-FR")}
        — origine : ${D.origine === "officiel" ? "pack officiel" : "données modifiées localement"}.</p>`;
  }

  function vuePriorites() {
    const tuiles = themes.map((t) => `
      <button class="tuile" data-theme="${esc(t.id)}" aria-pressed="${etat.prioritaires.includes(t.id)}">
        <span class="ico" aria-hidden="true">${esc(t.icone)}</span>${esc(t.nom)}
      </button>`).join("");
    return `
      <h1>Quels thèmes comptent le plus pour vous&nbsp;?</h1>
      <p class="doux">Les thèmes choisis comptent double dans le calcul. Vous pouvez n'en choisir aucun.</p>
      <div class="grille">${tuiles}</div>
      <div class="actions">
        <a class="btn secondaire" href="#/">Retour</a>
        <a class="btn" href="#/questionnaire/${esc(themes[0].id)}">Continuer</a>
      </div>`;
  }

  function vueQuestionnaire(themeId) {
    const t = themeParId[themeId] || themes[0];
    const i = themes.indexOf(t);
    const pct = Math.round((nbRepondues() / mesuresActives.length) * 100);
    const onglets = themes.map((x) => `<a href="#/questionnaire/${esc(x.id)}"
        class="${x.id === t.id ? "actif" : ""} ${themeFait(x.id) ? "fait" : ""}">${esc(x.icone)} ${esc(x.nom)}</a>`).join("");
    const cartes = ordreMesures(t.id).map((m) => {
      const r = etat.reponses[m.id] || {};
      const b = (cls, avis, txt) => `<button class="${cls}" data-mesure="${esc(m.id)}" data-avis="${avis}"
          aria-pressed="${r.avis === avis}">${txt}</button>`;
      return `<article class="carte bulletin mesure ${r.avis !== undefined ? "repondue" : ""}">
          <h3>${esc(m.intitule)}</h3>
          <p class="doux">${esc(m.description)}</p>
          <div class="choix" role="group" aria-label="Votre avis">
            ${b("oui", 1, "Je soutiens")}${b("non", -1, "Je m'oppose")}${b("neutre", 0, "Indifférent")}
            <button class="etoile" data-etoile="${esc(m.id)}" aria-pressed="${!!r.essentielle}"
              ${r.avis ? "" : "disabled"} title="Mesure essentielle (compte triple)">★ Essentielle</button>
          </div>
        </article>`;
    }).join("");
    const prec = i > 0 ? `#/questionnaire/${themes[i - 1].id}` : "#/priorites";
    const suiv = i < themes.length - 1 ? `#/questionnaire/${themes[i + 1].id}` : "#/resultats";
    return `
      <div class="progression" aria-label="Progression ${pct} %"><span style="width:${pct}%"></span></div>
      <nav class="onglets" aria-label="Thèmes">${onglets}</nav>
      <h1>${esc(t.icone)} ${esc(t.nom)}</h1>
      ${cartes}
      <div class="actions">
        <a class="btn secondaire" href="${prec}">Précédent</a>
        <a class="btn" href="${suiv}">${i < themes.length - 1 ? "Thème suivant" : "Voir les résultats"}</a>
      </div>`;
  }

  function couleurBarre(c) { return /^#[0-9a-f]{3,6}$/i.test(c.couleur || "") ? c.couleur : "var(--accent)"; }

  function vueResultats() {
    const { nbMesures, resultats } = Score.calculer(D, etat.reponses, etat.prioritaires);
    if (!nbMesures) {
      return `<h1>Résultats</h1><p>Vous n'avez encore donné aucun avis (soutien ou opposition).</p>
        <a class="btn" href="#/priorites">Commencer le questionnaire</a>`;
    }
    const top = resultats[0];
    const exAequo = resultats.filter((r) => r.exAequo);
    const item = (x) => `<li>${esc(x.mesure.intitule)}
        <span class="doux">— vous : ${x.avis > 0 ? "pour" : "contre"} ; candidat : ${LIBELLE_POS[String(x.position?.valeur ?? 0)]}
        ${x.position?.source_url ? `· <a href="${esc(x.position.source_url)}" rel="noopener noreferrer" target="_blank">source</a>` : ""}</span></li>`;
    const blocs = resultats.map((r, k) => `
      <section class="carte bulletin ${k === 0 ? "premier" : ""}" style="animation-delay:${k * 60}ms">
        <span class="rang">N° ${k + 1}</span>
        <div class="ligne-score">
          <span class="nom"><span class="pastille" style="background:${couleurBarre(r.candidat)}"></span>${esc(nomComplet(r.candidat))}</span>
          <div class="barre" aria-hidden="true"><span style="width:${r.score}%;background:${couleurBarre(r.candidat)};animation-delay:${k * 80}ms"></span></div>
          <span class="pct">${pct(r.score)}</span>
        </div>
        <div class="doux">${esc(r.candidat.parti)} · couverture ${r.couverture} %
          ${k === 0 ? '<span class="badge">Vote préférentiel</span>' : ""}${r.exAequo ? '<span class="badge">Ex æquo</span>' : ""}</div>
        <details>
          <summary>Détail : ${pluriel(r.accords.length, "accord")}, ${pluriel(r.desaccords.length, "désaccord")}, ${r.silences.length} sans position</summary>
          <div class="themes-mini">${Object.entries(r.themes).map(([t, v]) => `<span>${esc(themeParId[t]?.icone)} ${esc(themeParId[t]?.nom)} : ${pct(v)}</span>`).join("")}</div>
          ${r.accords.length ? `<h3 class="ok">Accords</h3><ul class="liste">${r.accords.map(item).join("")}</ul>` : ""}
          ${r.desaccords.length ? `<h3 class="ko">Désaccords</h3><ul class="liste">${r.desaccords.map(item).join("")}</ul>` : ""}
          ${r.silences.length ? `<h3>Sans position connue</h3><ul class="liste">${r.silences.map(item).join("")}</ul>` : ""}
          <p><a href="#/candidat/${esc(r.candidat.id)}">Voir la fiche du candidat</a></p>
        </details>
      </section>`).join("");
    return `
      <div class="podium">
        <div>
          <span class="surtitre">Dépouillement</span>
          <h1>${esc(nomComplet(top.candidat))}</h1>
          <p>est le candidat le plus proche de vos choix, avec <strong>${pct(top.score)}</strong> de concordance
            sur <strong>${nbMesures}</strong> mesures.</p>
        </div>
        <div class="tampon">Vote<br>préférentiel</div>
      </div>
      ${exAequo.length ? `<p class="carte">⚠️ Écart de moins de ${Score.SEUIL_EX_AEQUO} points avec :
        ${exAequo.map((r) => esc(nomComplet(r.candidat))).join(", ")}. Consultez le détail avant de vous décider.</p>` : ""}
      <p class="doux">La couverture indique la part de vos mesures sur lesquelles le candidat s'est prononcé.
        Ce résultat est un éclairage, pas une consigne de vote.</p>
      ${blocs}
      <div class="actions">
        <a class="btn secondaire" href="#/questionnaire/${esc(themes[0].id)}">Modifier mes réponses</a>
        <button class="btn secondaire" data-action="imprimer">Imprimer / PDF</button>
        <button class="btn secondaire" data-action="effacer">Recommencer</button>
      </div>`;
  }

  function vueCandidats() {
    return `<h1>Les candidats</h1>` + D.candidats.map((c) => `
      <a class="carte bulletin" href="#/candidat/${esc(c.id)}">
        <strong><span class="pastille" style="background:${couleurBarre(c)}"></span>${esc(nomComplet(c))}</strong>
        <span class="doux">— ${esc(c.parti)}</span><br><em>${esc(c.slogan || "")}</em>
      </a>`).join("");
  }

  function vueCandidat(id) {
    const c = candParId[id];
    if (!c) return "<p>Candidat introuvable.</p>";
    const pos = Object.fromEntries(D.positions.filter((p) => p.candidat === id).map((p) => [p.mesure, p]));
    const sections = themes.map((t) => `
      <h2>${esc(t.icone)} ${esc(t.nom)}</h2>
      <table><tbody>${mesuresDuTheme(t.id).map((m) => {
        const p = pos[m.id];
        const v = p ? p.valeur : 0;
        const cls = v > 0 ? "ok" : v < 0 ? "ko" : "doux";
        return `<tr><td>${esc(m.intitule)}</td><td class="${cls}">${LIBELLE_POS[String(v)]}${p?.a_confirmer ? " (à confirmer)" : ""}</td>
          <td>${p?.source_url ? `<a href="${esc(p.source_url)}" rel="noopener noreferrer" target="_blank">source</a>` : ""}</td></tr>`;
      }).join("")}</tbody></table>`).join("");
    return `
      <p><a href="#/candidats">← Tous les candidats</a></p>
      <h1><span class="pastille" style="background:${couleurBarre(c)}"></span>${esc(nomComplet(c))}</h1>
      <p><strong>${esc(c.parti)}</strong>${c.slogan ? ` — « ${esc(c.slogan)} »` : ""}</p>
      <p>${esc(c.biographie || "")}</p>
      ${c.site_officiel ? `<p>Site officiel : <a href="${esc(c.site_officiel)}" rel="noopener noreferrer" target="_blank">${esc(c.site_officiel)}</a></p>` : ""}
      ${sections}`;
  }

  function vueMethode() {
    return `
      <h1>Méthode de calcul</h1>
      <p>Pour chaque mesure où vous avez exprimé un avis (pour = +1, contre = −1), on compare avec la position du candidat :
        soutient (+1), soutient partiellement (+0,5), ne se prononce pas (0), s'oppose (−1).</p>
      <p>L'accord vaut le produit des deux. Chaque mesure est pondérée : ×2 si son thème est prioritaire, ×3 si vous l'avez marquée essentielle.</p>
      <p>Le score est la moyenne pondérée des accords, ramenée de [−1 ; +1] à [0 ; 100 %].
        Un candidat sans position sur une mesure obtient 0 pour celle-ci, soit 50 % : ni accord ni désaccord.</p>
      <p>La <strong>couverture</strong> indique la part de vos mesures sur lesquelles le candidat s'est prononcé.
        Deux candidats à moins de ${Score.SEUIL_EX_AEQUO} points sont signalés ex æquo.</p>
      <p>Les positions proviennent en priorité du site officiel et du programme de chaque candidat ; chaque position est sourcée.</p>`;
  }

  // ---------- Routage ----------
  function rendre() {
    const [, route, param] = (location.hash || "#/").split("/");
    const vues = {
      "": vueAccueil, priorites: vuePriorites, questionnaire: () => vueQuestionnaire(param),
      resultats: vueResultats, candidats: vueCandidats, candidat: () => vueCandidat(param), methode: vueMethode,
    };
    app.innerHTML = (vues[route] || vueAccueil)();
    window.scrollTo(0, 0);
    app.focus({ preventScroll: true });
  }

  // ---------- Interactions ----------
  app.addEventListener("click", (e) => {
    const el = e.target.closest("button");
    if (!el) return;
    if (el.dataset.theme) {
      const t = el.dataset.theme;
      const p = new Set(etat.prioritaires);
      p.has(t) ? p.delete(t) : p.add(t);
      etat.prioritaires = [...p];
      el.setAttribute("aria-pressed", p.has(t));
      sauver();
    } else if (el.dataset.mesure) {
      const id = el.dataset.mesure;
      const avis = Number(el.dataset.avis);
      const r = etat.reponses[id] || {};
      etat.reponses[id] = { avis, essentielle: avis !== 0 && !!r.essentielle };
      sauver();
      majCarte(el.closest(".mesure"), id);
    } else if (el.dataset.etoile) {
      const r = etat.reponses[el.dataset.etoile];
      if (r && r.avis) { r.essentielle = !r.essentielle; sauver(); majCarte(el.closest(".mesure"), el.dataset.etoile); }
    } else if (el.dataset.action === "imprimer") {
      window.print();
    } else if (el.dataset.action === "effacer") {
      if (confirm("Effacer toutes vos réponses ?")) {
        etat = { reponses: {}, prioritaires: [], ordre: {} };
        sauver();
        location.hash = "#/";
      }
    }
  });

  function majCarte(carte, id) {
    const r = etat.reponses[id] || {};
    carte.querySelectorAll("[data-avis]").forEach((b) => b.setAttribute("aria-pressed", Number(b.dataset.avis) === r.avis));
    const et = carte.querySelector("[data-etoile]");
    et.setAttribute("aria-pressed", !!r.essentielle);
    et.disabled = !r.avis;
    carte.classList.add("repondue");
    const pct = Math.round((nbRepondues() / mesuresActives.length) * 100);
    const barre = document.querySelector(".progression span");
    if (barre) barre.style.width = pct + "%";
    const t = mesuresActives.find((m) => m.id === id)?.theme;
    const onglet = document.querySelector(`.onglets a[href="#/questionnaire/${t}"]`);
    if (onglet) onglet.classList.toggle("fait", themeFait(t));
  }

  window.addEventListener("hashchange", rendre);
  bandeau();
  rendre();
})();
