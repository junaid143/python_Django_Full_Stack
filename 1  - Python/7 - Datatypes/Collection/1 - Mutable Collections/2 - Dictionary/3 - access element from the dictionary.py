# access element from the dictionary

school = {"school name":"xyz school",
          "class_8": [14 , 2 , 30],
          "class_9" : [10 , 15 , 12],
          "class_10" : [23 , 54 , 1]}
print(school)

# len of dict
print(len(school))

# find the keys of the dictionary
k = school.keys()
print(k)

# access element
# 1 - get()

data = school.get("class_10")
print(data)

# 2nd method

data1 = school["class_8"][2]
print(data1)
