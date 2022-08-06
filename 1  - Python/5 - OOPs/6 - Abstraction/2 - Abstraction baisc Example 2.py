#  Abstraction basic Example

from abc import ABC,abstractmethod
class car(ABC):   # abstract class 
    @abstractmethod
    def mileage(self):   # abstract method
        pass

    @abstractmethod
    def safty_level(self): # abstract method
        pass
    
    @abstractmethod
    def seats(self):   # abstract method
        pass

    def color(self):   # concrete method 
        return "Default Color is Black"

class Tesla(car):
    def mileage(self):
        print("The Mileage is 30Kmph")

    def safty_level(self):
        print("Safty Level is 4")

    def seats(self):
        print("4 seats ")

    def type(self):
        print("tela is Electric Vahicle")

obj_tesla = Tesla()
obj_tesla.mileage()
obj_tesla.safty_level()
obj_tesla.type()


























