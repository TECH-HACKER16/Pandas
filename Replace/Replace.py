import pandas as pd
import numpy as np

x = pd.read_csv("D:\Coding\Pandas\Replace\Courses.csv")

x.index = np.arange(1, len(x) + 1)

y= x.fillna(130)

print("\n",y.to_string())