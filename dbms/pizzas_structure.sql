
-- Remove any residuals
DROP DATABASE IF EXISTS pizzas;

-- Create Database
CREATE DATABASE pizzas;
USE pizzas;

-- Create pizzza table
CREATE TABLE Pizza (
    pizza_id INT NOT NULL AUTO_INCREMENT,
    pizza_name VARCHAR(255) NOT NULL,
    pizza_price_euros INT NOT NULL,
    pizza_price_cents INT NOT NULL,
    PRIMARY KEY (pizza_id));

CREATE TABLE Drink (
    drink_id INT NOT NULL AUTO_INCREMENT,
    drink_name VARCHAR(255) NOT NULL,
    drink_price_euros INT NOT NULL,
    drink_price_cents INT NOT NULL,
    PRIMARY KEY (drink_id));

CREATE TABLE Dessert (
    dessert_id INT NOT NULL AUTO_INCREMENT,
    dessert_name VARCHAR(255) NOT NULL,
    dessert_price_euros INT NOT NULL,
    dessert_price_cents INT NOT NULL,
    PRIMARY KEY (dessert_id));

CREATE TABLE ToppingMapping (
    topping_map_id INT NOT NULL AUTO_INCREMENT,
    pizza_id INT NOT NULL,
    topping_id INT NOT NULL,
    PRIMARY KEY (topping_map_id));

CREATE TABLE PizzaMapping (
    pizza_map_id INT NOT NULL AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    pizza_id INT NOT NULL,
    PRIMARY KEY (pizza_map_id));

CREATE TABLE DrinkMapping (
    drink_map_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    purchase_id INT NOT NULL,
    PRIMARY KEY (drink_map_id));

CREATE TABLE DessertMapping (
    dessert_map_id INT NOT NULL AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    dessert_id INT NOT NULL,
    PRIMARY KEY (dessert_map_id));

CREATE TABLE Topping (
    topping_id INT NOT NULL AUTO_INCREMENT,
    topping_name VARCHAR(255) NOT NULL,
    vegetarian BOOL NOT NULL,
    PRIMARY KEY (topping_id));

CREATE TABLE Purchase (
    purchase_id INT NOT NULL AUTO_INCREMENT,
    purchased_at DATETIME NOT NULL,
    customer_id INT NOT NULL,
    delivery_driver_id INT,
    primary key (purchase_id));

CREATE TABLE Customer (
    customer_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    address_id INT NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    primary key (customer_id));

CREATE TABLE DeliveryDriver (
    driver_id INT NOT NULL AUTO_INCREMENT,
    operating_area VARCHAR(6) NOT NULL,
    on_task BOOL NOT NULL,
    name VARCHAR(255) NOT NULL,
    primary key (driver_id));

CREATE TABLE Address (
    address_id INT NOT NULL AUTO_INCREMENT,
    street VARCHAR(255) NOT NULL,
    town VARCHAR(255) NOT NULL,
    postcode VARCHAR(6) NOT NULL,
    primary key (address_id));


