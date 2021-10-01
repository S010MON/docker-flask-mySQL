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
             "Pizza.pizza_price_euros, "
             "Pizza.pizza_price_cents, "
             "Topping.topping_name,"
             "Topping.vegetarian FROM Pizza "
             "INNER JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
             "INNER JOIN Topping on ToppingMapping.topping_id = Topping.topping_id;")
    cursor.execute(query)
    # The following algorithm makes sure, that all the toppings from a many-to-many relation
    # are geting mapped to the corresponding pizza
    allPizzas = []
    for (pizza_id, pizza_name, pizza_price_euros, pizza_price_cents, topping_name, vegetarian) in cursor:
        already_exists = False
        for check_pizza in allPizzas:
            if check_pizza.pizza_id == pizza_id:
                pointer = check_pizza
                already_exists = True
        if already_exists:
            pointer.toppings.append(topping_name)
            if vegetarian == False:
                pointer.vegetarian = False
        else:
            allPizzas.append(
                Pizza(pizza_id, pizza_name, pizza_price_euros, pizza_price_cents, [topping_name], bool(vegetarian)))  # add toppings
    return allPizzas


def get_pizza(current_pizza_id):
    query = ("SELECT Pizza.pizza_id, "
             "Pizza.pizza_name, "
             "Pizza.pizza_price_euros, "
             "Pizza.pizza_price_cents, "
             "Topping.topping_name FROM Pizza "
             "INNER JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
             "INNER JOIN Topping on ToppingMapping.topping_id = Topping.topping_id"
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
            result_pizza = Pizza(pizza_id, pizza_name, pizza_price_euros, pizza_price_cents, [topping_name])  # add toppings
    return result_pizza

# ----------------------------------------------------------------------------------------------------------------------

def get_all_desserts():
    query = (
        "SELECT dessert_id, dessert_name, dessert_price_euros, dessert_price_cents FROM Dessert;")
    cursor.execute(query)
    allDeserts = []
    for (dessert_id, dessert_name, dessert_price_euros, dessert_price_cents) in cursor:
        allDeserts.append(Dessert(dessert_id, dessert_name, dessert_price_euros, dessert_price_cents))  # add toppings
    return allDeserts


# ----------------------------------------------------------------------------------------------------------------------

def get_all_drinks():
    query = (
        "SELECT drink_id, drink_name, drink_price_euros, drink_price_cents FROM Drink;")  # need to add join for toppings
    cursor.execute(query)
    allDrinks = []
    for (drink_id, drink_name, drink_price_euros, drink_price_cents) in cursor:
        allDrinks.append(Drink(drink_id, drink_name, drink_price_euros, drink_price_cents))  # add toppings
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
    return Customer(result[0], result[1], customer_address, result[3])


# ----------------------------------------------------------------------------------------------------------------------

def create_purchase(purchase):
    query = ("INSERT INTO Purchase (purchased_at, customer_id, delivery_driver_id) VALUES (NOW(), %s, %s);")
    cursor.execute(query, (purchase.customer_id, purchase.delivery_driver_id))
    purchase_id = cursor.lastrowid
    new_purchase = copy.deepcopy(purchase)
    new_purchase.purchase_id = purchase_id

    for current_pizza in purchase.pizzas:
        query = ("INSERT INTO PizzaMapping (purchase_id, pizza_id) VALUES (%s, %s);")
        cursor.execute(query, (purchase_id, current_pizza.pizza_id))

    for current_drink in purchase.drinks:
        query = ("INSERT INTO DrinkMapping (purchase_id, drink_id) VALUES (%s, %s);")
        cursor.execute(query, (purchase_id, current_drink.drink_id))

    for current_dessert in purchase.desserts:
        query = ("INSERT INTO PizzaMapping (purchase_id, dessert_id) VALUES (%s, %s);")
        cursor.execute(query, (purchase_id, current_dessert.dessert_id))

    cnx.commit()
    return new_purchase


def get_purchase(purchase_id):
    query = ("SELECT purchase_id, purchased_at, customer_id, delivery_driver_id FROM Purchase WHERE purchase_id = %s;")
    cursor.execute(query, (purchase_id,))
    result = cursor.fetchone()
    new_purchase = Purchase(result[0], result[1], result[2], result[3], [], [], [])



    return new_purchase

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


def update_delivery_driver_status(DeliveryDriver, status):
    return None

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
    query = ("SELECT address_id. street, town, postcode FROM Address WHERE address_id = %s;")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return Address(result[0], result[1], result[2], result[3])


# ----------------------------------------------------------------------------------------------------------------------

# Main function to test query methods
if __name__ == '__main__':
    for pizza in get_all_pizzas():
        print(pizza.pizza_id, pizza.name, pizza.toppings, pizza.vegetarian)

    print("---")

    for drink in get_all_drinks():
        print(drink.drink_id, drink.name)

    print("---")

    for dessert in get_all_desserts():
        print(dessert.dessert_id, dessert.name)

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

    # test_purchase = Purchase()
