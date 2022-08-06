# Add Element into the set

# 1 -  add() # it takes 1 argument as data and add into the set

# add method add single element at the time

# syntax

#set_obj.add(data)

s1 = set()  # empty set 
print(s1)

# add data

data = "Python"
s1.add(data)
print(s1)

name = "omkar"
age = 22
location = "Thane"

s1.add(name)
s1.add(age)
s1.add(location)
print(s1)

# 2  -update()
# update method is used to add multiple of data at the same time
# update() takes 1 argument as a collection of data

# syntax

# set_obj.update(collection)

s1 = set()   # empty set
print(s1)

data = ["python","java","C","C++","Mysql"]

s1.update(data)
print(s1)





























