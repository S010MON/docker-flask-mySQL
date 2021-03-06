import copy
import random
import string

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
    all_pizzas = []
    for (pizza_id, pizza_name, topping_name, vegetarian) in cursor:
        already_exists = False
        for check_pizza in all_pizzas:
            if check_pizza.pizza_id == pizza_id:
                pointer = check_pizza
                already_exists = True
        if already_exists:
            pointer.toppings.append(topping_name)
            if not vegetarian:
                pointer.vegetarian = False
        else:
            all_pizzas.append(
                Pizza(pizza_id, pizza_name, [topping_name], bool(vegetarian)))  # add toppings
    # Add prices
    assign_pizza_prices(all_pizzas)
    return all_pizzas


def get_pizza(current_pizza_id):
    query = ("SELECT Pizza.pizza_id, Pizza.pizza_name, Topping.topping_name, Topping.vegetarian FROM Pizza "
             "INNER JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
             "INNER JOIN Topping ON ToppingMapping.topping_id = Topping.topping_id "
             "WHERE Pizza.pizza_id = %s;")
    cursor.execute(query, (current_pizza_id,))
    # The following algorithm makes sure, that all the toppings from a many-to-many relation
    # are getting mapped to the corresponding pizza
    first_entry = cursor.fetchone()
    vegetarian = first_entry[3]
    result_pizza = Pizza(first_entry[0], first_entry[1], [first_entry[2]], vegetarian)
    rest_entries = cursor.fetchall()
    for entry in rest_entries:
        result_pizza.toppings.append(entry[2])
        if not entry[3]:
            result_pizza.vegetarian = False
    all_pizzas = [result_pizza]
    assign_pizza_prices(all_pizzas)
    return result_pizza


def assign_pizza_prices(all_pizzas):
    for current_pizza in all_pizzas:
        query = ("SELECT SUM(topping_price) AS topping_price_sum FROM Pizza "
                 "JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
                 "JOIN Topping ON ToppingMapping.topping_id = Topping.topping_id "
                 "WHERE Pizza.pizza_id = %s;")
        cursor.execute(query, (current_pizza.pizza_id,))
        topping_cost_sum = cursor.fetchone()[0]
        current_pizza.cost = topping_cost_sum * 1.4 * 1.09


# ----------------------------------------------------------------------------------------------------------------------


def get_all_desserts():
    query = "SELECT dessert_id, dessert_name, dessert_price FROM Dessert;"
    cursor.execute(query)
    all_deserts = []
    for (dessert_id, dessert_name, dessert_price) in cursor:
        all_deserts.append(Dessert(dessert_id, dessert_name, dessert_price))
    return all_deserts


def get_dessert(current_dessert_id):
    query = "SELECT dessert_id, dessert_name, dessert_price FROM Dessert WHERE dessert_id = %s;"
    cursor.execute(query, (current_dessert_id,))
    result = cursor.fetchone()
    return Dessert(result[0], result[1], result[2])


# ----------------------------------------------------------------------------------------------------------------------


def get_all_drinks():
    query = "SELECT drink_id, drink_name, drink_price FROM Drink;"
    cursor.execute(query)
    all_drinks = []
    for (drink_id, drink_name, drink_price) in cursor:
        all_drinks.append(Drink(drink_id, drink_name, drink_price))
    return all_drinks


def get_drink(current_drink_id):
    query = "SELECT drink_id, drink_name, drink_price FROM Drink WHERE drink_id = %s;"
    cursor.execute(query, (current_drink_id,))
    result = cursor.fetchone()
    return Drink(result[0], result[1], result[2])


# ----------------------------------------------------------------------------------------------------------------------


def create_customer(customer):
    """
    Requires: customer.name, customer.address, customer.phone
    """
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
    query = "SELECT customer_id, name, address_id, phone_number FROM Customer WHERE customer_id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result is None:
        return None
    customer_address = get_address(result[2])
    if customer_address is None:
        return None
    else:
        return Customer(result[1], customer_address, result[3], result[0])


