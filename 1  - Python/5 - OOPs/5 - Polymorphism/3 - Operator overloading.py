# 2 - operator overloading


#1 -  basic operator understanding
'''
# Addition 
print(10 + 20)   #30

a = int.__add__(10,20)
print(a)

# concatinaion
print("10" + "20")

c = str.__add__("10","20")
print(c)

# Substraction 
print(20 - 10)


s = int.__sub__(20,10)

print(s)

'''
# 2 - magic methods

'''
a = 10
b = 20
print(a + b)
'''
# Example 1
'''

class A:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num - other.num
        

class B:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num * other.num


a = A(10)
b = B(20)

print(b + a)  # Multiplication
print(a + b)   # substraction
print(10 + 20) # addition 
'''
# Example 2
'''
class A:
    def __init__(self,a,b):
        self.a = a   # 100
        self.b = b   # 20

    def __sub__(self,other):
        return (self.a + self.b) - (other.c + other.d)
                #(100 + 20) - (50 + 60)
class B:
    def __init__(self,c,d):
        self.c = c   # 50
        self.d = d   # 60

x = A(100 , 20)
y = B(50 , 60)


print(x - y)     #A.__sub__((10,20) , (50 , 60))  #10

'''

# Query


class A:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num - other.num
        

class B:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num * other.num


a = A(10)
b = B(20)

print( a + b)
10 + 20
'''

+ (__add__() # magic method )
   10 + 10       = 20
   "10" + "10"   = 1010 

class int:
   def __add__():



class str:
    def __add__():


'''





































