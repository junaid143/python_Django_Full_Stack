# download pandas

#>>>pip install pandas



# Dataframe

# dataframe is a commenly used term in pandas
# it is able like structure it has multiple rows and multiple of columns 

import pandas as pd 
'''
# create dataframe
# 1 - Dictionary methods

data = {
    "Days":["Mon","Tues","Wed","Thur","Fri","Sat","Sun"],
    "Temp":[20,25,23,21,26,22,27],
    "Windspeed" :[1.8,2.0,2.5,3.2,3.3,1.5,1.8],
    "Event":["cloudy","sunny","cloudy","rainy","rainy","sunny","cloudy"]}

#print(data)
# convert dataframe

df = pd.DataFrame(data)
print(df)

# create .csv file  # comma seperated values

df.to_csv("weather_data.csv" , index = False)
'''


# create .xls fil usin dataframe

# library
# >>>pip install openpyxl

import pandas as pd 

# create dataframe
# 1 - Dictionary methods

data = {
    "Days":["Mon","Tues","Wed","Thur","Fri","Sat","Sun"],
    "Temp":[20,25,23,21,26,22,27],
    "Windspeed" :[1.8,2.0,2.5,3.2,3.3,1.5,1.8],
    "Event":["cloudy","sunny","cloudy","rainy","rainy","sunny","cloudy"]}

df = pd.DataFrame(data)
print(df)

# create Excel file .xlsx

df.to_excel("weather_data1.xlsx" , index = False)















































