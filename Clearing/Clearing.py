import pandas as pd

x = pd.read_csv("D:\Coding\Pandas\Cells\Courses.csv").dropna()

print("\n",x.to_string()) ## Clearing incomplete rows
