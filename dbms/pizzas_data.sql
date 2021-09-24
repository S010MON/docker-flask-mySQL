-- Add pizzas
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Margherita", 5, 0); -- 1
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Tuna", 6, 50); -- 2
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Pepperoni", 7, 0); -- 3
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Vegetaria", 6, 0); -- 4
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Salami", 8, 50); -- 5
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Chicken", 7, 50); -- 6
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Hawaii", 5, 0); -- 7
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Dutch Herbs", 4, 20); -- 8
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Lover", 6, 90); -- 9
INSERT INTO Pizza (pizza_name, pizza_price_euros, pizza_price_cents) VALUES ("Calzone", 5, 0); -- 10

-- Add drinks
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Water", 2, 0);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Coke", 3, 0);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Fanta", 3, 0);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Sprite", 3, 0);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Red Bull", 4, 50);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Ice Tea", 3, 50);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Bitter Lemon", 3, 0);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Paulaner Weissbier", 5, 0);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Glenfinnan 12 Years Old", 25, 50);
INSERT INTO Drink (drink_name, drink_price_euros, drink_price_cents) VALUES ("Veuve Clicquot Ponsardin", 99, 90);

-- Add desserts
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Tiramisu", 5, 0);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Cheesecake", 6, 50);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Twin Cannoli", 5, 0);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Lorem Ipsum Cupcake", 6, 90);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Banana Waffle", 5, 50);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Nutella Banana", 6, 50);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Apple Crumble", 7, 0);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Ice Cream", 5, 0);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Rice Pudding", 4, 0);
INSERT INTO Dessert (dessert_name, dessert_price_euros, dessert_price_cents) VALUES ("Protein Shake Ice", 24, 7);

-- Add toppings
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Cheese", TRUE); -- 1
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Tuna", FALSE); -- 2
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Pineapple", TRUE); -- 3
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Bacon", FALSE); -- 4
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Tomato", TRUE); -- 5
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Purple Haze", True); -- 6
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Chicken", FALSE); -- 7
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Salami", FALSE); -- 8
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Blue Pills", TRUE); -- 9
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Mozzarella", TRUE); -- 10
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Basil", TRUE); -- 11
INSERT INTO Topping (topping_name, vegetarian) VALUES ("Pepperoni", TRUE); -- 12

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
