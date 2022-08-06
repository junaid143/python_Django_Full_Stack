


# Encapsulation Example 1

'''
class Employee :
    def __init__(self,name,age,location):
        self.__name = name
        self.__age = age
        self.__location = location

    def get_info(self):  # getter method / accessor
        print("Personal Information ")
        print(f"Name is : {self.__name}")
        print(f"Age is : {self.__age}")
        print(f"Location is : {self.__location}")

    def set_location(self,loc):  # setter_ method / mutator
        self.__location = loc

    def set_name(self,name):# setter_ method / mutator
        self.__name = name

    def set_age(self,age): # setter_ method / mutator
        self.__age = age


viki = Employee("Viki",28,"Thane")
'''

# Encapsulation Example 1

'''

class car:
    def __init__(self):
        self.__color = "Black"
        self.__maxspeed = 200
        self.__seats = 4

    def get_car_details(self):
        print("Car Detail")
        print(f"car Color is : {self.__color}")
        print(f"car Max Speed is : {self.__maxspeed}")
        print(f"car seats : {self.__seats}")

    def set_speed(self,speed):
        self.__maxspeed = speed
'''

# Example 3

class customer:
    def __init__(self,product,price):
        self.__price = price
        self.product = product

    def get_product_info(self):
        print("Product Information")
        print(f"Product is : {self.product}")
        print(f"Prodcut of the price is :{self.__price }")

    def get_discount(self,discount):

        if (discount > 0) and (discount < 100):
            p = self.__price - self.__actual_discount(10)
            print(f"After Discount the Price of the Product is : {p}")

        else:
            print("Discount No Eligible")

    def __actual_discount(self,discount):
        return self.__price * (discount/100)
        

viki = customer("Smart watch" , 5000)
viki.get_product_info()

viki.get_discount(10)





























































