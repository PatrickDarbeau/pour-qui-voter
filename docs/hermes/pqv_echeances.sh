#!/usr/bin/env bash
# Échéances ponctuelles « Pour qui voter ? » avec rattrapage.
# Installé sur la VM : ~/.hermes/scripts/pqv_echeances.sh, appelé par la crontab toutes les 30 minutes et au démarrage
# (lignes marquées « # pqv-echeances »).
# Fichier ~/.hermes/state/pqv_echeances.txt : une ligne par échéance, « AAAA-MM-JJTHH:MM job_id libellé ».
# Dès que l'heure est passée, la tâche Hermès (créée en pause) est ajoutée à la file GLM, puis notée dans
# ~/.hermes/state/pqv_echeances.fait : si la VM était éteinte à l'heure prévue, l'ajout se fait dès son retour.
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
LISTE="$HOME/.hermes/state/pqv_echeances.txt"
FAIT="$HOME/.hermes/state/pqv_echeances.fait"
touch "$LISTE" "$FAIT"
MAINTENANT=$(date +%FT%R)
grep -vE '^\s*(#|$)' "$LISTE" | while read -r quand job libelle; do
  grep -q " $job " "$FAIT" && continue
  [[ "$MAINTENANT" < "$quand" ]] && continue
  if "$HOME/.hermes/scripts/glm_file.py" ajouter "$job" --flux pqv --type analyse >/dev/null 2>&1; then
    echo "$MAINTENANT $job $libelle" >> "$FAIT"
    echo "$MAINTENANT : $libelle ($job) ajoutée à la file$( [[ "${MAINTENANT:0:13}" > "${quand:0:13}" ]] && echo " — rattrapage de l'échéance du $quand")"
  else
    echo "$MAINTENANT : $libelle ($job) — ajout impossible, nouvel essai au prochain appel"
  fi
done
