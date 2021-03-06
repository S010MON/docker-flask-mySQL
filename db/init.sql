CREATE DATABASE pizzas;
USE pizzas;

CREATE TABLE Pizza (
    pizza_id INT NOT NULL AUTO_INCREMENT,
    pizza_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (pizza_id));

CREATE TABLE Drink (
    drink_id INT NOT NULL AUTO_INCREMENT,
    drink_name VARCHAR(255) NOT NULL,
    drink_price DOUBLE NOT NULL,
    PRIMARY KEY (drink_id));

CREATE TABLE Dessert (
    dessert_id INT NOT NULL AUTO_INCREMENT,
    dessert_name VARCHAR(255) NOT NULL,
    dessert_price DOUBLE NOT NULL,
    PRIMARY KEY (dessert_id));

CREATE TABLE Topping (
    topping_id INT NOT NULL AUTO_INCREMENT,
    topping_name VARCHAR(255) NOT NULL,
    vegetarian BOOL NOT NULL,
    topping_price DOUBLE NOT NULL,
    PRIMARY KEY (topping_id));

CREATE TABLE Address (
    address_id INT NOT NULL AUTO_INCREMENT,
    street VARCHAR(255) NOT NULL,
    town VARCHAR(255) NOT NULL,
    postcode VARCHAR(6) NOT NULL,
    primary key (address_id));

CREATE TABLE Customer (
    customer_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    address_id INT NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    primary key (customer_id),
    CONSTRAINT FK_address_id_c FOREIGN KEY (address_id) REFERENCES Address(address_id));

CREATE TABLE DeliveryDriver (
    driver_id INT NOT NULL AUTO_INCREMENT,
    operating_area VARCHAR(6) NOT NULL,
    on_task BOOL NOT NULL,
    name VARCHAR(255) NOT NULL,
    primary key (driver_id));

CREATE TABLE Purchase (
    purchase_id INT NOT NULL AUTO_INCREMENT,
    purchased_at DATETIME NOT NULL,
    customer_id INT NOT NULL,
    delivery_driver_id INT,
    status VARCHAR(255) NOT NULL, # accepted, dispatched, delivered
    PRIMARY KEY (purchase_id),
    CONSTRAINT FK_customer_id_pu FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    CONSTRAINT FK_delivery_driver_id_pu FOREIGN KEY (delivery_driver_id) REFERENCES DeliveryDriver(driver_id));

CREATE TABLE ToppingMapping (
    topping_map_id INT NOT NULL AUTO_INCREMENT,
    pizza_id INT NOT NULL,
    topping_id INT NOT NULL,
    PRIMARY KEY (topping_map_id),
    CONSTRAINT FK_pizza_id_to FOREIGN KEY (pizza_id) REFERENCES Pizza(pizza_id),
    CONSTRAINT FK_topping_id_to FOREIGN KEY (topping_id) REFERENCES Topping(topping_id));

CREATE TABLE PizzaMapping (
    pizza_map_id INT NOT NULL AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    pizza_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (pizza_map_id),
    CONSTRAINT FK_purchase_id_pi FOREIGN KEY (purchase_id) REFERENCES Purchase(purchase_id),
    CONSTRAINT FK_pizza_id_pi FOREIGN KEY (pizza_id) REFERENCES Pizza(pizza_id));

CREATE TABLE DrinkMapping (
    drink_map_id INT NOT NULL AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    drink_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (drink_map_id),
    CONSTRAINT FK_purchase_id_dr FOREIGN KEY (purchase_id) REFERENCES Purchase(purchase_id),
    CONSTRAINT FK_drink_id_dr FOREIGN KEY (drink_id) REFERENCES Drink(drink_id));

CREATE TABLE DessertMapping (
    dessert_map_id INT NOT NULL AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    dessert_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (dessert_map_id),
    CONSTRAINT FK_purchase_id_de FOREIGN KEY (purchase_id) REFERENCES Purchase(purchase_id),
    CONSTRAINT FK_dessert_id_de FOREIGN KEY (dessert_id) REFERENCES Dessert(dessert_id));

CREATE TABLE Discount (
    discount_id INT NOT NULL AUTO_INCREMENT,
    code VARCHAR(7) NOT NULL,
    used BOOL NOT NULL, PRIMARY KEY (discount_id));

