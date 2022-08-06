# dictionary comprehension
'''
k =[1,2,3,4,5]
v =['a' , 'b' , 'c' , 'd' , 'e']

# {1:'a' , 2: 'b' , 3: 'c', 4:'d' , 5:'e'}

# example 1

d = dict(zip(k,v))
print(d)

#z = zip(k,v)# ((1,a),(2,b),(3,c))
d = {k:v for k,v in zip(k,v)}
print(d)
'''
# example 2
ls = [2,3,4,5,6]

# {2 :4 , 3 :9 , 4:16 ,5:25 ,6 :36}
d = {i:i**2 for i in ls}
print(d[3])
