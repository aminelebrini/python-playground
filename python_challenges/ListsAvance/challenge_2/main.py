liste = [1,-2,5,-8,10,6,5]

def is_positif(x):
    return x > 0

def to_cube(n):
    return n ** 3


def multiple_in_list(lis, critere):
    result_2 = list(map(critere, lis))

    return result_2

def positive_list(liste, critere):

    result = list(filter(critere, liste))

    return multiple_in_list(result, to_cube)


result_final = positive_list(liste, is_positif)

print(sorted(result_final))




