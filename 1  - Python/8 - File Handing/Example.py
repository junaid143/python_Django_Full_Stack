






# right angle triangle
'''
n = int(input("Enter Number Of rows :"))# 8

for row in range(n):
    for col in range(row+1):
        print("*",end = " ")

    print()
'''


n = int(input("Enter Number Of rows :"))

file = open("pattern.txt","a")
file.write("Number Of rows :"+str(n)+"\n")

prt = "* "

for row in range(n):
    for col in range(row+1):
        print("*" , end = " ")
        file.write(prt)
    print()
    file.write("\n")
    
file.write("\n")

file.close()































