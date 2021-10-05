import copy

from entities.Purchase import Purchase
from entities.Address import Address
from entities.DeliveryDriver import DeliveryDriver
from entities.Pizza import Pizza
from entities.Dessert import Dessert
from entities.Drink import Drink
from entities.Customer import Customer
from mysql.connector import (connection)

import mysql.connector

# Docker config
config = {'user': 'root',
          'password': 'password',
          'host': 'db',
          'port': '3306',
          'database': 'pizzas'
          }

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

# ----------------------------------------------------------------------------------------------------------------------

def get_all_pizzas():
    query = ("SELECT Pizza.pizza_id, "
             "Pizza.pizza_name, "
             "Topping.topping_name,"
             "Topping.vegetarian FROM Pizza "
             "INNER JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
             "INNER JOIN Topping ON ToppingMapping.topping_id = Topping.topping_id;")
    cursor.execute(query)
    # The following algorithm makes sure, that all the toppings from a many-to-many relation
    # are geting mapped to the corresponding pizza
    allPizzas = []
    for (pizza_id, pizza_name, topping_name, vegetarian) in cursor:
        already_exists = False
        for check_pizza in allPizzas:
            if check_pizza.pizza_id == pizza_id:
                pointer = check_pizza
                already_exists = True
        if already_exists:
            pointer.toppings.append(topping_name)
            if not vegetarian:
                pointer.vegetarian = False
        else:
            allPizzas.append(
                Pizza(pizza_id, pizza_name, [topping_name], bool(vegetarian)))  # add toppings
    # Add prices
    assign_pizza_prices(allPizzas)
    return allPizzas


def get_pizza(current_pizza_id):
    query = ("SELECT Pizza.pizza_id, "
             "Pizza.pizza_name, "
             "Pizza.pizza_price_euros, "
             "Pizza.pizza_price_cents, "
             "Topping.topping_name FROM Pizza "
             "INNER JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
             "INNER JOIN Topping ON ToppingMapping.topping_id = Topping.topping_id"
             "WHERE Pizza.pizza_id = 2;")
    cursor.execute(query, (current_pizza_id,))
    # The following algorithm makes sure, that all the toppings from a many-to-many relation
    # are geting mapped to the corresponding pizza
    result_pizza = None
    for (pizza_id, pizza_name, pizza_price_euros, pizza_price_cents, topping_name) in cursor:
        already_exists = False
        for check_pizza in result_pizza:
            if check_pizza.pizza_id == pizza_id:
                pointer = check_pizza
                already_exists = True
        if already_exists:
            pointer.toppings.append(topping_name)
        else:
            result_pizza = Pizza(pizza_id, pizza_name, pizza_price_euros, [topping_name])  # add toppings

    allPizzas = [result_pizza]
    assign_pizza_prices(allPizzas)
    return result_pizza


def assign_pizza_prices(allPizzas):
    for current_pizza in allPizzas:
        query = ("SELECT SUM(topping_price) AS topping_price_sum FROM Pizza "
                 "JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
                 "JOIN Topping ON ToppingMapping.topping_id = Topping.topping_id "
                 "WHERE Pizza.pizza_id = %s;")
        cursor.execute(query, (current_pizza.pizza_id,))
        topping_cost_sum = cursor.fetchone()[0]
        current_pizza.cost = topping_cost_sum * 1.4

# ----------------------------------------------------------------------------------------------------------------------

def get_all_desserts():
    query = (
        "SELECT dessert_id, dessert_name, dessert_price FROM Dessert;")
    cursor.execute(query)
    allDeserts = []
    for (dessert_id, dessert_name, dessert_price) in cursor:
        allDeserts.append(Dessert(dessert_id, dessert_name, dessert_price))  # add toppings
    return allDeserts


# ----------------------------------------------------------------------------------------------------------------------

def get_all_drinks():
    query = (
        "SELECT drink_id, drink_name, drink_price FROM Drink;")  # need to add join for toppings
    cursor.execute(query)
    allDrinks = []
    for (drink_id, drink_name, drink_price) in cursor:
        allDrinks.append(Drink(drink_id, drink_name, drink_price))  # add toppings
    return allDrinks


# ----------------------------------------------------------------------------------------------------------------------

'''
Requires: customer.name, customer.address, customer.phone
'''
def create_customer(customer):
    query = ("INSERT INTO Customer (name, address_id, phone_number)"
             "VALUES (%s, %s, %s);")

    query_data = (customer.name, customer.address.address_id, customer.phone)
    cursor.execute(query, query_data)
    current_id = cursor.lastrowid
    new_customer = copy.deepcopy(customer)
    new_customer.customer_id = current_id
    cnx.commit()
    return new_customer


