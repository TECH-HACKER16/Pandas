import numpy as np
import pandas as pd


College = {
    'Courses' : ["CSE","IT","ECE","EEE","MECH","CIVIL"],
    'Seat alloted' : [60,120,240,120,180,120]
}

x = pd.DataFrame(College)

x.index = np.arange(1, len(x) + 1) ## Reindexing DataFrame to display index from 1

print (x)