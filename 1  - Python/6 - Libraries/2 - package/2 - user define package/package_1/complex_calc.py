
# This module is used for complex calculation


def factorial(num):
    '''
    Take 1 argument and return factorial of the number 
    '''
    
    if num <= 0:
        return "Cant Find Factorial"
    else:
        fact = 1
        for i in range(num,0,-1):
            fact = fact*i

        return fact


def percentage(total,obtain):
    if total < obtain:
        total,obtain = obtain,total
    per = obtain/total *100
    return per














