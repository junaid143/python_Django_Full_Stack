

# Scalar Function

scalar function are the built-in function in sql and whatever be the input provided
to the scalar function
the output return by these function will always be a single value

1 - UCASE()
2 - LCASE()
3 - MID()
4 - LENGTH()
5 - ROUND()
6 - NOW()
7 - FORMAT()


#***********************************************************************************

1 - UCASE()
# RETURN UPPER CASE DATA

>>> select ucase("junaid");

>>> select ucase("junaid") as upper_case_data ;


>>> select id , name , ucase(name) as upper_case_data from table_1;


#******************************************************************************
2 - LCASE()


return lower case data

>>> select lcase("JUNAID")
>>> select lcase("JUNAID") as lowercase_data;

>>> select id,name , lcase(name) as lowercase_data from table_1;

#******************************************************************************


3 - MID(string , start , length)

# return mid value from the string data

>>> select mid("python" , 2 ,3);

>>> select mid("python" , 2 ,3) as mid_data;

>>> select id,name , mid(name , 3 , 5) as mid_data from table_1;

#*****************************************************************************

#4 - LENGTH()

# return the length of the string data 


>>> select length("python");

>>> select length("python")as data_length;

select id,name ,length(name) as data_length from table_1;

#*****************************************************************************

5 - ROUND()

# round function is used to round numeric column to the number decimal

>>> select round(10.25879652);

>>> select round(10.25879652) as numeric_data;

>>> select round(10.25879652 , 3) as numeric_data;

>>> select round(10.25879652 , 2) as numeric_data;


>>> select id ,name, round(salary,2) as salary from table_1;

#*****************************************************************************

6 - NOW()

# it is used to get the current datae and time

>>> select now();


# add column in to the existing table 
>>> alter table table_2 add data_time datetime;

>>> insert into table_2(emp_name , id , data_time) values
    ("rohit" , 2 , now());

#*****************************************************************************

7 - FORMAT()

fomate() is used to format how column is to be dislayed

# syntax

>>> format(value , decimal)


# query

>>> select format(12.45698712 , 2) as format_number 

>>>  select emp_id , emp_name , emp_age , emp_salary , format(emp_salary/0.5 , 3) as salary_data
    from emp_info;

>>> select id ,name , format(age*2000 , 2) from table_1;

























