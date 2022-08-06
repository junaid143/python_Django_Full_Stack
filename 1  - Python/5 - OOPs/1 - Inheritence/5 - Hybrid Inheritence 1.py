# Hybrid Example

class grand_father:   # A
    def __init__(self,gname,gage):
        self.gname = gname
        self.gage = gage

    def m1(self):
        print(f"Grandpaa Name is {self.gname} and granpaa's age is {self.gage}")

class mother(grand_father):   #B(A)
    def __init__(self,mname,mage,fname,fage,gname,gage):
        super().__init__(fname,fage,gname,gage)
        self.mname = mname
        self.mage = mage

    def m2(self):
        print(f"Mother name is {self.mname} and age is {self.mage}")

class father(grand_father):  # C(A)
    def __init__(self,fname,fage,gname,gage):
        super().__init__(gname,gage)
        self.fname = fname
        self.fage = fage

    def m3(self):
        print(f"Father name is {self.fname} and age is {self.fage}")

class son(mother,father):  # D(B,C)
    def __init__(self,sname,sage,mname,mage,fname,fage,gname,gage ):
        super().__init__(mname,mage,fname,fage,gname,gage)
        self.sname = sname
        self.sage = sage

    def m4(self):
        print(f"Son name is {self.sname} and age is {self.sage}")



s = son("Son",15,"father",55,"mother",45,"grandpaa",70)
s.m4()
s.m3()
s.m2()
s.m1()





























