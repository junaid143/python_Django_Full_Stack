

# Multiple Exception 


'''
When Multiple of exception handle with a multiple except block its a single exception
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

except ValueError as e:
    sys.stderr.write(f"Can Not Convert Data {e}\n")

except ZeroDivisionError as e1:
    sys.stderr.write(f"Can Not Divis=d any Number By zero")
    
