# Sets

import re

#Set                      Description

#[arn]                 Return a match where one of the specified charachters
 #                   eg  ("a" , "r" , or "n")


# Example 1 

# 1 - findall() # return list  the match pattern character
# it takes 2 argument
# str_object.findall("pattern" , "string data ")

st = "the rain in mumbai"   # string data 
print(st)

p = "[amn]"   # pattern 
x = re.findall(p,st)
print(x)

# [a-z]              in between a to z
# [A-Z]              in between A to Z
# [0-9]              in between 0 to 9
# [a-zA-Z]           in between a to z and A to Z
# [a-zA-Z0-9]        
 
