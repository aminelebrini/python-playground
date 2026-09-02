L = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]

counter = 1
occurrence_count = []


for i in set(L):
    occurrence_count.append({
        "number": i,
        "counting": L.count(i)
    })


print(occurrence_count)

