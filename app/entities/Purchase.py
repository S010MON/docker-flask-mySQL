from datetime import datetime, timedelta


class Purchase:

    def __init__(self, customer_id, pizzas, drinks, desserts, status=None, discount_code=None):
        self.customer_id = customer_id
        self.pizzas = pizzas
        self.drinks = drinks
        self.desserts = desserts
        self.status = status
        self.purchase_id = None
        self.datetime = None
        self.estimated_delivery_time = None
        self.delivery_driver_id = None
        self.total_cost = None
        self.discount_code = discount_code

    def to_dict(self):
        if self.datetime is not None:
            self.estimated_delivery_time = self.datetime + timedelta(minutes=30)

        total_cost = None
        if self.total_cost is not None:
            total_cost = round(self.total_cost, 3)

        return {"order_id": self.purchase_id,
                "time_ordered": self.datetime,
                "time_estimated_delivery": self.estimated_delivery_time,
                "customer_id": self.customer_id,
                "pizzas": self.pizzas,
                "drinks": self.drinks,
                "desserts": self.desserts,
                "delivery_driver_id": self.delivery_driver_id,
                "total_cost": total_cost,
                "discount_code":self.discount_code}
