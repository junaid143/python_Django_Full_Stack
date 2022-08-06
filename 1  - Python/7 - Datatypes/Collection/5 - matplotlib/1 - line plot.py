

# import library
'''
import pandas as pd
import matplotlib.pyplot as plt


# read excel data into dataframe

df = pd.read_excel("weather_data1.xlsx")
print(df)


# Extract columns

days = df['Days'].values
temp = df['Temp'].values


# plot graph  (line plot)

plt.title("Weather Data")

plt.xlabel("Days")
plt.ylabel("Temp")

plt.plot(days , temp , marker = "*" , markersize = 15)

plt.show()



# plot 2
plt.title("Weather Data")

plt.xlabel("Days")
plt.ylabel("Temp")

plt.plot(days , temp , marker = "*" , markersize = 15 , color = "red" , markerfacecolor = "blue",linestyle = "dotted",linewidth = 5)

plt.show()
'''
# 

# plot multiple graphs

import matplotlib.pyplot as plt

x = ["MOn","Tues","Wed","Thur","Fri","Sat","Sun"]

min_temp = [21,19,22,20,21,24,20]
avg_temp = [25,22,26,24,23,26,24]
max_temp = [28,27,29,26,30,29,28]

plt.title("Weather Data")
plt.xlabel("Days")
plt.ylabel("Temp")

plt.plot(x,min_temp , color = "blue",marker = "*" , label = "Min Temp")
plt.plot(x,avg_temp, color = "green",marker = "+", label = "Avg Temp")
plt.plot(x,max_temp, color = "red",marker = "o", label = "Max Temp")

plt.legend()

plt.show()































