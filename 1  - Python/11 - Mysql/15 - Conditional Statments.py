
# Conditional Statements

1 - IF()
2 - IFNULL()
3 - NULLIF()

4 - IF
5 - IF ELSEIF

#********************************************************************************************

#1 -  IF(Expression1 ,Expression 2,Expression 3)


# If() function takes 3 Expression
if Expression 1 is True then Expression2 will Excecute
if Expression 1 if False then Expression3 will Execute


# Syntax

>>> IF (Expression1,Expression2,Expression3) ;

# Query 1

>>> Select IF( 10>5 , "True" , "False");

# Query 2

>>> Select IF( 10>20 , "True" , "False");

# Query 3

>>> select emp_id,emp_name,emp_age,IF(emp_age > 20 ,"True" , "False") from emp_info;

#********************************************************************************************


2 - IFNULL(Expression1 , Expression2)


it will take 2 expression
if Expression 1 is Not Null then it will return Expression 1
if Expression 1 is Null then it will return Expression 2


# Syntax

>>> IFNULL(Expression1 , Expression2);

# Query

>>> Select IFNULL("python" ,"CLass");

# output
+---------------------------+
| IFNULL("python" ,"CLass") |
+---------------------------+
| python                    |
+---------------------------+

# Query 2

>>> Select IFNULL(NULL ,"CLass");
# Output
+-----------------------+
| IFNULL(NULL ,"CLass") |
+-----------------------+
| CLass                 |
+-----------------------+

# Query 3

>>> select emp_id , emp_name ,emp_loc,IFNULL(emp_loc , "MUMBAI") from emp_info;


#*****************************************************************************************

3 - NULLIF(Expression1 , Expression2)

it will take 2 Expression

if Expression1 and Expression2 are the equal then it will return NULL
if Expression1 and Expression2 are not not equal then it will return Expression1

# Syntax

>>> NULLIF(Expression1 , Expression2);


# Query 1
>>> select NULLIF("Thane" , "Thane");
# Output
+---------------------------+
| NULLIF("Thane" , "Thane") |
+---------------------------+
| NULL                      |
+---------------------------+

# Query 2

>>> select NULLIF("Mumbai" , "Thane");
# output
+----------------------------+
| NULLIF("Mumbai" , "Thane") |
+----------------------------+
| Mumbai                     |
+----------------------------+


# Query 3

>>> select emp_id,emp_name,emp_loc , NULLIF(emp_loc , "Thane") from emp_info;


#********************************************************************************************

# IF statement


MYSQL IF STemenet  to execute a block of SQL code based on a specific condition

# Note :
IF()  and IF stement are different


# IF Statement have Three Forms

1 - IF - Then
2 - IF then -Else
3 - IF Then -ElSEIF-Else

#**********************************************************************************************

1 - IF -Then

# Syntax

IF Condition Then
    Statement;

End If ;


#**********************************************************************************************
2 - IF then -Else

# Syntax

IF Condition Then
    Statement;
Else
    else-statement;
    
End If ;

#**********************************************************************************************

3 - IF Then -ElSEIF-Else

# Syntax

IF Condition Then
    Statement;
ELSEIF Cindition Then
    Elseif-staemenet ;
    
ELSEIF Cindition Then
    Elseif-staemenet ;
Else
    else-statement;
    
End If ;



























