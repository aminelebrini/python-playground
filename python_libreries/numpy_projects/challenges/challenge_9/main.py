import numpy as np

vector = np.random.randint(-10, 11, size=20)
print(vector)
new_vector = np.where(
    (vector < 0) & (vector % 2 != 0), vector**2,
    np.where((vector > 0) & (vector % 2 == 0), 0,vector

             ) 
        )
print(new_vector)