# w+

# write + read

file = open("test_file1.txt","w+")

data = "Hello class This is Python"
file.write(data)

# position
file.seek(5)

data1 = file.read()
print(data1)

file.close()

# Example 2
with open("test_file1.txt","w+") as file:
    data = "Java Programming Language"
    file.write(data)

    # position
    file.seek(0)

    data1 = file.read()
    print(data1)













