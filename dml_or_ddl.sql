
ddl commands

create table employee (name varchar(20),email varchar(10),dob date);
drop table table_name;
drop table employee;
alter table stud_details add (address varchar(20));
alter table stud_details modify (address varchar(20));
truncate table table_name;
truncate table employee;

dml commands
insert into stud_details (col1,col2...colN) values (value1,value2...valueN);
update students set username = 'sonoo' where students_id = '3';
delete from table_name[where conditions]
delete from student where student_age > 18

