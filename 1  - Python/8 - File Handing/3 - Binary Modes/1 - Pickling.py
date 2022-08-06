
# Pickling

# in Python pickling is the process by wich python object are converted to byte streams
# picking is about serializing the object structure in python 

import pickle


file = open("write_data.pickle" , "wb")

data = "hello class python lecture "

pickle.dump(data , file)

file.close()
