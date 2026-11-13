#!/usr/bin/env bash
# Veille hebdomadaire « Pour qui voter ? » — relance la recherche des programmes et positions par Hermès.
# Installé sur la VM : ~/.hermes/scripts/pqv_hebdo.sh, lancé par la crontab (ligne marquée « # pqv-hebdo »).
# Pour chaque candidat de candidats_hebdo.txt : crée une tâche Hermès EN PAUSE, puis l'ajoute à la file GLM
# (flux pqv, type analyse). Aucune tâche n'est lancée directement : c'est le répartiteur (glm_file.py tick) qui décide.
# Usage : pqv_hebdo.sh [--essai]   (--essai : affiche ce qui serait créé, sans rien créer)
# Toute modification (candidats, consigne, fréquence) se fait à la demande de l'éditeur.
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
W=/home/patrick/workspace/Projets/pour-qui-voter
CONSIGNE="$W/consigne_positions_hebdo.md"
LISTE="$W/candidats_hebdo.txt"
D=$(date +%F)
ESSAI=0; [ "${1:-}" = "--essai" ] && ESSAI=1

[ -f "$CONSIGNE" ] && [ -f "$LISTE" ] && [ -f "$W/mesures_par_theme.md" ] || { echo "$D : fichier manquant (consigne, liste ou mesures)"; exit 1; }

echo "== $D : veille hebdomadaire PQV$( [ $ESSAI = 1 ] && echo ' (essai)')"
grep -vE '^\s*(#|$)' "$LISTE" | while read -r c; do
  f="${D}_positions-${c//_/-}.md"
  P="Projet Pour qui voter, veille hebdomadaire. Date du relevé : $D. Lis entièrement $CONSIGNE et $W/mesures_par_theme.md, puis traite UNIQUEMENT le candidat « $c » (section « $c » de la consigne). Respecte strictement les règles (sources officielles d abord, aucun agrégateur, citations exactes de moins de 30 mots avec URL et date, rien d inventé). Compare avec le relevé précédent de ce candidat s il existe. Écris le livrable $W/$f et termine par son chemin. Ne crée aucune tâche programmée."
  if [ $ESSAI = 1 ]; then echo "  [essai] $c -> $f"; continue; fi
  if [ -e "$W/$f" ]; then echo "  $c : $f existe déjà, ignoré"; continue; fi
  J=$(hermes cron create "every 1m" "$P" --name "PQV hebdo $D $c" --repeat 1 --deliver local --model glm-5.3 --provider zai \
        --workdir "$W" --paused --paused-reason "file GLM" 2>&1 | sed -n 's/.*Created job: \([0-9a-f]*\).*/\1/p')
  [ -n "$J" ] || { echo "  $c : création de la tâche impossible"; continue; }
  "$HOME/.hermes/scripts/glm_file.py" ajouter "$J" --flux pqv --type analyse >/dev/null
  echo "  $c : tâche $J ajoutée à la file -> $f"
done
