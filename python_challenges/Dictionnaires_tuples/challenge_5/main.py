etudiant_info = ("Yasmine", 22, "Informatique", 17.4)

print(f"Prénom : {etudiant_info[0]}")
print(f"Âge : {etudiant_info[1]}")
print(f"Filière : {etudiant_info[2]}")
print(f"Moyenne générale : {etudiant_info[3]}")

try:
    etudiant_info[2] = "Génie Logiciel"
except TypeError as e:
    print("\nModification échouée :", e)

prenom_et_age = etudiant_info[0:2]
print("\nPrénom et âge (slicing) :", prenom_et_age)

infos_supplementaires = ("Très Bien", 2024)
etudiant_info_complet = etudiant_info + infos_supplementaires
print("\nTuple final combiné :", etudiant_info_complet)