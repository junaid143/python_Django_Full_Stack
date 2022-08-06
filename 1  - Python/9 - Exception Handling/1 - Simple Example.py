
# Exception Definition
'''
An exception is an event,
which occurs during the execution of a program
that disrupts the normal flow of the program's instructions.

Exception is a Runtime Error 
'''


#=========================================================
# Built-in Exceptions in Python
'''
1 - NameError
2 - ValueError
3 - TypeError
4 - IndexError
5 - ZeroDivisionError
'''

#=========================================================

# Example 1

#1 - NameError

'''
NameError is a kind of error in python
that occurs when executing a function, variable, library or string
without quotes that have been typed in the code
without any previous Declaration
'''

# eg

print(name)



#=========================================================

# Example 2

#2 - ValueError

'''
ValueError in Python is raised
when a user gives an invalid value to a function
but is of a valid argument

'''

# eg

a = int("python") # int required a int value not str


#=========================================================

# Example 3

# 3 - TypeError

'''
TypeError is an exception in Python programming language
that occurs when the data type of objects in an operation is inappropriate

'''


# eg

print(10 + "a")



#=========================================================

# Example 4

# 4 - IndexError

'''
IndexError is an exception in python that occurs
when we try to access an element from a list or tuple from an index
that is not present in the list
'''

# eg

ls = [ "a" , "b" , "c" ]

data = ls[3]

print(data)


#=========================================================

# Example 5

# 5 - ZeroDivisionError

'''
The Python "ZeroDivisionError: float division by zero" occurs
when we try to divide a floating-point number by 0 .
'''

# eg 

print(20 / 0)






































