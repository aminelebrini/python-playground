import numpy as np

vector_3 = np.random.randint(1, 16, size=(4,4))
print(vector_3)

diagonale = np.diag(vector_3)
trace = np.trace(vector_3)
print(diagonale)
# print(sum(diagonale))
print(trace)