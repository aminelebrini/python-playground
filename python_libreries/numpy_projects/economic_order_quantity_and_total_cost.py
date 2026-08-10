import numpy as np

D = 12000
S = 150
H = 4

EOQ = np.sqrt((2*D*S)/H)
Q = np.array([500, 750, EOQ, 1200, 1500, 2000])

ordering_cost = (D/Q) * S
holding_cost = (Q/2) * H

total_cost = ordering_cost + holding_cost

for q, cost in zip(Q, total_cost):
    print(f"Order Quantity Q = {q:7.2f} units  --->  Total Annual Cost = ${cost:,.2f}")