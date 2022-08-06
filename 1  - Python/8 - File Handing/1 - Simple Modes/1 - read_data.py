
# read data
'''
# 1 - read()
# open() takes 2 argument open("file_name.extension" , "mode")

file = open("test_file.txt" , "r")
data = file.read() #read() return file data in str type
print(data)
file.close()

print(type(data))


# 2 - readline()
# readline() return first line

file = open("test_file.txt" , "r")

data = file.readline()
print(data)
file.close()

# 3 - readlines()

# readlines() returns the list every element insid that list is file data

file = open("test_file.txt" , "r")

data = file.readlines()
#print(data) 

file.close()

print(type(data))


'''



# read()

with open("test_file.txt" , "r") as file:
    data = file.read()

print(data)

#######################################################################
# readline()


with open("test_file.txt","r") as file:
    data = file.readline()

print(data)


#######################################################################
# readlines()


with open("test_file.txt" , "r") as file:
    data = file.readlines()

print(data)

































