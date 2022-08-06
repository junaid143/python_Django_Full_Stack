
# pip install tabulate

# fetch info from the database

import mysql.connector as db
import pandas as pd
from tabulate import tabulate


mydb = db.connect(host = "localhost" ,user = "root" , passwd = "root" , database ="company")
#print("connected to the database ")

cur = mydb.cursor()

fetch_query = '''select * from employee'''

cur.execute(fetch_query)

# fetchall return all the records from the database
# fetchone return only one record from the database 

data = cur.fetchall()   #data returns in the form of list
print(data)

df = pd.DataFrame(data,columns = ["emp_id","emp_name","emp_age","emp_salary","location","contact","designation"] )

df.set_index("emp_id",inplace = True)
#print(df)
print(tabulate(df,headers = 'keys', tablefmt = 'psql'))

mydb.close()
