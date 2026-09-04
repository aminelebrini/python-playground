First_dict = { 
    "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", 
    "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", 
    "Processeur": "Intel core i7-G11", "SSD": "1 To" 
    }

notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }


# nouveau_dict = { cle: "32G" if cle == "RAM" else valeur for cle, valeur in First_dict.items()}

for key in First_dict:
    if key == "RAM":
        First_dict[key] = "32G"
 
print(First_dict)
print(First_dict.keys())
print(First_dict.values())
print(First_dict.items())

tmp = First_dict["Processeur"]
First_dict["Processeur"] = First_dict["Carte Graphique"]
First_dict["Carte Graphique"] = tmp
print("\n",First_dict["Processeur"], "and" ,First_dict["Carte Graphique"])

First_dict["Système d’exploitation"] = "WINDOWS 10"
print(First_dict)

AdmiStudent = list(filter(lambda x: x[1] >= 10 ,notes_eleves.items()))
AdmiStudent = list(filter(lambda x: x[1] <= 10 ,notes_eleves.items()))

print(AdmiStudent)
