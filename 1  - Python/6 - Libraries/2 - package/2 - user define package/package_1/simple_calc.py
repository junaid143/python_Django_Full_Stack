
# This module is used only for simple calculation

# Addition 
def addition(*args):
    '''
    THis is for addition 
    '''
    s = 0
    for i in args:
        s = s+ i
    return s
    
# substraction
def substraction(num , num1):
    return num - num1

#multiplication
def multiplication(*args):
    m = 1
    for i in args:
        m = m*i

    return m

#Division
def Division(num ,num1):
    if num1 == 0:
        return "Cant divit any number by zero"
    else:
        return num/num1
















