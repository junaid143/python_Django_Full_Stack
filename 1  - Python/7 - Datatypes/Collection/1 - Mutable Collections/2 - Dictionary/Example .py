# Example
# take 5 input from the user name ,age and location and add into the dictionary

data = {"Name":[],
        "Age":[],
        "Location":[]}

print(data)

for i in range(1,6):
    n = input("Enter Name :")
    a = int(input("Enter Your Age :"))
    l = input("Enter Your Location")

    data["Name"].append(n)
    data["Age"].append(a)
    data["Location"].append(l)

    print(f"update {i} Data")

print(data)


    
