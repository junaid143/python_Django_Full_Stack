#Dimension of array

import numpy as np

# 1  - 1 Dimentional Array

arr = np.array(["Name","Age","Contact","Location"])
print(arr)

# find the hape of the array 
print("shape of the array : ",arr.shape)

# dimenssion of the array
print("Dimension of the arr : ",arr.ndim)



# 2 - 2 Dimentional Array

arr2 = np.array([
    ["junaid","26","789654185","Mumbai"],
    ["ayaan","18","852474185","Navi Mumbai"],
    ["sohail","36","6852147968","Thane"]])

print(arr2)

print("Shape of the array ",arr2.shape)

print("Dimension of the array is :",arr2.ndim)

# Example 2

arr_2 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]])
print(arr_2)
print(arr_2.shape)
print(arr_2.ndim)

















