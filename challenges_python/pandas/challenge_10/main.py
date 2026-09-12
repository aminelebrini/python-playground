import pandas as pd

df10 = pd.DataFrame({
    'Ville': ['paris', 'lyon', 'marseille', 'lille'],
    'Ventes': [80, 150, 200, 95]
})

df10["Ville"] = df10["Ville"].str.upper()
df10 = df10.loc[df10["Ventes"] > 100]
df10['TVA'] = df10["Ventes"] * 0.1

print(df10)