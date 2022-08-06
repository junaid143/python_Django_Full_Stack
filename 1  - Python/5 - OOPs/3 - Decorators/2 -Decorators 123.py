


# decorator is a function wich take function as a parameter and return function also .


# Decorators in Pthon ?

#Decorators are the very powerful and useful tools in python .
#it will allow programmers to modify the behaviour of the function or class .
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function


# type of decorators?
# 1 - Built-in Decorators
# 2 - User Define Decorators




# 1 - Built-in Decorators

# @staticmethod
# @classmethod
# @abstractmethod


# 2 - User Define Decorators

# Example
# Modify the function without change the actual code in div function

'''
def div(a,b):
    print(a/b)
'''
# eg div(2,4) answer should be 0.5
# eg div(4,2) answer should be 0.5

# for that we need to know more about these following things 


# 1 - clear logic (for modification)
# 2 - function arguments
# 3 - inner Function
# 4 - return 




# 1 - clear logic (for modification)

# this is our logic to modify the fnction 

'''

def div(a,b):
    if a > b:
        a,b = b,a

    print(a/b)


div(2,4)   # 0.5
div(4,2)   # 0.5

'''

# 2 - function arguments

# we can give whole function as a argument to the another function

# Example
'''
def inc(x):
    return x+1


def operate(func ,a):
    result = func(a) * 2
    return result

val = operate(inc , 5)

print(val)

'''


# 3 - inner Function

# when we write a function inside a functio it is called inner function


# Example 1 
'''
def show_msg(msg):   # outer function 
    greeting = "Hello "

    def printer(greeting , msg):    # inner function 
        print(greeting , msg)

    
    printer(greeting,msg)

show_msg("This is Python")

'''

# Example 2

def show_msg(msg):   # outer function 
    greeting = "Hello "

    def printer():    # inner function 
        print(greeting , msg)

    
    return printer

fun = show_msg("This is Python")
fun()




































































