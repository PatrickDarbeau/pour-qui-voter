// Tests du calcul de concordance (critère d'acceptation : 3 cas vérifiés à la main).
// Lancer : node tests/score.test.js
const assert = require("assert");
const Score = require("../assets/js/score.js");

const D = {
  themes: [{ id: "a" }, { id: "b" }],
  mesures: [
    { id: "m1", theme: "a" }, { id: "m2", theme: "a" }, { id: "m3", theme: "b" },
  ],
  candidats: [{ id: "X" }, { id: "Y" }],
  positions: [
    { candidat: "X", mesure: "m1", valeur: 1 }, { candidat: "X", mesure: "m2", valeur: -1 },
    { candidat: "X", mesure: "m3", valeur: 0.5 },
    { candidat: "Y", mesure: "m1", valeur: -1 }, { candidat: "Y", mesure: "m3", valeur: 1 },
  ],
};
const parId = (res) => Object.fromEntries(res.resultats.map((r) => [r.candidat.id, r]));

// Cas 1 : sans pondération. Pour m1, m2, contre m3.
// X : (1 - 1 - 0.5) / 3 = -0.1667 -> 41.7 % ; Y : (-1 + 0 - 1) / 3 = -0.667 -> 16.7 %
let r = parId(Score.calculer(D, { m1: { avis: 1 }, m2: { avis: 1 }, m3: { avis: -1 } }, []));
assert.strictEqual(r.X.score, 41.7);
assert.strictEqual(r.Y.score, 16.7);
assert.strictEqual(r.Y.couverture, 67); // Y muet sur m2

// Cas 2 : thème b prioritaire (×2), m3 essentielle (×3) -> poids m3 = 6.
// X : (1 - 1 + 6*(-0.5)) / 8 = -0.375 -> 31.3 % ; Y : (-1 + 0 + 6*(-1)) / 8 = -0.875 -> 6.3 %
r = parId(Score.calculer(D, { m1: { avis: 1 }, m2: { avis: 1 }, m3: { avis: -1, essentielle: true } }, ["b"]));
assert.strictEqual(r.X.score, 31.3);
assert.strictEqual(r.Y.score, 6.3);

// Cas 3 : avis indifférent ignoré ; égalité parfaite -> ex æquo.
// Seule m1 compte (pour) : X 100 %, Y 0 %. Puis m3 seule (pour) : X 0.5 -> 75 %, Y 1 -> 100 %.
r = parId(Score.calculer(D, { m1: { avis: 1 }, m2: { avis: 0 } }, []));
assert.strictEqual(r.X.score, 100);
assert.strictEqual(r.Y.score, 0);
const res = Score.calculer(D, { m2: { avis: 1 }, m3: { avis: 0 } }, []);
// m2 : X -1 -> 0 %, Y muet -> 50 %
assert.strictEqual(res.resultats[0].candidat.id, "Y");
assert.strictEqual(res.resultats[0].score, 50);

// Ex æquo : deux candidats identiques
const D2 = { ...D, positions: [{ candidat: "X", mesure: "m1", valeur: 1 }, { candidat: "Y", mesure: "m1", valeur: 1 }] };
const res2 = Score.calculer(D2, { m1: { avis: 1 } }, []);
assert.strictEqual(res2.resultats[1].exAequo, true);

console.log("Tous les tests passent.");
