import numpy as np

arr = np.array([1.0, 2.0, np.nan, 4.0, np.nan, 6.0])

moyenne = np.nanmean(arr)

arr_2 = arr[np.isnan(arr)] = moyenne
print(arr)
print("-"*10)
print(moyenne)
print("-"*10)
print(arr_2)