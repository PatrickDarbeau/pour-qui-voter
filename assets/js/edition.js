/* Mode Édition local (CDC §4.6, F19 à F21, F27, F36).
 * Les données modifiées sont enregistrées dans le navigateur (localStorage) et
 * remplacent le pack embarqué. Rien n'est envoyé sur le réseau.
 */
(function () {
  "use strict";

  const CLE = "pqv.donnees.v1";
  const CLE_SAUV = "pqv.donnees.sauvegarde.v1";
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const copie = (o) => JSON.parse(JSON.stringify(o));
  const lire = (cle) => { try { return JSON.parse(localStorage.getItem(cle)); } catch (_) { return null; } };
  const ecrire = (cle, v) => {
    try { v === null ? localStorage.removeItem(cle) : localStorage.setItem(cle, JSON.stringify(v)); return true; }
    catch (_) { alert("Impossible d'enregistrer dans le navigateur (stockage plein ou bloqué). Exportez vos données."); return false; }
  };

  let W = null;          // copie de travail
  let modifie = false;   // modifié pendant cette visite du mode Édition
  let selection = null;  // élément en cours d'édition { type, id } ou position { cid, mid }
  let filtreTheme = "";  // filtre de l'onglet Mesures
  const ouverts = new Set(); // sections de thèmes dépliées

  // Démo en ligne : édition d'essai, candidats VERROUILLÉS (liste, fiches et second tour du pack)
  const VERROU = !!window.EN_LIGNE;

  function verrouiller(d) {
    if (!VERROU || !d) return d;
    const ref = window.DONNEES;
    d.candidats = copie(ref.candidats);
    d.second_tour = ref.second_tour ? copie(ref.second_tour) : undefined;
    const ids = new Set(d.candidats.map((c) => c.id));
    d.positions = d.positions.filter((p) => ids.has(p.candidat));
    return d;
  }
  function donneesActives() {
    const d = lire(CLE);
    return d && Array.isArray(d.themes) && Array.isArray(d.positions) ? verrouiller(d) : null;
  }
  function travail() {
    if (!W) W = copie(donneesActives() || window.DONNEES);
    return W;
  }
  function enregistrer() {
    W.origine = "local";
    W.date_modification = new Date().toISOString().slice(0, 10);
    if (ecrire(CLE, W)) modifie = true;
  }
  function nbModifs() {
    const d = donneesActives();
    if (!d) return 0;
    return ["themes", "mesures", "candidats", "positions"].reduce(
      (n, k) => n + d[k].filter((x) => x.modif_local).length, 0);
  }
  const nouvelId = (prefixe) => prefixe + Date.now().toString(36);

  // ---------- Description des champs ----------
  const STATUTS = ["pressenti", "declare", "investi", "qualifie", "retire", "fictif"];
  const TYPES_SOURCE = ["site_officiel", "programme_pdf", "presse", "interview", "vote"];
  const CHAMPS = {
    themes: [
      ["nom", "Nom", "texte", true], ["icone", "Icône (emoji)", "texte"],
      ["couleur", "Couleur", "couleur"], ["ordre", "Ordre d'affichage", "nombre"],
    ],
    mesures: [
      ["theme", "Thème", "theme", true], ["intitule", "Intitulé (neutre)", "texte", true],
      ["description", "Description", "zone"], ["opposee_a", "Mesure opposée", "mesure"],
      ["actif", "Active", "case"],
    ],
    candidats: [
      ["prenom", "Prénom", "texte"], ["nom", "Nom", "texte", true], ["parti", "Parti / mouvement", "texte"],
      ["statut", "Statut", "statut"], ["couleur", "Couleur", "couleur"], ["slogan", "Slogan", "texte"],
      ["date_naissance", "Date de naissance", "date"], ["lieu_naissance", "Lieu de naissance", "texte"],
      ["formation", "Formation", "texte"], ["profession", "Profession", "texte"],
      ["photo", "Photo (chemin, ex. assets/img/candidats/id.jpg)", "texte"], ["wikipedia", "Article Wikipédia", "url"],
      ["biographie", "Biographie", "zone"], ["site_officiel", "Site officiel", "url"],
      ["pages_programme", "Pages programme (une URL par ligne)", "lignes"],
      ["programme_url", "Programme PDF", "url"], ["derniere_collecte", "Dernière collecte", "date"],
    ],
  };
  const LIBELLES = { themes: "Thèmes", mesures: "Mesures", candidats: "Candidats" };
  const NOM_ITEM = {
    themes: (t) => `${t.icone || ""} ${t.nom}`,
    mesures: (m) => m.intitule,
    candidats: (c) => `${c.prenom || ""} ${c.nom}`.trim(),
  };

  function champ(def, item) {
    const [cle, lib, type, requis] = def;
    const v = item[cle];
    const nom = `name="${cle}" id="ed-${cle}"`;
    const req = requis ? "required" : "";
    let html;
    switch (type) {
      case "zone": html = `<textarea ${nom} rows="3">${esc(v)}</textarea>`; break;
      case "lignes": html = `<textarea ${nom} rows="3">${esc((v || []).join("\n"))}</textarea>`; break;
      case "nombre": html = `<input type="number" ${nom} value="${esc(v ?? 0)}">`; break;
      case "couleur": html = `<input type="color" ${nom} value="${esc(/^#[0-9a-f]{6}$/i.test(v || "") ? v : "#1f3a8a")}">`; break;
      case "url": html = `<input type="url" ${nom} value="${esc(v)}" placeholder="https://…">`; break;
      case "date": html = `<input type="date" ${nom} value="${esc(v)}">`; break;
      case "case": html = `<input type="checkbox" ${nom} ${v !== false ? "checked" : ""}>`; break;
      case "theme":
        html = `<select ${nom} ${req}>${W.themes.map((t) => `<option value="${esc(t.id)}" ${t.id === v ? "selected" : ""}>${esc(NOM_ITEM.themes(t))}</option>`).join("")}</select>`; break;
      case "mesure":
        html = `<select ${nom}><option value="">— aucune —</option>${W.mesures.filter((m) => m.id !== item.id)
          .map((m) => `<option value="${esc(m.id)}" ${m.id === v ? "selected" : ""}>${esc(m.intitule)}</option>`).join("")}</select>`; break;
      case "statut":
        html = `<select ${nom}>${STATUTS.map((s) => `<option ${s === v ? "selected" : ""}>${s}</option>`).join("")}</select>`; break;
      default: html = `<input type="text" ${nom} value="${esc(v)}" ${req}>`;
    }
    return `<label class="ed-champ ${type === "case" ? "ed-case" : ""}" for="ed-${cle}"><span>${esc(lib)}${requis ? " *" : ""}</span>${html}</label>`;
  }

  function lireFormulaire(form, type, item) {
    for (const [cle, , t] of CHAMPS[type]) {
      const el = form.elements[cle];
      if (!el) continue;
      if (t === "case") item[cle] = el.checked;
      else if (t === "nombre") item[cle] = Number(el.value) || 0;
      else if (t === "lignes") item[cle] = el.value.split(/\r?\n/).map((s) => s.trim()).filter(Boolean);
      else item[cle] = el.value.trim() || null;
    }
    item.modif_local = true;
  }

  // ---------- Vues ----------
  function onglets(actif) {
    const o = [["themes", "Thèmes"], ["mesures", "Mesures"], ["candidats", "Candidats"],
      ["positions", "Positions"], ["fichiers", "Import / export"]];
    return `<nav class="onglets ed-onglets">${o.map(([k, l]) =>
      `<a href="#/edition/${k}" class="${k === actif ? "actif" : ""}">${l}</a>`).join("")}</nav>`;
  }

  function vueListe(type) {
    const liste = type === "themes" ? [...W.themes].sort((a, b) => a.ordre - b.ordre) : W[type];
    const sel = selection && selection.type === type ? selection : null;
    const item = sel ? (sel.id ? W[type].find((x) => x.id === sel.id) : sel.nouveau) : null;
    const form = item ? `
      <form class="carte ed-form" data-ed-form="${type}">
        <h3>${sel.id ? "Modifier" : "Ajouter"} : ${esc(NOM_ITEM[type](item) || "nouvel élément")}</h3>
        <div class="ed-grille">${CHAMPS[type].map((d) => champ(d, item)).join("")}</div>
        <div class="actions">
          <button type="button" class="btn secondaire" data-ed="annuler">Annuler</button>
          <button type="submit" class="btn">Enregistrer</button>
        </div>
      </form>` : "";
    const ligne = (x) => {
      let info = "";
      if (type === "mesures") info = x.opposee_a ? "↔ mesure opposée liée" : "";
      if (type === "candidats") info = x.parti || "";
      if (type === "themes") info = `${W.mesures.filter((m) => m.theme === x.id).length} mesures`;
      return `<tr>
        <td>${esc(NOM_ITEM[type](x))}${x.modif_local ? ' <span class="badge">modifié</span>' : ""}${x.actif === false ? ' <span class="badge">inactive</span>' : ""}</td>
        <td class="doux">${esc(info)}</td>
        <td class="ed-actions">${VERROU && type === "candidats" ? '<span class="doux">🔒 verrouillé</span>' : `<button class="lien" data-ed="modifier" data-ed-type="${type}" data-ed-id="${esc(x.id)}">Modifier</button>
          <button class="lien ko" data-ed="supprimer" data-ed-type="${type}" data-ed-id="${esc(x.id)}">Supprimer</button>`}</td></tr>`;
    };

    // Mesures : une section déroulante par thème, avec filtre
    if (type === "mesures") {
      const themes = [...W.themes].sort((a, b) => a.ordre - b.ordre);
      const filtre = themes.some((t) => t.id === filtreTheme) ? filtreTheme : "";
      const sections = themes.filter((t) => !filtre || t.id === filtre).map((t) => {
        const ms = liste.filter((m) => m.theme === t.id);
        const coul = /^#[0-9a-f]{3,8}$/i.test(t.couleur || "") ? `style="--c:${t.couleur}"` : "";
        return `<details class="ed-section th" ${coul} ${ouverts.has(t.id) || filtre ? "open" : ""} data-ed-section="${esc(t.id)}">
          <summary><span class="ed-section-titre">${esc(NOM_ITEM.themes(t))}</span>
            <span class="doux">${ms.length} mesure${ms.length > 1 ? "s" : ""}</span>
            <button class="lien" data-ed="ajouter" data-ed-type="mesures" data-ed-theme-cible="${esc(t.id)}">+ Ajouter ici</button></summary>
          ${ms.length ? `<table class="ed-table"><tbody>${ms.map(ligne).join("")}</tbody></table>` : '<p class="doux">Aucune mesure dans ce thème.</p>'}
        </details>`;
      }).join("");
      return `${form}
        <div class="actions ed-barre">
          <label class="ed-filtre">Thème :
            <select data-ed-filtre>${[["", "Tous les thèmes"], ...themes.map((t) => [t.id, NOM_ITEM.themes(t)])]
              .map(([v, l]) => `<option value="${esc(v)}" ${v === filtre ? "selected" : ""}>${esc(l)}</option>`).join("")}</select>
          </label>
          <span class="doux">${liste.length} mesures</span>
          <span><button class="lien" data-ed="tout-ouvrir">Tout déplier</button>
            <button class="lien" data-ed="tout-fermer">Tout replier</button></span>
          <button class="btn" data-ed="ajouter" data-ed-type="mesures">+ Ajouter</button>
        </div>${sections}`;
    }

    // Candidats : réglage du mode second tour (pack, CDC §9 ter)
    let t2 = "";
    if (type === "candidats" && VERROU) {
      return `<p class="carte ed-verrou">🔒 <strong>Candidats verrouillés dans la démo en ligne.</strong>
        Vous pouvez consulter la liste ci-dessous, et modifier thèmes, mesures et positions pour essayer l'outil.
        Pour gérer les candidats, téléchargez l'application.</p>
        <table class="ed-table"><tbody>${liste.map(ligne).join("")}</tbody></table>`;
    }
    if (type === "candidats") {
      const st = W.second_tour || { actif: false, qualifies: [] };
      const sel = (i) => `<select data-ed-t2="${i}"><option value="">— choisir —</option>${W.candidats.map((c) =>
        `<option value="${esc(c.id)}" ${st.qualifies?.[i] === c.id ? "selected" : ""}>${esc(NOM_ITEM.candidats(c))}</option>`).join("")}</select>`;
      t2 = `<section class="carte ed-t2"><h3>🗳 Mode second tour</h3>
        <p class="doux">À activer après le premier tour (18 avril 2027) : les résultats ne compareront plus que les deux candidats qualifiés.</p>
        <div class="ed-grille">
          <label class="ed-champ"><span>Qualifié n° 1</span>${sel(0)}</label>
          <label class="ed-champ"><span>Qualifié n° 2</span>${sel(1)}</label>
          <label class="ed-champ ed-case"><span>Activer le mode second tour</span><input type="checkbox" data-ed-t2="actif" ${st.actif ? "checked" : ""}></label>
        </div></section>`;
    }
    return `${t2}${form}
      <div class="actions"><span class="doux">${liste.length} ${LIBELLES[type].toLowerCase()}</span>
        <button class="btn" data-ed="ajouter" data-ed-type="${type}">+ Ajouter</button></div>
      <table class="ed-table"><tbody>${liste.map(ligne).join("")}</tbody></table>`;
  }

  const SYMBOLE = { "1": "＋", "0.5": "½", "0": "·", "-1": "−" };
  function vuePositions() {
    const idx = {};
    for (const p of W.positions) idx[p.candidat + "|" + p.mesure] = p;
    const themes = [...W.themes].sort((a, b) => a.ordre - b.ordre);
    const entete = W.candidats.map((c) => `<th title="${esc(c.parti)}">${esc(NOM_ITEM.candidats(c))}</th>`).join("");
    const corps = themes.map((t) => {
      const ms = W.mesures.filter((m) => m.theme === t.id);
      if (!ms.length) return "";
      return `<tr class="ed-theme"><th colspan="${W.candidats.length + 1}">${esc(NOM_ITEM.themes(t))}</th></tr>` +
        ms.map((m) => `<tr><th class="ed-mesure">${esc(m.intitule)}</th>${W.candidats.map((c) => {
          const p = idx[c.id + "|" + m.id];
          const v = String(p ? p.valeur : 0);
          const actif = selection && selection.cid === c.id && selection.mid === m.id;
          const manque = p && p.valeur !== 0 && !p.source_url;
          return `<td><button class="ed-cellule v${v.replace(".", "")} ${actif ? "actif" : ""} ${manque ? "manque" : ""} ${p?.a_confirmer ? "aconf" : ""}"
            data-ed="cellule" data-ed-c="${esc(c.id)}" data-ed-m="${esc(m.id)}"
            title="${esc(NOM_ITEM.candidats(c))} — ${esc(m.intitule)}">${SYMBOLE[v]}</button></td>`;
        }).join("")}</tr>`).join("");
    }).join("");

    let detail = `<p class="doux">Cliquez sur une case pour saisir la position et sa source.
      Légende : ＋ soutient · ½ partiellement · · ne se prononce pas · − s'oppose.
      Case barrée de rouge : source manquante ; pointillés : à confirmer.</p>`;
    if (selection && selection.cid) {
      const c = W.candidats.find((x) => x.id === selection.cid);
      const m = W.mesures.find((x) => x.id === selection.mid);
      const p = idx[selection.cid + "|" + selection.mid] || {};
      if (c && m) {
        const opt = (val, lib) => `<option value="${val}" ${String(p.valeur ?? 0) === String(val) ? "selected" : ""}>${lib}</option>`;
        detail = `<form class="carte ed-form" data-ed-form="position">
          <h3>${esc(NOM_ITEM.candidats(c))} — ${esc(m.intitule)}</h3>
          <div class="ed-grille">
            <label class="ed-champ"><span>Position</span><select name="valeur">${opt(1, "Soutient (+1)")}${opt(0.5, "Soutient partiellement (+0,5)")}${opt(0, "Ne se prononce pas (0)")}${opt(-1, "S'oppose (−1)")}</select></label>
            <label class="ed-champ"><span>Type de source</span><select name="source_type">${TYPES_SOURCE.map((s) => `<option ${s === (p.source_type || "site_officiel") ? "selected" : ""}>${s}</option>`).join("")}</select></label>
            <label class="ed-champ"><span>URL de la source</span><input type="url" name="source_url" value="${esc(p.source_url)}" placeholder="https://…"></label>
            <label class="ed-champ"><span>Date de consultation</span><input type="date" name="source_date" value="${esc(p.source_date || new Date().toISOString().slice(0, 10))}"></label>
            <label class="ed-champ ed-large"><span>Citation courte</span><textarea name="citation" rows="2">${esc(p.citation)}</textarea></label>
            <label class="ed-champ ed-case"><span>À confirmer</span><input type="checkbox" name="a_confirmer" ${p.a_confirmer ? "checked" : ""}></label>
          </div>
          <div class="actions"><button type="button" class="btn secondaire" data-ed="annuler">Fermer</button>
            <button type="submit" class="btn">Enregistrer la position</button></div>
        </form>`;
      }
    }
    return `${detail}<div class="ed-defil-haut" aria-hidden="true"><div></div></div><div class="ed-matrice"><table><thead><tr><th></th>${entete}</tr></thead><tbody>${corps}</tbody></table></div>`;
  }

  function vueFichiers() {
    const sauv = lire(CLE_SAUV);
    const local = donneesActives();
    if (enAttente) return vueImport();
    return `
      <section class="carte"><h3>Exporter</h3>
        <p class="doux">Enregistrez vos données dans un fichier pour les conserver, les partager ou les proposer au mainteneur.</p>
        <div class="actions" style="justify-content:flex-start">
          <button class="btn" data-ed="export-json">Exporter le pack (JSON)</button>
          <button class="btn secondaire" data-ed="export-csv">Exporter les positions (CSV)</button>
        </div></section>
      ${VERROU ? `<section class="carte ed-verrou"><h3>Importer un pack</h3>
        <p>🔒 Indisponible dans la démo en ligne. Téléchargez l'application pour importer des packs de données.</p></section>` : `
      <section class="carte"><h3>Importer un pack</h3>
        <p class="doux">Choisissez un fichier <code>donnees-AAAA-MM-JJ.json</code>. Avant tout remplacement, vous verrez
          les changements, l'empreinte du fichier et le sort de vos modifications locales. Une sauvegarde est faite automatiquement.</p>
        <input type="file" accept=".json,application/json" data-ed-fichier>
      </section>`}
      <section class="carte"><h3>Revenir en arrière</h3>
        <div class="actions" style="justify-content:flex-start">
          ${VERROU ? "" : `<button class="btn secondaire" data-ed="restaurer" ${sauv ? "" : "disabled"}>Restaurer la sauvegarde${sauv ? ` (${esc(sauv.version)})` : ""}</button>`}
          <button class="btn secondaire" data-ed="reinitialiser" ${local ? "" : "disabled"}>Revenir au pack embarqué (${esc(window.DONNEES.version)})</button>
        </div></section>`;
  }

  function afficher(app, onglet) {
    travail();
    onglet = onglet || "mesures";
    const etat = (VERROU ? `<p class="bandeau-ed ed-verrou">🧪 <strong>Mode essai (démo en ligne).</strong> Vous pouvez modifier thèmes, mesures et positions
        pour découvrir l'outil ; vos essais restent dans ce navigateur. Les candidats sont verrouillés. Pour revenir aux données d'origine :
        Import / export › Revenir au pack embarqué.</p>` : "") + (donneesActives()
      ? `<p class="bandeau-ed">Données modifiées localement — ${nbModifs()} élément(s) modifié(s).</p>`
      : `<p class="bandeau-ed doux">Données du pack ${esc(W.version)}. Toute modification sera enregistrée dans ce navigateur.</p>`);
    let corps;
    if (onglet === "positions") corps = vuePositions();
    else if (onglet === "fichiers") corps = vueFichiers();
    else corps = vueListe(CHAMPS[onglet] ? onglet : "mesures");
    app.innerHTML = `<span class="surtitre">Mode Édition</span><h1>Gérer les données</h1>${etat}${onglets(onglet)}${corps}`;
    app.dataset.edOnglet = onglet;
    lierDefilement(app);
  }

  // Ascenseur horizontal au-dessus du tableau des positions, synchronisé avec celui du tableau
  function lierDefilement(app) {
    const haut = app.querySelector(".ed-defil-haut"), mat = app.querySelector(".ed-matrice");
    if (!haut || !mat) return;
    const ajuster = () => {
      haut.firstElementChild.style.width = mat.scrollWidth + "px";
      haut.hidden = mat.scrollWidth <= mat.clientWidth + 1;
    };
    ajuster();
    new ResizeObserver(ajuster).observe(mat);
    let source = null;
    haut.addEventListener("scroll", () => { if (source !== mat) { source = haut; mat.scrollLeft = haut.scrollLeft; } source = null; });
    mat.addEventListener("scroll", () => { if (source !== haut) { source = mat; haut.scrollLeft = mat.scrollLeft; } source = null; });
  }
  const rafraichir = () => afficher(document.getElementById("app"), document.getElementById("app").dataset.edOnglet);

  // ---------- Import / export ----------
  function telecharger(nom, contenu, type) {
    const url = URL.createObjectURL(new Blob([contenu], { type }));
    const a = Object.assign(document.createElement("a"), { href: url, download: nom });
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function csvPositions() {
    const q = (s) => `"${String(s ?? "").replace(/"/g, '""')}"`;
    const lignes = [["candidat", "mesure", "theme", "intitule", "valeur", "source_type", "source_url", "source_date", "a_confirmer", "citation"].join(";")];
    for (const p of W.positions) {
      const m = W.mesures.find((x) => x.id === p.mesure) || {};
      const c = W.candidats.find((x) => x.id === p.candidat) || {};
      lignes.push([NOM_ITEM.candidats(c), p.mesure, m.theme, m.intitule, String(p.valeur).replace(".", ","),
        p.source_type, p.source_url, p.source_date, p.a_confirmer ? "oui" : "non", p.citation].map(q).join(";"));
    }
    return "﻿" + lignes.join("\r\n"); // BOM pour Excel
  }
  function verifierPack(p) {
    const erreurs = [];
    for (const k of ["themes", "mesures", "candidats", "positions"]) if (!Array.isArray(p[k])) erreurs.push(`« ${k} » manquant`);
    if (erreurs.length) return erreurs;
    const ids = (l) => new Set(l.map((x) => x.id));
    const t = ids(p.themes), m = ids(p.mesures), c = ids(p.candidats);
    p.mesures.forEach((x) => { if (!t.has(x.theme)) erreurs.push(`mesure ${x.id} : thème inconnu`); });
    p.positions.forEach((x) => {
      if (!c.has(x.candidat) || !m.has(x.mesure)) erreurs.push(`position ${x.candidat}/${x.mesure} : référence inconnue`);
      if (![-1, 0, 0.5, 1].includes(x.valeur)) erreurs.push(`position ${x.candidat}/${x.mesure} : valeur invalide`);
    });
    return erreurs.slice(0, 10);
  }

  // ---------- Événements ----------
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-ed]");
    if (!b || !document.getElementById("app").contains(b)) return;
    const act = b.dataset.ed, type = b.dataset.edType, id = b.dataset.edId;
    // Verrou de la démo en ligne : aucune action sur les candidats, pas d'import ni de restauration
    if (VERROU && (type === "candidats" || act === "restaurer")) return;
    if (act === "modifier") selection = { type, id };
    else if (act === "ajouter") {
      const n = { id: nouvelId(type.slice(0, 1)) };
      if (type === "themes") Object.assign(n, { nom: "", icone: "", couleur: "#1f3a8a", ordre: W.themes.length });
      if (type === "mesures") Object.assign(n, { theme: b.dataset.edThemeCible || filtreTheme || W.themes[0]?.id, intitule: "", actif: true });
      e.preventDefault(); // bouton placé dans un <summary> : ne pas replier la section
      if (type === "candidats") Object.assign(n, { nom: "", statut: "declare", pages_programme: [] });
      selection = { type, nouveau: n };
    } else if (act === "annuler") selection = null;
    else if (act === "tout-ouvrir") W.themes.forEach((t) => ouverts.add(t.id));
    else if (act === "tout-fermer") ouverts.clear();
    else if (act === "supprimer") {
      const item = W[type].find((x) => x.id === id);
      if (type === "themes" && W.mesures.some((m) => m.theme === id)) { alert("Ce thème contient des mesures : supprimez-les ou déplacez-les d'abord."); return; }
      if (!confirm(`Supprimer « ${NOM_ITEM[type](item)} » ? Les positions associées seront aussi supprimées.`)) return;
      W[type] = W[type].filter((x) => x.id !== id);
      if (type === "mesures") {
        W.positions = W.positions.filter((p) => p.mesure !== id);
        W.mesures.forEach((m) => { if (m.opposee_a === id) m.opposee_a = null; });
      }
      if (type === "candidats") W.positions = W.positions.filter((p) => p.candidat !== id);
      selection = null; enregistrer();
    } else if (act === "cellule") selection = { cid: b.dataset.edC, mid: b.dataset.edM };
    else if (act === "export-json") {
      const pack = copie(W); pack.origine = donneesActives() ? "local" : pack.origine;
      telecharger(`donnees-${new Date().toISOString().slice(0, 10)}.json`, JSON.stringify(pack, null, 2), "application/json");
      return;
    } else if (act === "export-csv") { telecharger("positions.csv", csvPositions(), "text/csv;charset=utf-8"); return; }
    else if (act === "restaurer") {
      if (!confirm("Remplacer les données actuelles par la sauvegarde ?")) return;
      W = lire(CLE_SAUV); ecrire(CLE, W); modifie = true;
    } else if (act === "reinitialiser") {
      if (!confirm("Abandonner toutes les modifications locales et revenir au pack embarqué ?")) return;
      ecrire(CLE_SAUV, donneesActives()); ecrire(CLE, null); W = copie(window.DONNEES); modifie = true;
    } else return;
    rafraichir();
  });

  document.addEventListener("submit", (e) => {
    const f = e.target.closest("[data-ed-form]");
    if (!f) return;
    e.preventDefault();
    const type = f.dataset.edForm;
    if (type === "position") {
      const { cid, mid } = selection;
      let p = W.positions.find((x) => x.candidat === cid && x.mesure === mid);
      if (!p) { p = { candidat: cid, mesure: mid }; W.positions.push(p); }
      Object.assign(p, {
        valeur: Number(f.elements.valeur.value), source_type: f.elements.source_type.value,
        source_url: f.elements.source_url.value.trim() || null, source_date: f.elements.source_date.value || null,
        citation: f.elements.citation.value.trim() || null, a_confirmer: f.elements.a_confirmer.checked, modif_local: true,
      });
      if (p.valeur !== 0 && !p.source_url && !confirm("Aucune source indiquée : la position sera signalée comme incomplète. Continuer ?")) return;
    } else {
      const item = selection.nouveau || W[type].find((x) => x.id === selection.id);
      lireFormulaire(f, type, item);
      if (selection.nouveau) W[type].push(item);
    }
    selection = null; enregistrer(); rafraichir();
  });

  // Mémorise les sections dépliées et le filtre de thème
  document.addEventListener("toggle", (e) => {
    const d = e.target;
    if (!d.dataset || !d.dataset.edSection) return;
    d.open ? ouverts.add(d.dataset.edSection) : ouverts.delete(d.dataset.edSection);
  }, true);
  document.addEventListener("change", (e) => {
    if (e.target.matches("[data-ed-filtre]")) { filtreTheme = e.target.value; rafraichir(); return; }
    if (e.target.matches("[data-ed-t2]") && !VERROU) {
      const st = W.second_tour || (W.second_tour = { actif: false, qualifies: ["", ""] });
      const k = e.target.dataset.edT2;
      if (k === "actif") st.actif = e.target.checked; else st.qualifies[Number(k)] = e.target.value;
      if (st.actif && (st.qualifies.filter(Boolean).length !== 2 || st.qualifies[0] === st.qualifies[1])) {
        alert("Choisissez deux candidats différents avant d'activer le mode second tour.");
        st.actif = false; rafraichir(); return;
      }
      enregistrer();
    }
  });

  document.addEventListener("change", (e) => {
    const inp = e.target.closest("[data-ed-fichier]");
    if (!inp || !inp.files[0]) return;
    const r = new FileReader();
    const nomFichier = inp.files[0].name;
    r.onload = async () => {
      let pack;
      try { pack = JSON.parse(r.result); } catch (_) { alert("Fichier illisible : ce n'est pas un JSON valide."); return; }
      const err = verifierPack(pack);
      if (err.length) { alert("Pack refusé (F34) :\n- " + err.join("\n- ")); return; }
      enAttente = preparerImport(pack, await empreinte(r.result), nomFichier);
      rafraichir();
    };
    r.readAsText(inp.files[0], "utf-8");
  });

  // ---------- Import d'un pack : aperçu, version, empreinte, fusion (F30, F33 à F37) ----------
  let enAttente = null;

  async function empreinte(texte) {
    try {
      const h = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(texte));
      return [...new Uint8Array(h)].map((b) => b.toString(16).padStart(2, "0")).join("");
    } catch (_) { return null; } // crypto.subtle indisponible dans ce contexte
  }

  const CLES = {
    themes: (x) => x.id, mesures: (x) => x.id, candidats: (x) => x.id,
    positions: (x) => x.candidat + "|" + x.mesure,
  };
  const LIB = { themes: "Thème", mesures: "Mesure", candidats: "Candidat", positions: "Position" };
  const egal = (a, b) => {
    const net = (o) => JSON.stringify(Object.keys(o).filter((k) => k !== "modif_local").sort().map((k) => [k, o[k]]));
    return net(a) === net(b);
  };

  function libelle(type, x, ref) {
    if (type === "positions") {
      const c = ref.candidats.find((y) => y.id === x.candidat);
      const m = ref.mesures.find((y) => y.id === x.mesure);
      return `${c ? NOM_ITEM.candidats(c) : x.candidat} / ${m ? m.intitule : x.mesure}`;
    }
    return NOM_ITEM[type](x);
  }

  function preparerImport(pack, sha, nomFichier) {
    const actuel = donneesActives() || window.DONNEES;
    const changements = [];
    const conflits = [];
    for (const type of Object.keys(CLES)) {
      const k = CLES[type];
      const a = new Map(actuel[type].map((x) => [k(x), x]));
      const n = new Map(pack[type].map((x) => [k(x), x]));
      for (const [cle, x] of n) {
        if (!a.has(cle)) changements.push(["ajout", `${LIB[type]} ajouté(e) : ${libelle(type, x, pack)}`]);
        else if (!egal(a.get(cle), x)) {
          const av = a.get(cle);
          const detail = type === "positions" ? ` : ${av.valeur} → ${x.valeur}` : "";
          changements.push(["modif", `${LIB[type]} modifié(e) : ${libelle(type, x, pack)}${detail}`]);
        }
      }
      for (const [cle, x] of a) if (!n.has(cle)) changements.push(["retrait", `${LIB[type]} retiré(e) : ${libelle(type, x, actuel)}`]);
      // Modifications locales (F36, F37) qui seraient perdues
      for (const [cle, x] of a) {
        if (!x.modif_local) continue;
        if (n.has(cle) && egal(n.get(cle), x)) continue; // le pack contient déjà la même chose
        conflits.push({ type, cle, local: x, officiel: n.get(cle) || null, libelle: libelle(type, x, actuel) });
      }
    }
    const versionActuelle = actuel.version || "";
    return {
      pack, sha, nomFichier, changements, conflits,
      choix: Object.fromEntries(conflits.map((c) => [c.type + ":" + c.cle, "local"])),
      plusAncien: (pack.version || "") < versionActuelle, versionActuelle,
    };
  }

  function vueImport() {
    const p = enAttente;
    const icone = { ajout: "＋", modif: "✎", retrait: "−" };
    const MAX = 60;
    const liste = p.changements.slice(0, MAX).map(([t, txt]) => `<li class="chg-${t}"><span>${icone[t]}</span> ${esc(txt)}</li>`).join("");
    const nb = (t) => p.changements.filter((c) => c[0] === t).length;
    const conflits = p.conflits.map((c) => {
      const id = c.type + ":" + c.cle;
      const r = (v, txt) => `<label><input type="radio" name="${esc(id)}" value="${v}" data-ed-choix="${esc(id)}" ${p.choix[id] === v ? "checked" : ""}> ${txt}</label>`;
      return `<tr><td>${esc(LIB[c.type])} : ${esc(c.libelle)}${c.officiel ? "" : ' <span class="badge">ajout local</span>'}</td>
        <td class="ed-choix">${r("local", "Garder ma version")} ${r("officiel", c.officiel ? "Prendre la version du pack" : "Supprimer")}</td></tr>`;
    }).join("");
    return `<section class="carte import">
      <h3>Aperçu de l'import</h3>
      <table class="import-infos"><tbody>
        <tr><th>Fichier</th><td>${esc(p.nomFichier)}</td></tr>
        <tr><th>Version</th><td>${esc(p.pack.version || "?")} du ${esc(p.pack.date || "?")}
          ${p.pack.origine === "officiel" ? '<span class="badge">pack officiel</span>' : '<span class="badge">pack local</span>'}
          ${p.pack.demo ? '<span class="badge">démonstration</span>' : ""}</td></tr>
        <tr><th>Contenu</th><td>${p.pack.candidats.length} candidats, ${p.pack.mesures.length} mesures, ${p.pack.positions.length} positions</td></tr>
        <tr><th>Empreinte SHA-256</th><td><code class="sha">${p.sha ? esc(p.sha) : "indisponible dans ce navigateur"}</code><br>
          <small class="doux">Comparez-la avec l'empreinte publiée à côté du pack : si elles sont identiques, le fichier n'a pas été modifié.</small></td></tr>
      </tbody></table>
      ${p.plusAncien ? `<p class="alerte">⚠️ Ce pack (${esc(p.pack.version)}) est <strong>plus ancien</strong> que vos données actuelles (${esc(p.versionActuelle)}).
        <label><input type="checkbox" data-ed-forcer> Je veux quand même l'importer</label></p>` : ""}
      <h4>Changements par rapport à vos données (${p.changements.length})</h4>
      <p class="doux">＋ ${nb("ajout")} ajout(s) · ✎ ${nb("modif")} modification(s) · − ${nb("retrait")} retrait(s)</p>
      ${p.changements.length ? `<ul class="changements">${liste}</ul>${p.changements.length > MAX ? `<p class="doux">… et ${p.changements.length - MAX} autre(s).</p>` : ""}` : "<p>Aucun changement : vos données sont déjà identiques.</p>"}
      ${p.conflits.length ? `<h4>Vos modifications locales (${p.conflits.length})</h4>
        <p class="doux">Ces éléments ont été modifiés ou ajoutés sur cet ordinateur. Choisissez pour chacun.</p>
        <p><button class="lien" data-ed="choix-tous" data-v="local">Tout garder</button> · <button class="lien" data-ed="choix-tous" data-v="officiel">Tout prendre du pack</button></p>
        <table class="ed-table"><tbody>${conflits}</tbody></table>` : ""}
      <div class="actions">
        <button class="btn secondaire" data-ed="import-annuler">Annuler</button>
        <button class="btn" data-ed="import-valider">Importer (sauvegarde automatique)</button>
      </div></section>`;
  }

  function appliquerImport() {
    const p = enAttente;
    if (p.plusAncien && !document.querySelector("[data-ed-forcer]")?.checked) {
      alert("Ce pack est plus ancien que vos données : cochez la case pour confirmer l'import.");
      return;
    }
    const final = copie(p.pack);
    let gardes = 0;
    for (const c of p.conflits) {
      if (p.choix[c.type + ":" + c.cle] !== "local") continue;
      const k = CLES[c.type];
      const i = final[c.type].findIndex((x) => k(x) === c.cle);
      const local = Object.assign(copie(c.local), { modif_local: true });
      if (i >= 0) final[c.type][i] = local; else final[c.type].push(local);
      gardes++;
    }
    // Une position gardée doit toujours pointer vers un candidat et une mesure existants
    const ids = (l) => new Set(l.map((x) => x.id));
    const cs = ids(final.candidats), ms = ids(final.mesures);
    final.positions = final.positions.filter((x) => cs.has(x.candidat) && ms.has(x.mesure));
    if (gardes) final.origine = "local";
    ecrire(CLE_SAUV, donneesActives() || window.DONNEES);
    W = final; ecrire(CLE, W); modifie = true; selection = null; enAttente = null;
    rafraichir();
    alert(`Pack ${p.pack.version || ""} importé${gardes ? ` (${gardes} modification(s) locale(s) conservée(s))` : ""}. Une sauvegarde des données précédentes est disponible.`);
  }

  document.addEventListener("change", (e) => {
    const r = e.target.closest("[data-ed-choix]");
    if (r && enAttente) enAttente.choix[r.dataset.edChoix] = r.value;
  });
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-ed]");
    if (!b || !enAttente) return;
    if (b.dataset.ed === "import-annuler") { enAttente = null; rafraichir(); }
    else if (b.dataset.ed === "import-valider") appliquerImport();
    else if (b.dataset.ed === "choix-tous") {
      Object.keys(enAttente.choix).forEach((k) => (enAttente.choix[k] = b.dataset.v));
      rafraichir();
    }
  });

  window.Edition = { donneesActives, afficher, modifie: () => modifie, nbModifs };
})();
