from entities.Address import Address
from entities.DeliveryDriver import DeliveryDriver
from entities.Pizza import Pizza
from entities.Dessert import Dessert
from entities.Drink import Drink
from entities.Customer import Customer
from mysql.connector import (connection)

import mysql.connector

# Docker config
config = {  'user': 'root',
            'password': 'password',
            'host': 'db',
            'port': '3306',
            'database': 'pizzas'
         }

'''
# Local test config
config = {'user': 'root',
          'password': 'password',
          'host': 'localhost',
          'port': '3306',
          'database': 'pizzas'
          }
'''

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()


def get_all_pizzas():
    query = ("SELECT Pizza.pizza_id, "
             "Pizza.pizza_name, "
             "Pizza.pizza_price_euros, "
             "Pizza.pizza_price_cents, "
             "Topping.topping_name FROM Pizza "
             "INNER JOIN ToppingMapping ON Pizza.pizza_id = ToppingMapping.pizza_id "
             "INNER JOIN Topping on ToppingMapping.topping_id = Topping.topping_id;")
    cursor.execute(query)
    # The following algorithm makes sure, that all the toppings from a many-to-many relation
    # are geting mapped to the corresponding pizza
    allPizzas = []
    for (pizza_id, pizza_name, pizza_price_euros, pizza_price_cents, topping_name) in cursor:
        already_exists = False
        for check_pizza in allPizzas:
            if check_pizza.pizza_id == pizza_id:
                pointer = check_pizza
                already_exists = True
        if already_exists:
            pointer.toppings.append(topping_name)
        else:
            allPizzas.append(
                Pizza(pizza_id, pizza_name, pizza_price_euros, pizza_price_cents, [topping_name]))  # add toppings
    return allPizzas


def get_all_desserts():
    query = (
        "SELECT dessert_id, dessert_name, dessert_price_euros, dessert_price_cents FROM Dessert;")
    cursor.execute(query)
    allDeserts = []
    for (dessert_id, dessert_name, dessert_price_euros, dessert_price_cents) in cursor:
        allDeserts.append(Dessert(dessert_id, dessert_name, dessert_price_euros, dessert_price_cents))  # add toppings
    return allDeserts


def get_all_drinks():
    query = (
        "SELECT drink_id, drink_name, drink_price_euros, drink_price_cents FROM Drink;")  # need to add join for toppings
    cursor.execute(query)
    allDrinks = []
    for (drink_id, drink_name, drink_price_euros, drink_price_cents) in cursor:
        allDrinks.append(Drink(drink_id, drink_name, drink_price_euros, drink_price_cents))  # add toppings
    return allDrinks


def create_purchase(Purchase):
    return None

def get_address_id(address):
    return None

def get_customer(id):
    query = ("SELECT customer_id, name, address_id, phone_number FROM Customer WHERE customer_id = %s")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    customer_address = get_address(result[2])
    return Customer(result[0], result[1], customer_address, result[3])

def create_customer(customer):
    query = ("INSERT INTO Customer (name, address_id, phone_number)"
             "VALUES (%s, %s, %s);")

    query_data = (customer.name, customer.address.address_id, customer.phone)
    cursor.execute(query, query_data)
    current_id = cursor.lastrowid
    customer.customer_id = current_id
    cnx.commit()

def get_customer_address(Customer):
    query = (
        "SELECT Address.street, Address.town, Address.postcode FROM Customer INNER JOIN Address ON Customer.customer_id = Order.customer_id;")
    return None


def get_purchase(purchase_id):
    return None


def get_delivery_driver(purchase_id):
    return None

def get_delivery_driver(id):
    query = ("SELECT driver_id, operating_area, on_task, name FROM DeliveryDriver WHERE driver_id = %s;")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return DeliveryDriver(result[0], result[1], result[2], result[3])

def set_delivery_driver_status(DeliveryDriver, status):
    return None

def get_address(id):
    query = ("SELECT address_id. street, town, postcode FROM Address WHERE address_id = %s;")
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return Address(result[0], result[1], result[2], result[3])

def set_address(address):
    query = ("INSERT INTO Address (street, town, postcode)"
             "VALUES (%s, %s, %s);")

    query_data = (address.street, address.town, address.postcode)
    cursor.execute(query, query_data)
    current_id = cursor.lastrowid
    address.address_id = current_id
    cnx.commit()


# Main function to test query methods
if __name__ == '__main__':
    for pizza in get_all_pizzas():
        print(pizza.pizza_id, pizza.name, pizza.toppings)

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
    set_address(test_address)
    print(test_address.address_id, test_address.town)

    test_customer = Customer("Leon", test_address, "+49 123456789")
    create_customer(test_customer)
    print(test_customer.customer_id, test_customer.name, test_customer.address.town)

    # get_customer_address()
