
# Triggers

# Trigger is a special type of stored procedure that is invoked automatically
  in response to an event

# Each trigger is associated with a table
# which activated on any DML statement
eg
Insert
update
Delete


# types of triggers

1 - Before Insert
2 - After Insert
3 - Before Update
4 - After Update
5 - Before Delete
6 - After Delete


#********************************************************************************************

# create table for trigger

create table student(s_id Int auto_increment ,
name varchar(50),
division varchar(50),
age int,
contact bigint,
location varchar(50),
primary key(s_id));


# insert values

insert into student(name , division,age,contact,location) values
("harsh","A",22,9874563215,"Thane");

#*******************************************************************************************
1 - Before Insert

# create trigger Before Insert Chech the age is less 10 then set age = 10

# Trigger Query

delimiter &&

create trigger before_insert_data BEFORE INSERT
ON student for each row

begin

if new.age < 10 then
set new.age = 10;

end if ;

end &&

delimiter ;

# check trigger
mysql> insert into student(name , division,age,contact,location) values
        ("shubham","A",2, 75345695,"");

#*******************************************************************************************

2 - After Insert

# create trigger after insert

# insert values into student table and trigger automatically insert
   values into batch table as well

# create table batch

create table batch (id int auto_increment primary key,
name varchar(50),division varchar(50));

# QUERY to create trigger

Delimiter &&

create trigger insert_into_batch AFTER INSERT
ON student for each row

begin

insert into batch(name , division) values (new.name , new.division);

end &&

Delimiter ;

# check trigger
mysql> insert into student(name , division,age,contact,location) values
       ("rohit","A",5, 4563217896,"Kalyan");


#****************************************************************************************
3 - Before Update

# create trigger before update
# if new.age is greater then 30 the set old.age 


# Query for trigger


Delimiter &&

create trigger update_age BEFORE UPDATE
On student for each row

begin

if new.age >= 30 then
set new.age = old.age;

end if ;

end &&

Delimiter ;

# check trigger

>>> update student set age = 35 where s_id = 4;

#***********************************************************************************************

4 - After Update

# create trigger after update
to store old data into log table


# create table log


create table log(id int auto_increment primary key,
user varchar(100) , data text);

# Query to create trigger

delimiter &&

create trigger after_update_data AFTER UPDATE
ON student for each row

begin

insert into log (user , data) values
(current_user() , concat(old.s_id ," updated by ",old.name , " to ",new.name , " Time is ",now()));

end &&

delimiter ;

# check trigger
>>> update student set name = "rahul" where s_id = 2;

#**********************************************************************************************

5 - Before Delete Trigger

# create trigger and restrict user to delete any record


delimiter &&

create trigger before_delete_data BEFORE DELETE
ON student for each row

begin

SIGNAL
sqlstate "15000"
set MESSAGE_TEXT = "Not Allowed to Delete any record from the student table";

end &&

delimiter ;



# check trigger

>>> delete from student where s_id = 1;


#*********************************************************************************************

6 - After Delete Trigger

# create backup of deleted data

# create backup table

create table backup(id int auto_increment,
user varchar(100),
s_id INT,
name  varchar(50),
division varchar(50),
age int,
contact bigint,
location varchar(50),
primary key(id));

# Query to create trigger after delete

delimiter &&

create trigger ddata AFTER DELETE
ON student for each row

begin

insert into backup(user ,s_id , name,division,age,contact,location) values
(concat("user deleted data ",current_user()),old.s_id,old.name,
 old.division,old.age,old.contact,old.location); 

end &&

delimiter ;

>>>delete from student where s_id = 1;

>>> drop trigger after_delete_data;




























