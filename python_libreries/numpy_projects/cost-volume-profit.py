import numpy as np

fc = 50000
P = np.array([150, 200, 350])
VC = np.array([90, 120, 210])

cm = P - VC
q = fc / cm
for index, (margin, units) in enumerate(zip(cm, q)):
    print(f"Product {index + 1}: CM = ${margin} | Breakeven = {np.ceil(units):.0f} units")

