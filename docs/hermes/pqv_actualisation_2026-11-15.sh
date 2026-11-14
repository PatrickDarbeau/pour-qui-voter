#!/usr/bin/env bash
# Prépare l'actualisation ponctuelle du 15/11/2026 (demande de l'éditeur du 14/11/2026).
# Crée sur la VM, EN PAUSE, une tâche Hermès par candidat (mode « complément ») puis une tâche de synthèse,
# et les inscrit dans ~/.hermes/state/pqv_echeances.txt pour le 15/11/2026 à 07:00 : pqv_echeances.sh les ajoutera
# à la file GLM à l'heure dite (avec rattrapage si la VM est éteinte), dans l'ordre des lignes (synthèse en dernier).
# À lancer une seule fois : ssh hermes 'bash -s' < docs/hermes/pqv_actualisation_2026-11-15.sh
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
W=/home/patrick/workspace/Projets/pour-qui-voter
D=2026-11-15
QUAND=2026-11-15T07:00
ECH="$HOME/.hermes/state/pqv_echeances.txt"
C="$W/consigne_actualisation_2026-11-15.md"
[ -f "$C" ] || { echo "consigne absente : $C"; exit 1; }
grep -q "PQV-actualisation-$D" "$ECH" 2>/dev/null && { echo "déjà préparé"; exit 0; }

creer() {  # nom, prompt -> id de tâche
  hermes cron create "every 1m" "$2" --name "$1" --repeat 1 --deliver local --model glm-5.3 --provider zai \
    --workdir "$W" --paused --paused-reason "échéance $QUAND" 2>&1 | sed -n 's/.*Created job: \([0-9a-f]*\).*/\1/p'
}
for c in lepen zemmour attal roussel retailleau lisnard philippe glucksmann melenchon; do
  f="${D}_positions-${c//_/-}.md"
  P="Projet Pour qui voter, actualisation du $D. Lis entièrement $C, puis $W/consigne_positions_hebdo.md, $W/mesures_par_theme.md et la section « $c » de $W/positions_actuelles.md. Traite UNIQUEMENT le candidat « $c », en mode « complément », avec les trois priorités de la partie 1 de $C (14 nouvelles mesures, règles R1 à R6, nouveautés depuis le 12/11). Respecte strictement les règles (sources officielles d abord, aucun agrégateur, citations exactes de moins de 30 mots avec URL et date, rien d inventé). Écris le livrable $W/$f au fur et à mesure et termine par son chemin. Ne crée aucune tâche programmée."
  J=$(creer "PQV actualisation $D $c" "$P"); [ -n "$J" ] || { echo "$c : création impossible"; exit 1; }
  echo "$QUAND $J PQV-actualisation-$D-$c" >> "$ECH"; echo "$c -> $J ($f)"
done
P="Projet Pour qui voter, rapport de synthèse de l'actualisation du $D. Lis entièrement $C et suis sa partie 2 : lis les livrables ${D}_positions-*.md du dossier $W et écris $W/${D}_veille-actualisation.md. Aucune nouvelle recherche : résume seulement les livrables présents, signale ceux qui manquent. Ton neutre. Termine par le chemin du fichier. Ne crée aucune tâche programmée."
J=$(creer "PQV actualisation $D synthèse" "$P"); [ -n "$J" ] || { echo "synthèse : création impossible"; exit 1; }
echo "$QUAND $J PQV-actualisation-$D-synthese" >> "$ECH"; echo "synthèse -> $J"
