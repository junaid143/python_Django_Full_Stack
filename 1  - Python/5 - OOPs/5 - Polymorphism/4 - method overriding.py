
# method overriding


# method overriding is an ability any oops language that allows a subclass or child class
# to provide a specific implementation of a method that is already provided by the one of its
# super classes or parent class .
'''
class parent:
    def __init__(self):
        pass

    def car(self):
        print("maruti 800")



class child(parent):
    def __init__(self):
        super().__init__()

    def car(self):
        super().car()
        print("benz")
    

c = child()
c.car()

'''

# Example 2


class calc:
    def __init__(self):
        pass

    def add(self,x,y):
        print( "addition is "+str(x+y))


class calc_1(calc):
    def __init__(self):
        super().__init__()

    def add(self,x,y):
        super().add(x,y)
        return "Multiplication is "+str(x*y)


obj = calc_1()
print(obj.add(10,20))






















































