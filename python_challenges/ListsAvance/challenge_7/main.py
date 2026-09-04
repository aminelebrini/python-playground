liste = [1,2,5,[5,2],4] 
def transformer_imbriquee(liste, transformer):

    resu = map(lambda x: transformer_imbriquee(x, transformer) if isinstance(x, list) else transformer(x), liste)

    return resu

print(transformer_imbriquee(liste, lambda x: x * 2))