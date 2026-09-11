import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2021-01-01", end="2021-01-31", freq="D")

ventes = np.random.randint(100, 1000, size=len(dates))

data_frame = pd.DataFrame({"Date" : dates, "Ventes" : ventes})

data_frame.set_index("Date", inplace=True)

result_1 = data_frame.resample("W").sum()

print(result_1)