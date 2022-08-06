
# pip install tabulate

import mysql.connector as db
import pandas as pd 
from tabulate import tabulate


class crud_operation:
    def __init__(self):
        # create database 
        mydb = db.connect(host = "localhost",user = "root",passwd = "root")
        cur = mydb.cursor()
        create_db = '''create database if not exists squad;'''
        cur.execute(create_db)
        mydb.close()

        #create table 
        mydb = db.connect(host='localhost',user = 'root',passwd = 'root',database = 'squad')
        cur = mydb.cursor()
        create_table = '''create table if not exists student(
                            id INT auto_increment primary key,
                            name varchar(50) not null,
                            age int not null,
                            location varchar(50)not null,
                            contact bigint unique,
                            qualification varchar(50));'''

        cur.execute(create_table)
        mydb.close()

    # this method is used to create connection between python and database
    def connection(self):
        self.mydb = db.connect(host = "localhost",user = "root",passwd = "root",database = "squad")
        self.cur = self.mydb.cursor()

    # this method is used to insert values into the database 
    def insert_data(self,name , age ,loc,contact ,qualification):
        self.connection()

        insert_query = f'''insert into student(name,age,location,contact,qualification) values
                            ("{name}" , {age} , "{loc}" , {contact} ,"{qualification}");'''

        self.cur.execute(insert_query)
        self.cur.execute("commit;")
        self.mydb.close()

        print("\n***************** Data Inserted **************************\n")


    # This method is used to display all the records from the database 
    def read_data(self):
        self.connection()
        select_query = '''select * from student;'''

        self.cur.execute(select_query)
        data = self.cur.fetchall()
        
        df = pd.DataFrame(data,columns = ["id","name","age","location","contact","qualification"] )

        df.set_index("id",inplace = True)
        #print(df)
        print(tabulate(df,headers = 'keys', tablefmt = 'psql'))

        self.mydb.close()


    # This method is used to update the current table 
    def update_data(self,sid , column_name , column_data):
        self.connection()

        update_query = f'''update student set {column_name} = "{column_data}" where id = "{sid}";'''

        self.cur.execute(update_query)
        self.cur.execute("commit;")

        self.mydb.close()

    # This method is used to delete the existing records 
    def delete_data(self,sid):
        self.connection()

        delete_query = f'''delete from student where id = {sid};'''
        self.cur.execute(delete_query)
        self.cur.execute("commit;")

        self.mydb.close()
        print("\n*********************** Record Removed From The database ***************\n")


if __name__=="__main__":
    obj = crud_operation()

    while True:
        print("\n*************************** Main Options ***************************\n")
        print("1 - Insert Data \n2 - Read All data \n3 - Update Data\n4 - Delete Data\n5 - Exit")

        ch = int(input("Enter Choice :"))

        if ch ==1:
            print("\n******************** Insert Data ******************************\n")
            name = input("Enter Your Name :")
            age = int(input("Enter Your Age :"))
            loc = input("Enter Your Location :")
            contact = int(input("ENter Your Contact :"))
            qualification = input("Enter Your Qualification :")

            obj.insert_data(name , age ,loc,contact ,qualification)

            

        elif ch == 2:
            print("\n*********************** Show All Data ******************************\n")
            obj.read_data()

        elif ch == 3:
            print("\n*************************** Update Data *****************************\n")
            print("Choose Option To update Info")
            print("1 - Name Update\n2 - Age Update\n3 - Location Update\n4 - Contact Update\n5 - Qualification Update")
            ch1 = int(input("Enter Choice Which You Want To update :"))

            if ch1 ==1:
                column_data = input("Enter New Name For update :")
                user_input = input("Are You Sure You want to update Your Name ? yes or no :")
                if user_input == "yes":
                    sid = int(input("Enter Your Id To update Your Name :"))
                    column_name = "name"
                    obj.update_data(sid , column_name , column_data)
                    print("\n**************Information Updated ....********************\n")

                else:
                    print("\n******************** Operation terminated ****************\n")

            elif ch1 == 2:
                column_data = input("Enter New Age For update :")
                user_input = input("Are You Sure You want to update Your Age ? yes or no :")
                if user_input == "yes":
                    sid = int(input("Enter Your Id To update Your age :"))
                    column_name = "age"
                    obj.update_data(sid , column_name , column_data)
                    print("\n**************Information Updated ....********************\n")

                else:
                    print("\n******************** Operation terminated ****************\n")

            elif ch1 == 3:
                column_data = input("Enter New Location For update :")
                user_input = input("Are You Sure You want to update Your Location ? yes or no :")
                if user_input == "yes":
                    sid = int(input("Enter Your Id To update Your location :"))
                    column_name = "location"
                    obj.update_data(sid , column_name , column_data)
                    print("\n**************Information Updated ....********************\n")

                else:
                    print("\n******************** Operation terminated ****************\n")

            elif ch1 == 4:
                column_data = input("Enter New Contact For update :")
                user_input = input("Are You Sure You want to update Your Contact ? yes or no :")
                if user_input == "yes":
                    sid = int(input("Enter Your Id To update Your contact :"))
                    column_name = "contact"
                    obj.update_data(sid , column_name , column_data)
                    print("\n**************Information Updated ....********************\n")

                else:
                    print("\n******************** Operation terminated ****************\n")

            elif ch1 == 5:
                column_data = input("Enter New Qualification For update :")
                user_input = input("Are You Sure You want to update Your Qualification ? yes or no :")
                if user_input == "yes":
                    sid = int(input("Enter Your Id To update Your Qualification :"))
                    column_name = "qualification"
                    obj.update_data(sid , column_name , column_data)
                    print("\n**************Information Updated ....********************\n")

                else:
                    print("\n******************** Operation terminated ****************\n")

            else:
                print("\n*****************Invalid Choice *********************\n")


        elif ch == 4:
            print("\n ******************** Delete Information *************************\n")
            sid = int(input("Enter Your Record Id which you Delete :"))
            
            user = input("Are you Sure You Want to delete The record ? yes or no :")
            if user == "yes":
                obj.delete_data(sid)
            else:
                print("\n************* Operation Terminated Thank You **************\n")

        elif ch == 5:
            print("\n***************************** Exit From The Application *********************\n")
            break
        else:
            print("\n******************************** Invalid Option *****************************\n")