def customer_exists(customer) -> bool():
    query = "SELECT customer_id, name, address_id FROM Customer WHERE name = %s AND phone_number = %s;"
    cursor.execute(query, (customer.name, customer.phone))
    row_number = cursor.fetchall()
    results = len(row_number)
    if results > 0:
        return True
    else:
        return False


def customer_exists_by_id(customer_id) -> bool():
    query = "SELECT customer_id, name, address_id FROM Customer WHERE name = %s;"
    cursor.execute(query, customer_id)
    row_number = cursor.fetchall()
    results = len(row_number)
    if results > 0:
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------


def create_purchase(purchase):
    # check for valid customer id
    query = "SELECT customer_id FROM Customer WHERE customer_id = %s;"
    cursor.execute(query, (purchase.customer_id,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        # insert customer
        query = "INSERT INTO Purchase (purchased_at, customer_id, status) VALUES (NOW(), %s, 'accepted');"
        cursor.execute(query, (purchase.customer_id,))
        purchase_id = cursor.lastrowid
        new_purchase = copy.deepcopy(purchase)
        query = "SELECT purchased_at FROM Purchase WHERE purchase_id = %s"
        cursor.execute(query, (purchase_id,))
        result = cursor.fetchone()
        new_purchase.datetime = result[0]
        new_purchase.purchase_id = purchase_id
        new_purchase.status = "accepted"

        for current_pizza in purchase.pizzas:
            query = "INSERT INTO PizzaMapping (purchase_id, pizza_id, quantity) VALUES (%s, %s, %s);"
            cursor.execute(query, (purchase_id, current_pizza['pizza_id'], current_pizza['quantity']))

        for current_drink in purchase.drinks:
            query = "INSERT INTO DrinkMapping (purchase_id, drink_id, quantity) VALUES (%s, %s, %s);"
            cursor.execute(query, (purchase_id, current_drink['drink_id'], current_drink['quantity']))

        for current_dessert in purchase.desserts:
            query = "INSERT INTO DessertMapping (purchase_id, dessert_id, quantity) VALUES (%s, %s, %s);"
            cursor.execute(query, (purchase_id, current_dessert['dessert_id'], current_dessert['quantity']))

        cnx.commit()
        return new_purchase


def get_purchase(purchase_id):
    if type(purchase_id) is not int:
        return None
    query = ("SELECT purchase_id, purchased_at, customer_id," +
             "delivery_driver_id, status FROM Purchase WHERE purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    result = cursor.fetchone()
    new_purchase = Purchase(result[2], [], [], [])
    new_purchase.datetime = result[1]
    new_purchase.purchase_id = purchase_id
    new_purchase.delivery_driver_id = result[3]
    new_purchase.status = result[4]
    # Query pizzas
    query = ("SELECT PizzaMapping.pizza_id, PizzaMapping.quantity, Pizza.pizza_name FROM Purchase "
             "JOIN PizzaMapping ON Purchase.purchase_id = PizzaMapping.purchase_id "
             "JOIN Pizza ON PizzaMapping.pizza_id = Pizza.pizza_id WHERE Purchase.purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    for (pizza_id, quantity, pizza_name) in cursor:
        new_purchase.pizzas.append({"pizza_id": pizza_id,
                                    "name": pizza_name,
                                    "quantity": quantity})
    # Query drinks
    query = ("SELECT DrinkMapping.drink_id, DrinkMapping.quantity, Drink.drink_name FROM Purchase "
             "JOIN DrinkMapping ON Purchase.purchase_id = DrinkMapping.purchase_id "
             "JOIN Drink ON DrinkMapping.drink_id = Drink.drink_id WHERE Purchase.purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    for (drink_id, quantity, drink_name) in cursor:
        new_purchase.drinks.append({"drink_id": drink_id,
                                    "name": drink_name,
                                    "quantity": quantity})
    # Query desserts
    query = ("SELECT DessertMapping.dessert_id, DessertMapping.quantity, Dessert.dessert_name FROM Purchase "
             "JOIN DessertMapping ON Purchase.purchase_id = DessertMapping.purchase_id "
             "JOIN Dessert ON DessertMapping.dessert_id = Dessert.dessert_id WHERE Purchase.purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    for (dessert_id, quantity, dessert_name) in cursor:
        new_purchase.desserts.append({"dessert_id": dessert_id,
                                      "name": dessert_name,
                                      "quantity": quantity})
    return new_purchase


def delete_purchase(purchase_id):
    deleted_order = get_purchase(purchase_id)
    query = "DELETE FROM Purchase WHERE purchase_id = %s;"
    cursor.execute(query, (purchase_id,))
    cnx.commit()
    return deleted_order


def purchase_exists(purchase_id) -> bool():
    """ Return True if the purchase exists AND has not been closed yet, else return False """
    query = "SELECT purchase_id FROM Purchase WHERE purchase_id = %s;"
    cursor.execute(query, (purchase_id,))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True
    return True


def get_undelivered_purchases():
    """ Return a list of purchases that have not been delivered, return None if none exist """
    query = "SELECT purchase_id FROM Purchase;"
    cursor.execute(query)
    undelivered_purchases = []
    result = cursor.fetchall()
    if result is None:
        return None
    else:
        for (purchase_id,) in result:
            undelivered_purchases.append(get_purchase(purchase_id))
    return undelivered_purchases


def update_purchase_status(purchase_id, dispatched_time):
    """ Sets the purchase of """
    query = "UPDATE Purchase SET purchased_at = %s WHERE purchase_id = %s;"
    cursor.execute(query, (dispatched_time, purchase_id))


def set_delivery_driver(purchase_id, driver_id):
    """ For purchase with the id `purchase_id` set driver to id `driver_id` """
    query = "UPDATE Purchase SET delivery_driver_id = %s WHERE purchase_id = %s"
    cursor.execute(query, (driver_id, purchase_id))


# ----------------------------------------------------------------------------------------------------------------------


def get_delivery_drivers(area):
    delivery_drivers = []
    query = "SELECT driver_id, operating_area, on_task, name FROM DeliveryDriver WHERE operating_area = %s;"
    cursor.execute(query, (area,))
    for (driver_id, operating_area, on_task, name) in cursor:
        delivery_drivers.append(DeliveryDriver(driver_id, operating_area, on_task, name))
    return delivery_drivers


def get_delivery_driver(id):
    query = "SELECT driver_id, operating_area, on_task, name FROM DeliveryDriver WHERE driver_id = %s;"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return DeliveryDriver(result[0], result[1], result[2], result[3])


def update_delivery_driver(delivery_driver, status):
    query = "UPDATE DeliveryDriver SET on_task = %s WHERE driver_id = %s"
    cursor.execute(query, (status, delivery_driver.driver_id))
    new_delivery_driver = DeliveryDriver(delivery_driver.driver_id, delivery_driver.operating_area, status,
                                         delivery_driver.name)
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


def generate_discount_code() -> str:
    """ Create a new discount code and set it's boolean flag to `Valid=True` """
    code = ''.join(random.choice(string.ascii_letters) for x in range(7))
    query = ("INSERT INTO Discount (code, used) VALUES (%s, FALSE );")
    cursor.execute(query, (code,))
    cnx.commit()
    return code


def valid_discount_code(code) -> bool:
    """ Check if the code has been used, return True if it is valid """
    query = ("SELECT discount_id FROM Discount WHERE code = %s AND used = FALSE;")
    cursor.execute(query, (code,))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True


def set_discount_code_invalid(code) -> None:
    """ Set the code to invalid """
    query = ("UPDATE Discount SET used = TRUE WHERE code = %s;")
    cursor.execute(query, (code,))
    cnx.commit()


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
    query = "SELECT address_id, street, town, postcode FROM Address WHERE address_id = %s;"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result is None:
        return None
    else:
        return Address(result[1], result[2], result[3], result[0])
