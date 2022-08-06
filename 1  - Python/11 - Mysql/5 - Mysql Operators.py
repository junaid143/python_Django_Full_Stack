

# MYSQL Operator

# operator supports in mysql



# 1 - Arithmetic Operator

# 2 - Logical Operator

# 3 - Relational or Comparision Operator

# 4 - IS NUll , IS Not NUll Operator

# 5 - IN , Not In Operator

# 6 - Between _ _AND_ _ , Not Between _ _AND_ _    operator

# 7 - wild card Characters

# 8 - Like , Not Like Operator



#**************************************************************************************


# 1 - Arithmetic Operator

# + , - , * , / , %


# these are the arithmetic operator to perform maths operation on the tables

# >>>select emp_id , emp_name , emp_salary+1000 , designation from emp_info;

# >>>select emp_id , emp_name , emp_salary - 2000 , designation from emp_info;

# >>>select emp_id , emp_name , emp_salary *2  from emp_info;

# >>>select emp_id , emp_name , emp_salary /2  from emp_info;

# >>>select emp_id , emp_name , emp_salary %2  from emp_info;



# **********************************************************************************

# 2 - Logical Operator

# AND    , &&

# all expression True then AND return True otherwise False


# OR     , ||
# if one Expression is True The its Return True
# otherwise False

#************************************************************************************

# 3 - Relational or Comparision Operator

#   >       greater 
#   <       less then 
#   >=      greater equal 
#   <=      lenn then equal

#   =         Equal
#   != , <>   Not equal


# Queries

# Q1.
# Fetch only those records where employee designation is Developer .

# Query
#>>> select * from emp_info where designation = "Developer";




# Q2
# fetch only those records where salary is more the 20000.

# query
# >>> select * from emp_info where salary > 20000;

# >>> select * from emp_info where emp_salary >= 20000;




# Q3
# fetch Aniket id ,salary and designation

# query

# > select emp_name , emp_id , emp_salary , designation from emp_info where emp_name = "aniket";


# with logical operators

#Q 4
# Fetch thos records the employee salary is in between 18000 to 25000

# Query
# >>> select * from emp_info where emp_salary >= 18000 AND emp_salary <=25000;
# >>> select * from emp_info where emp_salary >= 18000 && emp_salary <=25000;


# Q5
# check aniket ,vaibhav and ayaan is employee or not and fetch the records

'''
mysql>select * from emp_info
    -> where
    -> emp_name = "aniket" or emp_name = "vaibhav" or emp_name = "ayaan";

'''
#                   or
'''
mysql>select * from emp_info
    -> where
    -> emp_name = "aniket" || emp_name = "vaibhav" || emp_name = "ayaan";
'''


#***************************************************************************************

# 4 - IS NUll , IS Not NUll        Operator

# Null is datatype to represent Empty data
#



#Q1 -  fetch Those record which dont have joining dates

# >>>> select emp_id,emp_name from emp_info where date_of_join IS NULL;


#Q1 -  fetch Those record which have joining dates

# >>>> select emp_id,emp_name from emp_info where date_of_join IS Not NULL;


#******************************************************************************************

# 5 - IN , Not In Operator

#"ajay" , "vijay" , "aniket" , "rahul"


# >>> select * from emp_info where emp_name IN ("ajay" , "vijay" , "aniket" , "rahul");

#>>>select * from emp_info where emp_name Not IN ("ajay" , "vijay" , "aniket" , "rahul");


#********************************************************************************************

# 6 - Between _ _AND_ _ , Not Between _ _AND_ _    operator

# works with numeric data


# >>> select * from emp_info where emp_salary BETWEEN 18000 AND 25000;


# >>> select * from emp_info where emp_salary Not BETWEEN 18000 AND 25000;



#***********************************************************************************************

# 7 - wild card Characters

# '%'   # for any character or for any length

# '_'   # for any character but single lenth 


#*****************************************************************************************

# 8 - Like , Not Like Operator

# >>> select emp_name from emp_info where emp_name like 'a%'

# >>>  select emp_id ,emp_name from emp_info where emp_name like 'r%t';

#>>> select * from emp_info where emp_name like 'a_ _ _ _ _';

# >>> select * from emp_info where emp_name not like 'r_ _ _ _';






















