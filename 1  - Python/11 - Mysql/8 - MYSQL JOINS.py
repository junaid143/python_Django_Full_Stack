

# Joins



1 - INNER JOIN


# mysql inner join is used to fetch common recods into the multiple tables


# syntax

>>> select column_names from table_1
    inner join table_2
    on table_1.column_name = table2.column_name;



# Query

>>> select * from customer
    inner join orders
    on customer.c_id = orders.c_id;




# Full Join (Full Outer Join )    # Mysql Does not Support Directly Full Join 

# return Common Data and left table data and right table data

# We use alternet Query To ret the full outer jin result


# Syntax

select columns_names from table_1
Full Join table_2
On table_1.column_name = column_2.column_name;

#******************************************************************************

# alternet Query using union

# demo table
# 1 - table_1

>>> create table table_1(id int auto_increment, name varchar(50) , age int , primary key(id));

# insert values into table_1

>>> insert into table_1(name , age ) values
("vaibhav",22),
("Rohit",22),
("rahul",22),
("Shubham",22),
("Aniket",22),
("mayur",22);


# 2 - table_2

>>> create table table_2(emp_id int auto_increment, emp_name varchar(50) , id int ,
                         primary key(emp_id),foreign key(id) references table_1(id));


# insert into table_2 values

>>> insert into table_2(emp_name , id ) values
("prasad",1),
("vaibhav",1),
("Rohit",2),
("vaibhav",1),
("rahul",3),
("rahul",3);


# alternet query for full outer join 

select * from table_1 left Join table_2 on table_1.id = table_2.id
union
select * from table_1 right Join table_2 on table_1.id = table_2.id;


#********************************************************************************

# Self Join

 a self join is a join that used to join table with itself


 # Query
 >>> select A.id , A.name , A.age , B.id , B.name from table_1 A,table_1 B
     where A.id = B.id order by a.id;




























