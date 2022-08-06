
import package_1
from package_1 import simple_calc,complex_calc,pattern



#print(dir(package_1.simple_calc))
#print(help(package_1.simple_calc))

#print(help(package_1.complex_calc))

a = simple_calc.addition(20,30,50)
print(a)


f = complex_calc.factorial(6)
print(f)

p = complex_calc.percentage(450,650)
print(p)

pattern.right_angle(10)
print("\n\n")

pattern.squar_pattern(5)





