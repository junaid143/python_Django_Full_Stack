

# Access Modifier / Access Specifier


# when we need to put the access restrictions on attributes or methods then we used
# access modifier


# there are three type of access Modifier
# 1 - Public Access Modifier
# 2 - Protected Access Modifier
# 3 - Private Access Modifier


# 1 - Public Access Modifier

# Public Access Modifier
# The Member of a class that are declear public easily accessible from any part of the program
# All data members and member public by default

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


class Director(Employee):
    def __init__(self,name,age,location):
        super().__init__(name,age,location)

    def test(self):
        print(self.name)
        print(self.age)
        print(self.location)



viki = Director("Viki" , 25,"Thane")



# 2 - Protected Access Modifier

# The member of the class that are declear protected are only accesible to a class derived from it
# Data members of a class are decleared by adding "_" underscore
# symbol before the data member of that class


class Employee:
    
    def __init__(self,name,age,location):
        self._name = name            # protected attributes 
        self._age = age
        self._location = location

    def _show_data(self):           # protechted method 
        print("Show Information")
        print(f"Name is  : {self._name}")
        print(f"Age is : {self._age}")
        print(f"Location is : {self._location}")

class Director(Employee):
    def __init__(self,name,age,location):
        super().__init__(name,age,location)

    def test(self):
        print(self._name)
        print(self._age)
        print(self._location)

viki = Director("Viki" , 25,"Thane")



# 3 - Private Access Modifier 

# The member of the class that are decleared private are accessible within the class only
# private access modifier is the most secure access modifier
# data members of a class are decleared private by adding "__" double underscore
# before the data member


class Employee:
    
    def __init__(self,name,age,location):
        self.__name = name            # Private attributes 
        self.__age = age
        self.__location = location

    def show_data(self):           # Private method 
        print("Show Information")
        print(f"Name is  : {self.__name}")
        print(f"Age is : {self.__age}")
        print(f"Location is : {self.__location}")

class Director(Employee):
    def __init__(self,name,age,location):
        super().__init__(name,age,location)

    def test(self):
        print(self.__name)
        print(self.__age)
        print(self.__location)

viki = Director("Viki" , 25,"Thane")

























































