liste = [2,4,-5,-8,9,10,15]

def reduire_list(liste, operation, valeur_initiale):

    accumulateur = valeur_initiale

    for ele in liste:
        accumulateur = operation(accumulateur, ele)

    return accumulateur

print(reduire_list(liste, lambda x, y: x + y, 0))