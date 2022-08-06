
#  login and register

import random 

class login_system:   # Step 1 create class
    def __init__(self):
        self.flag = True
        
        # create file if file not exists
        with open("User_login.txt","a") as file:
            pass

    def read_file_data(self): # read all the file data and return 
        with open("User_login.txt","r") as file:
            data = file.read()

        return data

    def register(self , name , mail_Id ,password ):
        # read all data
        all_data = self.read_file_data()

        # remove extra spaces from begging and ending
        name = name.strip()
        mail_Id = mail_Id.strip()
        password = password.strip()

        # Check mail id already exists or not
        if mail_Id not in all_data:
            # write the user data to register
            with open("User_login.txt","a") as file:
                file.write(f"{name},{mail_Id},{password}\n")
            print("\n ****** Registeration Successful ******\n")
            

        else:
            print("\n ****** mail Id Already Exists ******\n")
            self.flag = False
        
        
    
    def login(self, mail_Id , password):
        

        
        
        mail_Id = mail_Id.strip()
        password = password.strip()

        # read all the data from the register file
        with open("User_login.txt","r") as file:
            data_list = file.readlines()
            #print(data_list)

        login_count = 0   # for uncessfull login
        for info in data_list:
            u_name , u_email_id ,u_password = info.split(",")
            #print(f" {u_emai_id}        {u_password} ")
            u_password = list(u_password)  # str to list typcast
                
            # this loop is removing the last element of the list i.e "\n"
            for n in u_password:
                if n == "\n":
                    u_password.remove(n)

            # typecast list into str
            u_password = "".join(u_password)

            # match the user entered mail id or password for login
            if (mail_Id == u_email_id) and (password == u_password):
                print(" \n ****** Login Successful ***** \n")
                break

            else:
                login_count = login_count + 1

            
        if len(data_list) == login_count:
            print("\n ****** Login Id or Password Invalid ******\n")

############################## End Class Login Register ###################################

class Application(login_system):
    def __init__(self):
        super().__init__()

        self.id_admin = "admin"
        self.pass_admin = "admin"
        with open("user_detail.txt","a") as file:
            pass

    # return all the user info 
    def read_user_detail(self):
        with open("user_detail.txt","r") as file:
            file_data = file.read()

        return file_data

    # return unique code for all user 
    def generate_unique_code(self):
        return random.randint(1000,9999)

    # this is used to add user detail into the txt file
    def insert_info(self,list_info):
        file_data = self.read_user_detail()
        uniq_code = self.generate_unique_code()  # 1234

        # details = ["Name","Age","Gender","Contact Number","Email Id","Qualification","Incom","Location"]

        if (str(uniq_code) not in file_data) and (list_info[3] not in file_data) and (list_info[4] not in file_data):
            # info write in file
            with open("user_detail.txt","a") as file:
                
                print(f"\n *** Uique Code for User {list_info[0]} is {uniq_code} ***\n")
                file.write(f"*** Uique Code for User {list_info[0]} is {uniq_code} ***\n")
                file.write(f"Name : {list_info[0]}\n")
                file.write(f"Age : {list_info[1]}\n")
                file.write(f"Gender : {list_info[2]}\n")
                file.write(f"Contact Number : {list_info[3]}\n")
                file.write(f"Email Id : {list_info[4]}\n")
                file.write(f"Qualification : {list_info[5]}\n")
                file.write(f"Income : {list_info[6]}\n")
                file.write(f"Location : {list_info[7]}\n\n")
                
                

        else:
            print("\n ****** Contact Number or Email Id Already Exists In Our Database ******\n")
        
    # return specific user details if otp is correct
    def seach_user_details(self,otp):
        # read all user data
        with open("user_detail.txt","r") as file:
            file_data = file.readlines()   # return list

        opt_count = 0
        for line in file_data:
            if otp in line:
                pos = file_data.index(line)

                # slice user detail from the list
                user_info = file_data[ pos : pos+10]
                # convert list into str
                user_info = "".join(user_info)
                
                print("\n",user_info)

            else:
                opt_count = opt_count + 1

        if len(file_data) == opt_count:
            print("\n ********* Unique Identification Code is Invalid **********\n")
                

    # return all user info if admin id and password is correct 
    def show_all_detail(self, admin_id , admin_pas):

        #self.id_admin = "admin"
        #self.pass_admin = "admin"

        admin_id = admin_id.strip()
        admin_pas = admin_pas.strip()

        if (admin_id == self.id_admin) and (admin_pas == self.pass_admin):
            print("\n ********* Admin Login SucessFul **********\n")
            data = self.read_user_detail()
            print(data)
            print("\n ******************************************\n")

        else:
            print("\n ********* Admin Id or Password Invalid **************\n")
            
            


if __name__=="__main__": # main function # afer the main function execution will start
    
    log = Application()

    while True:
        print("1 - Register\n2 - Login\n3 - Exit Main Menu")
        log_ch = input("Enter Your Option :")

        if log_ch == "1":
            print("\n ################### Register Start From Here  ###################\n")

            name = input("Enter Your Name :")
            mail_Id = input("Enter Your Email Id :")
            password = input("Enter Your Password :")

            log.register(name , mail_Id ,password )

            print("\n #################################################################\n")
            
        elif log_ch == "2":
            print("\n ################### Login Start From Here  ######################\n")

            mail_Id = input("Enter Your Email Id :")
            password = input("Enter Your Password :")
            log.login( mail_Id , password)

            print("\n ############## Application Start From Here  #####################\n")
            # Application start from here
            while True:
                print("\n1 - Enter User Details\n2 - Search User Details\n3 - Check All Details (Addmin Only)")
                print("4 - Exit From Application\n")

                app_ch = input("Enter Your Choice :")

                if app_ch == "1":
                    details = ["Name","Age","Gender","Contact Number","Email Id","Qualification","Incom","Location"]
                    '''
                    list_info = []

                    for i in details:
                        info = input(f"Enter Your {i} :")
                        list_info.append(info)
                    print(list_info)
                    '''
                    list_info = [input(f"Enter Your {i} :") for i in details ]

                    log.insert_info(list_info)
                    print("\n ******* Information Successully Recorded ********\n")
                    print("\n *************************************************\n")

                elif app_ch == "2":
                    print("\n *********** Search user Detail ******************\n")
                    otp = input("Enter Your unique Identification Code :")   # 3179  # 9915
                    log.seach_user_details(otp)

                    print("\n *************************************************\n")

                elif app_ch == "3":
                    print("\n *********** Admin Login ******************\n")
                    
                    admin_id = input("Enter Admin Id :")
                    admin_pas = input("Enter Admin password :")

                    log.show_all_detail(admin_id , admin_pas)

                elif app_ch == "4":
                    print("\n ############# Exit From Application ##################\n")
                    break

                else:
                    print("\n ################### Invalid Option ###################\n")
            
            
            
            print("\n #################################################################\n")

        elif log_ch == "3":
            print("\n ########################## Than You  ############################\n")

            break

        else:
            print("\n ######################## Invalid Option #########################\n")
    

















