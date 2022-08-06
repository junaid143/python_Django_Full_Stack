#1 - Advantages of oops
#2 - Multiple inheritence
#3 - lambda function





#1 - Advantages of oops

# Attributes represent class behaviour
# Method represent class functionality


# 1 - Re-usability
# 2 - Data Redundancy
# 3 - Code Maintanace
# 4 - Security (encapsulation : hiding the data from outside the class (Wrapping the attributes and methods in a single entity)
                #abstraction : Hiding the actual implementation from outside world )

# 5 - Design Benifis  
# 6 - Better Productivity
# 7 - Easy Troubleshooting
# 8 - Polymorphism flexibility  (one object can take many forms )




#2 -  Multiple Inheritence

'''
class A:   
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def m1(self):
        print(f"Name is {self.name} and age is {self.age}")

class B:
    def __init__(self,location):
        self.location = location
        

    def m2(self):
        print(f"Location is : {self.location}")


class C(A,B):
    def __init__(self,emp_id,emp_salary,name,age,location):
        super().__init__(name ,age)
        B.__init__(self,location)
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def m3(self):
        print(f"Employe id is : {self.emp_id} and emp_salary is : {self.emp_salary}")

suraj = C("emp_123",5000,"Suraj",21,"Mumbai")
'''


# 3 - lambda function
# Functions : we can re-use the block of code

# 1 - lambda function : it is used for small execution
# 2 - because it a single line execution function

# syntax  :

#obj = lambda list_of_para(optional) : Expression(operation)


# Addition Example 1
'''
add = lambda num_1,num_2 : "Addition is : "+str(num_1 + num_2)

print(add(20,30))
'''

# Square of the Number Example 2
'''
square = lambda num : "Square of the Number is : "+str(num**2)
print(square(45))
'''


# Right angle triangle pattern using lambda function
ptr = "* "

p = lambda ptr,num : ptr*num

for i in range(1,8):
    print(p(ptr,i))


'''
print(p(ptr,1))
print(p(ptr,2))
print(p(ptr,3))
print(p(ptr,4))
print(p(ptr,5))
'''


















