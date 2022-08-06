
# list methods


# 1 - copy()
# copy() returns a copy of the specific list

ls = [1,2,3,4,5,6]
print(ls)
ls1 = ls.copy()
print(ls1)

ls1.pop()
print(ls1)
print(ls)

# 2 - clear()
# clear method removes all the elements from a list

ls = [1,2,3,4,5,6]
print(ls)

ls.clear()
print(ls)

# 3 - count() # its works on index basis 
# count method returns a value count in the list 

ls = ['a' , 'b' , 'c' , 'a' ,'a' , 'c']
print(ls)
print(len(ls))

c = ls.count('a')
print(c)
c1 = ls.count('b')
print(c1)
c2 = ls.count('c')
print(c2)


# 4 - index()
# index() returns the position at the first occurence of the specific value

ls = [12 , 48 , 25 , 45 , 62 , 48 , 20 , 12]
print(ls)
print(len(ls))

i = ls.index(25)
print(i)

i1 = ls.index(48)
print(i1)

# 5 - reverse()

ls = ['a','b','c','d','e','f','g','h','i'] # given list 

# output should be
#rev_ls = ['i','h','g','e','d','c','b','a']

# Solution 1
ls1 = []
for i in range(len(ls)):
    ls1.append(ls.re())
    
print(ls1)

# Solution 2

rev_ls = []

for element in range(len(ls)-1 , -1 , -1):
    n = ls[element]
    rev_ls.append(n)

print(rev_ls)

# Solution 3
ls = ['a','b','c','d','e','f','g','h','i'] # given list
ls.reverse()

print(ls)


# Solution 4

ls = ['a','b','c','d','e','f','g','h','i'] # given list 

ls1 = list(reversed(ls))   #
print(ls1)



# 6 - sort()
# sort() method is used to sort the list ascending default

ls = [4,2,8,3,55,41,0]

ls1 = ["hello","class","python","lecture","cat"]

ls.sort()
print(ls)

ls1.sort()
print(ls1)

# dece
ls = [4,2,8,3,55,41,0]

ls1 = ["hello","class","python","lecture","cat"]

ls.sort(reverse = True)
ls1.sort(reverse = True)

print(ls)
print(ls1)







































