import pandas as pd

data1 = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Âge': [25, 30, 35, 40, 22, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon', 'Lille'],
    'Salaire': [35000, 42000, 50000, 48000, 29000, 38000]
}

df1 = pd.DataFrame(data1)

result_by_ville = df1.sort_values(by="Ville")
result_by_salaire = df1.sort_values(by="Salaire")

print(result_by_ville)
print("-------------------------")
print(result_by_salaire)

