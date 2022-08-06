

# Example

class Employee:
    def __init__(self,name , age , location):
        self.__name = name           # private attribute
        self.__age = age
        self.__location = location

    def info(self):
        print("Personal Information ")
        print(f"Name is : {self.__name}")
        print(f"Age is : {self.__age}")
        print(f"Location is : {self.__location}")


viki = Employee("Viki",28,"Thane")



# getter and setter method


# we use getter method and setter
# method to add validation logic around
# getting and settting a values


# To avoid direct access of a class field
# private variable cannot accessed
# directly or modified by external user 


























