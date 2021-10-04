import sys
from flask_cors import CORS
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_apscheduler import APScheduler
import PizzaController as ctrlr
from entities.Customer import Customer as Customer_obj
from entities.Purchase import Purchase as Purchase_obj
from entities.Address import Address

app = Flask(__name__)
api = Api(app)
CORS(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


'''
Pizza Service
- API endpoints
- JSON Input Parsing
'''


class Home(Resource):
    def get(self):
        return {"message":"Welcome to Pizza Maastricht"}, 200


class Pizza(Resource):
    def get(self):
        return ctrlr.get_all_pizzas()


class Drink(Resource):
    def get(self):
        return ctrlr.get_all_drinks()


class Dessert(Resource):
    def get(self):
        return ctrlr.get_all_desserts()


class Customer(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id', type=int)
        args = parser.parse_args()
        response = ctrlr.get_customer_by_id(args['customer_id'])
        return response

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_name', type=str)
        parser.add_argument('street', type=str)
        parser.add_argument('town', type=str)
        parser.add_argument('postcode', type=str)
        parser.add_argument('phone_number', type=str)
        args = parser.parse_args()

        address = Address(args['street'], args['town'], args['postcode'])
        customer = Customer_obj(args['customer_name'], address, args['phone_number'])
        return ctrlr.post_customer(customer)


class Purchase(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('purchase_id', type=int)
        args = parser.parse_args()

        response = ctrlr.get_purchase_by_id(args['purchase_id'])
        return response

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id', type=int)
        parser.add_argument('pizzas', type=dict, action='append')
        parser.add_argument('drinks', type=dict, action='append')
        parser.add_argument('desserts', type=dict, action='append')
        args = parser.parse_args()
        
        purchase = Purchase_obj(args['customer_id'], args['pizzas'], args['drinks'], args['desserts'])
        response = ctrlr.post_purchase(purchase)
        return response

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('purchase_id', type=int)
        args = parser.parse_args()

        response = ctrlr.delete_purchase(args['purchase_id'])
        return response


@scheduler.task('interval', id='update_orders', minutes=5, misfire_grace_time=30)
def update_orders():
    ctrlr.update_orders()


api.add_resource(Home, '/')
api.add_resource(Pizza, '/pizza')
api.add_resource(Drink, '/drink')
api.add_resource(Dessert, '/dessert')
api.add_resource(Customer, '/customer')
api.add_resource(Purchase, '/purchase')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

