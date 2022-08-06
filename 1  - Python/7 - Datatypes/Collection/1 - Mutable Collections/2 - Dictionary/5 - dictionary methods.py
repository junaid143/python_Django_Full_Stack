# dictionary methods

# 1 - copy() # is used to create copy of the dic
'''
d = {"name":"rahul","age":21,"contact":9876541235}
d1 = d.copy()
print(d1)
'''
# 2 - clear() # is used to clear the dictionary
'''
d = {"name":"rahul","age":21,"contact":9876541235}
print(d)
d.clear()
print(d)
'''
# 3 - fromkeys() # return a dictionary with the specific keys and specified values
'''
k = ("name","age","contact")
v = []
d = dict.fromkeys(k,v)
print(d)
'''
# 4 - values() # return values inside the dictionary 
d = {"name":"rahul","age":21,"contact":9876541235}
k = d.keys()
print(k)

v = d.values()
print(v)

# 5 - items() return zip data 

d = {"name":"rahul","age":21,"contact":9876541235}
print(d)
# [('name','rahul'),('age',21),('contact',9876543216)]
i = d.items()
print(i)

# 6 - update() # update method is used to update dictionary

d = {"name":"rahul","age":21,"contact":9876541235}
print(d)

#d['Location']='Mumbai'
#print(d)

d.update({'Location':'Mumbai'})
print(d)



















