# Hierarchical Inheritecne



class Details: # A
    def __init__(self):
        self.id = "No Data"
        self.name = "No Data"
        self.age = "No Data"
        self.gender = "No Data"
        print("Constructor A is Ready")

    def set_data(self , id , name ,age, gender):  # setter methods / mutators
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        print("Information Updated ")

    def show_data(self):    # getter method / accessor method 
        print("Personal Info ")
        print(f"Id is : {self.id}")
        print(f"Name is :{self.name}")
        print(f"Age is : {self.age}")
        print(f"Gender : {self.gender}")


class Employee(Details):  # B(A)
    def __init__(self):
        self.company = "No Data"
        self.dep = "No data"

    def set_emp(self, id , name ,age, gender , company ,dep):
        
        self.set_data(id , name ,age, gender)
        self.company = company
        self.dep = dep
        print("Information Updated ")

    def show_emp_info(self):
        
        self.show_data()
        print(f"Company Name : {self.company}")
        print(f"Department : {self.dep}")


class Doctor(Details):
    def __init__(self):
        self.hospital = "No Data"
        self.dept = "No Data"


    def set_emp(self,id , name ,age, gender , hospital ,dept):
        self.set_data( id , name ,age, gender)
        self.hospital = hospital
        self.dept = dept

    def show_emp_info(self):
        self.show_data()
        print(f"Hospital Name : {self.hospital}")
        print(f"Department : {self.dept}")
        



def main():
    rohit = Employee()
    ajay = Doctor()
    
    rohit.set_emp(2021,"Rohit",25,"Male","ABC","Sales")
    ajay.set_emp(102,"Ajay",32,"Male","Apollo","Medicine")

    rohit.show_emp_info()
    ajay.show_emp_info()



main()
'''


# Example 2 


class Person:  # A
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename

    def Display_persn_data(self):
        print("Person Information")
        print(f"Id is : {self.eid}")
        print(f"Name is : {self.ename}")


class Employee(Person):   # B
    def __init__(self,salary,eid,ename):
        super().__init__(eid,ename)
        
        self.salary = salary
        
    def employee_data(self):
        print(f"Salary is : {self.salary}")


class Student(Person):    # C
    def __init__(self , fees,eid,ename):
        super().__init__(eid,ename)
        self.fees = fees

    def student_data(self):
        print(f"Student fees: {self.fees}")

        
def main():
    # Employee class Instance
    e = Employee(1000,101,"Ramesh")
    e.Display_persn_data()
    e.employee_data()
    
    print("\n")

    # student class instance
    s = Student(20000,101,"Ramesh")
    
    s.Display_persn_data()
    s.student_data()


main()


'''







































    


