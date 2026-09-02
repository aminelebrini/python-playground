Ch1 = "Le langage Python est très populaire"
Ch2 = "Python est un langage puissant"

arr_str_1 = []
arr_str_2 = []
new_arr_same_word = []

arr_str_1 = Ch1.split(' ')
arr_str_2 = Ch2.split(' ')

for i in arr_str_1:
    for j in arr_str_2:
        if i == j:
            new_arr_same_word.append(i)

print(new_arr_same_word)

