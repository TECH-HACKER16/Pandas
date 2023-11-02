import pandas as pd

data = ['2020-07-23', '2019-10-12', '2019-07-03','2020-01-28','2018-12-14']
x = pd.DataFrame({'date_strings': data})

pd.to_datetime(x['date_strings'], format='%Y-%m-%d')

print(x)