
# create array
import numpy as np

# 1 - zeros method

# default datatype float
z = np.zeros((4,3))
print(z)

# check datatype
print(z.dtype)

print(type(z[0][0]))

# create int array
z1 = np.zeros((4,3),dtype = np.int32)
print(z1)
print(z1.dtype)

# 2 - ones method 

one = np.ones((3,4),dtype = np.int32)
print(one)

# 3 - arange() method
# generate range of int number in form of array collection
# generate 1D array

x = np.arange(1,11)
print(x)







