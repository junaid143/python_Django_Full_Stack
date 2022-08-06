# Example 1


#1 -  DEFAULT PARAMETER  

def show(name , age = 26):
    print(f"Name is {name} and age is {age}")

show("Junaid")
show("Junaid",20)


#############################################################




#2 -  positional argument 

def show(name , age ):
    print(f"Name is {name} and age is {age}")

show(age = 26 , name = "junaid")   # these are the positional arguments 


###############################################################





# 3 -  variable length argument  (*args)
# store multiple data in the form of tuple


def sum1(*args):
    data = args  # tuple
    #print(type(data))
    s = 0
    for i in data:
        s+=i  #s = s+i
    print("Sum is "+str(s))


sum1(3,5,4,8,6,2,3,5,8,5,4,7,8,6,3,5,2)



##################################################


# 4 -   **kwargs  (disctionary)
# {key:value}

def show(**kwargs):
    data = kwargs
    #print(type(data))
    k = data.keys()
    print(k)
    print(data["contact"])
    
show(name="Junaid" , age = 26 , location = "mumbai",contact = [9821209237,982339358])



################################################################


# 5 -  return


# variable Example

a = None
print(type(a))

# store data into variable 
a = 10
print(type(a))

print(a)

# return Example 
# function priorties
# 1 - when we call function 1st priorty is execute the program inside it
# 2 - behave like a variable

def show(name):
     return f"My name is {name}"


data = show("Junaid")
print(data)



#######################################################################


# 6 -  masking   (call function with different object) 

def show(name,age):
    return f"Name is {name} and age is {age}"


display = show

d = display("junaid",26)
print(d)



###########################################################3


# 7 - funnction as argument
# Example


# function 1
def add(list_data):
    s = 0
    for i in list_data:
        s+=i
    return s

def per(data,function):
    total = len(data)*100
    obtain = function(data)
    p = round(obtain/total *100,2)
    return p
    

data = [84,65,75,68,52,45]

p = per(data , add)
print(p)




































































































