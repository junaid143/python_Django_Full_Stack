# cube of the list data

# Example 1
'''
ls = [8,6,2,4,5,7,3,6,12,20,41]  # given list 
c = []
for i in ls:
    c.append(i ** 3)
print(c)
'''


# Example 2
'''
ls = [20,1,-2,-4,-35,42,6,-4,25,-14,15] # given list
p = []

for i in ls:
    if i >0:
        p.append(i)
print(p)
'''
# Example 3
'''
ls = [4,6,8,2,3,55,7,41,25,10] # given list
print(ls)
# find the odd numbers and add into list odd
# find the even numbers and add into list even

odd = []
even = []

for i in ls:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)    

# Comprehesion Syntax
# What is comprehension ?

# why comprehension is used ? 

# 1 - logic
# 2 - operation

# obj = [operation logic]

# list Comprehesion
# generate cube of the element

ls = [8,6,2,4,5,7,3,6,12,20,41]  # given list 
c = [i**3 for i in ls] 
print(c)
'''
# Question 1
# make every character in string data as a elemenet in list ch
# first use simple program then use comprehesion 
'''
data = "Hello class this is python"
ch = []

# method 1

ch = list(zip(*data))
print(ch)
print(len(ch))


for i in data:
    ch.append(i)

print(ch)
print(len(ch))
'''


#  Question 2
# seperate positive numbers in list p

ls = [20,1,-2,-4,-35,42,6,-4,25,-14,15] # given list
'''
p = []
for i in ls:
    if i>0:
        p.append(i)
print(p)

# list comprehension using if condition
# Syntax

# 1 - logic
# 2 - operation

p = [i for i in ls if i>0]
print(p)
'''
# Question
# add only those fruits name which have alphabt "a"
'''
fruits = ["apple","banana","cherry","kiwi","mango","orange"]
f = []

for word in fruits:
    if "a" in word:
        f.append(word)

print(f)

# comprehension 

f = [element for element in fruits if "a" in element]
print(f)
'''

# Q3
# odd even 
ls = [4,6,8,2,3,55,7,41,25,10] # given list
print(ls)

# Example 1
'''
# comprehension with if 
even = [i for i in ls if i%2 == 0]
odd = [i for i in ls if i%2 != 0]

print(even)
print(odd)
'''
# Example
# list comprehension with if else

odd = []
even = [i if i%2==0 else odd.append(i) for i in ls] #
print(even)
# 1 way
e = []
for i in even:
    if i is not None:
        e.append(i)
# comprehension 
e = [i for i in even if i != None]
print(e)

# filter with lambda function
fun = lambda n: n!=None
e = list(filter(fun ,even))   # syntax  filter(function , itterable)
print(e)

# user define function
def e(num):
    if num != None:
        return num

x = list(filter(e , even))
print(x)

# direct method (works only with None)
y = list(filter(None,even))
print(y)














