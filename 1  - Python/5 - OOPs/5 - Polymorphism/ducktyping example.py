

class calc:
    def add(self,a,b):
        return "addition is :"+str(a+b)

    def sub(self,a,b):
        return "substraction is :"+str(a-b)

    def mul(self,a,b):
        return "multiplication is :"+str(a*b)

    def per(self,obt,total):
        if total >= obt:
            return "Percentage is :"+str(obt/total*100)

        else:
            return "check the values"


class adv_calc:
    def add(self,a,*args):
        s = a
        for i in args:
            s = s+i
        return "Addition is :"+str(s)

    def sub(self,a,*args):
        s = a
        for i in args:
            s = s-i
        return "Substracion is :"+str(s)

    def mul(self,a,*args):
        s = a
        for i in args:
            s = s*i
        return "Multiplication is :"+str(s)


simple = calc()
adv = adv_calc()


def main(obj,value1,value2):
    
    print(obj.add(value1,*value2))
    print(obj.sub(value1,*value2))
    print(obj.mul(value1,*value2))




a = 20
b = []

















        








