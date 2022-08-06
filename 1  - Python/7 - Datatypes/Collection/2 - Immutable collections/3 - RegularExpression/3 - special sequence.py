# Special Sequence
import re

# 1 - "\d"    # find the digits

st = "my rol number is 785 and the prn number is 12547546"

x = re.findall("\d",st)
print(x)


# 2 - "\D"    # return all the characters expect digits

st = "my rol number is 785 and the prn number is 12547546"

x = re.findall("\D",st)
print(x)


# 3 - "\s"   # return white space character 
st = "my rol number is 785 and the prn number is 12547546"
x = re.findall("\s",st)
print(x)

# 4 - "\S"  # return all the characters exect white spaces 
st = "my rol number is 785 and the prn number is 12547546"
x = re.findall("\S",st)
print(x)

import re

# 5- "\w"  #return the match where the string containg any word character
            #character a-z gigits from 0-9 and the under score(_)

st = "% * @"
x = re.findall("\w",st)
if x:
    print("there is a match")

else:
    print("No match")


# 5- "\W"  #return the match where the string does notcontaing any word character
            #character a-z gigits from 0-9 and the under score(_)

st = "thisisjunaid"
x = re.findall("\W",st)
if x:
    print("there is a match")

else:
    print("No match")



# 6 - "\B"  # return ending match

st = "Rain in train"

x = re.findall(r"in\b",st)
x1 = re.findall(r"\bt",st)

print(x)
print(x1)


# 7 - "\A"   # similer as "^" start with

st = "hello class"

x = re.findall("\Ahello",st)
x1 = re.findall("^hello",st)
print(x)
print(x1)






































