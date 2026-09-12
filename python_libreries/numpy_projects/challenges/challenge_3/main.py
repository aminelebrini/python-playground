import numpy as np

vector = np.arange(1, 11)
vector_2 = np.arange(1,17)

vector_1 = np.flip(vector)
vector_2_2 = vector_2.reshape(4,4)
vector_2_2 = np.flip(vector_2_2)

print(vector_1)
print("---------------------------")
print(vector_2_2)