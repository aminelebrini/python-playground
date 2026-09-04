def challenge_6_ecriture(fichier_sortie, lignes):
    with open(fichier_sortie, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(ligne + "\n")

    # Vérification
    with open(fichier_sortie, "r", encoding="utf-8") as f:
        print("Contenu enregistré :")
        print(f.read())