
# frozenset()


#fuction returns an unchangeable frozen object
# which is look like a set but unchageable

# syntax
# frozenset(itterable)

s1 = {1,2,3,4,5,6} # set

# set comprehension

cube = {i**3 for i in s1}
print(cube)

cube  = frozenset(cube)
print(cube)
