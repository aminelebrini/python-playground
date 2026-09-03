#  Écrivez du code Python ici
liste = [1,2,5,6,1,2,4,11,15]

def is_greater_than_10(x):
    return x > 10

def filter_list(liste, critere_filter):

    result = list(filter(critere_filter , liste))

    print(result)


filter_list(liste, is_greater_than_10)