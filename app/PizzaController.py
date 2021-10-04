from flask import jsonify
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

    return jsonify(message="pizzas",
                   category="success",
                   data=data,
                   status=200)


def get_all_drinks():
    drinks = db.get_all_drinks()
    if drinks is None:
        return not_found_404()

    data = []
    for i in range(0, len(drinks)):
        data.append(drinks[i].to_dict())

    return jsonify(message="drinks",
                   category="success",
                   data=data,
                   status=200)


def get_all_desserts():
    desserts = db.get_all_desserts()
    if desserts is None:
        return not_found_404()

    data = []
    for i in range(0, len(desserts)):
        data.append(desserts[i].to_dict())

    return jsonify(message="Sweet Sweets!",
                   category="success",
                   data=data,
                   status=200)


def get_customer_by_id(customer_id):
    customer = db.get_customer(customer_id)
    if customer is None:
        return not_found_404()

    data = customer.to_dict()
    return jsonify(message="customer found",
                   category="success",
                   data=data,
                   status=200)


def get_purchase_by_id(purchase_id):
    data = db.get_purchase(purchase_id).to_dict()
    if data is None:
        return not_found_404()
    else:
        return jsonify(message="purchase",
                       category="success",
                       data=data,
                       status=200)


def post_customer(customer):
    if db.customer_exists(customer):
        return jsonify(message="customer already exists",
                       category="failed",
                       status=400)
    else:
        customer.address = db.create_address(customer.address)
        data = db.create_customer(customer).to_dict()
        return jsonify(message="customer added",
                       category="success",
                       data=data,
                       status=201)


def post_purchase(purchase):
    if purchase.pizzas is None:
        return jsonify(message="order must contain a pizza",
                       category="failed",
                       data=None,
                       status=400)

    if purchase.customer_id is None:
        return jsonify(message="customer does not exist",
                       category="failed",
                       status=400)

    if db.get_customer(purchase.customer_id) is None:
        return jsonify(message="customer does not exist",
                       category="failed",
                       status=400)

    data = db.create_purchase(purchase).to_dict()
    return jsonify(message="pizzas",
                   category="success",
                   data=data,
                   status=201)


def delete_purchase(purchase_id):
    purchase = db.get_purchase(purchase_id)
    if purchase is None:
        return jsonify(message="Order does not exist",
                       category="failed",
                       data=None,
                       status=404)

    last_minute = purchase.datetime + timedelta(minutes=5)
    if datetime.now() > last_minute:
        return jsonify(message="Cannot Cancel Order",
                       category="failed",
                       data=purchase.to_dict(),
                       status=400)

    else:
        return jsonify(message="Order Deleted",
                       category="success",
                       data=purchase.to_dict(),
                       status=200)


def update_orders():
    # TODO - run update on all current orders
    # undelivered_purchases = db.get_all_undelivered_purchases()
    # for purchase in undelivered_purchases:
    #    dispatch_time = purchase.datetime + timedelta(minutes=5)
    #    if dispatch_time > datetime.now():
    #        driver =
    #        db.update_order_dispatched(purchase.purchase_id, datetime.now())
    print('Orders updated', flush=True)


def not_found_404():
    return jsonify(message="Not found",
                   status=404)


def not_implemented_501():
    return jsonify(message='Not yet implemented',
                   status=501)
