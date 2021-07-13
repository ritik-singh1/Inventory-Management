create database warehouse;
use warehouse;

---Table Creation

create table login_details(
	Name nvarchar(20),
	Email nvarchar(30),
	Password nvarchar(20),
	PhoneNo nvarchar(12) primary key
	)

create table shop_items(
	S_No int primary key,
	Items nvarchar(20),
	Qty int,
	Price int
	);

create table cart(
	S_No int primary key,
	Items nvarchar(20),
	Qty int,
	Price int,
	Total_Amount int
	)

create table payment(
	Name nvarchar(20),
	Phone_No nvarchar(20),
	Total_Amount int,
	Mode_of_Payment nvarchar(20),
	Payment_Status nvarchar(5)
	)

---Drop commands

drop table payment;

drop table login_details;

drop table cart;

drop table shop_items;

---Insert values in shop items

insert into shop_items values(1, 'Bread', 10, 20);
insert into shop_items values(2, 'Butter', 15, 10);
insert into shop_items values(3, 'Britania Cakes', 17, 10);
insert into shop_items values(4, 'Milk', 19, 60);
insert into shop_items values(5, 'Lays', 30, 20);
insert into shop_items values(6, 'Ice creams', 20, 25);
insert into shop_items values(7, 'Kurkure', 25, 20);
insert into shop_items values(8, 'Munch', 40, 10);
insert into shop_items values(9, 'Pepsi', 25, 35);
insert into shop_items values(10, 'Soap', 25, 15);
insert into shop_items values(11, 'Maggi', 30, 60);
insert into shop_items values(12, 'Muffins', 18, 20);
insert into shop_items values(13, 'Flour', 14, 100);

---Select Commands

select * from shop_items;

select * from cart;

select * from payment;

select * from login_details;

---truncate options

truncate table cart;

truncate table payment;

truncate table login_details;

truncate table shop_items;