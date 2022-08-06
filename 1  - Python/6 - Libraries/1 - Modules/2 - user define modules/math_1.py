

# this is user define module
# this module helps with maths function


def addition(*args):
    '''
    This addition function it takes multiple int argumen and return
    sum of that numbers 
    '''
    s = 0
    for i in args:
        s += i
    return s

def substraction(num_1 , num_2):
    '''
    This is substraction function it is used to substract the int values
    it takes 2 arguments and return substraction
    '''
    return num_1 - num_2

def division(num_1 , num_2):
    '''
    This function takes 2 argument as int or float and return true Division
    in form of float data 
    '''
    if num_2 == 0:
        return "cant divid any number by zero"
    else:
        return num_1 / num_2
        













































