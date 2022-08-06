#  Example Questions

# Q - 1

'''
Write a python program to find sequence of lowercase letters
joined with a underscore

eg

'hello_class'   # valid
'Hello_class'   # invalid
'hello_cLass'   # Invalid
'''
# Solution 
import re
def text_match(text):
    pattern = r'^[a-z]+_[a-z]+$'

    if re.search(pattern , text):
        return "Valid Match"
    else:
        return "Invalid Match"


print(text_match("hello_class"))
print(text_match("heLlo_class"))
print(text_match("hello_class0"))




# Q - 2
'''
write a python program that matches a string that has an 'a' followed by
anything ending in 'b'

eg
'aaabbbb'    # valid
'aabdgsduhf' # invalid
'asdjshdb'  # valid

'''
# Solution

import re
def text_match(text):
    pattern = r'a.*?b$'

    if re.search(pattern , text):  # True
        return "Valid Match"
    else:
        return "Invalid Match"

#print(text_match("basdasda"))
print(text_match("aaaaabbbbb"))
print(text_match("aasfdsdbfjsdb"))


# Q - 3

'''
write a python program that matches a word containg 'z'

eg

'python exercises'   # invalid
'cat is very lazy'   # valid 

'''
# Solution

import re

def text_match(text):
    pattern = r'\w*z\w*'

    if re.search(pattern , text):
        return "Valid Match"
    else:
        return "Invalid Match"

print(text_match('python exercises'))
print(text_match('cat is very lazy'))




# Q - 4

'''
write a python program to remove leading zeros from an Ip address

eg


Ip = '192.168.012.20'     into     ip = '192.168.12.20'
Ip = '192.016.65.054'     into     ip = '192.16.65.54'
'''

import re
def remove_zero(ip):
    pattern = r'\.[0]*'

    return re.sub(pattern , "." , ip)


print(remove_zero('192.168.012.20'))
print(remove_zero('192.016.65.054'))
























