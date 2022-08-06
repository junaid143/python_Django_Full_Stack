

# Single Exception 


'''
When Multiple of exception handle with a single except block its a single exception
'''

#eg

'''
ValueError
ZeroDivisionError
'''

import sys

try:
    a = int(input("Enter Number "))
    b = int(input("Enter Number "))

    print(a+b)
    print(a/b)

except:
    sys.stderr.write("This is Error ...\n")

    
