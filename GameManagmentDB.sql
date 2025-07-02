create database exp12;
show databases;
use exp12;

create table CLINTE_MASTER(
CLINTENO varchar(6),
NAME varchar(20) NOT NULL,
ADDRESS1 varchar(30),
ADDRESS2 varchar(30),
CITY varchar(15),
PINCODE integer,
STATE varchar(15),
BALDUE decimal(10,2),
primary key(CLINTENO)
);


create table PRODUCT_MASTER(
PRODUCTNO varchar(6),
DESCRIPTION varchar(15) NOT NULL,
PROFITPERCENT decimal(4,2) NOT NULL,
UNITMEASURE varchar(10) NOT NULL,
QTYONHAND integer(8) not null,
REORDERLVL integer(8) not null,
SELLPRICE decimal(8,2) not null,
COSTPRICE decimal(8,2) not null,
PRIMARY KEY(PRODUCTNO)  
);

create table salesman_master(
salesmanno varchar(6),
salesmanname varchar(20) not null,
ADDRESS1 varchar(30) not null,
ADDRESS2 varchar(30),
CITY varchar(20),
PINCODE integer(8),
STATE varchar(20),
salamt real(8,2) not null,
tgttoget decimal(6,2) not null,
ytdsales double(6,2) not null,
remarks varchar(60) not null,
primary key(salesmanno)
);
show tables;
insert into PRODUCT_MASTER(PRODUCTNO,DESCRIPTION,PROFITPERCENT,UNITMEASURE,QTYONHAND,REORDERLVL,SELLPRICE,COSTPRICE) values
('P00001','T-Shirt',5,'Piece',200,50,350,250),
('P0345', 'Shirts', 6, 'Piece', 150, 50, 500, 350),
('P06734', 'Cotton jeans',5 ,'Piece', 100, 20, 600, 450),
('P07865', 'Jeans', 5, 'Piece' ,100 ,20, 750, 500),
('P07868', 'Trousers', 2, 'Piece', 150, 50, 850, 550),
('P07885', 'Pull Overs' ,2.5 ,'Piece', 80, 30, 700, 450),
('P07965' ,'Denim jeans',4, 'Piece' ,100, 40, 350, 250),
('P07975', 'Lycra tops', 5, 'Piece' ,70, 30, 300, 175),
('P08865' ,'Skirts', 5, 'Piece' ,75, 30, 450, 300);


insert into CLINTE_MASTER(CLINTENO,NAME,ADDRESS1,ADDRESS2,CITY,PINCODE,STATE,BALDUE) values 
('C00001','Ivan Bayross','ufhgbwoirgbiejrgbwure','dhavkhrvjdvbakjv','Mumbai',400054,'Maharastra',15000),
('C00002','Mamta muzumdar','dhvajdfn vadfndjv','dsjvfhjsdvakhdsv','Madras',780001,'Tamil nadu',0),
('C00003','Chhaya bankar','JFGBWLJKJRWVLKER','EKFBRQEBQEROFER','Mumbai',400057,'Maharashtra',5000),
('C00004','Ashwini joshi','LRKGBLWJEKRVEL','EHFVKADHVJHERLV','Bangalore',560001,'Karnataka',0),
('C00005','Hansel colaco','LFJRGBLWITEGW','KHVFQEHUEVDW','Mumbai',400060,'Maharashtra',2000),
('C00006','Deepak sharma','KJREGBLWERJVBGIO','JEWHIVFEQHRV','Mangalore ',560050 ,'Karnataka',0);
insert into salesman_master(salesmanno,	salesmanname ,ADDRESS1,ADDRESS2 , CITY , PINCODE , STATE ,salamt , tgttoget,ytdsales ,remarks) values
("s00001"," Aman"," A/14"," Worli ","Mumbai" ,400002 ,"Maharashtra",3000 ,100, 50 ,"Good"),
("S00002"," Omkar","65"," Nariman"," Mumbai", 400001, "Maharashtra",3000 ,200 ,100,"Good"), 
("S00003" ,"Raj" ,"P-7" ,"Bandra ","Mumbai" ,400032 ,"Maharashtra" ,3000 ,200 ,100,"Good");

select * from CLINTE_MASTER;
select * from PRODUCT_MASTER;
select * from salesman_master;
select name from CLINTE_MASTER;
select name,city,state from CLINTE_MASTER ;
select description from PRODUCT_MASTER;
select name from CLINTE_MASTER where city='Mumbai';
select salesmanname from salesman_master where salamt=3000; 
update CLINTE_MASTER set CITY='Bengalore' where CLINTENO='C00005';
UPDATE CLINTE_MASTER set BALDUE=1000 where CLINTENO='C00001';
set sql_safe_updates=0;
update PRODUCT_MASTER set SELLPRICE=950 where DESCRIPTION='Trousers';
update salesman_master set CITY='Pune';
 DELETE  FROM salesman_master WHERE salamt=3500;
 DELETE FROM PRODUCT_MASTER WHERE QTYONHAND=100;
 DELETE FROM CLINTE_MASTER WHERE STATE='Tamil nadu';
ALTER TABLE salesman_master RENAME TO sman_mast;
select * from sman_mast;
ALTER TABLE sman_mast RENAME TO salesman_master;

ALTER TABLE CLINTE_MASTER ADD Telephone INT;
ALTER TABLE PRODUCT_MASTER MODIFY SELLPRICE DECIMAL(10,2);