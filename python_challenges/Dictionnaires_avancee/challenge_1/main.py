def fusionner_dictionnaires(dict1, dict2, fonction_fusion):
    resultat = {}

    for cle, valeur in dict1.items():
        resultat.update({cle: valeur})

    for cle, valeur in dict2.items():
        if cle in resultat:
            resultat[cle] = fonction_fusion(resultat[cle], valeur)
        else:
            resultat.setdefault(cle, valeur)

    return resultat


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

res_somme = fusionner_dictionnaires(dict1, dict2, lambda x, y: x + y)
print("Test Addition :", res_somme)

res_max = fusionner_dictionnaires(dict1, dict2, max)
print("Test Maximum  :", res_max)
