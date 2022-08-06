# Operations 


# read csv file 

import pandas as pd

# dataframe 
df = pd.read_csv("weather_data.csv")
print(df)
print()

# Q.1 - find the maximum temp

temp = df["Temp"].max()
print(f"Maximum Temp is {temp}")

# Q.2 Find the minimum Temp

temp1 = df["Temp"].min()
print(f"Minimum Temp is {temp1}")

# Q.3 Find the average Windspeed

avg = df['Windspeed'].mean()
print(f"Average Windspeed is {avg}")

# Q.4 Show the day which hav max temp

day = df[df["Temp"] == df["Temp"].max()]
print(day)

# Q.5 Show only rainy Event data

rain = df[df["Event"] == "rainy"]
print(rain)






