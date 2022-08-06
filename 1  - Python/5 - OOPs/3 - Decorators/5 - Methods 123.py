# type of method

# 1 - instance method
# 2 - class method
# 3 - static method

# Example

class Employee:
    salary = 10000   # class attribute/static attribute
    def __init__(self,name,age,location):
        self.name = name                  # instance attribute 
        self.age = age
        self.location = location

    def get_employee_info(self):  # instance method  
        print("Employee Information")
        print(f"Employee Name is : {self.name}")
        print(f"Employee Age : {self.age}")
        print(f"Employee location : {self.location}")
        print(f"Employee Salry is : {self.salary}")

    def set_employee_info(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        print("Information Updated ")

    @classmethod
    def modify_salary(cls,salary): # class method
        cls.salary = salary

    @staticmethod
    def m1(name):
        print(f"Hello {name} this is static method ")
        print(self.name)


rahul = Employee("Rahul",28,"Mumbai")
vijay = Employee("Vijay",22,"Navi Mumbai")






        


        
