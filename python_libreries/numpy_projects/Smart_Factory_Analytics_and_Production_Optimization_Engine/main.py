import numpy as np
from DemandSimulator import DemandSimulator
from ProductionOptimizer import ProductionOptimizer

if __name__ == "__main__":

    ds = DemandSimulator(num_products=3, time_periods=12)
    base_demand = np.array([500, 300, 200])
    volatility=0.15

    demand_matrix = ds.generate_scenarios(base_demand, volatility)

    print(f"[Module 1] Generated Monte Carlo Demand Shape: {demand_matrix.shape}")

    unit_profits = [150, 200, 300]
    resource_matrix = [[1,2,3],[3,2,1]]
    capacities = [1200,800]

    po = ProductionOptimizer(unit_profits,resource_matrix,capacities)

    optimal_units, max_profit = po.optimize_monthly_plan()

    print("\n[Module 2] Optimal Production Plan for Month 1:")
    for idx, units in enumerate(optimal_units, 1):
        print(f"  - Product {idx}: {np.floor(units):.0f} units")
    print(f"  --> Expected Profit: ${max_profit:,.2f}")
