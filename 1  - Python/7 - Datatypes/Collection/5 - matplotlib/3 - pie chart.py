

# impoer library

import matplotlib.pyplot as plt


exp_label = ["Home Rent" , "Food" , "Phone/Internet" , " Bike" , "Other Utilities"]
exp_values = [5000 , 3000 , 2500 , 4500 , 4000]


exp = [0,0.5,0,0,0]
plt.pie(exp_values , labels =  exp_label , autopct = "%1.2f%%",explode = exp ,shadow = True)

plt.savefig("pie.pdf")  # save graph
plt.show()




