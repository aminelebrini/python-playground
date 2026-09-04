notes_eleves = {
    "Amine": 14.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, 
    "Manal": 20.0, "Ahmed": 7.5, "Saad": 11.3, "Hannae": 9.8
}

paires_triees = sorted(notes_eleves.items(), key=lambda x: x[1])

notes_triees_dict = dict(paires_triees)

print(notes_triees_dict)
