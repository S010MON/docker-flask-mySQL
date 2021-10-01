import os
import json
from flask_cors import CORS
import PizzaController as controller
from entities.Customer import Customer as Customer_object
from entities.Purchase import Purchase as Purchase_object
from entities.Address import Address
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
CORS(app)

'''
Pizza Service
- API endpoints
- 
'''

class Home(Resource):
    def get(self):
        return {"message":"Welcome to Pizza Maastricht"}, 200

class Pizza(Resource):
    def get(self):
        data = controller.get_all_pizzas()
        if data == None:
            return not_found_404()
        else:
            return jsonify( message="test message",
                            category="success",
                            data=data,
                            status=200)

class Drink(Resource):
    def get(self):
        data = controller.get_all_drinks()
        if data == None:
            return not_found_404()
        else:
            return jsonify( message="test message",
                            category="success",
                            data=data,
                            status=200)

class Dessert(Resource):
    def get(self):
        data = controller.get_all_desserts()
        if data == None:
            return not_found_404()
        else:
            return jsonify( message="Sweet Sweets!",
                            category="success",
                            data=data,
                            status=200)

class Customer(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id', type=int)
        args = parser.parse_args()
        return controller.get_customer_by_id(args['customer_id']),200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_name', type=str)
        parser.add_argument('street', type=str)
        parser.add_argument('town', type=str)
        parser.add_argument('postcode', type=str)
        parser.add_argument('phone_number', type=str)
        args = parser.parse_args()

        address = Address(args['street'],
                          args['town'],
                          args['postcode'])
        

        customer = Customer_object(args['customer_name'],
                                   address,
                                   args['phone_number'])
        data = controller.post_customer(customer)
        if data == None:
            return jsonify( message="customer already exists",
                            category="success",
                            data=data,
                            status=201)


        else:
            return jsonify( message="customer added",
                            category="success",
                            data=data,
                            status=201)

class Purchase(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('purchase_id', type=int)
        args = parser.parse_args()
        response = controller.get_purchase_by_id(args['purchase_id'])
        return response

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id', type=int)
        parser.add_argument('pizzas', type=dict, action='append')
        parser.add_argument('drinks', type=dict, action='append')
        parser.add_argument('desserts', type=dict, action='append')
        args = parser.parse_args()
        
        purchase = Purchase_object(args['customer_id'], args['pizzas'], args['drinks'], args['desserts'])
        response = controller.post_purchase(purchase) 
        return response

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('purchase_id', type=int)
        args = parser.parse_args()
        response = controller.delete_purchase(args['purchase_id'])
        return response

def not_found_404():
    return jsonify( message="Not found",
                    status=404)

def not_implemented_501():
    return jsonify( message='Not yet implemented',
                    status=501)

api.add_resource(Home, '/')
api.add_resource(Pizza, '/pizza')
api.add_resource(Drink, '/drink')
api.add_resource(Dessert, '/dessert')
api.add_resource(Customer, '/customer')
api.add_resource(Purchase, '/purchase')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=5000)

