# re Methods
import re



# 1 - findall()  #return list of the match patern




# Find Valid Mobile Number

st = "75395 , 7896541235,456952387 , 8521479635 , 4569872548 , 258763"

# Example without Re

x = st.split(",")
#print(x)
x1 = []
for i in x:
    x1.append(i.strip())

print(x1)
for i in x1:
    if len(i) == 10:
        print(i)

##########################################################################



# Example with re

pattern = r'\d{10}'
x = re.findall(pattern ,st)
print(x)


##########################################################################


# Example 2
# find the valid mail Id 

email = 'abc.xyz@gmail.in hello@.in pqrsabc145@gmail.com and 123gmail.com ansarijunaid957@gmail.com '

pattern = r'[a-zA-Z0-9\.*]+@[a-z]+\.+[com|in|net]+'
x = re.findall(pattern,email)
print(x)



##########################################################################



# Example 2
email = 'abc.xyz@gmail.in hello@.in pqrsabc145@gmail.com and 123gmail.com ansarijunaid957@gmail.com '

pattern = r'[\w\.]+@[\w]+\.[\w]'

x = re.findall(pattern ,email)
print(x)

##############################################################################






# 2 - match()


# find the pattern from the begginig and return match object
# if not match return None 

# Example 1

st = 'My contact number is 7539518527 and the mail is '

pattern = r'\d{10}'

x = re.match(pattern , st)
print(x)


###############################################


# Example 2

st = '7539518527 My contact number and the mail is '

pattern = r'\d{10}'

x = re.match(pattern , st)

# group()  return the object data

print(x.group())

##########################################################################
# 3 - search()

# similer to match()
# matches the pattern from overall string and return the search object
# if not matches then return None 


st = "Hello python program this is python lecture"

pattern = r"p.{4}n"

x = re.search(pattern , st)

print(x.group())



############################################################################



# 4 - sub()

# is used to replace the spacific pattern inside the string data

# Example 1  Without re

st = "hello class this python .class have only 6 students"

x = st.replace('class','')
print(x)




# Example 2

st = "hello class this python .class have only 6 students"

patern = r"class|python"

x = re.sub(patern , "-" , st)
print(x)




# Example 3
# remove Punc

st = 'Hello class . python ! is the? best, : programming ; language,'
print(st)

p = r'[\.\!\:\;\,\?]*'

x = re.sub(p , "" , st)
print(x)





























































