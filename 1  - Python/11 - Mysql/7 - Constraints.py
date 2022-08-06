

# MYSQL Contraints

# Constraints is used to implement the restriction on columns




# 1 - NOT NULL
# 2 - UNIQUE
# 3 - DEFAULT
# 4 - CHECK

# 5 - AUTO_INCREMENT
# 6 - PRIMARY KEY
# 7 - FORIEGN KEY 




# 1 - NOT NULL
# NoT Null does not allow any null values


# 2 - UNIQUE
# Unique does not allow dublicate values 


# 3 - DEFAULT

# 4 - CHECK

# create table with constraints

'''
> create  table student(s_id INT NOT NULL ,
    -> s_name varchar(20) NOT NULL,
    -> s_age INT NOT NULL,
    -> contact BIGINT NOT NULL UNIQUE,
    ->  city varchar(50) NOT NULL DEFAULT "MUMBAI",
    -> check (s_age < 25));
'''

# to inset Values ;
'''
> insert into student (s_id , s_name , s_age , contact) values
    -> (1 , "ayaan" , 20 , 9876541235);
'''
#***********************************************************************************
# 5 - AUTO_INCREMENT

# by default values start from 1 and increment by 1

# *******************************************************************************
# 6 - PRIMARY KEY

'''
> create table customer(c_id INT auto_increment ,
    c_name varchar(50) not null,
    c_email varchar(50) not null,
    primary key(c_id) );
'''

# insert values

>> insert into customer(c_name , c_email) values("Rohit" , "rohit@gmail.com");
>> insert into customer(c_name , c_email) values("vaibhav" , "vaibhav@gmail.com");

# not null unique 

#*********************************************************************************

# 7 - FORIEGN KEY 
'''
> create table orders(o_id INT auto_increment ,
    o_date date not null,
    amount INT not null ,
    c_id INT NOT null,
    primary key(o_id),
    foreign key(c_id) references customer(c_id));
'''


# insert values

insert into orders(o_date , amount ,c_id ) values
("2022-01-25" , 250 , 1),
("2022-01-30" , 50 , 1),
("2022-02-10" , 500 , 4);

#***********************************************************************************

# add constrain in Existing table



# create table temp(id int,name varchar(50),conatct varchar(50));




#********************************************************************************

                    # Add Constain in Existing table 

#********************************************************************************
# add Not null constrain in existing table

>>> alter table temp modify id int NOT null;

#********************************************************************************


# add UNIQUE Constrain to existing table

>>> alter table temp add unique(id);

#**********************************************************************************

# add default constraint in existing table

>>> alter table temp alter contact set default 1111111;

#************************************************************************************

# Add check constraint in existing column

>>>  alter table temp add check (age > 18);

#***************************************************************************************

# Add primary key constraint in existing table

>>> alter table temp add primary key(id);


#**************************************************************************************

# add foreign key in existing table

>>> alter table student add foreign key(s_id) references temp(id);























































