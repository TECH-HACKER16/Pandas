import pandas as pd

x = pd.read_csv('D:\Coding\Pandas\Replace\Courses.csv')

x.loc[7,'Seats_remaining'] = 45 ## Replacing or updating specific value in row and column

print(x.to_string())