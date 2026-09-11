import pandas as pd


df8 = pd.DataFrame({
    'Region': ['Nord', 'Nord', 'Sud', 'Sud', 'Nord', 'Sud'],
    'Produit': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Ventes': [100, 200, 150, 250, 120, 220]
})

result = df8.pivot_table(
    values="Ventes",
    index="Region",
    columns="Produit",
    aggfunc="mean"
)

print(result)