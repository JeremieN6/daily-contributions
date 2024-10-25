import os
import subprocess
from datetime import datetime

# Chemin du répertoire où se trouve le dépôt (ici on suppose que c'est le dossier actuel)
repo_path = "https://github.com/JeremieN6/daily-contributions.git"  # Remplace par le chemin réel

# 1. Se rendre dans le répertoire du dépôt
os.chdir(repo_path)

# 2. Créer ou modifier un fichier pour générer un commit unique par jour
filename = "daily_update.txt"
with open(filename, "a") as file:
    file.write(f"Commit du jour - {datetime.now().isoformat()}\n")

# 3. Ajouter et committer les modifications
subprocess.run(["git", "add", filename])
subprocess.run(["git", "commit", "-m", f"Commit automatique - {datetime.now().date()}"])

# 4. Pusher le commit sur GitHub
subprocess.run(["git", "push", "origin", "main"])  # Remplace "main" si ta branche principale a un autre nom
