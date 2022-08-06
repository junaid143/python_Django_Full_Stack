
# Example 1

# guess the Number 

import sys
import random

class Error(Exception):
    pass

class SmallError(Error):
    pass

class LargError(Error):
    pass

while True :

    n = random.randint(1,6)
    print("\n",n)
    user = int(input("Guess The Number :"))
    try:
        if user > n:
            raise LargError
        elif user < n:
            raise SmallError
        else:
            print("Perfect Number ...")

    except LargError:
        sys.stderr.write("Guess Number is Greater then Actual Number ..\n")

    except SmallError:
        sys.stderr.write("Guess Number is Smaller then Actual Number ...\n")
        
