

# joins

# 1 - Inner Join


# table 1
# customer

# table 2
# orders

# inner join is used to fetch common records  from the tables

# syntax

>>> select column_names from table_1
    INNER JOIN table_2
    ON table_1.column_name = table_2.column_name ;


# query

>>> select * from customer
    INNER JOIN orders
    ON customer.c_id = orders.c_id;



# LEFT JOIN

# left join is used to fetch common or first table records


# Syntax
>>> select column_names from table_1
    LEFT JOIN table_2
    ON table_1.column_name = table_2.column_name ;

#Query
>>> select * from customer
    LEFT JOIN orders
    ON customer.c_id = orders.c_id;


# Query 2
>>> select * from customer
    LEFT JOIN orders
    ON customer.c_id = orders.c_id
    order by customer.c_id;


# Query 3
# show only customer name location and order amount

>>> select customer.c_name , customer.c_address , orders.amount from customer
    LEFT JOIN orders
    ON customer.c_id = orders.c_id ;
    


# RIGHT JOIN

# right join keyword return all records from the right table (table 2)
# and the matching records from left table (1)


# syntax
>>> select column_names from table_1
    RIGHT JOIN table_2
    ON table_1.column_name = table_2.column_name ;

# Query

>>> select * from customer
    RIGHT JOIN orders
    ON customer.c_id = orders.c_id;

# Query 2
>>> select customer.c_name ,orders.o_date_time , orders.amount from customer
    RIGHT JOIN orders
    ON customer.c_id = orders.c_id 
    where customer.c_id = 2 ;



# FULL OUTER JOIN 

# mysql does not supports mysql outer join 

# mysql outer join keywords return all records when there is a match in left (table1)
# or right ( table 2) records

# full join and full outer join are the same

# we can use alternet query to achive full outer join

eg
>>> left join
    union
    right join

# Syntax
>>> select column_names from table_1
    FULL OUTER JOIN table_2
    ON table_1.column_name = table_2.column_name ;






# Cross JOIN

# the cross keywords return all the records from both the tables (table 1 and table 2)

# Syntax
>>> select columns_names from table_1
    CROSS JOIN table_2;

# Query
>>> select * from customer CROSS JOIN orders;




























    
