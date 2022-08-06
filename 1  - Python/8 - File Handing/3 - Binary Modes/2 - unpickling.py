# Unpickling

# Unpickling is the procss of retrieving original python object
# from the stored string representation


import pickle

file = open("write_data.pickle","rb")

data = pickle.load(file)
print(data)
file.close()
