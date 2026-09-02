stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]

numbers_arr = []
strings_arr = []

for value in stock:
    if isinstance(value, int):
        numbers_arr.append(value)
    elif isinstance(value, str):
        strings_arr.append(value)

print(numbers_arr)
print(strings_arr)