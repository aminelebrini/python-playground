import numpy as np

vector_1d = np.arange(0, 51)

vector_1d_result = vector_1d[(vector_1d > 25) & (vector_1d % 2 == 0)]

print(vector_1d_result)