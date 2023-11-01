import pandas as pd
import numpy as np

x = pd.read_csv("D:\Coding\Pandas\Replace\Courses.csv")

y = x["Seats_remaining"].median()

x.index = np.arange(1, len(x) + 1)

z = x["Seats_remaining"].fillna(y,inplace=True) ## Replacing empty cells with value of median of specified column 

print("\n",x.to_string())