import numpy as np

vector = np.random.randint(1, 18, size=(6,8))
print(vector)

indice_croissant = np.argsort(vector, axis=1)
print("-"*30)
indice_decroissant = indice_croissant[:, ::-1]

top_3_indices = indice_decroissant[:, :3]

top_3_valeurs = np.take_along_axis(vector, top_3_indices, axis=1)

print("\n=== LES 3 PLUS GRANDS INDICES PAR LIGNE ===")
print(top_3_indices)

print("\n=== LES 3 PLUS GRANDES VALEURS PAR LIGNE ===")
print(top_3_valeurs)