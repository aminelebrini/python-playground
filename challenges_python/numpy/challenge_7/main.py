import numpy as np

arr = np.arange(1,14)
condition = (arr >= 10) & (arr <= 20)
indice = np.where(condition)[0]
print(indice)