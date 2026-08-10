import numpy as np

class DemandSimulator:

    def __init__(self, num_products, time_periods):
        self.num_products = num_products
        self.time_periods = time_periods

    def generate_scenarios(self, base_demand, volatility, num_simulations=1000):

        noice = np.random.normal(1.0, volatility, size=(num_simulations, self.num_products, self.time_periods))

        senario = base_demand[None, : , None] * noice

        return np.maximum(senario, 0) #0 to replace any negative number 
