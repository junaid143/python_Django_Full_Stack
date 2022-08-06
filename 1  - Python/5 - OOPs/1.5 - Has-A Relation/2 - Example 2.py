class A:
	def __init__(self):
		print('Class - A Constructor')

	def m1(self):
		print('M1 method of Class - A.')


class B:
	def __init__(self):
		print('Class - B Constructor.')

	# instance method
	def m2(self):

		# creating object of class A inside
		# B class instance method
		obj = A()

		# calling m1() method of class-A
		obj.m1()
		print('M2 method of Class - B.')


# creating object of class-B
obj = B()

# calling B class m2() method
obj.m2()

# Explaination 
# we are creating an object of class A inside instance method of class B that is m2() method.
# So the flow of execution will be Initially,
# the object of class B will be created so the constructor of class B will get executed.
# Now object of class B is calling m2() method,
# so the cursor will go to the m2() method of class B.
# Inside the m2() method of class B object of class A is created
# so the constructor of class A will be executed then m1() method of class A will be executed
# finally it will print the final statement of m2() method and execution end’s here.








