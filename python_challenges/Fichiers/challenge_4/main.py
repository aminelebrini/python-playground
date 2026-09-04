import os

def challenge_4_creation_repertoires(dossier_principal, sous_dossiers):
    if not os.path.exists(dossier_principal):
        os.mkdir(dossier_principal)

    for dossier in sous_dossiers:
        chemin = os.path.join(dossier_principal, dossier)
        if not os.path.exists(chemin):
            os.mkdir(chemin)