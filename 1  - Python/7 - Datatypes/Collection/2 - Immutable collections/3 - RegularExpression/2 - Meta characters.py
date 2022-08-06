# Meta characters
import re

#1 - "[]"  set charecter

import re

st = "Hello class This is Python lecture"
x = re.findall("[a-j]" , st)
# return list
print(x)


# 2 - "\d"   # return digit

st = "total 6 students "
a = re.findall("\d" , st)

print(a)


# 3 - "." # any character Expect new line

st = "hello class this is python lecture ,my name is junaid"
a = re.findall("p....n",st)
b = re.findall("j.....",st)
print(a)
print(b)

# 4 -  "^"    # start With   # string start with pattern

st = "hello class this is python lecture ,my name is junaid"

a = re.findall("^h...o",st)
print(a)
if a:
    print("data start with hello")
else:
    print("Not match")

# 5 - "$"   # End with 

st = ["hello class", "this is junaid","my name is junaid","cat"]
nw = []
for i in st:
    if re.findall("junaid$",i):
       nw.append(i) 

print(nw)


# 6 - "*"   # Zero of more occurence

st =  "this is clss py is the extension of python pyton is not correct"

x = re.findall("py.*n",st)
print(x)


# 7 -  "+"    one or more occurence

st = "hello python "

x = re.findall("py.+n",st)
print(x)

# 8 - "?"  # Zero or one occurrence

st = "cls python"

x = re.findall("cl.?s",st)
print(x)

# 9 - "{}"   Exactly the specified number of occurrences

st = "python lecture "

x = re.findall("le.{4}e" , st)
x1 = re.findall("le....e",st)
print(x)
print(x1)

# 10 - " | "   # or
st = "hello class this is python "

x = re.findall("class|lecture",st)
print(x)















































