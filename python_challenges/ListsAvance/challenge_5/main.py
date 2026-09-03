liste = [2,4,-5,-8,9,10,15]

my_list = []

def partitionner_list(liste, critere_1, critere_2):
    result_1 = list(filter(critere_1, liste))
    result_2 = list(filter(critere_2, liste))

    my_list.append(result_1)
    my_list.append(result_2)

    print(my_list)


partitionner_list(liste, lambda x: x % 2 == 0, lambda x: x % 2 != 0)
