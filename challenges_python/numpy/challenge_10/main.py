import numpy as np

vector = np.array([1,2,3,4,5,6,7,8])
vector1 = np.lib.stride_tricks.sliding_window_view(vector, 3)
print(vector1)
