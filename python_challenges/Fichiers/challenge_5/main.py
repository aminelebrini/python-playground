import os
import shutil
def challenge_5_copie_selective(repertoire_source, repertoire_destination, extension=".csv"):
    if not os.path.exists(repertoire_destination):
        os.makedirs(repertoire_destination)

    for fichier in os.listdir(repertoire_source):
        if fichier.endswith(extension):
            chemin_source = os.path.join(repertoire_source, fichier)
            shutil.copy(chemin_source, repertoire_destination)