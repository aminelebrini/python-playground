import pandas as pd
import numpy as np


data1 = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Âge': [25, 30, 35, 40, 22, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon', 'Lille'],
    'Salaire': [35000, 42000, 50000, 48000, 29000, 38000]
}

df1 = pd.DataFrame(data1)

df_deps = pd.DataFrame({
        'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse'],
        'Departement': ['RH', 'IT', 'Ventes', 'Marketing']
})

result = df1.merge(df_deps)

print(result)

