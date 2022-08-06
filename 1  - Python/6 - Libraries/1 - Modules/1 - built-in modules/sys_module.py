import sys


# Example 1
'''
a = 10  # int
b = 2.0   #float
c = "Hello"  # str

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
'''

#print(sys.copyright)
#print(sys.path)
#print(sys.platform) #  linux , win32 , darwin

#print(sys.getrecursionlimit())# 

#sys.setrecursionlimit(50)

#print(sys.getrecursionlimit())# 
# eg of recursion
'''
def test():
    print("Hello Python")
    test()
test()
'''

# eg print function

def show(*args):
    #(30,"Addition")
    data = ""
    for i in args:
        data = data + str(i)

    sys.stdout.write(data)
show("Addition is :",20+30)
'''
# Eg display user define errors
err = "This is small Error "
sys.stderr.write(err)

'''
#show(dir(sys))
help(sys)




























