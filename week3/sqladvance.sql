create table users(id serial primary key,name varchar(100),phone varchar(15));
create table user_detaile(id serial primary key,address varchar(200),user_id int references users(id));
insert into users(name,phone) values('Surendra',6303023283),('Afzal',7788990066),('Suri',8899007766),('Pavan',9900887766),('Sai',6677889900),('Kiran',9988007766);
insert into user_detaile(address,user_id)values('Nandyal',1),('Nellore',2),('Nandyal',3),('Hyderabad',4),('Proddatur',5),('Chennai',6);
select * from users;
select * from user_detaile;
select users.name,user_detaile.address from users,user_detaile where user_detaile.user_id=users.id;
insert into users(name ,phone)values
('vishnu',6300998877),
('Hemanth',8899770055),
('Yogi',7766558899),
('Raja vardhan',9955667788),
('Arun',8855667799);
insert into user_detaile(address,user_id)values
('Proddatur',6),
('Nandyal',7),
('Anantapur',8),
('Allagda',9),
('Anantapur',10);
select * from users;
select * from user_detaile;
select users.name,user_detaile.address from users,user_detaile where user_detaile.user_id=users.id and address in ('Nandyal','Proddatur','Anantapur','Allagda') ;
select count(distinct phone) from users;
select users.name,user_detaile.address from users,user_detaile where user_detaile.user_id=users.id order by users.name ASC;
select * from users Limit 6;
select users.phone,user_detaile.address from users Inner join user_detaile on user_detaile.user_id=users.id;
select users.name,user_detaile.address from users left join user_detaile on user_detaile.user_id=users.id;
select users.name,user_detaile.address from users right join user_detaile on user_detaile.user_id=users.id;
select * from users full join user_detaile on user_detaile.user_id=users.id;
alter table users add column amount int;
update users set amount=10000 where id=1;
update users set amount =9500 where id=2;
update users set amount=8000 where id=3;
update users set amount=9900 where  id=4;
update users set amount=8200 where id=5;
update users set amount =7000 where id=6;
update users set amount =6500 where id=7;
update users set amount =8900 where id=8;
update users set amount =9200 where id=9;
update users set amount=7500 where id=10;
update users set amount =8600 where id=11;
select * from users;
select max(amount) from users;
select min(amount) from users;
select sum(amount) from users;
