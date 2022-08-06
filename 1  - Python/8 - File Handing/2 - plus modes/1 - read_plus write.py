# r+ mode 
'''
file = open("test_file.txt","r+")
data = file.readlines()
print(data)

#position
file.seek(0)
data = input("Enter data:")
file.write(data)

file.close()



# method 2

with open("test_file.txt" , "r+") as file: # read +write
    data = file.read()
    print(f"read() : \n{data}\n")

    # position
    file.seek(0)
    data = input("Enter data:")
    file.write(data)


print("File close ")

'''

# Example 2

# read + write

with open("test_file.txt","r+") as file:
    data = file.read()
    print(data)

    # position
    file.seek(0)

    data1 = "my"
    file.write(data1)



print("Operation Complete ")































