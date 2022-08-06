

# Mysql Stored Procedure


Stored Procedure is a collection of pre-compiled SQL statements  stored inside he database

#***********************************************************

#1 -  Simple stored procedure with single query

create procedure show_all_records() 
select * from emp_info;


# call procedure

>>> call show_all_records();

#***********************************************************

# 2 -  Simple stored procedure with multiple query


# delimiter is a keyword i sql which help you to implemet multiple of query

delimiter &&

create procedure data1()

begin

select emp_id , emp_name ,emp_salary ,designation from emp_info;
select count(emp_id) as data_count from emp_info;

end &&

delimiter ;

#****************

# call data1();

#***********************************************************

# 3 - create procedure with single input

delimiter &&

create procedure show_data(IN var INT)

begin

select * from emp_info limit var;

end &&

delimiter ;

# call show_data(2);
# call show_data(4);
# call show_data(6);

#***********************************************************

# 4 - create procedure with multiple input


delimiter &&

create procedure filter_data(IN desig Varchar(50) , IN num INT)

begin

select * from emp_info where designation = desig limit num;

end &&

delimiter ;

# call procedure
>>> call filter_data("Developer",4);

>>> call filter_data("Tester",3);


# **********************************************************

5 - creat procedure with single output

# Query 

delimiter &&

create procedure get_data(OUT result INT)

begin

select max(emp_salary) into result from emp_info;

end &&

delimiter ;

# call get_data(@result);
# select @result;


#*********************************************************************************

6 - creat procedure with multiple output

# Query 

delimiter &&

create procedure get_data1(OUT result INT , OUT result1 INT)

begin

select max(emp_salary) into result from emp_info;
select min(emp_salary) into result1 from emp_info;

end &&

delimiter ;

# call get_data1(@result , @result1);
# select @result , @result1;


#*********************************************************************************************

# 7 - procedure with input and output


delimiter &&

create procedure input_output(IN name varchar(50) , OUT data INT)

begin

select emp_salary into data from emp_info where emp_name = name;

end &&

delimiter ;

# call procedure

>>> call input_output("vaibhav" , @data);

>>>select @data;

#*********************************************************************************************

# 8 - procedure with input and output


delimiter &&

create procedure in_out(INOUT var INT)

begin

select emp_salary into var from emp_info where emp_id = var; 

end &&

delimiter ;


# call procedure 
>>> set @var = 4;

>>> call in_out(@var);

>>> select @var;


#*****************************************************************************

show all the stored procedure in database

>>> show procedure status where db = 'test';



# drop procedure

>>> drop procedure data;

















