

import pandas as pd

data = [(1, 'Ansari', 29, 2000, 'mumbai', 9874563215, 'trainer'),
        (2, 'Junaid', 26, 5000, 'Navi mumbai', 7536541598, 'dev')]

df = pd.DataFrame(data,columns = ["emp_id","emp_name","emp_age","emp_salary","location","contact","designation"] )

df.set_index("emp_id",inplace = True)
print(df)
