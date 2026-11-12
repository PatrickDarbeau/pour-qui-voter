/* Application « Pour qui voter ? » — parcours électeur (CDC §4.3 à §4.5).
 * Routage par hash, aucun appel réseau, réponses conservées dans localStorage.
 */
(function () {
  "use strict";

  // Démo en ligne (CDC §6 bis) : servie par un hébergeur web, hors poste local.
  // « ?demo » dans l'adresse permet de tester ce mode en local.
  const EN_LIGNE = (/^https?:$/.test(location.protocol) && !/^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname))
    || /[?&]demo\b/.test(location.search);
  const CONFIG = window.CONFIG || {};
  // Données modifiées localement (mode Édition, F27) prioritaires sur le pack embarqué — sauf en démo en ligne
  const D = (!EN_LIGNE && window.Edition && window.Edition.donneesActives()) || window.DONNEES;
  if (EN_LIGNE) document.documentElement.classList.add("en-ligne");
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
  // Mode second tour : identifiants des deux qualifiés, ou null
  const T2 = D.second_tour && D.second_tour.actif && Array.isArray(D.second_tour.qualifies)
    && D.second_tour.qualifies.length === 2 && D.second_tour.qualifies.every((id) => candParId[id])
    ? D.second_tour.qualifies : null;
  const mesuresDuTheme = (t) => mesuresActives.filter((m) => m.theme === t);
  const nomComplet = (c) => `${c.prenom || ""} ${c.nom}`.trim();
  // Couleur propre à chaque thème (validée pour éviter toute injection CSS)
  const thStyle = (t) => (t && /^#[0-9a-f]{3,8}$/i.test(t.couleur || "") ? `style="--c:${t.couleur}"` : "");
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
    b.hidden = !msgs.length && !EN_LIGNE;
    b.textContent = msgs.join(" ");
    if (EN_LIGNE) {
      // Bandeau permanent de la démo en ligne, avec lien de téléchargement
      const demo = document.createElement("div");
      demo.className = "bandeau-demo";
      demo.innerHTML = `<strong>Version de démonstration en ligne.</strong>
        Pour une confidentialité totale, téléchargez l'application et utilisez-la sur votre ordinateur, même sans internet.
        ${CONFIG.telechargement ? `<a class="btn-mini" href="${esc(CONFIG.telechargement)}" target="_blank" rel="noopener noreferrer">⬇ Télécharger</a>` : ""}`;
      b.before(demo);
    }
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
          <g class="fente-bulletin">
            <rect x="72" y="20" width="56" height="40" rx="2" fill="var(--carte)" stroke="currentColor" stroke-width="3"/>
            <text x="100" y="41" text-anchor="middle" dominant-baseline="central" class="urne-question">?</text>
          </g>
          <rect x="30" y="70" width="140" height="18" rx="3" fill="var(--papier-2)" stroke="currentColor" stroke-width="3"/>
          <rect x="70" y="76" width="60" height="5" rx="2" fill="currentColor"/>
          <rect x="38" y="88" width="124" height="96" rx="4" fill="color-mix(in srgb, var(--bleu) 8%, transparent)" stroke="currentColor" stroke-width="3"/>
          <path d="M60 170 l12 -14 l12 10 l14 -18" fill="none" stroke="var(--rouge)" stroke-width="3" stroke-linecap="round" opacity=".7"/>
        </svg>
      </section>
      <div class="decompte">${decompte()}
        ${T2
          ? `<div><strong>2</strong> candidats au second tour<br><span class="doux">${T2.map((id) => esc(nomComplet(candParId[id]))).join(" · ")}</span></div>`
          : `<div><strong>${D.candidats.length}</strong> candidats<br><span class="doux">${mesuresActives.length} mesures, ${themes.length} thèmes</span></div>`}
      </div>
      <ol class="etapes">
        <li>Choisissez vos thèmes prioritaires (facultatif).</li>
        <li>Donnez votre avis sur chaque mesure ; marquez d'une ★ celles qui vous sont essentielles.</li>
        <li>Découvrez le classement et le détail des accords et désaccords avec les candidats, sources à l'appui.</li>
      </ol>
      <p class="doux">Rien n'est envoyé sur internet : vos réponses restent sur cet appareil.</p>
      ${n ? `
      <div class="carte reprise">
        <p><strong>Vous avez déjà commencé&nbsp;!</strong> ${n} mesure${n > 1 ? "s" : ""} sur ${mesuresActives.length}
          ${n >= mesuresActives.length ? "— questionnaire terminé." : "— vous pouvez reprendre où vous en étiez."}</p>
        <div class="progression" role="progressbar" aria-label="Progression du questionnaire" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.min(100, Math.round((n / mesuresActives.length) * 100))}"><span style="width:${Math.min(100, Math.round((n / mesuresActives.length) * 100))}%"></span></div>
        <div class="actions">
          <a class="btn" href="#/questionnaire/${esc((themes.find((t) => !themeFait(t.id)) || themes[0]).id)}">${n >= mesuresActives.length ? "✎ Revoir mes réponses" : "▶ Poursuivre"}</a>
          <a class="btn secondaire" href="#/resultats">Voir mes résultats</a>
          <button class="btn secondaire" data-action="effacer">↺ Recommencer à zéro</button>
        </div>
      </div>` : `
      <div class="actions"><a class="btn" href="#/priorites">Commencer</a></div>`}
      <p class="doux" style="margin-top:2rem">Données : version ${esc(D.version)} du ${new Date(D.date).toLocaleDateString("fr-FR")}
        — origine : ${D.origine === "officiel" ? "pack officiel" : `données modifiées localement (${window.Edition ? pluriel(window.Edition.nbModifs(), "élément") : "?"})`}.</p>`;
  }

  function vuePriorites() {
    const tuiles = themes.map((t) => `
      <button class="tuile th" ${thStyle(t)} data-theme="${esc(t.id)}" aria-pressed="${etat.prioritaires.includes(t.id)}">
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
    const onglets = themes.map((x) => `<a href="#/questionnaire/${esc(x.id)}" ${thStyle(x)}
        class="th ${x.id === t.id ? "actif" : ""} ${themeFait(x.id) ? "fait" : ""}">${esc(x.icone)} ${esc(x.nom)}</a>`).join("");
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
              ${r.avis ? "" : "disabled"} aria-label="Mesure essentielle (compte triple)">★ Essentielle</button>
          </div>
        </article>`;
    }).join("");
    const prec = i > 0 ? `#/questionnaire/${themes[i - 1].id}` : "#/priorites";
    const suiv = i < themes.length - 1 ? `#/questionnaire/${themes[i + 1].id}` : "#/resultats";
    return `
      <div class="progression" role="progressbar" aria-label="Progression du questionnaire" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${pct}"><span style="width:${pct}%"></span></div>
      <nav class="onglets" aria-label="Thèmes">${onglets}</nav>
      <h1 class="th titre-theme" ${thStyle(t)}>${esc(t.icone)} ${esc(t.nom)}</h1>
      ${cartes}
      <div class="actions">
        <a class="btn secondaire" href="${prec}">Précédent</a>
        <button class="lien" data-action="effacer">↺ Recommencer à zéro</button>
        <a class="btn" href="${suiv}">${i < themes.length - 1 ? "Thème suivant" : "Voir les résultats"}</a>
      </div>`;
  }

  function couleurBarre(c) { return /^#[0-9a-f]{3,6}$/i.test(c.couleur || "") ? c.couleur : "var(--accent)"; }

  function vueResultats(option) {
    // Mode second tour : comparaison limitée aux deux qualifiés, sauf si l'on demande « tous »
    const restreint = T2 && option !== "tous";
    const { nbMesures, resultats } = Score.calculer(D, etat.reponses, etat.prioritaires, restreint ? T2 : null);
    const bandeauT2 = T2 ? `<p class="carte t2">🗳 <strong>Second tour</strong> —
      ${restreint
        ? `comparaison limitée aux deux candidats qualifiés. <a href="#/resultats/tous">Voir aussi tous les candidats du premier tour</a>`
        : `vous voyez tous les candidats du premier tour. <a href="#/resultats">Revenir aux deux qualifiés</a>`}</p>` : "";
    if (!nbMesures) {
      return `<h1>Résultats</h1><p>Vous n'avez encore donné aucun avis (soutien ou opposition).</p>
        <a class="btn" href="#/priorites">Commencer le questionnaire</a>`;
    }
    const top = resultats[0];
    const exAequo = resultats.filter((r) => r.exAequo);
    const item = (x) => `<li>${esc(x.mesure.intitule)}
        <span class="doux">— vous : ${x.avis > 0 ? "pour" : "contre"} ; candidat : ${LIBELLE_POS[String(x.position?.valeur ?? 0)]}
        ${x.position?.source_url ? `· <a href="${esc(x.position.source_url)}" rel="noopener noreferrer" target="_blank">source</a>` : ""}</span></li>`;
    // Regroupe une liste de mesures par thème, dans l'ordre des thèmes
    const groupe = (liste, titre, cls) => {
      if (!liste.length) return "";
      const sousListes = themes
        .map((t) => [t, liste.filter((x) => x.mesure.theme === t.id)])
        .filter(([, l]) => l.length)
        .map(([t, l]) => `<div class="groupe-theme th" ${thStyle(t)}><h4>${esc(t.icone)} ${esc(t.nom)} <span class="doux">(${l.length})</span></h4>
            <ul class="liste">${l.map(item).join("")}</ul></div>`).join("");
      return `<h3 class="${cls}">${titre} <span class="doux">(${liste.length})</span></h3>${sousListes}`;
    };
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
          <div class="themes-mini">${Object.entries(r.themes).map(([t, v]) => `<span class="th" ${thStyle(themeParId[t])}>${esc(themeParId[t]?.icone)} ${esc(themeParId[t]?.nom)} : ${pct(v)}</span>`).join("")}</div>
          ${groupe(r.accords, "✔ Accords", "ok")}
          ${groupe(r.desaccords, "✘ Désaccords", "ko")}
          ${groupe(r.silences, "… Sans position connue", "")}
          <p><a href="#/candidat/${esc(r.candidat.id)}">Voir la fiche du candidat</a></p>
        </details>
      </section>`).join("");
    const G = window.Graphiques;
    const profil = G ? `
      <h2>Votre profil par thème</h2>
      ${G.radar(themes, resultats.slice(0, 3))}
      <details class="carte" open><summary>Tous les candidats, thème par thème</summary>${G.chaleur(themes, resultats)}</details>` : "";
    return `
      <div class="entete-impression">
        <strong>Pour qui voter ? — Présidentielle 2027</strong><br>
        Résultats du ${new Date().toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" })}
        · données ${esc(D.version)} · ${nbMesures} mesures · outil non officiel, aide à la décision
      </div>
      ${bandeauT2}
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
      <h2>Classement</h2>
      ${blocs}
      ${profil}
      <div class="actions">
        <a class="btn secondaire" href="#/questionnaire/${esc(themes[0].id)}">Modifier mes réponses</a>
        <button class="btn secondaire" data-action="imprimer">🖨 Imprimer / PDF</button>
        <button class="btn secondaire" data-action="partager">🔗 Lien de partage</button>
        <button class="btn secondaire" data-action="effacer">Recommencer</button>
      </div>
      <div id="zone-partage"></div>`;
  }

  function vueCandidats() {
    const ordre = T2 ? [...D.candidats].sort((a, b) => T2.includes(b.id) - T2.includes(a.id)) : D.candidats;
    return `<h1>Les candidats</h1>${T2 ? '<p class="doux">Second tour : les deux candidats qualifiés sont en tête ; les autres sont grisés.</p>' : ""}` + ordre.map((c) => {
      const elimine = T2 && !T2.includes(c.id);
      return `<a class="carte bulletin ${elimine ? "elimine" : ""}" href="#/candidat/${esc(c.id)}">
        <strong><span class="pastille" style="background:${couleurBarre(c)}"></span>${esc(nomComplet(c))}</strong>
        <span class="doux">— ${esc(c.parti)}</span>
        ${T2 ? (elimine ? '<span class="badge">Non qualifié</span>' : '<span class="badge qualifie">Qualifié au second tour</span>') : ""}
        <br><em>${esc(c.slogan || "")}</em>
      </a>`;
    }).join("");
  }

  function vueCandidat(id) {
    const c = candParId[id];
    if (!c) return "<p>Candidat introuvable.</p>";
    const pos = Object.fromEntries(D.positions.filter((p) => p.candidat === id).map((p) => [p.mesure, p]));
    const sections = themes.map((t) => `
      <h2 class="th titre-theme" ${thStyle(t)}>${esc(t.icone)} ${esc(t.nom)}</h2>
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
      ${sections}
      <div class="actions">
        <a class="btn secondaire" href="#/candidats">← Tous les candidats</a>
        ${nbRepondues() ? '<a class="btn" href="#/resultats">Voir mes résultats</a>' : ""}
      </div>`;
  }

  function vueMethode() {
    return `
      <span class="surtitre">Transparence</span>
      <h1>Comment est calculé votre résultat&nbsp;?</h1>
      <p class="chapo">En résumé : pour chaque mesure, on regarde si le candidat pense comme vous.
        On additionne les points, en donnant plus de poids à ce qui compte pour vous, puis on traduit le total en pourcentage.</p>

      <h2>1. Chaque mesure rapporte ou fait perdre des points</h2>
      <p>On compare votre avis à la position du candidat. Les mesures pour lesquelles vous avez répondu « Indifférent » ne comptent pas.</p>
      <div class="carte"><table class="methode">
        <thead><tr><th>Votre avis</th><th>Le candidat soutient</th><th>Soutient en partie</th><th>Ne se prononce pas</th><th>S'oppose</th></tr></thead>
        <tbody>
          <tr><th>Je soutiens</th><td class="ok">+1 point<br><small>d'accord</small></td><td class="ok">+½ point<br><small>plutôt d'accord</small></td><td>0 point</td><td class="ko">−1 point<br><small>en désaccord</small></td></tr>
          <tr><th>Je m'oppose</th><td class="ko">−1 point<br><small>en désaccord</small></td><td class="ko">−½ point<br><small>plutôt en désaccord</small></td><td>0 point</td><td class="ok">+1 point<br><small>d'accord</small></td></tr>
        </tbody></table></div>

      <h2>2. Ce qui compte pour vous pèse plus lourd</h2>
      <p><strong>C'est facultatif.</strong> Vous n'êtes pas obligé de choisir des thèmes prioritaires ni de marquer des mesures essentielles.
        Sans ces choix, toutes les mesures comptent de la même façon (poids 1).</p>
      <ul class="liste">
        <li>Une mesure d'un <strong>thème prioritaire</strong> compte <strong>2 fois</strong>.</li>
        <li>Une mesure marquée <strong>★ essentielle</strong> compte <strong>3 fois</strong>.</li>
        <li>Les deux se cumulent : une mesure essentielle d'un thème prioritaire compte <strong>6 fois</strong>.</li>
      </ul>

      <h2>3. Le total devient un pourcentage</h2>
      <p>On compare les points obtenus au maximum possible (accord total sur toutes vos mesures), puis on place le résultat sur une échelle de 0 à 100 % :</p>
      <ul class="liste">
        <li><strong>100 %</strong> : le candidat est d'accord avec vous sur tout ;</li>
        <li><strong>50 %</strong> : autant d'accords que de désaccords, ou aucune position connue ;</li>
        <li><strong>0 %</strong> : le candidat est en désaccord avec vous sur tout.</li>
      </ul>

      <h2>Un exemple</h2>
      <div class="carte">
        <p>Vous avez donné votre avis sur trois mesures, et la santé est un de vos thèmes prioritaires.</p>
        <table class="methode">
          <thead><tr><th>Mesure</th><th>Vous</th><th>Le candidat</th><th>Poids</th><th>Points</th></tr></thead>
          <tbody>
            <tr><td>Recruter des soignants <small>(santé, ★ essentielle)</small></td><td>Pour</td><td>Soutient</td><td>2 × 3 = 6</td><td class="ok">+1 × 6 = +6</td></tr>
            <tr><td>Augmenter le SMIC</td><td>Pour</td><td>Soutient en partie</td><td>1</td><td class="ok">+½ × 1 = +0,5</td></tr>
            <tr><td>Taxer le kérosène</td><td>Contre</td><td>Soutient</td><td>1</td><td class="ko">−1 × 1 = −1</td></tr>
            <tr><th colspan="3">Total</th><th>8 (maximum possible)</th><th>+5,5</th></tr>
          </tbody></table>
        <p>Le candidat obtient 5,5 points sur 8 possibles. Sur l'échelle de 0 à 100 %, cela donne <strong>84,4 %</strong> de concordance.</p>
        <p class="doux"><small>Pour les curieux : le total va de −8 (désaccord sur tout) à +8 (accord sur tout).
          On ramène cet intervalle à 0–100 % : (5,5 + 8) ÷ 16 × 100 = 84,4 %.</small></p>
      </div>

      <h2>Deux indicateurs pour bien lire le résultat</h2>
      <ul class="liste">
        <li><strong>La couverture</strong> : la part de vos mesures sur lesquelles le candidat a une position connue.
          Une couverture faible signifie que le score repose sur peu d'éléments : à prendre avec prudence.</li>
        <li><strong>Ex æquo</strong> : quand deux candidats ont moins de ${Score.SEUIL_EX_AEQUO} points d'écart, ils sont signalés comme ex æquo.
          La différence n'est alors pas significative.</li>
      </ul>

      <h2>D'où viennent les positions&nbsp;?</h2>
      <p>En priorité du site officiel et du programme de chaque candidat. Chaque position est accompagnée de sa source, que vous pouvez consulter.
        Une position tirée seulement de la presse ou d'une interview est marquée « à confirmer ».</p>
      <p class="doux">Ce résultat est un éclairage, pas une consigne de vote. Il ne remplace pas la lecture des programmes.</p>
      ${boutonsBasDePage()}`;
  }

  function vueAide() {
    const q = (titre, corps) => `<details class="carte faq"><summary>${titre}</summary>${corps}</details>`;
    return `
      <span class="surtitre">Aide</span>
      <h1>Questions fréquentes</h1>
      <p class="chapo">Astuce : survolez un bouton avec la souris (ou touchez-le longuement) pour afficher une bulle d'aide.</p>

      <h2>Utiliser le comparateur</h2>
      ${q("Comment ça marche, en bref ?", `<ol class="liste">
        <li>Choisissez éventuellement vos <strong>thèmes prioritaires</strong> : ils comptent double.</li>
        <li>Pour chaque mesure, cliquez sur <strong>Je soutiens</strong>, <strong>Je m'oppose</strong> ou <strong>Indifférent</strong>.
          Ajoutez l'étoile <strong>★ Essentielle</strong> aux mesures qui comptent le plus (×3).</li>
        <li>Consultez vos <strong>résultats</strong> : le classement des candidats et le détail par thème.</li></ol>`)}
      ${q("Dois-je répondre à toutes les mesures ?", `<p>Non. Vous pouvez passer des mesures ou des thèmes entiers.
        Seules les mesures où vous avez dit « Je soutiens » ou « Je m'oppose » comptent. Plus vous répondez, plus le résultat est fiable.</p>`)}
      ${q("Comment reprendre plus tard ?", `<p>Vos réponses sont gardées dans ce navigateur. Revenez sur l'<a href="#/">accueil</a> et cliquez sur
        <strong>▶ Poursuivre</strong> : vous reprendrez au premier thème non terminé.</p>`)}
      ${q("Comment tout recommencer ?", `<p>Sur l'<a href="#/">accueil</a> ou en bas du questionnaire, cliquez sur <strong>↺ Recommencer à zéro</strong>.
        Toutes vos réponses et vos thèmes prioritaires sont effacés.</p>`)}
      ${q("Comment lire mes résultats ?", `<ul class="liste">
        <li><strong>Le pourcentage</strong> : 100 % = d'accord sur tout, 50 % = autant d'accords que de désaccords, 0 % = en désaccord sur tout.</li>
        <li><strong>La couverture</strong> : la part de vos mesures sur lesquelles le candidat a une position connue. Faible couverture = prudence.</li>
        <li><strong>Ex æquo</strong> : moins de ${Score.SEUIL_EX_AEQUO} points d'écart, la différence n'est pas significative.</li>
        <li>Cliquez sur <strong>Détail</strong> pour voir accords, désaccords et mesures sans position, classés par thème, avec leurs sources.</li></ul>
        <p>Le calcul complet est expliqué dans la page <a href="#/methode">Méthode</a>.</p>`)}
      ${q("Comment imprimer ou enregistrer mes résultats en PDF ?", `<p>Sur la page de résultats, cliquez sur <strong>Imprimer / PDF</strong>,
        puis choisissez « Enregistrer au format PDF » comme imprimante.</p>`)}

      <h2>Vie privée</h2>
      ${q("Mes réponses sont-elles envoyées quelque part ?", `<p><strong>Non.</strong> Tout le calcul se fait dans votre navigateur.
        Aucune réponse n'est envoyée sur internet : pas de compte, pas de cookie, pas de statistiques.
        Vos réponses sont seulement enregistrées dans ce navigateur pour que vous puissiez reprendre plus tard.</p>`)}
      ${q("Comment effacer toute trace sur cet ordinateur ?", `<p>Cliquez sur <strong>↺ Recommencer à zéro</strong>.
        Pour effacer aussi les données modifiées dans le mode Édition, utilisez <strong>Revenir au pack embarqué</strong> (voir plus bas).
        Vous pouvez aussi effacer les données du site dans les réglages de votre navigateur.</p>`)}
      ${q("Puis-je l'utiliser sans internet ?", `<p>Oui. Téléchargez l'archive ZIP, décompressez-la, puis double-cliquez sur <code>index.html</code>.
        Seuls les liens « source » vers les sites des candidats demandent une connexion.</p>`)}

      <h2>Données et mode Édition</h2>
      ${q("D'où viennent les positions des candidats ?", `<p>En priorité du site officiel et du programme de chaque candidat.
        Chaque position a un lien « source ». Une position tirée seulement de la presse est marquée « à confirmer ».</p>`)}
      ${q("Les données sont-elles à jour ?", `<p>La date des données est indiquée en bas de l'accueil. Un bandeau vous prévient si elles sont anciennes.
        Les mises à jour sont publiées sous forme de <strong>packs</strong> : un par mois jusqu'en janvier 2027, puis un par semaine jusqu'au scrutin.</p>`)}
      ${q("Comment installer une mise à jour (un pack) ?", `<ol class="liste">
        <li>Téléchargez le fichier <code>donnees-AAAA-MM-JJ.json</code>.</li>
        <li>Ouvrez <a href="#/edition/fichiers">Édition</a>, onglet <strong>Import / export</strong>.</li>
        <li>Dans « Importer un pack », choisissez le fichier, puis confirmez. Une sauvegarde de vos données actuelles est faite automatiquement.</li></ol>`)}
      ${q("Comment revenir aux données d'origine ?", `<p>Ouvrez <a href="#/edition/fichiers">Édition</a>, onglet <strong>Import / export</strong>,
        puis cliquez sur <strong>Revenir au pack embarqué</strong>. Toutes les modifications locales sont abandonnées
        (une sauvegarde est conservée : <strong>Restaurer la sauvegarde</strong> permet d'annuler).</p>`)}
      ${q("Comment corriger une position ou ajouter une mesure ?", `<p>Ouvrez <a href="#/edition/positions">Édition</a>, onglet <strong>Positions</strong>,
        puis cliquez sur la case du candidat et de la mesure. Indiquez la position et sa source, puis enregistrez.
        Pour ajouter une mesure : onglet <strong>Mesures</strong>, bouton <strong>+ Ajouter ici</strong> dans le thème voulu.
        Les éléments modifiés portent la mention « modifié ».</p>`)}
      ${q("Comment sauvegarder ou partager mes modifications ?", `<p>Dans <a href="#/edition/fichiers">Édition › Import / export</a>,
        cliquez sur <strong>Exporter le pack (JSON)</strong>. Pour un tableau lisible dans Excel, utilisez <strong>Exporter les positions (CSV)</strong>.</p>`)}
      ${q("Puis-je l'utiliser en classe ou pour une autre élection ?", `<p>Oui. L'outil est pensé aussi pour un usage pédagogique.
        Avec le mode <a href="#/edition/themes">Édition</a>, un enseignant peut remplacer les thèmes, les mesures et les candidats
        pour simuler une autre élection : délégués de classe, représentants des parents d'élèves, conseil de la vie lycéenne,
        conseil municipal des jeunes…</p>
        <ol class="liste">
          <li>Dans <strong>Thèmes</strong>, <strong>Mesures</strong> et <strong>Candidats</strong>, modifiez ou remplacez les éléments existants.</li>
          <li>Dans <strong>Positions</strong>, indiquez la position de chaque candidat sur chaque mesure (la source peut être sa profession de foi).</li>
          <li>Dans <strong>Import / export</strong>, exportez le pack (JSON) et distribuez-le aux élèves, qui l'importent sur leur poste.</li>
        </ol>
        <p class="doux">Comme rien n'est envoyé sur internet, l'outil peut être utilisé avec des élèves sans collecte de données personnelles.</p>`)}
      ${q("Puis-je essayer avec des candidats fictifs ?", `<p>Oui. Un <strong>pack de démonstration</strong> avec des candidats fictifs est fourni
        dans l'archive téléchargée (dossier <code>exemples</code>, fichier <code>donnees-demo.json</code>).
        Importez-le dans <a href="#/edition/fichiers">Édition › Import / export</a> pour une présentation, une formation ou un usage en classe.
        Pour revenir ensuite aux données réelles : <strong>Revenir au pack embarqué</strong>.</p>`)}
      ${q("J'ai trouvé une erreur, que faire ?", `<p>Notez la mesure, le candidat et la source correcte, puis signalez-la au mainteneur
        (ticket sur le dépôt GitHub du projet). Elle sera corrigée dans le pack suivant.</p>`)}

      <h2>Voter</h2>
      ${q("Quand a lieu l'élection ?", `<p>Premier tour le <strong>dimanche 18 avril 2027</strong>, second tour le <strong>dimanche 2 mai 2027</strong>.</p>`)}
      ${q("Et pour le second tour ?", `<p>Après le premier tour, seuls <strong>deux candidats</strong> restent en lice. L'outil passe alors en <strong>mode second tour</strong> :</p>
        <ul class="liste">
          <li>Un <strong>pack « second tour »</strong> est publié le lendemain du premier tour (19 avril 2027). Installez-le comme toute mise à jour
            (<a href="#/edition/fichiers">Édition › Import / export</a>).</li>
          <li><strong>Vos réponses sont conservées</strong> : inutile de refaire le questionnaire. Vous pouvez toutefois le revoir.</li>
          <li>Les résultats ne comparent plus que les <strong>deux qualifiés</strong>. Un lien permet de revoir aussi tous les candidats du premier tour.</li>
          <li>Dans la liste des candidats, les non-qualifiés apparaissent grisés.</li>
        </ul>
        <p class="doux">Vous pouvez aussi activer ce mode vous-même : <a href="#/edition/candidats">Édition › Candidats</a>,
          section « Mode second tour », choisissez les deux qualifiés puis cochez « Activer ».
          Un écart faible entre les deux reste possible : consultez le détail des accords et désaccords avant de vous décider.</p>`)}
      ${q("Comment vérifier mon inscription ou donner procuration ?", `<p>Inscription :
        <a href="https://www.service-public.fr/particuliers/vosdroits/R16396" target="_blank" rel="noopener noreferrer">service-public.fr</a>.
        Procuration : <a href="https://www.maprocuration.gouv.fr" target="_blank" rel="noopener noreferrer">maprocuration.gouv.fr</a>.</p>`)}
      ${boutonsBasDePage()}`;
  }

  function vueMentions() {
    const lien = (u, t) => (u ? `<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">${esc(t || u)}</a>` : "");
    return `
      <span class="surtitre">Informations</span>
      <h1>Mentions légales</h1>

      <h2>Statut de l'outil</h2>
      <p>« Pour qui voter ? » <strong>n'est pas un outil officiel</strong>. C'est un projet indépendant et bénévole, édité par un particulier.
        Il n'est lié ni à l'État, ni à une administration, ni à un candidat, ni à un parti, et n'accepte aucun financement de leur part.</p>
      <p>Contact et signalement d'erreurs : ${lien(CONFIG.signalement, "tickets du dépôt du projet")}.</p>
      ${EN_LIGNE ? `<p>Hébergement de la démo en ligne : GitHub, Inc., San Francisco, États-Unis (${lien("https://github.com", "github.com")}).</p>` : ""}

      <h2>Limitation de responsabilité</h2>
      <ul class="liste">
        <li>L'outil est une <strong>aide à la réflexion</strong>, fournie à titre informatif. Le résultat <strong>n'est pas une consigne de vote</strong>
          et ne remplace pas la lecture des programmes officiels.</li>
        <li>Les positions sont établies à partir de sources publiques, citées pour chaque position. Elles <strong>peuvent contenir des erreurs,
          être incomplètes ou devenir obsolètes</strong>.</li>
        <li>Le choix des mesures et la <a href="#/methode">méthode de calcul</a> comportent nécessairement une part de simplification.</li>
        <li><strong>Aucune garantie</strong> d'exactitude, d'exhaustivité ou d'actualité n'est donnée. Vous restez <strong>seul responsable de votre vote</strong>.</li>
        <li>Dans les limites permises par la loi, l'éditeur et les contributeurs ne sauraient être tenus responsables des conséquences de l'utilisation de l'outil.</li>
        <li>Les données modifiées ou importées dans le mode Édition, ou diffusées par des tiers, relèvent de la responsabilité de leurs auteurs.</li>
      </ul>

      <h2>Confidentialité</h2>
      <ul class="liste">
        <li>L'outil <strong>ne collecte aucune donnée personnelle</strong> : ni compte, ni cookie, ni traceur, ni mesure d'audience, ni publicité.</li>
        <li>Vos réponses sont enregistrées <strong>uniquement dans votre navigateur</strong>, pour reprendre plus tard. Elles ne sont jamais transmises.
          Effacez-les avec « Recommencer à zéro » ou en effaçant les données du site dans votre navigateur.</li>
        <li>Le lien de partage contient vos réponses dans l'adresse : ne le transmettez qu'à des personnes de confiance.</li>
        <li>Les liens « source » mènent vers des sites tiers, soumis à leurs propres règles.</li>
        ${EN_LIGNE ? "<li>Démo en ligne : l'hébergeur peut enregistrer des données techniques de connexion selon sa propre politique ; l'éditeur n'y a pas accès. Pour une confidentialité totale, utilisez la version téléchargée.</li>" : ""}
      </ul>

      <h2>Licences</h2>
      <ul class="liste">
        <li><strong>Code</strong> : Licence publique de l'Union européenne <strong>EUPL 1.2</strong> (fichier <code>LICENCE</code>).</li>
        <li><strong>Données</strong> (mesures, positions, fiches) : <strong>Creative Commons BY-SA 4.0</strong> (fichier <code>LICENCE-DONNEES</code>).
          Réutilisation libre en citant « Pour qui voter ? » et en partageant dans les mêmes conditions.</li>
        <li>Les courtes citations des programmes restent la propriété de leurs auteurs et sont reproduites au titre du droit de courte citation, avec leur source.</li>
      </ul>
      <p class="doux">Code source : ${lien(CONFIG.depot)} · Données : version ${esc(D.version)}${D.licence ? ` (${esc(D.licence)})` : ""}</p>
      ${boutonsBasDePage()}`;
  }

  // Boutons de fin des pages d'information (Aide, Méthode) : Retour, résultats, questionnaire
  function boutonsBasDePage() {
    const n = nbRepondues();
    return `<div class="actions">
        <button class="btn secondaire" data-action="retour">← Retour</button>
        ${n ? `<a class="btn secondaire" href="#/resultats">Voir mes résultats</a>` : ""}
        ${n
          ? `<a class="btn" href="#/questionnaire/${esc((themes.find((t) => !themeFait(t.id)) || themes[0]).id)}">▶ ${n >= mesuresActives.length ? "Revoir mes réponses" : "Continuer le questionnaire"}</a>`
          : `<a class="btn" href="#/priorites">▶ Commencer le questionnaire</a>`}
      </div>`;
  }

  // ---------- Accessibilité : titre de l'onglet et annonce de la page ----------
  function annoncerPage() {
    const h1 = app.querySelector("h1");
    const titre = h1 ? h1.textContent.trim() : "Accueil";
    document.title = `${titre} — Pour qui voter ? 2027`;
    const a = document.getElementById("annonce-page");
    if (a) a.textContent = titre;
  }
  document.getElementById("aller-contenu")?.addEventListener("click", () => app.focus());

  // ---------- Routage ----------
  function rendre() {
    const [, route, param] = (location.hash || "#/").split("/");
    if (route === "edition" && EN_LIGNE) {
      app.innerHTML = `<span class="surtitre">Mode Édition</span><h1>Indisponible dans la démo en ligne</h1>
        <p>La modification des données se fait uniquement dans la version téléchargée de l'application, installée sur votre ordinateur.</p>
        <div class="actions">
          <a class="btn secondaire" href="#/">Retour à l'accueil</a>
          ${CONFIG.telechargement ? `<a class="btn" href="${esc(CONFIG.telechargement)}" target="_blank" rel="noopener noreferrer">⬇ Télécharger l'application</a>` : ""}
        </div>`;
      annoncerPage();
      return;
    }
    if (route === "edition" && window.Edition) {
      window.Edition.afficher(app, param);
      annoncerPage();
      window.scrollTo(0, 0);
      return;
    }
    // En quittant le mode Édition après des modifications, on recharge pour les prendre en compte
    if (!EN_LIGNE && window.Edition && window.Edition.modifie()) { location.reload(); return; }
    const vues = {
      "": vueAccueil, priorites: vuePriorites, questionnaire: () => vueQuestionnaire(param),
      resultats: () => vueResultats(param), candidats: vueCandidats, candidat: () => vueCandidat(param), methode: vueMethode, aide: vueAide, mentions: vueMentions, partage: () => vuePartage(param),
    };
    app.innerHTML = (vues[route] || vueAccueil)();
    annoncerPage();
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
      // Pour l'impression : détail du premier candidat et tableau par thème dépliés, les autres résumés ;
      // l'état d'affichage est restauré ensuite.
      const etats = [...app.querySelectorAll("details")].map((d) => [d, d.open]);
      etats.forEach(([d]) => (d.open = !!d.closest(".premier") || d.classList.contains("carte")));
      window.print();
      etats.forEach(([d, o]) => (d.open = o));
    } else if (el.dataset.action === "retour") {
      // Revient à la page précédente de l'application, sinon à l'accueil
      location.hash = pagePrecedente && !/^#\/(aide|methode|mentions)/.test(pagePrecedente) ? pagePrecedente : "#/";
    } else if (el.dataset.action === "partager") {
      afficherPartage();
    } else if (el.dataset.action === "copier-partage") {
      const champ = document.getElementById("lien-partage");
      champ.select();
      (navigator.clipboard ? navigator.clipboard.writeText(champ.value) : Promise.reject())
        .then(() => { el.textContent = "✓ Copié"; })
        .catch(() => { document.execCommand && document.execCommand("copy"); el.textContent = "✓ Copié"; });
    } else if (el.dataset.action === "charger-partage") {
      const p = decoderPartage(el.dataset.code);
      if (p) { etat.reponses = p.reponses; etat.prioritaires = p.prioritaires; sauver(); location.hash = "#/resultats"; }
    } else if (el.dataset.action === "ouvrir-tout") {
      app.querySelectorAll("details").forEach((d) => (d.open = true));
    } else if (el.dataset.action === "effacer") {
      if (confirm("Effacer toutes vos réponses ?")) {
        etat = { reponses: {}, prioritaires: [], ordre: {} };
        sauver();
        if (location.hash === "#/" || location.hash === "") rendre(); else location.hash = "#/";
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
    if (barre) { barre.style.width = pct + "%"; barre.parentElement.setAttribute("aria-valuenow", pct); }
    const t = mesuresActives.find((m) => m.id === id)?.theme;
    const onglet = document.querySelector(`.onglets a[href="#/questionnaire/${t}"]`);
    if (onglet) onglet.classList.toggle("fait", themeFait(t));
  }

  // ---------- Messages civiques de l'en-tête ----------
  const MESSAGES_CIVIQUES = [
    "Voter est un droit, c'est aussi un devoir civique.",
    "N'oubliez pas de vous inscrire sur les listes électorales !",
    "Imaginez un pays décidé sans vous… Votez les 18 avril et 2 mai 2027.",
    "Chaque voix compte : l'abstention ne choisit jamais à votre place.",
    "Absent le jour J ? Pensez à la procuration.",
    "Imaginez que votre voix soit celle qui fait la différence.",
  ];
  function messagesCiviques() {
    const el = document.getElementById("civique-texte");
    if (!el || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    let i = 0;
    setInterval(() => {
      el.classList.add("cache");
      setTimeout(() => {
        i = (i + 1) % MESSAGES_CIVIQUES.length;
        el.textContent = MESSAGES_CIVIQUES[i];
        el.classList.remove("cache");
      }, 400);
    }, 6000);
  }

  // ---------- Lien de partage (F17) ----------
  // Format : prioritaires séparés par « , » puis « | » puis « id:p|c|i[*] » séparés par « ; »
  // (p = pour, c = contre, i = indifférent, * = essentielle). Encodé en base64 « URL ».
  const b64 = (s) => btoa(unescape(encodeURIComponent(s))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  const deb64 = (s) => decodeURIComponent(escape(atob(s.replace(/-/g, "+").replace(/_/g, "/"))));
  function encoderPartage() {
    const rep = Object.entries(etat.reponses)
      .map(([id, r]) => `${id}:${r.avis === 1 ? "p" : r.avis === -1 ? "c" : "i"}${r.essentielle ? "*" : ""}`).join(";");
    return b64(`${etat.prioritaires.join(",")}|${rep}`);
  }
  function decoderPartage(code) {
    try {
      const [prio, rep] = deb64(code).split("|");
      const ids = new Set(D.mesures.map((m) => m.id));
      const reponses = {};
      for (const e of (rep || "").split(";").filter(Boolean)) {
        const [id, v] = e.split(":");
        if (!ids.has(id) || !/^[pci]\*?$/.test(v)) continue; // ignore les mesures inconnues
        reponses[id] = { avis: v[0] === "p" ? 1 : v[0] === "c" ? -1 : 0, essentielle: v.endsWith("*") };
      }
      const prioritaires = (prio || "").split(",").filter((t) => themeParId[t]);
      return { reponses, prioritaires };
    } catch (_) { return null; }
  }
  function afficherPartage() {
    const zone = document.getElementById("zone-partage");
    const lien = location.href.split("#")[0] + "#/partage/" + encoderPartage();
    zone.innerHTML = `<div class="carte partage">
      <h3>🔗 Partager vos réponses</h3>
      <p><strong>⚠️ Attention :</strong> ce lien contient <strong>toutes vos réponses</strong>, donc vos opinions politiques.
        Toute personne qui l'ouvre pourra les voir. Ne le partagez qu'avec des personnes de confiance,
        et évitez les réseaux sociaux publics.</p>
      <p class="doux">Le lien ne passe par aucun serveur : vos réponses sont écrites dans l'adresse elle-même.
        Il fonctionne avec la même version de l'application${location.protocol === "file:" ? " (ici un fichier local : il ne marchera que sur un ordinateur qui a l'application au même emplacement)" : ""}.</p>
      <div class="partage-ligne">
        <input type="text" id="lien-partage" readonly value="${esc(lien)}" aria-label="Lien de partage">
        <button class="btn" data-action="copier-partage">Copier</button>
      </div></div>`;
    zone.scrollIntoView({ behavior: "smooth", block: "center" });
  }
  function vuePartage(code) {
    const p = decoderPartage(code || "");
    if (!p || !Object.keys(p.reponses).length) {
      return `<h1>Lien de partage invalide</h1><p>Ce lien est incomplet ou provient d'une autre version des données.</p>
        <a class="btn" href="#/">Retour à l'accueil</a>`;
    }
    const n = Object.values(p.reponses).filter((r) => r.avis).length;
    const res = Score.calculer(D, p.reponses, p.prioritaires).resultats[0];
    return `<span class="surtitre">Lien de partage</span>
      <h1>Quelqu'un vous a partagé ses réponses</h1>
      <p>Ce lien contient <strong>${n}</strong> avis sur ${mesuresActives.length} mesures${p.prioritaires.length ? ` et ${p.prioritaires.length} thème(s) prioritaire(s)` : ""}.
        ${res ? `Le candidat le plus proche de ces réponses est <strong>${esc(nomComplet(res.candidat))}</strong> (${pct(res.score)}).` : ""}</p>
      ${nbRepondues() ? `<p class="carte">⚠️ Charger ces réponses <strong>remplacera les vôtres</strong> (${nbRepondues()} réponses) sur cet appareil.</p>` : ""}
      <div class="actions">
        <a class="btn secondaire" href="#/">Ne pas charger</a>
        <button class="btn" data-action="charger-partage" data-code="${esc(code)}">Charger et voir les résultats</button>
      </div>`;
  }

  // ---------- Avertissement au démarrage ----------
  const CLE_AVERT = "pqv.avertissement.masque";
  function avertissement() {
    const dlg = document.getElementById("avertissement");
    if (!dlg || typeof dlg.showModal !== "function") return;
    const caseMasquer = document.getElementById("avert-masquer");
    const ouvrir = () => { try { caseMasquer.checked = localStorage.getItem(CLE_AVERT) === "1"; } catch (_) {} dlg.showModal(); };
    dlg.addEventListener("close", () => {
      try { caseMasquer.checked ? localStorage.setItem(CLE_AVERT, "1") : localStorage.removeItem(CLE_AVERT); } catch (_) {}
    });
    document.getElementById("avert-aide").addEventListener("click", () => dlg.close());
    document.getElementById("ouvrir-avertissement").addEventListener("click", ouvrir);
    let masque = false;
    try { masque = localStorage.getItem(CLE_AVERT) === "1"; } catch (_) {}
    if (!masque) ouvrir();
  }

  let pagePrecedente = null; // pour le bouton « Retour » de la page d'aide
  window.addEventListener("hashchange", (e) => {
    const ancien = "#" + (e.oldURL.split("#")[1] || "/");
    if (!/^#\/(aide|methode|mentions)/.test(ancien)) pagePrecedente = ancien;
    rendre();
  });
  avertissement();
  messagesCiviques();
  bandeau();
  rendre();
})();
