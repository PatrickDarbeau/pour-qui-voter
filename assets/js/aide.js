/* Bulles d'aide au survol (souris), au focus (clavier) et à l'appui long (écran tactile).
 * Le texte vient de l'attribut data-aide, ou de la table AIDES ci-dessous (sélecteur CSS → texte).
 */
(function () {
  "use strict";

  const AIDES = [
    [".nav-cta", "Commencer ou reprendre le questionnaire"],
    ["a[href='#/candidats']", "Fiches des candidats et leurs positions, sources à l'appui"],
    ["a[href='#/methode']", "Comment le pourcentage de concordance est calculé"],
    [".civique a", "Site officiel service-public.fr (ouvre un nouvel onglet)"],
    [".tuile", "Cliquez pour faire de ce thème une priorité : ses mesures compteront double"],
    [".choix .oui", "Vous êtes favorable à cette mesure"],
    [".choix .non", "Vous êtes opposé à cette mesure"],
    [".choix .neutre", "Sans avis : la mesure ne comptera pas dans le calcul"],
    [".choix .etoile", "Mesure essentielle pour vous : elle comptera trois fois plus. Donnez d'abord un avis pour l'activer"],
    [".onglets a.fait", "Thème terminé : toutes ses mesures ont une réponse"],
    [".progression", "Part des mesures auxquelles vous avez répondu"],
    ["[data-action='effacer']", "Efface toutes vos réponses et vos thèmes prioritaires (confirmation demandée)"],
    ["[data-action='imprimer']", "Imprimer, ou choisir « Enregistrer au format PDF »"],
    [".pct", "Concordance : 100 % = d'accord sur tout, 50 % = autant d'accords que de désaccords, 0 % = désaccord sur tout"],
    [".tampon", "Le candidat dont le programme est le plus proche de vos choix. Ce n'est pas une consigne de vote"],
    ["details summary", "Cliquez pour afficher ou masquer le détail"],
    ["a[href^='http']", "Ouvre la source dans un nouvel onglet (connexion internet nécessaire)"],
    ["[data-ed='ajouter']", "Créer un nouvel élément"],
    ["[data-ed='modifier']", "Modifier cet élément"],
    ["[data-ed='supprimer']", "Supprimer cet élément (confirmation demandée)"],
    ["[data-ed='cellule']", "Cliquez pour saisir la position du candidat et sa source"],
    ["[data-ed='export-json']", "Enregistre toutes les données dans un fichier .json (sauvegarde ou partage)"],
    ["[data-ed='export-csv']", "Tableau des positions lisible dans Excel ou LibreOffice"],
    ["[data-ed-fichier]", "Choisissez un fichier pack (.json). Vos données actuelles seront sauvegardées avant"],
    ["[data-ed='restaurer']", "Annule le dernier import ou la dernière réinitialisation"],
    ["[data-ed='reinitialiser']", "Abandonne vos modifications et revient aux données fournies avec l'application"],
    ["[data-ed-filtre]", "Afficher un seul thème ou tous"],
    ["[data-ed='tout-ouvrir']", "Déplier toutes les sections de thèmes"],
    ["[data-ed='tout-fermer']", "Replier toutes les sections de thèmes"],
  ];

  const bulle = document.createElement("div");
  bulle.className = "bulle-aide";
  bulle.setAttribute("role", "tooltip");
  bulle.hidden = true;
  document.body.appendChild(bulle);

  let cible = null, minuteur = null;

  function texte(el) {
    if (el.dataset.aide) return el.dataset.aide;
    for (const [sel, t] of AIDES) if (el.matches(sel)) return t;
    return null;
  }
  function trouver(node) {
    for (let el = node; el && el !== document.body; el = el.parentElement) {
      if (el.nodeType === 1 && texte(el)) return el;
    }
    return null;
  }
  function montrer(el) {
    const t = texte(el);
    if (!t) return;
    cible = el;
    bulle.textContent = t;
    bulle.hidden = false;
    const r = el.getBoundingClientRect();
    const b = bulle.getBoundingClientRect();
    let x = r.left + r.width / 2 - b.width / 2;
    x = Math.max(8, Math.min(x, window.innerWidth - b.width - 8));
    let y = r.bottom + 8;
    if (y + b.height > window.innerHeight - 8) y = r.top - b.height - 8; // au-dessus si pas de place
    bulle.style.left = x + "px";
    bulle.style.top = y + "px";
  }
  function cacher() { clearTimeout(minuteur); bulle.hidden = true; cible = null; }

  document.addEventListener("mouseover", (e) => {
    const el = trouver(e.target);
    if (el === cible) return;
    cacher();
    if (el) minuteur = setTimeout(() => montrer(el), 450);
  });
  document.addEventListener("focusin", (e) => { const el = trouver(e.target); cacher(); if (el) montrer(el); });
  document.addEventListener("focusout", cacher);
  document.addEventListener("scroll", cacher, true);
  document.addEventListener("click", cacher, true);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") cacher(); });
  // Appui long sur écran tactile
  document.addEventListener("touchstart", (e) => {
    const el = trouver(e.target);
    cacher();
    if (el) minuteur = setTimeout(() => montrer(el), 600);
  }, { passive: true });
  document.addEventListener("touchend", () => clearTimeout(minuteur), { passive: true });
})();
