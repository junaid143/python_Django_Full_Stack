# Delete Elemenet From the list

# 1 - pop()
'''
d = {"Name":"Python","cours":["Python","Java","C","C++"],"Location":"Thane"}
print(d)

print(len(d))    

d.pop("Location")
print(d)

print(len(d))    
# 2 - del

del d["cours"][1]
print(d)

print(len(d))   
'''
# 3 popitem()
d = {"Name":"Python","cours":["Python","Java","C","C++"],"Location":"Thane"}
print(d)
print(len(d))

d.popitem()
print(d)
print(len(d))
