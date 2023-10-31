import pandas as pd

Seats_alloted = [60,120,240,120,180,120]

x = pd.Series(Seats_alloted,index = ["CSE","IT","ECE","EEE","MECH","CIVIL"])

print ("\n",x)