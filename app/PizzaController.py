from flask import jsonify
import json
import PizzaPersistence as db

# Pizza Controller

def get_all_pizzas():
    pizzas = db.get_all_pizzas()
    data = []
    for i in range(0, len(pizzas)):
        data.append(pizzas[i].to_dict())
    return data

def get_all_drinks():
    drinks = db.get_all_drinks()
    data = []
    for i in range(0, len(drinks)):
        data.append(drinks[i].to_dict())
    return data

def get_all_desserts():
    desserts = db.get_all_desserts()
    data = []
    for i in range(0, len(desserts)):
        data.append(desserts[i].to_dict())
    return data

def get_purchase_by_id(purchase_id):
    return {"purchase_id": purchase_id}

def get_customer_by_id(customer_id):
    db.get_customer(customer_id)
    return None

def post_customer(customer):
    
    return True

def post_purchase(purchase):
    
    return True

