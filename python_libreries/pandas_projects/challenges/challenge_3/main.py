import pandas as pd
import numpy as np

df3 = pd.DataFrame({
    'Score': [85.0, np.nan, 92.0, 78.0, np.nan, 88.0],
    'Categorie': ['A', 'B', np.nan, 'A', 'B', 'B'],
    'Ventes': [100, 150, 120, 90, 110, 130]
})
print("DataFrame original :\n", df3)
print("-------------------------------------------")
res = df3.isna().sum()
print(res)
print("-------------------------------------------")
resu = df3["Score"].fillna(df3["Score"].median())
print(resu)
resu1 = df3["Categorie"].dropna()
print("-------------------------------------")
print(resu1)