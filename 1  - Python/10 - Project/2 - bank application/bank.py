# bank application 
import re 
import os
from application import app

class bank(app):
    def __init__(self) :
        self.cash = None
        self.login_flag = False
        self.file_name = None
        super().__init__()

    def register(self, name ,contact , mail_id , Address , init_amount , password ):

        # remove Extra spaces from the string data 
        name = name.strip()
        contact = contact.strip()
        mail_id = mail_id.strip()
        Address = Address.strip()
        init_amount = init_amount.strip()
        password = password.strip()

        try:
            os.mkdir("user_detail")
        except:
            pass

        # add initial amount as cash
        self.cash = int(init_amount)

        # Contact Number should be 10 digit
        contact_flag = True   # flag
        if (len(contact) > 10 ) or (len(contact) < 10):
            print("\n ****** Invalid Contact Number ***********\n")
            contact_flag = False
        
        # check the mail id is valid or not 
        mail_flag = False
        ptr = r"[a-zA-Z0-9\.]+@+[a-z]+\.+[com|in|net|org]+"
        if re.match(ptr , mail_id):
            mail_flag = True
            #print("mail Id is correct")
        
        # password should be greater then 5 and less then 18
        pass_flag = True
        if (len(password)<5) or (len(password)>18):
            print("\n ******* Enter Password greate then 5 and less then 18 Characters *********\n")
            pass_flag = False



        # to check mail id already Exists or not 

        mail_not_exists_flag = True
        os.chdir("user_detail\\")    # change folder to user_detail folder 
        all_files = os.listdir()     # all Existing file name in form of list 
        os.chdir("..")              # back to previous directory 
        fil_name = mail_id+".txt"

        if fil_name in all_files:
            mail_not_exists_flag = False
            print("\n *********** Mail Id Already Exits in Our database ************\n")
        
        

        if (contact_flag == True) and (mail_flag == True) and (pass_flag ==True) and (mail_not_exists_flag == True):
            # detail list
            detail  = [name ,contact , mail_id , Address , init_amount , password ]
            with open(f"user_detail\{mail_id}.txt" , "w") as file:
                for data in detail:
                    file.write(str(data)+"\n")
            
            print("\n ********* Register Successfull ****************\n")



    # for already register user         
    def login(self , mail_id , password):

        try:
            os.mkdir("user_detail")
        except:
            pass

        # remove Extra spaces
        mail_id = mail_id.strip()
        password = password.strip()

        # change working directory 
        os.chdir("user_detail")
        all_files_data = os.listdir()

        user_mail = mail_id+".txt"
        self.file_name = user_mail
        os.chdir("..")    # back to the previous directory

        # check Valid mail id 
        mail_flag = False
        ptr = r"[a-zA-Z0-9\.]+@+[a-z]+\.+[com|in|net|org]+"
        if re.match(ptr , mail_id):
            mail_flag = True

        else:
            print("\n********** Enter Valid Mail Id ******************\n")

        # check the user mail exists or not 
        mail_exists = False
        if user_mail in all_files_data:
            mail_exists = True
        else:
            print("\n********** Mail Id Not Exists ***************\n")
            print("************ Register First and Login *************\n")

        
        if (mail_exists == True) and (mail_flag == True):
            # check password 
            with open("user_detail/"+user_mail , "r") as file:
                file_data = file.readlines()

            #print(file_data)
            sys_pass = file_data[5]   # str data 
            sys_pass = list(sys_pass)
            #print(sys_pass)
            for i in sys_pass:
                if i == "\n":
                    sys_pass.remove(i)

            #print(sys_pass)
            sys_pass = "".join(sys_pass)

            #print(sys_pass)
             
            if sys_pass == password:

                print("\n ***************Login Successful ****************")
                self.login_flag = True

            else:
                print("\n*********** Incorrect Password ************* \n")
                
        

    
if __name__ == "__main__": 
    bank_object = bank()

    print("\n ################ Welcome TO The bank Application ##################\n")

    while True:
        print("1 - Create a New Account :\n2 - Login Existing Account\n3 - Exit From Bank Application")
        user = int(input("Make Decision :"))

        if user ==1:   # create account
            print("\n######################### Register Start From Here ################\n")
            name = input("Enter Your Name :")
            contact = input("Enter Your Contact :")
            mail_id = input("Enter Your mail Id :")
            Address = input("Enter Your Address :")
            init_amount = input("Enter Your initial Amount :")
            password = input("Enter Your Password :")

            if int(init_amount) >= 1000:
                bank_object.register(name ,contact , mail_id , Address , init_amount , password )

                print("\n##############################################################\n")
            
            else:
                print("\n ********* Amount Should  be greater then 1000 ****************\n")

        elif user == 2:  # login account
            print("\n######################### Login Start From Here ################\n")
            mail_id = input("Enter Your mail Id :")
            password = input("Enter Your Password :")

            bank_object.login(mail_id , password)

            if bank_object.login_flag == True:
                # Application start 
                while True:
                    print("1 - Check Balance \n2 - Deposit Amount \n3 - Widraw Amount \n4 - Check Loan EMI\n5 - Logout Account")
                    app_ch = int(input("Enter Your Choice :"))

                    if app_ch == 1:
                        bank_object.check_balance(bank_object.file_name)

                    elif app_ch == 2:
                        amount = int(input("Enter Deposit Amount :"))

                        bank_object.deposit_amount(bank_object.file_name ,amount )

                    elif app_ch == 3:
                        amount = int(input("Enter Widraw Amount :"))
                        bank_object.windraw_amount(bank_object.file_name,amount)

                    elif app_ch == 4:

                        # Varaible name details:
                        # p = Principal or Loan Amount
                        # r = Interest Rate Per Month
                        # n = Number of monthly installments

                        p = float(input("Enter principal amount: "))
                        
                        R = 24
                        print(f"Interest Rate Per Month {R}%")
                        n = int(input("Enter number of months: " ))

                        bank_object.emi_calculator(p , R , n)

                    elif app_ch == 5:
                        print("\n****************** Logged Out *************")
                        break


            print("\n##############################################################\n")

        elif user == 3:
            print("\n####################### Thank You ################################\n")
            break
