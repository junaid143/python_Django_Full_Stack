

# Basic Example

# take input from user and show the number is negaive ,positive or its a zero

'''
num = int(input("Enter Number :"))

if (num > 0 ):
    # body of if
    print(num , "is Positive ...")


elif (num == 0):
    # body of elif
    print(num , "its a Nutral ...")

else:
    # body of else
    print(num , "is Negative ")
'''


# Nested if condition
'''

n = int(input("Enter Number :"))

if (n < 0):
    # body of if
    print(n , "Number is Negative .....")

else:
    # body of else
    if (n > 0): # nested if
        # body of nested if
        print(n ,"Number is Positive ....")
        
    else:
        # body of nested else
        print(n , "Its Nutral Number ....")

'''

# find the greates Number in between 3 Numbers 
'''
a = int(input("Enter Number :"))
b = int(input("Enter Number :"))
c = int(input("Enter Number :"))


if ( a  > b):
    # body of if
    if ( a > c):   # nested Condition
        # body of Nested if
        print(a , "is greater ")
    else:
        # body of Nested else
        print(c , "is greater ")

else:
    # body of else
    if ( b > c):
        print(b , "is greater ")
    else:
        print(c , "is greater ")


'''

# Find the greates Number in between 4
# Nestes if Example 
'''
a = int(input("Enter Number :"))
b = int(input("Enter Number :"))
c = int(input("Enter Number :"))
d = int(input("Enter Number :"))

if (a > b):
    if (a > c):
        if (a > d):
            print(a ,"is greater")
        else:
            print(d ,"is greater")

    else:
        if (c > d):
            print(c,"is greater")
        else:
            print(d,"is greater")

else:
    if (b > c):
        if (b > d):
            print(b ,"is greater")
        else:
            print(d,"is greater")

    else:
        if (c > d):
            print(c ,"is greater")
        else:
            print(d,"is greater ")
'''


# Find the greates Number in between 4
# if elif else

a = int(input("Enter Number :")) 
b = int(input("Enter Number :")) 
c = int(input("Enter Number :")) 
d = int(input("Enter Number :")) 

if (a > b) and (a > c) and (a > d):
    print(a ,"is greater ")

elif (b > a) and (b > c) and (b > d):
    print(b,"is greater")

elif (c > a) and (c > b) and (c > d):
    print(c ,"is greater")

else:
    print(d,"is greater ")
    



































