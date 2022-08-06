

# array
# array is a collection of same datatype
# numpy or arr (we can create array )

import numpy as np

arr = np.array([1,2,3,4,5,6])  # 1   (6,)
print(arr)
print(type(arr))
print(f"Dimesnion of the array :{arr.ndim}")
print(f"Shape of the array :{arr.shape}")



# (3,2)

arr2 = np.array([[1,2],
                 [4,5],
                 [7,8]])

print(arr2)
print(type(arr2))
print(f"Dimesnion of the array :{arr2.ndim}")
print(f"Shape of the array :{arr2.shape}")


# methods to create array

# 1 - arange()
# 2 - ones()
# 3 - zeros()

# 1 - arange()
# arange is similer to range()
# arange is used to create sequence of int numbers in the form of array
# generated array always in 1D

arr = np.arange(1 ,9)
print(arr)
print("Dimension of the array ",arr.ndim)
print("Shape of the array ",arr.shape)
print()

# reshape
# convert 

# arr 1D array to 2D array (2,4)

arr1 = arr.reshape(2,4)
print(arr1)
print("Dimension of the array ",arr1.ndim)
print("Shape of the array ",arr1.shape)
print()


# arr 1D array to 2D array (4,2)

arr2 = arr.reshape(4,2)
print(arr2)
print("Dimension of the array ",arr2.ndim)
print("Shape of the array ",arr2.shape)
print()


# arr 1D array to 2D array (1,8)

arr3 = arr.reshape(1,-1)  # single row and multiple column 
print(arr3)
print("Dimension of the array ",arr3.ndim)
print("Shape of the array ",arr3.shape)
print()


arr3 = arr.reshape(-1,1)  # single column and multiple row 
print(arr3)
print("Dimension of the array ",arr3.ndim)
print("Shape of the array ",arr3.shape)
print()


# convert 2D into 1D array

arr4 = arr3.reshape(8)
print(arr4)
print("Dimension of the array ",arr4.ndim)
print("Shape of the array ",arr4.shape)
print()


# method

arr5 = arr3.flatten()
print(arr5)
print("Dimension of the array ",arr5.ndim)
print("Shape of the array ",arr5.shape)
print()



# 2 - ones()

o = np.ones((3,3))
print(o)
print(type(o))
print("Dimension of the array ",o.ndim)
print("Shape of the array ",o.shape)
print("Datatype inside the array :",o.dtype)
print()

# create ones array in int datatype
o1 = np.ones((3,3),dtype = np.int64)
print(o1)
print(type(o1))
print("Dimension of the array ",o1.ndim)
print("Shape of the array ",o1.shape)
print("Datatype inside the array :",o1.dtype)
print()

# 3 - zeros()


z = np.zeros((3,4))
print(z)
print(type(z))
print("Dimension of the array ",z.ndim)
print("Shape of the array ",z.shape)
print("Datatype inside the array :",z.dtype)
print()


#
z1 = np.zeros((3,4) , dtype=np.int64)
print(z1)
print(type(z1))
print("Dimension of the array ",z1.ndim)
print("Shape of the array ",z1.shape)
print("Datatype inside the array :",z1.dtype)
print()


















































