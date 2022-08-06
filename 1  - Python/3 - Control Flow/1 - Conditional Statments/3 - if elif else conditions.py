
# if elif else Conditions

# basic Program

'''

num = int(input("Enter Number :"))


if (num >= 0):
    print("Positive Number ...")

else:
    print("Negative Number ...")

'''

# Example 1
'''

num = int(input("Enter Number :"))

if (num > 0):
    print(num , "Positive Number ...")


elif (num < 0):
    print(num , "Negative Number ...")

else:
    print(num ,"is Nutral ...")

'''



# Basic Calc
'''
1 - Addition
2 - Substraction
3 - Multiplication
4 - Division
5 - Percentage


Enter Your Choice :1

Enter Number for Multiplication :3
Enter Number for Multiplication :2
Multiplication is :6

'''

# Basic Calc Example
'''
print("1 - Addition")
print("2 - Substraction")
print("3 - Multiplication ")
print("4 - Division")
print("5 - Percentage ")

choice = input("Enter Your Choice :") # '1'

if (choice == '1'):
    # body of if
    a = int(input("ENter Number For Adition :"))
    b = int(input("ENter Number For Adition :"))
    print("Addition is :",a+b)

elif (choice == '2'):
    
    a = int(input("Enter Number For Substraction :"))
    b = int(input("Enter Number For Substraction :"))
    print("Substraction is :",a-b)

elif (choice == '3'):
    
    a = int(input("Enter Number For multiplication :"))
    b = int(input("Enter Number For multiplication :"))
    print("multiplication is :",a*b)

elif (choice == '4'):
    
    a = int(input("Enter Number For Division :"))
    b = int(input("Enter Number For Division :"))
    print("Division is :",a/b)

elif (choice == '5'):
    total = int(input("Enter Total Number :"))
    obtain = int(input("Enter Obtain Number :"))
    per = (obtain/total) * 100

    print("Percentage is :",per)


else:
    print("Invalid Choice ...")






# Basic  Calculator with logical Operator

print("1 - Addition")
print("2 - Substraction")
print("3 - Multiplication ")
print("4 - Division")
print("5 - Percentage ")

choice = input("Enter Your Choice :") # sub

if (choice == '1') or (choice == 'add'):
    a = int(input("Enter Number for Addition :"))
    b = int(input("Enter Number for Addition :"))
    print("Addition is :",a+b)  # 

elif (choice == '2') or (choice == 'sub'):

    a = int(input("Enter Number for Substraction :"))
    b = int(input("Enter Number for Substraction :"))
    print("Substraction is :",a-b)

'''




# 1 , add  , ADD , Add , ADDITION , addition , Addition ,+
# 2 , sub  ,SUB , Sub , SUBSTRACTION , substraction , Substraction , -
# 3 , mul , MUL , Mul , MULTIPLICATION , multiplication , Multiplication , *
# 4 
# 5 

add = ('1' , 'add'  , 'ADD' , 'Add' , 'ADDITION' , 'addition' , 'Addition' ,'+')
sub = []
ch = input("Enter Your Choice :")

if (ch in add):
    
    a = int(input("Enter Number for Addition :"))
    b = int(input("Enter Number for Addition :"))
    print("Addition is :",a+b)

elif (ch in sub):



































