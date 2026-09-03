list_1 = [9,1,2,5,6]
list_2 = [7,8,4,5,8]

list_1.extend(list_2)

resu = set(list_1)
final_result = sorted(resu)

print(final_result)