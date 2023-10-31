import pandas as pd

x = pd.read_csv("D:\Coding\Pandas\Cells\Courses.csv").dropna(inplace=True)

print("\n",x.to_string()) ## Clearing incomplete rows in source file(Original)
