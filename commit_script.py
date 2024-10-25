import os
from datetime import datetime

# Chemin du fichier où seront enregistrées les contributions quotidiennes
filename = "daily_update.txt"

# Créer ou modifier un fichier pour générer un commit unique par jour
with open(filename, "a") as file:
    file.write(f"Commit du jour - {datetime.now().isoformat()}\n")
