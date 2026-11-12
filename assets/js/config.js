/* Configuration de diffusion. À adapter si le dépôt ou la page de téléchargement change. */
window.CONFIG = {
  // Page où télécharger la dernière version de l'application (archive ZIP) et des packs
  telechargement: "https://github.com/PatrickDarbeau/pour-qui-voter/releases/latest",
  // Code source et signalement d'erreurs
  depot: "https://github.com/PatrickDarbeau/pour-qui-voter",
  signalement: "https://github.com/PatrickDarbeau/pour-qui-voter/issues",
};

/* Démo en ligne (CDC §6 bis) : application servie par un hébergeur web, hors poste local.
 * « ?demo » dans l'adresse permet de tester ce mode en local.
 * En ligne : mode Édition en ESSAI (modifications gardées dans le navigateur du visiteur),
 * liste et fiches des candidats VERROUILLÉES, import de packs désactivé. */
window.EN_LIGNE = (/^https?:$/.test(location.protocol) && !/^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname))
  || /[?&]demo\b/.test(location.search);
