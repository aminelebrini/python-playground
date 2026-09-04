import os
def challenge_1_extraction(repertoire="."):
    contenu_combine = ""
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            chemin_complet = os.path.join(repertoire, fichier)
            with open(chemin_complet, "r", encoding="utf-8") as f:
                contenu_combine += f.read() + "\n"
    return contenu_combine