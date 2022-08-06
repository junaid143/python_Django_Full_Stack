
# read csv file 

import pandas as pd

# dataframe 
df = pd.read_csv("weather_data.csv")
print(df)
print()

# extract multiple columns

multi_col = df[["Days","Event"]]
print(multi_col)
print(type(multi_col))


# extract single col

temp = df["Temp"]
print(temp)
print(type(temp))


# Extract single column values only

day = df["Days"].values
print(day)
print(type(day))
print(day.ndim)
print(day.shape)
day = day.reshape(-1,1)
print(day)


# extract multiple column values only

cols = df[["Days","Event"]].values
print(cols)
print(cols.shape)
print(cols.ndim)










