def transformer_tuples(liste_tuples, fonction_transfo):
    return [tuple(map(fonction_transfo, t)) for t in liste_tuples]


entree = [(1, 2), (3, 4)]

res_double = transformer_tuples(entree, lambda x: x * 2)
print("Test Multiplication (*2) :", res_double)

res_plus_un = transformer_tuples(entree, lambda x: x + 1)
print("Test Addition (+1) :", res_plus_un)
