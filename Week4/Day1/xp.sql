create table items (
	item_id int PRIMARY KEY,
	item_description VARCHAR(100) NOT NULL,
	item_price int NOT NULL
);
 
INSERT INTO items (item_id, item_description, item_price)
VALUES 
	(1, 'Small Desk', 100), 
	(2, 'Large Desk',300), 
	(3, 'Fan', 80)
;


create table customers (
	customer_id int primary key,
	customer_last_name varchar(20) not null,
	customer_first_name varchar(20) not null
);

insert into customers (customer_id,customer_first_name,customer_last_name)
values
	(1 , 'Greg' , 'Jones'),
    (2 , 'Sandra' , 'Jones'),
    (3 , 'Scott' , 'Scott'),
    (4 , 'Trevor' , 'Green'),
    (5 , 'Melanie' , 'Johnson');

select * from items;
select * from items where item_price < 80;
select * from items where item_price < 300;
select * from customers   where customer_last_name = 'Smith';
select * from customers   where customer_last_name = 'Jones';
select * from customers   where customer_first_name != 'Scott';