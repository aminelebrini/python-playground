import numpy as np

arr_2d = np.random.randint(1,100, size=(3,2))
arr_1_2d = np.random.randint(1,100, size=(3,2))

new_arr_v = np.concatenate((arr_2d,arr_1_2d), axis=0)
new_arr_h = np.concatenate((arr_2d,arr_1_2d), axis=1)
print(arr_2d)
print("---"*5)
print(arr_1_2d)
print("---"*5)
print(new_arr_v)
print(np.shape(new_arr_v))
print("---"*5)
print(new_arr_h)
print(np.shape(new_arr_h))