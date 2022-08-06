

# list zip and unzip

# python zip() takes itterable or containers and returns a single itterator object
# having mapped values from all the containers

# it is used to mape the similer index of multiple containers
# so that they can be used just using a single entry

# zip()

name = ["Vishal" , "akash" ,"dakshata" , "fahad"]
age = [19 , 21 , 20 , 28 , 22] 
location = ["kalwa" , "thane" ,"kalwa", "kurla"]

result = list(zip(name , age , location))
print(result)
# [("vishal" , 19 , "kalwa") , ("akash",21 , "thaen")]

print("Name \t Age \t Location\t")
for i,j,k in result:
    print(f"{i}\t{j}\t{k}")

# unzip()

result = [('Vishal', 19, 'kalwa'),('akash', 21, 'thane'),('dakshata', 20, 'kalwa'),('fahad', 28, 'kurla')]


a,b,c = zip(*result)

print(list(a))
print(list(b))
print(list(c))






















