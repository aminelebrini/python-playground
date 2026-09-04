def regrouper_tuples(liste_tuples):
    dico = {}
    for cle, valeur in liste_tuples:
        dico.setdefault(cle, []).append(valeur)
    return dico


entree = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
resultat = regrouper_tuples(entree)

print(resultat)
