

# write mode "w"

# if text file is not exist in our system then "w" mode create that file
# if text file exist in our system then "w" mode overwrite the whole data 

file = open("test_file2.txt","w")

a = int(input("Enter Number :"))
b = int(input("Enter Number :"))
ans = f"Addition is {a+b}"
print(ans)

file.write("Value of a is "+str(a) + "\n")
file.write(f"Value of b is {b} \n")
file.write(ans)

file.close()


# method 2

with open("test_file2.txt" , "w") as file:
    x = int(input("Enter Number :"))
    y = int(input("Enter Number :"))
    ans = f"Multipliaction is : {x*y}"
    print(ans)

    # write data
    file.write(f"Value of x is :{x}\nValue of y is :{y}\n{ans}")

    
print("File Exit")



















