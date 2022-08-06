
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def m1(self):
        print(self.name)
        print(self.age)

class B(A):
    def __init__(self,location,name,age):

        # method 1
        #self.name = name
        #self.age = age

        # method 2
        #A.__init__(self,name,age)

        # method 3
        super().__init__(name,age)
        
        self.location = location

    def m2(self):
        print(self.location)
        


ob = B("Mumbai","python",26)
ob.m1()
ob.m2()
