import os
import json
import PizzaController
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {"Connected to":"Pizza Maastricht"}, 200

class Pizza(Resource):
    def get(self):
        data = PizzaController.get_all_pizzas()
        return jsonify( message="test message",
                        category="success",
                        data=data,
                        status=200)

class Drink(Resource):
    def get(self):
        data = PizzaController.get_all_drinks()
        return jsonify( message="test message",
                        category="success",
                        data=data,
                        status=200)
class Dessert(Resource):
    def get(self):
        data = PizzaController.get_all_desserts()
        return jsonify( message="test message",
                        category="success",
                        data=data,
                        status=200)


class Customer(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id', type=int)
        args = parser.parse_args()
        return PizzaController.get_customer_by_id(args['customer_id']),200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id', type=int)
        parser.add_argument('house_number', type=int)
        parser.add_argument('street', type=str)
        parser.add_argument('town', type=str)
        parser.add_argument('postcode', type=str)
        args = parser.parse_args()
        return PizzaController.get_customer_by_id(args['customer_id']),200

class Order(Resource):
    def get(self):
        return PizzaController.get_order_by_id(1), 200

    def post(self):
        # Add making a new order
        return {"not yet implemented":"true"},404

api.add_resource(Home, '/')
api.add_resource(Pizza, '/pizza')
api.add_resource(Drink, '/drink')
api.add_resource(Dessert, '/dessert')
api.add_resource(Customer, '/customer')
api.add_resource(Order, '/order')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=5000)

