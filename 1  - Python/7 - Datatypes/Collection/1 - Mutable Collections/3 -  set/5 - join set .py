# join sets

# 1 - join two sets
#1 - union()
'''
set1 = {1,2,3}
set2 = {'a','b','c'}

set3 = set1.union(set2)
print(set3)
'''
#2 - update()
'''
set1 = {1,2,3}
set2 = {'a','b','c'}

set1.update(set2)
print(set1)
'''
'''
# 2 - intersection_update()   # inner join()
# keep the item that are present in both set
s1 = {1,2,3,4}
s2 = {3,5,7,98}

s1.intersection_update(s2)
print(s1)

# 3 - intersection() # similer as intersection_update()
s1 = {1,2,3,4}
s2 = {3,5,7,98}

s3 = s1.intersection(s2)
print(s3)

'''

# 4 - symmetric_difference()  # keep different data from both sets

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}

s3 = s1.symmetric_difference(s2)
print(s3)










