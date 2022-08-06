# Abstraction Example 3

from abc import ABC,abstractmethod

class shop(ABC):
    def __init__(self,product,description,price ,quantity):
        self.product = product
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def sale(self):
        pass

    abstractmethod
    def exiry(self):
        pass


class electronic(shop):
    
    def sale(self , discount = 20):
        if self.quantity >= 10:
            print("You are Eligible for 20% Discount")
            
            self.total_price = self.price *self.quantity  # get total price
            # Apply 20% discount
            self.dis = self.total_price - (self.total_price *(discount/100))
            print(f"Product is : {self.product}")
            print(f"Product Description : {self.description}")
            print(f"Product Price : {self.price}")
            print(f"Quantity of the product : {self.quantity}")
            print(f"Total Price After Discount : {self.dis}")
            print(f"Thank You")
            
        else:
            print("You are not Eligible for Discount")
            print(f"Product is : {self.product}")
            print(f"Product Description : {self.description}")
            print(f"Product Price : {self.price}")
            print(f"Quantity of the product : {self.quantity}")
            print(f"Thank You")
        

    def expiry(self):
        print("Product Expire After 1 Year ")


class mobile(shop):
    def sale(self):
        print("Sale 10 Mobiles ")

    def expiry(self):
        print("Product Expire After 1 Year ")




Rahul = electronic("Watch" , "Display the Time",3000,1)
Rahul.sale()
Rahul.expiry()


mobile = mobile("smartphone","many",10000,50)
mobile.sale()







