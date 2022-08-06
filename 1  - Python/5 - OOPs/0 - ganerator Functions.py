

# 1 - genarator function

# A generator-function is defined like a normal function,
# but whenever it needs to generate a value,
# it does so with the yield keyword rather than return.

# If the body of a def contains yield,
# the function automatically becomes a generator function.



# 2 - yield keyword
# yield keyword is mililer to return
# but return only used one but yield return multiple of itterable gerator object




# Example 1

def display(name):
    yield f"hello this is {name}"

x = display("junaid")
for i in x:
    print(i)

###################################################

# Example 2

def show(num,num1):
    if num > num1:
        while num > num1:
            yield num
            num -= 1

x = show(5 , 2)
x = list(x)
print(x)



###########################################3

# Example 3

def factorial(x):
    f = 1
    for i in range(x , 0 , -1):
        f*=i
        yield f

fact = factorial(5)
for i in fact:
    print(i)

#print(dir(fact))
print(fact)




















