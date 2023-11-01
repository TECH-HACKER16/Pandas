import pandas as pd
import numpy as np

x = pd.read_csv("D:\Coding\Pandas\Replace\Courses.csv")

x.index = np.arange(1, len(x) + 1)

y = x["Seats_allotted"].fillna(130,inplace=True) ## Replacing value for specified column 

print("\n",x.to_string())