import os

def challenge_2_recherche(repertoire="."):
    chemin_config = os.path.join(repertoire, "config.yaml")
    if os.path.exists(chemin_config):
        with open(chemin_config, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Le fichier config.yaml n'existe pas.")