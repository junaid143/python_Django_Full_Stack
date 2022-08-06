
# append mode is like a write "a"

# if text file is not exists in our system then "a" create that file
# if text file is exist in out system the "a" write new data in the end position 


file = open("test_file3.txt" , "a")

a = int(input("Enter Number :"))
b = int(input("Enter Number :"))
ans = f"Addition is :{a+b}"
print(ans)

file.write("Value of a is :"+str(a)+"\n")
file.write(f"Value of b is : {b}\n")
file.write(ans+"\n\n")

file.close()

# method 2

with open("test_file3.txt","a") as file:
    x = int(input("Enter Number :"))
    y = int(input("Enter Number :"))
    ans = f"multiplication is :{x*y}"
    print(ans)

    file.write(f"Value of x :{x}\nValue of y:{y}\n{ans}\n\n")

print("File Exit")












