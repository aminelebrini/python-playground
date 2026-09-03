liste = [1,2,5,[5,2],4] 
def transformer_imbriquee(liste, transformer):

    resultat = []

    for ele in liste:
        if isinstance(ele, list):
            resultat.append(transformer_imbriquee(ele, transformer))
        else:
            resultat.append(transformer(ele))
            
    return resultat

print(transformer_imbriquee(liste, lambda x: x * 2))