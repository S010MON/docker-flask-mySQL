from entities.Pizza import Pizza
from entities.Dessert import Dessert
from entities.Drink import Drink
from mysql.connector import (connection)

import mysql.connector

'''
cnx = mysql.connector.connect(user='root', 
                              password='password',
                              host='db',
                              database='pizzas')
'''

'''
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
          'host': '127.0.0.1',
          'port': '3306',
          'database': 'pizzas'
          }

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
        "SELECT dessert_id, dessert_name, dessert_price_euros, dessert_price_cents FROM Dessert;")  # need to add join for toppings
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


def create_customer(Customer):
    return None


def get_customer_address(Customer):
    query = (
        "SELECT Address.street, Address.town, Address.postcode FROM Customer INNER JOIN Address ON Customer.customer_id = Order.customer_id;")
    return None


def get_purchase(purchase_id):
    return None


def get_delivery_driver(purchase_id):
    return None


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

    # test_customer = Customer(1, )

    # get_customer_address()
