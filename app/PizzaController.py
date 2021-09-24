from flask import jsonify
import json
import PizzaPersistence

def get_all_pizzas():
    pizzas = PizzaPersistence.get_all_pizzas()
    return {'temp':str(pizzas)}

def get_all_drinks():
    return {"drinks": [ {
            "drink_id": 1,
            "name": "beer",
            "price": 3
        },{
            "drink_id": 2,
            "name": "coke",
            "price": 3
        }]},200

def get_all_deserts():
        return {"deserts": [
        {
            "desert_id": 1,
            "name": "ice cream",
            "price": 4
        },{
            "desert_id": 2,
            "name": "cheese cake",
            "price": 5
        }]}, 200

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
