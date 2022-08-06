# 1 - Add element into the list

# 1 - append()
# its is a list method which is used to add element into the list from the ending
# syntax

# list_object.append(data)   # it takes 1 argument as data

ls = []  # empty list
print(ls)

name = "junaid"
age = 26
location = "mumbai"

ls.append(name)
print(ls)

ls.append(age)
print(ls)

# Example 
name = []

for i in range(5):
    n = input("Enter name :")
    name.append(n)

print(name)


# 2 - insert()
# insert method is list method which is used to add elemeent into the list
# it adds data into the specific position

# list have index position system ,index always start from 0

# syntax
# list_object.insert(position,data)



ls = ['junaid', 'ansari', 'ayaan', 'khan', 'cat']
print(ls)

data = "python"
ls.insert(1 , data)
print(ls)

data1 = 456
ls.insert(0 , data1)
print(ls)


# Example

ls = ["name","age"]
print(ls)
print(len(ls))

ls.append([1,2,3])
print(ls)
print(len(ls))

# 3 - extend()

# it is used to add multiple data at the same time
# at the ending position 
# syntax

# list_object.extend(collection of data)


ls = ["junaid","ansari","ayaan"]
print(ls)
print(len(ls))

names = ["cat","dog","fish"]

ls.extend(names)
print(ls)
print(len(ls))




















