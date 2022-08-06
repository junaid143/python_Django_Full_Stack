# Hybrid Inheritence


# Example 1
'''
class grand_father:   # A
    def __init__(self):
        self.gname = "Grand_father"
        self.gage = 70

    def m1(self):
        print(f"Grandpaa Name is {self.gname} and granpaa's age is {self.gage}")

class mother(grand_father):   #B(A)
    def __init__(self):
        super().__init__()
        self.mname = "Mother"
        self.mage = 45

    def m2(self):
        print(f"Mother name is {self.mname} and age is {self.mage}")

class father(grand_father):  # C(A)
    def __init__(self):
        super().__init__()
        self.fname = "Father"
        self.fage = 50

    def m3(self):
        print(f"Father name is {self.fname} and age is {self.fage}")

class son(mother , father):  # D(B,C)
    def __init__(self):
        super().__init__()
        self.sname = "Son"
        self.sage = 15

    def m4(self):
        print(f"Son name is {self.sname} and age is {self.sage}")


ob = son()
'''

# Example 2

class company: #A
    def __init__(self):
        self.cname = "Abc techno"
        self.emp_count = 250
        self.req = "senior Developer"

    def get_comp_info(self):  # accessor / getter 
        print(f"Company Name is : {self.cname}")
        print(f"Employee Count : {self.emp_count}")
        print(f"Company Requirments : {self.req}")

    def set_comp_info(self,cname,emp_count,req):
        self.cname = cname
        self.emp_count = emp_count
        self.req = req


class developer(company): #B(A)
    def __init__(self):
        super().__init__()
        self.dev_id = "Dev_4502"
        self.dev_count = 48

    def get_developer_info(self):
        print(f"Develover Id is : {self.dev_id}")
        print(f"Developer count is : {self.dev_count}")

    def set_developer_info(self,dev_id,dev_count):
        self.dev_id = dev_id
        self.dev_count = dev_count

class tester(company):  #C
    def __init__(self):
        super().__init__()
        self.tester_id = "test_3985"
        self.tester_count = 21

    def get_tester_info(self):
        print(f"Tester Id is : {self.tester_id}")
        print(f"Tester count is : {self.tester_count}")

    def set_tester_info(self,tester_id,tester_count):
        self.tester_id = tester_id
        self.tester_count = tester_count


class project(developer,tester): # D
    
    def __init__(self):
        super().__init__()
        self.project_id = "Nothing_423"
        self.project_name = "Nothing Project"
        self.project_leader = "Rahul"

    def get_project_info(self):
        print(f"Project Id is : {self.project_id}")
        print(f"Project Name is : {self.project_name}")
        print(f"Project Leader is : {self.project_leader}")

    def set_project_info(self,project_id,project_name,project_leader):
        self.project_id = project_id
        self.project_name = project_name
        self.project_leader = project_leader














































