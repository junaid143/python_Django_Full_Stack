#  Application.py


class app:
    def __init__(self):
        pass


    # read user file data and return all the info in list form 
    def read_file_data(self,file_name):
        with open("user_detail/"+file_name , "r") as file:
            self.read_data = file.readlines()
        return self.read_data


    def check_balance(self , user_mail):
        data = self.read_file_data(user_mail)
        print("\n ************** User Acount Ino ****************\n")
        print(f"Acount Holder Name is : {data[0]}")
        print(f"Available Balance is : {data[4]}")
        print("\n************* Thank You *********************\n")

    def deposit_amount(self , file_name ,amount ):

        data = self.read_file_data(file_name)

        previous_amount = int(data[4])   # previous amount

        deposit_amount = previous_amount + amount

        print(f"\nPrevious available balance is :{previous_amount} **********\n")
        print(f"\nDeposit Amount is :{amount} ***************\n")

        data = "".join(data)
        #print(data)

        # replace method 
        data1 = data.replace(str(previous_amount) , str(deposit_amount))
        print(f"\n********* Current Available Balance is : {deposit_amount} ************\n")

        # update values into the file 
        with open("user_detail/"+file_name , "w") as file:
            file.write(data1)


    # widraw Amount 
    def windraw_amount(self , file_name,amount):
        data = self.read_file_data(file_name)   

        if int(data[4]) < amount:  
            print("\n******** Entered Amount is Invalid ***********\n")

        else:
            
            previous_amount = int(data[4]) 
            current_amount = int(data[4]) - amount

            data = "".join(data)   # list to str
            data1 = data.replace(str(previous_amount) , str(current_amount))
            # update values into the file 
            with open("user_detail/"+file_name , "w") as file:
                file.write(data1)

                print(f"\n******** Previous Available Balance is : {previous_amount}")
                print(f"\n******** Widraw Amount : {amount}")
                print(f"\n ******* Current Available Balance : {current_amount}\n")


    def emi_calculator(self , p , R , n):
        # Calculating interest rate per month
        r = R/(12*100)

        # Calculating Equated Monthly Installment (EMI)
        emi = p * r * ((1+r)**n)/((1+r)**n - 1)

        print("Monthly EMI = ", emi)
        print()

