import os
import json
import PizzaController as controller
from entities.Customer import Customer as Customer_object
from entities.Address import Address
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

'''
Pizza Service
- API endpoints
- 
'''

class Home(Resource):
    def get(self):
        return {"Connected to":"Pizza Maastricht"}, 200

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
        parser.add_argument('name', type=str)
        parser.add_argument('street', type=str)
        parser.add_argument('town', type=str)
        parser.add_argument('postcode', type=str)
        parser.add_argument('phone', type=str)
        args = parser.parse_args()

        address = Address(args['street'],
                          args['town'],
                          args['postcode'])
        

        customer = Customer_object(args['name'],
                                     address,
                                     args['phone'])
        data = controller.post_customer(customer)
        if data == None:
            return not_found_404()
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
        data = controller.get_purchase_by_id(args['purchase_id'])
        if data == None:
            return not_found_404()
        if type(data) != dict:
            return
        else:
            return jsonify( message="purchase",
                            category="success",
                            data=data,
                            status=200)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('', type=int)
        parser.add_argument('', type=str)
        parser.add_argument('', type=str)
        parser.add_argument('', type=str)
        args = parser.parse_args()
        return {"not yet implemented":"true"},404

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

