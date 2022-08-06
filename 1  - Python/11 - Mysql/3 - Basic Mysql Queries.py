


# basic Mysql Queries

# 1 - to show all the databases .

        #>>> show databases;

        # output
            '''
            mysql> show databases;
            +--------------------+
            | Database           |
            +--------------------+
            | collage            |
            | dbuser             |
            | emp                |
            | hotel              |
            | information_schema |
            | junnu              |
            | mysql              |
            | performance_schema |
            | sakila             |
            | sys                |
            | test               |
            | world              |
            +--------------------+
            '''
            
#################################################################################

# 2 - create queries .
    # 1 - create database

        # 1 - Query 
        # This query is used to create database
        # if database is exists in our severit will through an error
        
        # >>> create database database_name;
        # eg
        # >>> create database company;

    #************************************************************************
        
        # 2 - Query 
        # This query is used to create database
        # if database already exists in our server it will not through any error
        
        # >>> create database if not exists database_name;
        # eg
        # >>> create database if not exists company;


    #*************************************************************************

        # use database to perform Operation

        #Query
        # >>> use database_name;
        # eg
        # >>> use company;


##############################################################################
        
    # 2 - create table

    # Query to check all the tables inside the database
    # >>> show tables;

    #*******************************************************************************

    #  1 - Query to create table
    # columns (emp_id , emp_name , emp_age , emp_loc , DOJ , emp_salary , Designation)

    # Query
    '''
    
        mysql> create table emp_info (
            emp_id INT ,
            emp_name varchar(30) ,
            emp_age int ,
            emp_loc varchar(50),
            date_of_join date ,
            emp_salary decimal,
            designation varchar(50)
            );
    '''
    #************************************************************************
    
    # Quey 2
    # if table exists in our system it will not through any error 
    '''
    
        mysql> create table if not exists emp_info (
            emp_id INT ,
            emp_name varchar(30) ,
            emp_age int ,
            emp_loc varchar(50),
            date_of_join date ,
            emp_salary decimal,
            designation varchar(50)
            );
    '''

    #****************************************************************************

    # Query to check the description of our table
    
    # >>> DESC table_name;
    # eg
    # >>> DESC emp_info;

    # output
    '''
        mysql> desc emp_info;
    +--------------+---------------+------+-----+---------+-------+
    | Field        | Type          | Null | Key | Default | Extra |
    +--------------+---------------+------+-----+---------+-------+
    | emp_id       | int           | YES  |     | NULL    |       |
    | emp_name     | varchar(30)   | YES  |     | NULL    |       |
    | emp_age      | int           | YES  |     | NULL    |       |
    | emp_loc      | varchar(50)   | YES  |     | NULL    |       |
    | date_of_join | date          | YES  |     | NULL    |       |
    | emp_salary   | decimal(10,0) | YES  |     | NULL    |       |
    | designation  | varchar(50)   | YES  |     | NULL    |       |
    +--------------+---------------+------+-----+---------+-------+

    '''
            


##############################################################################

# 3 - insert query
    # 1 - insert single record (row)
    
    '''
    >>>insert into emp_info ( emp_id ,emp_name ,emp_age ,emp_loc , date_of_join , emp_salary , designation)
        values
        (1 , "Shubham" , 24 , "Thane" , "2021-08-23" , 23500.50 , "Developer");
    '''


    #************************************************************************************
    
    # 2 - insert multiple records (rows)

    '''
    mysql> insert into emp_info ( emp_id ,emp_name ,emp_age ,emp_loc , date_of_join , emp_salary , designation)
    alues
    (2 , "vaibhav" , 22 , "kalyan" , "2021-03-10" , 20000.00 , "Tester"),
    (3 , "Aniket" , 26 , "kalwa" , "2022-01-28" , 18000.00 , "Developer"),
    (4 , "Rahul" , 20 , "Diva" , "2021-06-18" , 25000.50 , "Tester");
    '''

######################################################################################
    
# 4 - fetch columns

    #***********************************************************************************
    # 1 - fetch all the columns info
    
    #>>> Select * from table_name;
    # eg
    # >>> Select * from emp_info;


    #***************************************************************************************
    
    # 2 - fetch single columns

    # syntax
    #>>> select column_name(s) from table_name;

    #Query
    #>>> select emp_name from emp_info;


    #****************************************************************************************
    
    
    # 3 - fetch multiple columns 

    # syntax
    #>>> select column_name(s) from table_name;

    # query
    #>>> select emp_id , emp_name , designation from emp_info;

























