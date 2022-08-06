


# Set Operations


# The SQL Set Operation is used to combine the two or more SQL select Statements


# Type Of Operations In SET

# 1 - Union
# 2 - Union All
# 3 - Intersection    (Mysql Does Not Support )
# 4 - Minus           (Mysql Does Not Support )

# Example table

# ************************************************************************

# table_1

> create table table_1 (id INT primary key );

# insert values
>>>insert into table_1 values(1),(2),(3),(4),(5);

# table_1

+----+
| id |
+----+
|  1 |
|  2 |
|  3 |
|  4 |
|  5 |
+----+

#***************************************************************************


# table 2

>>> create table table_2 (id INT  );

# insert values
>>>insert into table_2 values(4),(5),(6),(7),(8);


# table_2

+------+
| id   |
+------+
|    4 |
|    5 |
|    6 |
|    7 |
|    8 |
+------+

#***************************************************************************



# 1 - Unionn

# The Sql Union Operation is Used to combine the result of two or more SQL Select Queries
# IN the Union Operation All the number of datatypes and columns must be same in length
# The Union Operation Eliminates the dublicates rows from its result, 

# Syntax

selct column_names from table1
union
select column_names from table2

# Query

mysql> select id from table_1
    -> union
    -> select id from table_2;


#***************************************************************************************
    
# 2 - Union All

# Union All cant eliminate the dublicate rows or records 

# Syntax
'''
selct column_names from table1
union all
select column_names from table2
'''

# Query 

mysql> select id from table_1
    -> union all
    -> select id from table_2;



# ***************************************************************************************

# 3 - Intersection

# Intersection Operator returns the distict (common ) records  from two or more tables

# Syntax
'''
select id from table1
intersection
select id from table2;
'''


# but MYSQL DOES NOT support intersection

# we have a alternate query to perform Insersection Operation 


# alternate Query 

>>> select DISTINCT id from table_1
    inner join table_2 using (id);


#*******************************************************************************************


# 4 - Minus    (MYSQL DOES NOT SUPPORT )

# The MINUS Operator returns the uniq elemenet from the table
# which is not found in the second table


# Syntax

'''
select id from table_1
minus
select id from table_2;
'''


# Alternate Query to perform minus Operation
'''
>>> select id from table_1
    Left JOIN table_2 using (id)
    where table_2.id is NULL;

'''































