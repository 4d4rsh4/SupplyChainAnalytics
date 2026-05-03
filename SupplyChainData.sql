--create database SupplyChain
--use SupplyChain

create table customer(
	customer_id int PRIMARY KEY,
	customer_fname varchar(255),
	customer_lname varchar(255),
	customer_city varchar(255),
	customer_country varchar(255),
	customer_street varchar(255));
	
create table category(
	category_id int PRIMARY KEY,
	category_name varchar(255));

create table item(
	product_id int PRIMARY KEY,
	product_category_id int FOREIGN KEY REFERENCES category(category_id),
	product_name varchar(255),
	product_price DECIMAL(10,2));

create table customer_order(
	order_id int PRIMARY KEY,
	order_customer_id int FOREIGN KEY REFERENCES customer(customer_id),
	order_datetime datetime,
	order_region varchar(255),
	order_status varchar(255),
	pay_type varchar(255));

create table order_item(
	order_item_id int PRIMARY KEY,
	order_item_order_id int FOREIGN KEY REFERENCES customer_order(order_id),
	order_product_id int FOREIGN KEY REFERENCES item(product_id),
	order_item_product_price DECIMAL(10,2),
	order_item_qty int,
	order_item_discount DECIMAL(10,2),
	order_item_total DECIMAL(10,2));

create table delivery_detail(
	delivery_id int IDENTITY(1,1) PRIMARY KEY,
	delivery_order_id int FOREIGN KEY REFERENCES customer_order(order_id),
	real_shipping_days int,
	scheduled_shipping_days int,
	delivery_status varchar(255),
	late_delivery_risk int,
	shipping_date datetime,
	shipping_mode varchar(255));
