

# What is Encapsulation

# General terms
# Encapsulation is a concept of OOps 
# Encapsulation means hiding the data ,to prevent the outside modification


# Definition

#Encapsulation is one of the fundamental concept of oops .
#It describes the idea of wrapping data and the methods that works on data within one unit
#This put restrictions on accessing  variables and the methods directly can prevent
#the accidental modification of data

# Example with problem

class Employee:
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location

    def show_data(self):
        print("Show Information")
        print(f"Name is  : {self.name}")
        print(f"Age is : {self.age}")
        print(f"Location is : {self.location}")


viki = Employee("Viki" , 25,"Thane")  # instance 1
rahul = Employee("rahul" , 21,"Mumbai")  # instance 2


viki.show_data()  #  instance 1 call method show_data(
rahul.show_data()

viki.name = "Vikram"    # outside modification
viki.show_data()






























