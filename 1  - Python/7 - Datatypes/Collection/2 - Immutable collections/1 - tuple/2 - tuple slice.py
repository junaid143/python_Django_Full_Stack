# tuple slicng

tp = ('a','b','c','d','e','f','g','h','i')
#print(tp)

#print(len(tp))

# index
# index is a position system
# 1 - positive index
    # always start from 0
    # count start with left to right
    # system bydefault used positive index

# 2 - reverse / Negative index
    # count start with right to left
    # always start from -1


# access single elemenet

d = tp[1]
print(d)

d1 = tp[-8]
print(d1)

# slicing
# access multiple element in sequence 

# example
'''
tp = ('a','b','c','d','e','f','g','h','i')
print(tp)

# slicing syntax
# obj[start_position : end_position]


# b to f
d = tp[ 1: 6]
print(d)

# a to e

d1 =tp[0:5]
print(d1)

d2 = tp[ :5]
print(d2)

# e to i
d3 = tp[4:]
print(d3)
'''

# slicing with reverse index

tp = ('a','b','c','d','e','f','g','h','i')
print(tp)

# c to f # midd data

d = tp[ -7: -3]
print(d)

# a to e

d1 =tp[-9:-4]
print(d1)

d2 = tp[:-4]
print(d2)

# f to i
d3 = tp[-4:]
print(d3)

# c to f # combination of positive and revers index
d4 =tp[-7:6]
print(d4)
d5 = tp[2:-3]
print(d5)
































