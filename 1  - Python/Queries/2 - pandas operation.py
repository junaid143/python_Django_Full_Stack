

# pandas operation

import pandas as pd

'''
name = ["ayaan","sohail","zaid","shan","shaz"]
age = [26 , 20 , 24 , 20 , 22]
location = ["mumbai","vashi","kurla","chembur","thane"]

data = {
    "Name":name,
    "Age":age,
    "Location":location
    }

#print(data)

# convert dictionary to dataframe

df = pd.DataFrame(data)
print(df)
print(type(df))

# convert DataFrame to excel file
# openpyxl

df.to_excel("data.xlsx", index = False)
df.to_csv("data.csv",index = False)

'''


# read excel or csv data

df = pd.read_excel("data.xlsx")
print(df)
print(type(df))
print()
# read csv file

df1 = pd.read_csv("data.csv")
print(df1)
print(type(df1))
print()

# extract single column only Values

name = df["Name"].values
print(name)
print("DImension of the array :",name.ndim)
print("Shape of the array :",name.shape)
print()


name = name.reshape(-1,1)
print(name)
#extract multiple columns only values


cols = df[["Name","Location"]].values
print(cols)
print("DImension of the array :",cols.ndim)
print("Shape of the array :",cols.shape)
print()




























