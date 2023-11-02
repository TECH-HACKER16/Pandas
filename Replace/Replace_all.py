import pandas as pd

x = pd.read_csv('D:\Coding\Pandas\Replace\Courses.csv')

for i in x.index:
    if x.loc[i, "Seats_allotted"] > 120:
        x.loc[i, "Seats_allotted"] = 100 ## Replacing all values based on given condition

print(x.to_string())