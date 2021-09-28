from flask import jsonify
import json
import PizzaPersistence

def get_all_pizzas():
    pizzas = PizzaPersistence.get_all_pizzas()
    data = []
    for i in range(0, len(pizzas)):
        data.append(pizzas[i].to_dict())
    return data

def get_all_drinks():
    drinks = PizzaPersistence.get_all_drinks()
    data = []
    for i in range(0, len(drinks)):
        data.append(drinks[i].to_dict())
    return data

def get_all_desserts():
    desserts = PizzaPersistence.get_all_desserts()
    data = []
    for i in range(0, len(desserts)):
        data.append(desserts[i].to_dict())
    return data

def get_order_by_id(order_id):
    if order_id == 1:
        return {"order_id": id,
        "customer": "John Smith",
        "price": 100,
        "order_time": 202109071530,
        "delivery_time": 202109071600,
        "pizzas_order": [
            {
                "pizza_id":1,
                "quantity":1
            },{
                "pizza_id":2,
                "quantity":2
            }
        ],
        "drinks_order":[
            {
                "desert_id":1,
                "quantity":4
            },{
                "desert_id":1,
                "quantity":4
            }
        ],
        "deserts_order":[
            {
                "desert_id":1,
                "quantity":4
            },{
                "desert_id":2,
                "quantity":2
        }]}
    else:
        return {" ":" "},404


def get_customer_by_id(customer_id):
    response = {"customer_name":"Elizabeth Regina",
        "house_number":1,
        "street":"The Mall",
        "town":"London",
        "postcode":"WD1 1AB"}
    return response

