import numpy as np
from scipy.optimize import linprog

c = [-40, -30]
a = [[2,1],[1,2]]
b = [100,80]

result = linprog(c, A_ub=a, b_ub=b)

print(result)


