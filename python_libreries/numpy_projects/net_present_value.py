import numpy as np

cf = np.array([200, 300, 400])
r = 0.08
t = np.array([1,2,3])
npv = cf / ((1+r)**t)

npv_sum = np.sum(npv)

print(npv_sum)