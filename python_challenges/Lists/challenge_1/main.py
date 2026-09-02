notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

avrage = 0
n_total = len(notes)
total = 0

new_notes = []
for i in notes:
    total += i


avrage = total / n_total


for i in notes:
    if i >= avrage:
        new_notes.append(i)

print(f"{new_notes}")