import numpy as np
from scipy.optimize import linprog

class ProductionOptimizer:

    def __init__(self, unit_profits, resource_matrix, capacities):
        self.c = -np.array(unit_profits)

        self.A = np.array(resource_matrix)
        self.B = np.array(capacities)

    def optimize_monthly_plan(self):

        result = linprog(self.c, A_ub=self.A, b_ub=self.B)

        if result.success:
            return result.x, -result.fun
        else:
            raise ValueError("Optimization failed to find a feasible solution.")


        