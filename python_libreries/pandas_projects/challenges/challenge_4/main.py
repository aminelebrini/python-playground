import pandas as pd
import numpy as np

data1 = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Âge': [25, 30, 35, 40, 22, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon', 'Lille'],
    'Salaire': [35000, 42000, 50000, 48000, 29000, 38000]
}

df1 = pd.DataFrame(data1)

salaire_moyen = df1.groupby("Ville")["Salaire"].mean()
max_age = df1.groupby("Ville")["Âge"].max()
total_emp = df1.groupby("Ville")["Nom"].value_counts()

print(salaire_moyen)
print("---------------------------")
print(max_age)
print("---------------------------")
print(total_emp)