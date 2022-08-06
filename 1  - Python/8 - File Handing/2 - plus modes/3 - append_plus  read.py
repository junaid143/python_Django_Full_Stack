# a+

# append + read

file = open("test_file2.txt","a+")

data = "python class"
file.write(data+"\n")

# position
file.seek(0)

data1 = file.read()
print(data1)

file.close()


# example

with open("test_file2.txt","a+")as file:
    data = input("Enter Data :")
    file.write(data+"\n")

    # position
    file.seek(0)

    data1 = file.readlines()
    print(data1)
