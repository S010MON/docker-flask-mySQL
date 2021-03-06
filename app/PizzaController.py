from flask import jsonify, make_response
from datetime import datetime, timedelta
import PizzaPersistence as db

'''
Pizza Controller
- Query Logic
- Error Management
- JSON serialisation
'''


def get_all_pizzas():
    pizzas = db.get_all_pizzas()
    if pizzas is None:
        return not_found_404()

    data = []
    for i in range(0, len(pizzas)):
        data.append(pizzas[i].to_dict())

    return make_response(jsonify(message="pizzas",
                                 category="success",
                                 data=data), 200)


def get_all_drinks():
    drinks = db.get_all_drinks()
    if drinks is None:
        return not_found_404()

    data = []
    for i in range(0, len(drinks)):
        data.append(drinks[i].to_dict())

    return make_response(jsonify(message="drinks",
                                 category="success",
                                 data=data), 200)


def get_all_desserts():
    desserts = db.get_all_desserts()
    if desserts is None:
        return not_found_404()

    data = []
    for i in range(0, len(desserts)):
        data.append(desserts[i].to_dict())

    return make_response(jsonify(message="Sweet Sweets!",
                                 category="success",
                                 data=data), 200)


def get_customer_by_id(customer_id):
    customer = db.get_customer(customer_id)
    if customer is None:
        return not_found_404()

    data = customer.to_dict()
    return make_response(jsonify(message="customer found",
                                 category="success",
                                 data=data), 200)


def get_purchase_by_id(purchase_id):
    data = db.get_purchase(purchase_id).to_dict()
    if data is None:
        return not_found_404()
    else:
        return make_response(jsonify(message="purchase found",
                                     category="success",
                                     data=data), 200)


def post_customer(customer):
    if db.customer_exists(customer):
        return make_response(jsonify(message="customer already exists",
                                     category="failed"), 400)
    else:
        customer.address = db.create_address(customer.address)
        data = db.create_customer(customer).to_dict()
        return make_response(jsonify(message="customer added",
                                     category="success",
                                     data=data), 201)


def post_purchase(purchase):
    customer = db.get_customer(purchase.customer_id)
    if customer is None:
        return make_response(jsonify(message="customer does not exist",
                                     category="failed",
                                     data=None), 400)

    if purchase.pizzas is None:
        return make_response(jsonify(message="order must contain a pizza",
                                     category="failed",
                                     data=None), 400)

    if purchase.customer_id is None:
        return make_response(jsonify(message="customer does not exist",
                                     category="failed"), 400)

    if db.get_customer(purchase.customer_id) is None:
        return make_response(jsonify(message="customer does not exist",
                                     category="failed"), 400)

    purchase.total_cost = calculate_total_cost(purchase)

    if purchase.discount_code is None:
        purchase.discount_code = db.generate_discount_code()

    elif not db.valid_discount_code(purchase.discount_code):
        return make_response(jsonify(message="invalid discount code",
                                     category="failed"), 400)
    else:
        purchase.total_cost = purchase.total_cost * 0.9
        purchase.discount_code = None

    data = db.create_purchase(purchase)
    if data is None:
        return make_response(jsonify(message="Failed to create order",
                                     category="failed"), 400)

    data = data.to_dict()
    return make_response(jsonify(message="order created",
                                 category="success",
                                 data=data), 201)


def cancel_purchase(purchase_id):
    purchase = db.get_purchase(purchase_id)
    if purchase is None:
        return make_response(jsonify(message="Order does not exist",
                                     category="failed",
                                     data=None), 404)

    last_minute = purchase.datetime + timedelta(minutes=5)
    if datetime.now() > last_minute:
        return make_response(jsonify(message="Cannot Cancel Order",
                                     category="failed",
                                     data=purchase.to_dict()), 400)

    db.update_purchase_status(purchase_id, "cancelled")
    return make_response(jsonify(message="Order cancelled",
                                 category="success",
                                 data=purchase.to_dict()), 200)


def update_orders():
    undelivered_purchases = db.get_undelivered_purchases()
    print(str(len(undelivered_purchases)) + ' undelivered orders in queue', flush=True)

    for purchase in undelivered_purchases:
        dispatch_time = purchase.datetime + timedelta(minutes=5)
        print('Order ' + str(purchase.purchase_id) + ' ordered at ' + str(purchase.datetime), flush=True)

        if dispatch_time > datetime.now():
            print('Looking for driver for order ' + str(purchase.purchase_id), flush=True)
            customer = db.get_customer(purchase.customer_id)
            drivers = db.get_available_drivers(customer.address.postcode)

            if len(drivers) >= 1:
                db.set_delivery_driver(purchase.purchase_id, drivers[0].driver_id)
                db.update_purchase_status(purchase.purchase_id, datetime.now())
                print('Order: ' + str(purchase.purchase_id) + ' dispatched', flush=True)
            else:
                print('No driver available', flush=True)
    print('Orders updated', flush=True)


def get_all_orders():
    data = []
    for order in db.get_undelivered_purchases():
        data.append(order.to_dict())
    return make_response(jsonify(message="All Orders",
                                 category="success",
                                 data=data), 200)


def calculate_total_cost(purchase) -> int:
    total_cost = 0
    for i in purchase.pizzas:
        total_cost = total_cost + (db.get_pizza(i['pizza_id']).cost * i['quantity'])
    if purchase.drinks is not None:
        for i in purchase.drinks:
            total_cost = total_cost + (db.get_drink(i['drink_id']).cost * i['quantity'])
    if purchase.desserts is not None:
        for i in purchase.desserts:
            total_cost = total_cost + (db.get_dessert(i['dessert_id']).cost * i['quantity'])
    return total_cost


def not_found_404():
    return make_response(jsonify(message="Not found"), 404)


def not_implemented_501():
    return make_response(jsonify(message='Not yet implemented'), 501)
