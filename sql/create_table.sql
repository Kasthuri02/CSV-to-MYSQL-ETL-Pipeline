CREATE DATABASE etl_project;
USE etl_project;

CREATE TABLE orders (
    order_id INT primary key,
    customer_id VARCHAR(20) ,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    order_date DATE,
    city VARCHAR(100),
    total_amount DECIMAL(10,2)
);