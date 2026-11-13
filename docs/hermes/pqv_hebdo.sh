#!/usr/bin/env bash
# Veille hebdomadaire « Pour qui voter ? » — relance la recherche des programmes et positions par Hermès.
# Installé sur la VM : ~/.hermes/scripts/pqv_hebdo.sh, lancé par la crontab (lignes marquées « # pqv-hebdo »).
#
# Échéance : chaque samedi à 07:00. RATTRAPAGE : la crontab appelle ce script toutes les 30 minutes et au démarrage
# de la VM ; il ne fait quelque chose que si un candidat de la semaine en cours n'a pas encore été mis en file.
# Si la VM était éteinte ou injoignable le samedi, la veille part donc dès son retour ; si une création échoue,
# elle est retentée à l'appel suivant. L'état est sauvegardé sur la VM : ~/.hermes/state/pqv_hebdo/<samedi>.txt
# (un candidat par ligne, « candidat job_id livrable »).
#
# Candidats : tous ceux de candidats_hebdo.txt (mode « relevé »), plus le groupe de la semaine de candidats_rotation.txt
# (mode « complément » : groupe 1 la semaine du 21/11/2026, puis 2, puis 3, puis on recommence).
# Pour chaque candidat : crée une tâche Hermès EN PAUSE, puis l'ajoute à la file GLM
# (flux pqv, type analyse). Aucune tâche n'est lancée directement : c'est le répartiteur (glm_file.py tick) qui décide.
# Usage : pqv_hebdo.sh [--essai]   (--essai : affiche ce qui serait fait, sans rien créer)
# Toute modification (candidats, consigne, fréquence) se fait à la demande de l'éditeur.
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
W=/home/patrick/workspace/Projets/pour-qui-voter
CONSIGNE="$W/consigne_positions_hebdo.md"
LISTE="$W/candidats_hebdo.txt"
ROTATION="$W/candidats_rotation.txt"
DEBUT_ROTATION=2026-11-21
ETAT_DIR="$HOME/.hermes/state/pqv_hebdo"
ESSAI=0; [ "${1:-}" = "--essai" ] && ESSAI=1

# Semaine en cours = dernier samedi 07:00 passé
jours=$(( ($(date +%u) - 6 + 7) % 7 ))
if [ "$jours" -eq 0 ] && [ "$(date +%H)" -lt 7 ]; then jours=7; fi
SEMAINE=$(date -d "$jours days ago" +%F)
ETAT="$ETAT_DIR/$SEMAINE.txt"
D=$(date +%F)                      # date du relevé = jour réel de la mise en file (peut être postérieur au samedi)
mkdir -p "$ETAT_DIR"; touch "$ETAT"

[ -f "$CONSIGNE" ] && [ -f "$LISTE" ] && [ -f "$W/mesures_par_theme.md" ] && [ -f "$W/positions_actuelles.md" ] || { echo "$(date '+%F %R') : fichier manquant (consigne, liste ou mesures)"; exit 1; }

# Groupe de rotation de la semaine (aucun avant le 21/11/2026)
GROUPE=""
if [ -f "$ROTATION" ] && [[ ! "$SEMAINE" < "$DEBUT_ROTATION" ]]; then
  k=$(( ( $(date -d "$SEMAINE" +%s) - $(date -d "$DEBUT_ROTATION" +%s) ) / 604800 ))
  NB=$(grep -vE '^\s*(#|$)' "$ROTATION" | awk '{print $2}' | sort -un | wc -l)
  [ "$NB" -gt 0 ] && GROUPE=$(( k % NB + 1 ))
fi
CANDIDATS=$( { grep -vE '^\s*(#|$)' "$LISTE" | awk '{print $1" releve"}'
               [ -n "$GROUPE" ] && grep -vE '^\s*(#|$)' "$ROTATION" | awk -v g="$GROUPE" '$2==g {print $1" complement"}'; } || true)
A_FAIRE=$(echo "$CANDIDATS" | while read -r c m; do [ -n "$c" ] && ! grep -q "^$c " "$ETAT" && echo "$c:$m"; done || true)
[ -z "$A_FAIRE" ] && { [ $ESSAI = 1 ] && echo "Semaine du $SEMAINE : rien à faire (tout est en file)"; exit 0; }

echo "== $(date '+%F %R') : veille hebdomadaire PQV, semaine du $SEMAINE${GROUPE:+, groupe de rotation $GROUPE}$( [ "$D" != "$SEMAINE" ] && echo ' (rattrapage)')$( [ $ESSAI = 1 ] && echo ' (essai)')"
for cm in $A_FAIRE; do
  c=${cm%%:*}; m=${cm#*:}
  if [ "$m" = complement ]; then MODE="Mode « complément » : lis d abord la section de ce candidat dans $W/positions_actuelles.md et ne recopie pas les positions déjà saisies."; else MODE="Mode « relevé »."; fi
  f="${D}_positions-${c//_/-}.md"
  P="Projet Pour qui voter, veille hebdomadaire. Date du relevé : $D. Lis entièrement $CONSIGNE et $W/mesures_par_theme.md, puis traite UNIQUEMENT le candidat « $c » (sa section dans la consigne). $MODE Respecte strictement les règles (sources officielles d abord, aucun agrégateur, citations exactes de moins de 30 mots avec URL et date, rien d inventé). Compare avec le relevé précédent de ce candidat s il existe. Écris le livrable $W/$f et termine par son chemin. Ne crée aucune tâche programmée."
  if [ $ESSAI = 1 ]; then echo "  [essai] $c ($m) -> $f"; continue; fi
  J=$(hermes cron create "every 1m" "$P" --name "PQV hebdo $D $c" --repeat 1 --deliver local --model glm-5.3 --provider zai \
        --workdir "$W" --paused --paused-reason "file GLM" 2>&1 | sed -n 's/.*Created job: \([0-9a-f]*\).*/\1/p') || true
  [ -n "$J" ] || { echo "  $c : création de la tâche impossible, nouvel essai au prochain appel"; continue; }
  if "$HOME/.hermes/scripts/glm_file.py" ajouter "$J" --flux pqv --type analyse >/dev/null 2>&1; then
    echo "$c $J $f" >> "$ETAT"
    echo "  $c ($m) : tâche $J ajoutée à la file -> $f"
  else
    echo "  $c : tâche $J créée mais non ajoutée à la file, nouvel essai au prochain appel"
    hermes cron remove "$J" >/dev/null 2>&1 || true
  fi
done
