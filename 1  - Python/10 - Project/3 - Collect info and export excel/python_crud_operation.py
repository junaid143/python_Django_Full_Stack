import mysql.connector as db

class user_data:
    def __init__(self):
        
        mydb = db.connect(host = "localhost",user = "root",passwd = "root")
        cur = mydb.cursor()
        cur.execute("create database if not exists user_info;")
        mydb.close()

        # create table 
        mydb = db.connect(host = "localhost",user = "root",passwd = "root",database = "user_info")
        cur = mydb.cursor()
        query = '''create table info(id INT auto_increment ,
                    Name varchar(50) not null ,
                    Age INT not null,
                    Location varchar(100) not null ,
                    Contact bigint not null , 
                    Qualification varchar(50),
                    primary key(id)
                    );'''
        cur.execute(query)
        mydb.close()
        print("table create ")

if __name__=="__main__":
    obj = user_data()

    while True:
        print("1 - Insert Data\n2 - Read data \n3 - update data \n4 - delete data  ")
        ch = int(input("Enter Your Choice :"))
        if 1 == ch:
            print("\n########################### Insert User data ###############################\n")
            user_info = ["Name","Age" , "Location" , "Contact" , "Qualification "]

            data = [input(f"Enter Your {i} :") for i in user_info]
            try:
                obj.insert_data(user_info ,data )
            except:
                print("\n######################## Something Wrong ....#################################\n")

            else:
                print("\n######################## Record Successfully Inserted ########################\n")

        elif ch == 2:
            pass

        elif ch == 3:
            pass

        elif ch == 4:
            pass

        else:
            print("\n############################# Invalid Option ##############################\n")
