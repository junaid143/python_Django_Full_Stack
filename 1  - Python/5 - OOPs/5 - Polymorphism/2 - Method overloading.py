
# 1 - method overloading

# c++ ,java 
# other language definition
# in a single class have multiple of method with the same name but different parameter
# it is called method overloading


# This Definition is not applicable in Python (because python is Dynamic Programming Language )

# Example
'''
class calc:
    def __init__(self):
        pass

    def add(self):
        print("This is 1st addition method ")

    def add(self,a):
        print("This is 2nd Addition method")

    def add(self,a,b):
        print("This is 3rd Addition method ")

a = calc()
a.add()
'''


# In python we can achine method overloading using parameters

# one method can take single parameter and perform operation also the same method can take 2 para
# and  perform operation  one method can perfom multiple operation

# example builtin len()
# len() is polymorphic method

ls = [1,2,3,4,5,6,7,8,9]

st = "python is awsom"

print(len(st))    

# method overloading 1

class calc:
    def __init__(self):
        pass

    def add(self,*args):
        
        s = 0
        for i in args:
            s = s+i
        print(s)

c = calc()
c.add(10)
c.add(10,20)
c.add(10,20,30)


# Example 2
import multipledispatch
from multipledispatch import dispatch

# download library
# 1 - open cmd
# type
#>>>pip install multipledispatch

class calc:
    def __init__(self):
        pass

    @dispatch(int)
    def add(self,a):
        print("1st Addition ",a)

    @dispatch(int,int)
    def add(self,a,b):
        print("2nd Addition ",a+b)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print("3rd Addition ",a+b+c)
        
a = calc()
a.add(20)
a.add(20,30)
a.add(20,30,50)







       
