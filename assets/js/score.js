/* Calcul de concordance (CDC §4.4, F13 à F16).
 * Module sans dépendance, utilisable dans le navigateur (window.Score) et sous Node (tests).
 *
 * reponses : { [mesureId]: { avis: 1 | -1 | 0, essentielle: bool } }
 * prioritaires : Set ou tableau d'identifiants de thèmes (poids ×2)
 */
(function (global) {
  "use strict";

  const SEUIL_EX_AEQUO = 2; // points de pourcentage

  function poidsMesure(mesure, rep, prioritaires) {
    let p = 1;
    if (prioritaires.has(mesure.theme)) p *= 2;
    if (rep.essentielle) p *= 3;
    return p;
  }

  function indexPositions(donnees) {
    const idx = {};
    for (const p of donnees.positions) {
      (idx[p.candidat] = idx[p.candidat] || {})[p.mesure] = p;
    }
    return idx;
  }

  function calculer(donnees, reponses, prioritaires, candidatsRetenus) {
    prioritaires = new Set(prioritaires || []);
    const idx = indexPositions(donnees);
    const mesures = donnees.mesures.filter(
      (m) => m.actif !== false && reponses[m.id] && reponses[m.id].avis !== 0
    );
    const candidats = donnees.candidats.filter(
      (c) => !candidatsRetenus || candidatsRetenus.includes(c.id)
    );

    const resultats = candidats.map((c) => {
      let num = 0, den = 0, exprimees = 0;
      const accords = [], desaccords = [], silences = [];
      const parTheme = {};
      for (const m of mesures) {
        const rep = reponses[m.id];
        const pos = (idx[c.id] || {})[m.id];
        const val = pos ? pos.valeur : 0;
        const w = poidsMesure(m, rep, prioritaires);
        const accord = rep.avis * val; // de -1 à +1
        num += w * accord;
        den += w;
        const t = (parTheme[m.theme] = parTheme[m.theme] || { num: 0, den: 0 });
        t.num += w * accord;
        t.den += w;
        const item = { mesure: m, position: pos || null, avis: rep.avis, poids: w };
        if (val === 0) silences.push(item);
        else {
          exprimees++;
          (accord > 0 ? accords : desaccords).push(item);
        }
      }
      const versPct = (n, d) => (d ? Math.round(((n / d + 1) / 2) * 1000) / 10 : null);
      const themes = {};
      for (const [t, v] of Object.entries(parTheme)) themes[t] = versPct(v.num, v.den);
      return {
        candidat: c,
        score: versPct(num, den),
        couverture: mesures.length ? Math.round((exprimees / mesures.length) * 100) : 0,
        themes, accords, desaccords, silences,
      };
    });

    resultats.sort((a, b) => (b.score ?? -1) - (a.score ?? -1));
    // F16 : ex æquo avec le premier
    if (resultats.length) {
      const top = resultats[0].score;
      for (const r of resultats) r.exAequo = top !== null && r !== resultats[0] && top - r.score < SEUIL_EX_AEQUO;
    }
    return { nbMesures: mesures.length, resultats };
  }

  const Score = { calculer, SEUIL_EX_AEQUO };
  if (typeof module !== "undefined" && module.exports) module.exports = Score;
  else global.Score = Score;
})(typeof window !== "undefined" ? window : globalThis);
