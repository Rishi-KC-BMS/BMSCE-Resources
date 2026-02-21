show databases;
create database IF NOT exists rishidatabase;
use rishidatabase;
show tables;


create table person (driver_id varchar(10),
name varchar(20), address varchar(30), primary key(driver_id));

create table car(reg_num varchar(10),model varchar(10),year int, primary
key(reg_num));

create table accident(report_num int, accident_date date, location
varchar(20),primary key(report_num));

create table owns(driver_id varchar(10),reg_num varchar(10),
primary key(driver_id, reg_num),
foreign key(driver_id) references person(driver_id),
foreign key(reg_num) references car(reg_num));

create table participated(driver_id varchar(10), reg_num varchar(10),
report_num int, damage_amount int,
primary key(driver_id, reg_num, report_num),
foreign key(driver_id) references person(driver_id),
foreign key(reg_num) references car(reg_num),
foreign key(report_num) references accident(report_num));

insert into accident values (11, '2003-01-01','Mysore Road');
insert into accident values (12,'2004-02-02','South end Circle');
insert into accident values (13,'2003-01-21','Bull temple Road');
insert into accident values (14,'2008-02-17','Mysore Road');
insert into accident values (15,'2004-03-05','Kanakpura Road');

insert into person values ('A01','Richard','Srinivas Nagar');
insert into person values ('A02','Pradeep','Rajaji Nagar');
insert into person values ('A03','Smith','Ashok Nagar');
insert into person values ('A04','Venu','NR Colony');
insert into person values ('A05','John','Hanumanth Nagar');

insert into car values('KA052250','Lexus',2002);
insert into car values('KA031181','Lancer',1990);
insert into car values('KA095477','Toyota',2010);
insert into car values('KA095408','Audi',2016);
insert into car values('KA041702','BMW',1995);

insert into owns values('A01','KA052250');
insert into owns values('A02','KA031181');
insert into owns values('A03','KA095477');
insert into owns values('A04','KA095408');
insert into owns values('A05','KA041702');

insert into participated values('A01','KA052250',11,10000);
insert into participated values('A02','KA031181',12,50000);
insert into participated values('A03','KA095477',13,25000);
insert into participated values('A04','KA095408',14,3000);
insert into participated values('A05','KA041702',15,5000);

insert into accident values(16,'2008-03-08','Domlur');


update participated set damage_amount=25000
where reg_num='KA095408' and report_num=14;


select count(distinct driver_id) CNT
from participated a, accident b
where a.report_num=b.report_num and b.accident_date like '%08';

SELECT * FROM PARTICIPATED ORDER BY DAMAGE_AMOUNT DESC;
SELECT AVG(DAMAGE_AMOUNT) FROM PARTICIPATED;

SELECT NAME FROM PERSON A, PARTICIPATED B WHERE A.DRIVER_ID = B.DRIVER_ID AND
DAMAGE_AMOUNT > (SELECT AVG(DAMAGE_AMOUNT) FROM PARTICIPATED);

SELECT MAX(DAMAGE_AMOUNT) FROM PARTICIPATED;

SELECT * FROM accident;
SELECT * FROM person;
SELECT * FROM car;
SELECT * FROM owns;
SELECT * FROM participated;

----------------------------week-4--------------------------

SELECT * FROM PARTICIPATED ORDER BY DAMAGE_AMOUNT DESC;
SELECT AVG(DAMAGE_AMOUNT) FROM PARTICIPATED;
DELETE FROM PARTICIPATED WHERE DAMAGE_AMOUNT<(SELECT AVG (DAMAGE_AMOUNT) FROM PARTICIPATED); 
SELECT NAME FROM PERSON A, PARTICIPATED B WHERE A.DRIVER_ID = B.DRIVER_ID AND DAMAGE_AMOUNT>(SELECT AVG(DAMAGE_AMOUNT) FROM PARTICIPATED);
SELECT MAX(DAMAGE_AMOUNT) FROM PARTICIPATED;
