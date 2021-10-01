from flask import jsonify
import json
import PizzaPersistence as db

'''
Pizza Controller
- Converts objects into JSON serialisable data
- Checks for logical errors and returns None if unable to complete query
'''

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

def get_customer_by_id(customer_id):
    data = db.get_customer(customer_id).to_dict()
    return data

def get_delivery_driver_by_id(driver_id):
    return None

def get_purchase_by_id(purchase_id):
    data = db.get_purchase(purchase_id).to_dict()
    if data == None:
        return not_found_404()
    else:
        return jsonify( message="purchase",
                        category="success",
                        data=data,
                        status=200)

def post_customer(customer):
    if db.customer_exists(customer):
        return None
    else:
        customer.address = db.create_address(customer.address)
        data = db.create_customer(customer).to_dict()
    return customer.to_dict()

def post_purchase(purchase):
    if purchase.pizzas == None:
        return jsonify( message="order must contain a pizza",
                        category="failed",
                        data=None,
                        status=400)
    
    data =  db.create_purchase(purchase).to_dict() 
    return jsonify( message="pizzas",
                    category="success",
                    data=data,
                    status=200)

def delete_purchase(purchase_id):
    if db.get_purchase(purchase_id) == None:
        return jsonify( message="Order does not exist",
                        category="failed",
                        data=None,
                        status=404)
    else:
        data = db.delete_purchase(purchase_id).to_dict()
        return jsonify( message="Order Deleted",
                        category="success",
                        data=data,
                        status=200)

def not_found_404():
    return jsonify( message="Not found",
                    status=404)

def not_implemented_501():
    return jsonify( message='Not yet implemented',
                    status=501)

