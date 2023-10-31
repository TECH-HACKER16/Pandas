import pandas as pd

College = {
    'Course_name' : ["CSE","IT","ECE","EEE","MECH","CIVIL"],
}
data = {
    'Seats allotted' : [60,120,240,120,180,120]
}
x = pd.DataFrame(College)
y = pd.DataFrame(data)
print(x)

z = int(input("Input Sno to find seats allotted : "))
print("\n",x.loc[z].to_string(),"\n",y.loc[z].to_string(),"\n") ## Excluding display of data types(used) in output
