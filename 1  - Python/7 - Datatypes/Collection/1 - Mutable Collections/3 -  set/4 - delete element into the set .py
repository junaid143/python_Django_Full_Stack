# Delete elemenet into the set
# set is a unordered colection
'''
s1  = {'C++', 'C', 'Mysql', 'python', 'java' , 'ruby','android'}
print(s1)
print(len(s1))
# 1 - remove()
# remove() is used to delete the set element
# it takes 1 argument as an element ,if element not present inside the set
# it raise error
# syntax
# set_obj.remove(elemet)

data = "java"
s1.remove(data)
s1.remove("java")
print(s1)
print(len(s1))

# 2 - discard()
# discard() is used to delete elemet
# it take one argument as element , if elemenet not present inside the set
# dont raise any error 
# syntax
# set_obj.discard(element)
s1  = {'C++', 'C', 'Mysql', 'python', 'java' , 'ruby','android'}
print(s1)
print(len(s1))

s1.discard("java")
s1.discard("java")
print(s1)
print(len(s1))
'''

# 3 - pop()
# bydefault its remove the last data
# set is a unordered collection we dont knw which element is removed

s1  = {'C++', 'C', 'Mysql', 'python', 'java' , 'ruby','android'}
print(s1)
print(len(s1))

s1.pop()
print(s1)
print(len(s1))

# 4 - clear()
s2 = {1,2,3,4,5}
print(s2)
s2.clear()

print(s2)

# 5 - del # del is a keyword which is used to delete any object
s2 = {1,2,3,4,5}
print(s2)

del s2
print(s2)




















