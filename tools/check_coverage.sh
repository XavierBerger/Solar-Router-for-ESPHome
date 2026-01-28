#!/bin/bash

# Utilisation de la commande tput pour les couleurs
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
RESET=$(tput sgr0)

for iloop in $(ls solar_router/*); do 
    # Extraction du nom de fichier sans le chemin relatif
    filename=$(basename "$iloop")
    
    echo -n "$iloop -> "
    
    # Première recherche dans les fichiers .yaml
    if grep -q "$iloop" *.yaml; then
        COUNT=$(grep $iloop *.yaml 2> /dev/null | wc -l)
        echo "${GREEN}OK ($COUNT)${RESET}"
    else
        # Si non trouvé, recherche du nom de fichier dans les fichiers du répertoire solar_router
        if grep -r "$filename" solar_router/*.yaml > /dev/null; then
            echo "${GREEN}OK (include)${RESET}"
        else
            echo "${RED}KO${RESET}"
        fi
    fi
done