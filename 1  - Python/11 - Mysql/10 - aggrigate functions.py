
# aggrigate Functions


# 1 - count()
# 2 - sum()
# 3 - avg()        # average
# 4 - min()        # minimum
# 5 - max()        # maximum
# 6 - concat()     # concatenation
# 7 - group_concat()
# 8 - limit       
# 9 - desc         # descending 



# 1 - count()
# return count of specific column

# Query
>>> select count(emp_name) from emp_info;

>>> selct count(emp_name) as data_count from emp_info;


#**********************************************************

#2 - sum()

# it will return sum of the column
# works only with Numeric type column

# query

>>> select sum(emp_salary) from emp_info;

>>> select sum(emp_salary) as sum_of_salary from emp_info;


#***************************************************************

# 3 - avg()

# it will return the average (mean ) of the column
# # works only with Numeric type column

# query
>>> select avg(emp_salary) from emp_info;

>>> select avg(emp_salary) as average_salary from emp_info;

#***************************************************************

# 4 - min()

# return the minimum value inside the column

# Query

# int column
>>> select min(emp_salary) from emp_info;

>>> select min(emp_salary) as minimum_salary from emp_info;

# string column

>>> select min(emp_name) from emp_info;


#****************************************************************

# 5 - max()

# return the maximum value inside the column

# query

>>> select max(emp_salary) from emp_info;

>>> select max(emp_salary) as maximum_salary from emp_info;

#****************************************************************

# 6 - concat()     # concatenation

# return concatenation

>>> select concat(emp_name , "    " , emp_address)  from emp_info;

>>> select concat(emp_name , "    " , emp_address) as combine_data from emp_info;

#****************************************************************

# 7 - group_concat()

# create demo table for group_concat

create table demo(id int, name varchar(50), age int, qualification varchar(50));

# insert some records inside demo table

insert into demo(id , name , age , qualification ) values
(1 , "vaibhav" , 20 , "BSC CS"),
(2 , "shubham" , 22 , "BE"),
(3 , "Rohit" , 21 , "BSC IT"),
(4 , "mayur" , 23 , "BSC CS"),
(1 , "vaibhav" , 20 , "MS CS"),
(2 , "shubham" , 22 , "ME"),
(3 , "Rohit" , 21 , "MSC IT"),
(4 , "mayur" , 23 , "MSC CS");



# Group_concat() query

>>>  select id ,group_concat(qualification) as "qualification" from demo group by id;

>>> select name ,group_concat(qualification) as "qualification" from demo group by name;

>>> select age ,group_concat(qualification) as "qualification" from demo group by age;



#****************************************************************
# 8 - limit

# we can retrict the output using limit

# Query 
>>> select * from emp_info;

>>> select * from emp_info limit 3;

>>> select emp_id , emp_name from emp_info where emp_address = "thane" limit 1;

#****************************************************************

# 9 - desc         # descending 

# show output in descending order

>>> select * from emp_info;

>>> select * from emp_info order by emp_id desc;

>>> select * from emp_info order by emp_name desc;

>>> select * from emp_info order by emp_address desc;