-- Add pizzas
INSERT INTO Pizza (pizza_name) VALUES ("Margherita"); -- 1
INSERT INTO Pizza (pizza_name) VALUES ("Tuna"); -- 2
INSERT INTO Pizza (pizza_name) VALUES ("Pepperoni"); -- 3
INSERT INTO Pizza (pizza_name) VALUES ("Vegetaria"); -- 4
INSERT INTO Pizza (pizza_name) VALUES ("Salami"); -- 5
INSERT INTO Pizza (pizza_name) VALUES ("Chicken"); -- 6
INSERT INTO Pizza (pizza_name) VALUES ("Hawaii"); -- 7
INSERT INTO Pizza (pizza_name) VALUES ("Dutch Herbs"); -- 8
INSERT INTO Pizza (pizza_name) VALUES ("Lover"); -- 9
INSERT INTO Pizza (pizza_name) VALUES ("Calzone"); -- 10

-- Add drinks
INSERT INTO Drink (drink_name, drink_price) VALUES ("Water", 2.0);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Coke", 3.0);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Fanta", 3.0);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Sprite", 3.0);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Red Bull", 4.5);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Ice Tea", 3.5);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Bitter Lemon", 3.0);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Paulaner Weissbier", 5.0);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Glenfinnan 12 Years Old", 25.50);
INSERT INTO Drink (drink_name, drink_price) VALUES ("Veuve Clicquot Ponsardin", 99.90);


-- Add desserts
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Tiramisu", 5.0);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Cheesecake", 6.50);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Twin Cannoli", 5.0);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Lorem Ipsum Cupcake", 6.90);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Banana Waffle", 5.50);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Nutella Banana", 6.50);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Apple Crumble", 7.0);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Ice Cream", 5.0);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Rice Pudding", 4.0);
INSERT INTO Dessert (dessert_name, dessert_price) VALUES ("Protein Shake Ice", 24.7);

-- Add toppings
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Cheese", TRUE, 2.5); -- 1
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Tuna", FALSE, 3.0); -- 2
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Pineapple", TRUE, 2.5); -- 3
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Bacon", FALSE, 4.0); -- 4
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Tomato", TRUE, 2.2); -- 5
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Purple Haze", True, 4.2); -- 6
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Chicken", FALSE, 3.5); -- 7
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Salami", FALSE, 4.1); -- 8
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Blue Pills", TRUE, 6.9); -- 9
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Mozzarella", TRUE, 3.5); -- 10
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Basil", TRUE, 1.5); -- 11
INSERT INTO Topping (topping_name, vegetarian, topping_price) VALUES ("Pepperoni", FALSE, 4.5); -- 12

-- Map toppings to pizza
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (1, 1); -- Margherita, Cheese
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (2, 2); -- Tuna, Tuna
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (2, 1); -- Tuna, Cheese
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (3, 12); -- Pepperoni, Pepperoni
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (4, 5); -- Vegetaria, Tomato
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (4, 11); -- Vegetaria, Basil
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (5, 8); -- Salami, Salami
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (6, 7); -- Chicken, Chicken
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (6, 1); -- Chicken, Cheese
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (7, 3); -- Hawaii, Pineapple
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (7, 4); -- Hawaii, Bacon
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (8, 6); -- Dutch Herbs, Purple Haze
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (8, 1); -- Dutch Herbs, Cheese
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (9, 9); -- Lover, Blue Pills
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (10, 1); -- Calzone, Cheese
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (10, 5); -- Calzone, Tomato
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (10, 11); -- Calzone, Basil
INSERT INTO ToppingMapping(pizza_id, topping_id) VALUES (10, 4); -- Calzone, Bacon

-- Add delivery drivers
INSERT INTO DeliveryDriver(operating_area, on_task, name) VALUES ("1234AA", FALSE, "Christof");
INSERT INTO DeliveryDriver(operating_area, on_task, name) VALUES ("1234AA", FALSE, "Peter");
INSERT INTO DeliveryDriver(operating_area, on_task, name) VALUES ("1234AA", FALSE, "Tom");
INSERT INTO DeliveryDriver(operating_area, on_task, name) VALUES ("1234AA", FALSE, "Pietro");
INSERT INTO DeliveryDriver(operating_area, on_task, name) VALUES ("1234AA", FALSE, "Enrique");
