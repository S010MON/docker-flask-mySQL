from datetime import datetime, timedelta


class Purchase:

    def __init__(self, customer_id, pizzas, drinks, desserts):
        self.purchase_id = None
        self.datetime = None
        self.estimated_delivery_time = None
        self.delivery_driver_id = None
        self.customer_id = customer_id
        self.pizzas = pizzas
        self.drinks = drinks
        self.desserts = desserts

    def to_dict(self):
        if self.datetime is not None:
            self.estimated_delivery_time = self.datetime + timedelta(minutes=30)
        return {"purchase_id": self.purchase_id,
                "time_ordered": self.datetime,
                "time_estimated_delivery": self.estimated_delivery_time,
                "customer": self.customer_id,
                "pizzas": self.pizzas,
                "drinks": self.drinks,
                "desserts": self.desserts,
                "delivery_driver_id": self.delivery_driver_id}
