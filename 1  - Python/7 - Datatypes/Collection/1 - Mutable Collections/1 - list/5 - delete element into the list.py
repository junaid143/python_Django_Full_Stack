

# delete element into the list

ls = ['a','b','c','d','e','f','g','h']

print(ls)
print(len(ls))

# 1 - remove()
# list_object.remove(element)
# it is used to delete element from the list # using element name

ls.remove('c')
print(ls)
print(len(ls))

# 2 - pop()

# list_object.pop(index)  # index is optional 
# delete using index position
# by default delete ending position data 
ls = ['a','b','c','d','e','f','g','h']
print(ls)
print(len(ls))

# Example 

ls.pop()
print(ls)
print(len(ls))

# Example
ls.pop(0)
print(ls)
print(len(ls))

# 3 - del 

# it is used to delete object memory
'''
a = 10
print(a)

del a

print(a)
'''

# Example 

ls = ['a','b','c','d',['e','f','g'],'h']  #
print(ls)

del ls[2]

print(ls)


del ls[3][1]
print(ls)

