def get_customer(id):
    query = ("SELECT customer_id, name, address_id, phone_number FROM Customer WHERE customer_id = %s")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    customer_address = get_address(result[2])
    if customer_address is None:
        return None
    else:
        return Customer(result[1], customer_address, result[3], result[0])

def customer_exists(customer) -> bool():
    query = ("SELECT customer_id, name, address_id FROM Customer WHERE name = %s AND phone_number = %s;")
    cursor.execute(query, (customer.name, customer.phone))
    row_number = cursor.fetchall()
    results = len(row_number)
    if results > 0:
        return True
    else:
        return False

def add_to_customer_pizzas_total(no_of_pizzas) -> None:
    """ Adds the number of pizzas to the customer's total number"""
    pass

def get_customer_pizzas_total(customer_id) -> int:
    """ Gets the number of pizzas to the customer's total number"""
    return 10

def remove_from_customer_pizzas_total(no_of_pizzas) -> None:
    """ Removes the number of pizzas from the customer's total"""
    pass

# ----------------------------------------------------------------------------------------------------------------------

def create_purchase(purchase):
    return None
    # check for valid customer id
    query = ("SELECT customer_id FROM Customer WHERE customer_id = %s;")
    cursor.execute(query, (purchase.customer_id,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        # insert customer
        query = ("INSERT INTO Purchase (purchased_at, customer_id) VALUES (NOW(), %s);")
        cursor.execute(query, (purchase.customer_id,))
        purchase_id = cursor.lastrowid
        new_purchase = copy.deepcopy(purchase)
        query = ("SELECT purchased_at FROM Purchase WHERE purchase_id = %s")
        cursor.execute(query, (purchase_id,))
        result = cursor.fetchone()
        new_purchase.datetime = result[0]
        new_purchase.purchase_id = purchase_id

        for current_pizza in purchase.pizzas:
            query = ("INSERT INTO PizzaMapping (purchase_id, pizza_id, quantity) VALUES (%s, %s, %s);")
            cursor.execute(query, (purchase_id, current_pizza['pizza_id'], current_pizza['quantity']))

        for current_drink in purchase.drinks:
            query = ("INSERT INTO DrinkMapping (purchase_id, drink_id, quantity) VALUES (%s, %s, %s);")
            cursor.execute(query, (purchase_id, current_drink['drink_id'], current_drink['quantity']))

        for current_dessert in purchase.desserts:
            query = ("INSERT INTO DessertMapping (purchase_id, dessert_id, quantity) VALUES (%s, %s, %s);")
            cursor.execute(query, (purchase_id, current_dessert['dessert_id'], current_dessert['quantity']))

        cnx.commit()
        return new_purchase


def get_purchase(purchase_id):
    query = ("SELECT purchase_id, purchased_at, customer_id, delivery_driver_id FROM Purchase WHERE purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    result = cursor.fetchone()
    new_purchase = Purchase(result[2], [], [], [])
    new_purchase.datetime = result[1]
    new_purchase.purchase_id = purchase_id
    new_purchase.delivery_driver_id = result[3]
    # Query pizzas
    query = ("SELECT PizzaMapping.pizza_id, PizzaMapping.quantity FROM Purchase "
             "JOIN PizzaMapping ON Purchase.purchase_id = PizzaMapping.purchase_id WHERE Purchase.purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    for (pizza_id, quantity) in cursor:
        new_purchase.pizzas.append({"pizza_id": pizza_id,
                                    "quantity": quantity})
    # Query drinks
    query = ("SELECT DrinkMapping.drink_id, DrinkMapping.quantity FROM Purchase "
             "JOIN DrinkMapping ON Purchase.purchase_id = DrinkMapping.purchase_id WHERE Purchase.purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    for (drink_id, quantity) in cursor:
        new_purchase.drinks.append({"drink_id": drink_id,
                                    "quantity": quantity})

    #Query desserts
    query = ("SELECT DessertMapping.dessert_id, DessertMapping.quantity FROM Purchase "
             "JOIN DessertMapping ON Purchase.purchase_id = DessertMapping.purchase_id WHERE Purchase.purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    for (dessert_id, quantity) in cursor:
        new_purchase.desserts.append({"dessert_id": dessert_id,
                                    "quantity": quantity})

    return new_purchase

def delete_purchase(purchase_id):
    deleted_order = get_purchase(purchase_id)
    query = ("DELETE FROM Purchase WHERE purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    cnx.commit()
    return deleted_order

"""Return True if the purchase exists AND has not been closed yet, else return False"""
def purchase_exists(purchase_id) -> bool():
    query = ("SELECT purchase_id FROM Purchase WHERE purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True
    return True


""" Return a list of purchases that have not been delivered, return None if none exist"""
def get_undelivered_purchases():
    query = ("SELECT purchase_id FROM Purchase WHERE purchased_at > DATE_SUB(NOW(), INTERVAL '35' MINUTES);")
    cursor.execute(query)
    undelivered_purchases = []
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        for (purchase_id,) in result:
            undelivered_purchases.append(get_purchase(purchase_id))
    return undelivered_purchases


""" Sets the purchase of """
def update_purchase_status(purchase_id, dispatched_time):
    query = ("UPDATE Purchase SET purchased_at = %s WHERE purchase_id = %s;")
    cursor.execute(query, (dispatched_time, purchase_id))


""" For purchase with the id `purchase_id` set driver to id `driver_id` """
def set_delivery_driver(purchase_id, driver_id):
    query = ("UPDATE Purchase SET delivery_driver_id = %s WHERE purchase_id = %s")
    cursor.execute(query, (driver_id, purchase_id))


# ----------------------------------------------------------------------------------------------------------------------

def get_delivery_drivers(area):
    delivery_drivers = []
    query = ("SELECT driver_id, operating_area, on_task, name FROM DeliveryDriver WHERE operating_area = %s;")
    cursor.execute(query, (area,))
    for (driver_id, operating_area, on_task, name) in cursor:
        delivery_drivers.append(DeliveryDriver(driver_id, operating_area, on_task, name))
    return delivery_drivers


def get_delivery_driver(id):
    query = ("SELECT driver_id, operating_area, on_task, name FROM DeliveryDriver WHERE driver_id = %s;")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return DeliveryDriver(result[0], result[1], result[2], result[3])


def update_delivery_driver(delivery_driver, status):
    query = ("UPDATE DeliveryDriver SET on_task = %s WHERE driver_id = %s")
    cursor.execute(query, (status, delivery_driver.driver_id))
    new_delivery_driver = DeliveryDriver(delivery_driver.driver_id, delivery_driver.operating_area, status, delivery_driver.name)
    cnx.commit()
    return new_delivery_driver


""" Return a list of all available drivers for postcode `postcode` """
def get_available_drivers(postcode):
    all_available_drivers = []
    query = ("SELECT driver_id, operating_area, on_task, name FROM DeliveryDriver "
             "WHERE operating_area = %s AND on_task = FALSE;")
    cursor.execute(query, (postcode,))
    result = cursor.fetchall()
    if result is None:
        return all_available_drivers
    else:
        for (driver_id, operating_area, on_task, name) in result:
            all_available_drivers.append(DeliveryDriver(driver_id, operating_area, on_task, name))
        return all_available_drivers


# ----------------------------------------------------------------------------------------------------------------------

def create_address(address):
    query = ("INSERT INTO Address (street, town, postcode)"
             "VALUES (%s, %s, %s);")

    query_data = (address.street, address.town, address.postcode)
    cursor.execute(query, query_data)
    current_id = cursor.lastrowid
    new_address = copy.deepcopy(address)
    new_address.address_id = current_id
    cnx.commit()
    return new_address


def get_address(id):
    query = ("SELECT address_id, street, town, postcode FROM Address WHERE address_id = %s;")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        return Address(result[1], result[2], result[3], result[0])

# ----------------------------------------------------------------------------------------------------------------------

def generate_discount_code() -> str:
    """ Create a new discount code and set it's boolean flag to `Valid=True` """
    return "CODE123"

def valid_discount_code(code) -> bool:
    """ Check if the code has been used, return True if it is valid """
    if code == "CODE123":
        return True
    else:
        return False

def set_discount_code_invalid(code):
    """ Set the code to invalid"""
# ----------------------------------------------------------------------------------------------------------------------

# Main function to test query methods
if __name__ == '__main__':
    for pizza in get_all_pizzas():
        print(pizza.pizza_id, pizza.name, pizza.cost, pizza.toppings, pizza.vegetarian)

    print("---")

    for drink in get_all_drinks():
        print(drink.drink_id, drink.name, drink.cost)

    print("---")

    for dessert in get_all_desserts():
        print(dessert.dessert_id, dessert.name, dessert.cost)

    print("---")

    # create example entities
    test_driver = get_delivery_driver(1)
    print(test_driver.name, test_driver.operating_area)

    print("---")

    test_address = Address("Dampstraat", "Maastricht", "6226GJ")
    test_address = create_address(test_address)
    print(test_address.address_id, test_address.town)

    test_customer = Customer("Leon", test_address, "+49 123456789")
    test_customer = create_customer(test_customer)
    print(test_customer.customer_id, test_customer.name, test_customer.address.town)

    print("---")

    #sample_pizza = get_pizza(3)
    #print(sample_pizza.name, sample_pizza.toppings)

    tp = Purchase(1, [], [], [])
    new_test_driver = update_delivery_driver(test_driver, True)
    # test_purchase = Purchase()
