
# bar char

import matplotlib.pyplot as plt
import numpy as np


# data
# Example 1

company = ["Google" , "Facebook" , "Microsoft" , "IMB"]
revenue = [120 , 100 , 150 , 130]

plt.title("Stock")
plt.xlabel("Company Name")
plt.ylabel("Revenue")

plt.bar(company , revenue , label = "Revenue")

plt.legend()

plt.show()




# Example 2

company = ["Google" , "Facebook" , "Microsoft" , "IMB"]
revenue = [120 , 100 , 150 , 130]
profit = [50 , 60 , 90 , 70]

plt.title("Stock")
plt.xlabel("Company Name")
plt.ylabel("Revenue")

plt.bar(company , revenue , label = "Revenue")
plt.bar(company , profit , label = "Profit")

plt.legend()

plt.show()

# Example 3

company = ["Google" , "Facebook" , "Microsoft" , "IMB"]
revenue = [120 , 100 , 150 , 130]
profit = [50 , 60 , 90 , 70]

comp_count = np.arange(len(company)) #[0,1,2,3]

plt.title("Stock")
plt.xlabel("Company Name")
plt.ylabel("Revenue")

plt.bar(comp_count-0.2 , revenue ,width = 0.4, label = "Revenue")
plt.bar(comp_count+0.2 , profit ,width = 0.4, label = "Profit")

plt.xticks(comp_count , company)
plt.legend()
plt.show()





























