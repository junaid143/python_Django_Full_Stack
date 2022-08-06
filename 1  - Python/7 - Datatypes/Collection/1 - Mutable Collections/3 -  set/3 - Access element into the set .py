# access element into the set

s1  = {'C++', 'C', 'Mysql', 'python', 'java' , 'ruby','android'}
print(s1)

# set dont have any type of position system
# you cant access elemenet from the set directly

# we can used logic for access element

# 1 - type casting
# change the set to other collection time

s2 = list(s1)  # set converted into the list
print(s2)

# 2 - set is itterable (for loop )

for i in s1: # s1 is a set 
    print(i)

