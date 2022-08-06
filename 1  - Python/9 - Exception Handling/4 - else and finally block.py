

# Exception With else and Finally block 

# else block
'''
The else block lets you execute code when there is no error.
'''


# finally block
'''
Finally block execute anyway
'''

#eg

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
    
else:
    print("There is No Error ...")

finally:
    print("Program Finish ...")
