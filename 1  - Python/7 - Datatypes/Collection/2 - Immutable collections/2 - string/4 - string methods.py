# String methods

# 1 - replace()

# it is used to replace the data inside the string
# replace() takes 2 argument (old_data , new_data )

st = "Hello class This java lecture"
print(st)

st1 = st.replace("java" , "python")
print(st1)

# 2 - split()
# split method is used to break the string data and return into the list

st = "hello class this is python lecture"
s = st.split()    # by default it split the string basis on space 
print(s)

# we can also split data according to our requirments 
st = "hello-class,this is python-lecture"
s1 = st.split(",")   #["hello-class" , "this is python-lecture"]
s2 = st.split("-")   # ["hello","class,this is python","lecture"]
print(s1)
print(s2)


# 3 - join()
# join() is opp to the split()
# it is used to join the list element (if only string ) and return str data 

ls = ["Hello","class","this","is","python"]
print(ls)
print(type(ls))

# "Hello class this is python" # str 
st = " ".join(ls)
print(st)
print(type(st))


# 4 - strip()
#  remove spaces at the beging and at the end of the string
# Example 1

st = "       python        "
print(st)

x = st.strip()
print(x)

# Example 2
# cant remove spaces in between two characters in str 
st = "       python        class    "
print(st)

x1 = st.strip()
print(x1)

# Example 3

st = ",,,,,,,,hgk....python....hhh"
print(st)

x2 = st.strip(",hgk.")
print(x2)


# 5 - upper()
# returns upper case alphabets

st = "Hello class this is Python program"
print(st)

x = st.upper()
print(x)


# 6 - lower()
# return lower case alphabets

st = "HELLO CLASS THIS IS PYTHON PROGRAM"
print(st)

x1 = st.lower()
print(x1)


# 6 - islower()         7 - isupper()
# return True when all the string character is in small

st = input("Enter Data :")
if st.islower():
    print("Lowecase Alphabets ")
elif st.isupper():
    print("Uppercase Alphabets ")
else:
    print("Small and capital both alphabets are there")

# 8 - isdigit()
# its return the Boolean Value if str contain only digit data

st = "123456789"

if st.isdigit():
    print("String Contain Numeric Data ")

else:
    print("Combine Data ")


# 9 - find()
# return lowest Index

st = "Hello class This python program"

data = "class"

p = st.find(data)
print(p)

# Example 
p1 = st.find("o" , 15 , 25)
print(p1)


# 10 - capitalize()

st = "hello class This python program."
a = st.capitalize()
print(a)

# Example 2
# if string start with digit capitalize() return as it is data

st = "25 hello class This python program."
a = st.capitalize()
print(a)


# 11 - center()
st = "Python"
print(st.center(50))








































