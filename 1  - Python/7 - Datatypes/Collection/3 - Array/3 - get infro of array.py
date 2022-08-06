# get info of array

import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]])

print(arr)

# 1 - Check Dimension

print("Dimension ",arr.ndim)

# 2 - Check shape

print("Shape ",arr.shape)

# 3 - size of array

print("Size  ",arr.size)

# 4 - memory consume sigle elemenet

print(arr.itemsize)

# 5 - check datatype

print(arr.dtype)



