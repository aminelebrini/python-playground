import pandas as pd
import json

data = []
with open("salary_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def getNthHighestSalary(N):

    if N <= 0:
        print("invalid id entred !")
        return
    
    df = pd.DataFrame(data)
    df = df.dropna()
    
    df = df.sort_values(by="salary",ascending=False)
    df = df['salary'].drop_duplicates()


    if len(df) < N:
        return None
    else:
        res = df.iloc[N-1]

    print(res)


getNthHighestSalary(5)