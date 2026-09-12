import numpy as np


vector_2 = np.random.randint(1,100, size=(5,3))

moyenne = np.mean(vector_2)
somme = np.sum(vector_2, axis=0)
max = np.max(vector_2, axis=1)
print(vector_2)
print("-"*20)
print(moyenne)
print("-"*20)
print(somme)
print("-"*20)
print(max)