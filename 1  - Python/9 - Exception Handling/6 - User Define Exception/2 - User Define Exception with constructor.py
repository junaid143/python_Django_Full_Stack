
# user define Exception Example

# Guess the Number program 

import sys
import random

class Error(Exception):
    def __init__(self,msg):
        self.msg = msg
        return msg

class SmallError(Error):
    def __init__(self,msg):
        self.msg = msg
        print(msg)

class LargError(Error):
    def __init__(self,msg):
        self.msg = msg
        print(msg)


while True :

    n = random.randint(1,6)
    print("\n",n)
    user = int(input("Guess The Number :"))
    if user > n:
        raise LargError("Guess Number is Greater Then Actual Number ...")
    elif user < n:
        raise SmallError("Guess Number is Smaller Then Actual Number ...")
    else:
        print("Perfect Number ...")
