# list slicing

# access multiple of element in a sequence

# for that we required index position system

ls = ['a','b','c','d','e','f','g','h']

# index
# index is a position system

# we have two type of index
#1 - positive index
    # bydefault system used positive index system

    # index position always start from 0
    # and element counting start from left to right  

# 2 - negative / reverse index
    # index always start from -1
    # element count start from right to left
    

# 1 - Access single element

# d 
ls = ['a','b','c','d','e','f','g','h']

data = ls[3]  # positive indexing
print(data)

data1 = ls[-5] # reverse indexing 
print(data1)

# 2 - list slicing 
#syntax

#list_object[ start_position : end_position ]

ls = ['a','b','c','d','e','f','g','h']

# access 'c' to 'f'

sl = ls[ 2 : 6]   # positive index
print(sl)

sl1 = ls[-6 : -2] # reversed index 
print(sl1)


# access  'a' to 'e'

s = ls[ 0: 5]
print(s)

s1 = ls[ : 5] # bydefault 0
print(s1)

s2 = ls[-8 : -3]  # reversed index
print(s2)

s3 = ls[ : -3]  # combination
print(s3)

# access 'd' to 'h'

s = ls[3 : ]
print(s)

s1 = ls[-5: ]
print(s1)


# Example

print(ls[ : ])



















