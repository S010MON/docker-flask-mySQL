class Purchase:

    def __init__(self, purchase_id, datetime, customer_id, delivery_driver_id):
        self.purchase_id = purchase_id
        self.datetime = datetime
        self.customer_id = customer_id,
        self.delivery_driver_id = delivery_driver_id

    def to_dict(self):
        return{"purchase_id": self.purchase_id,
                "datetime": self.datetime,
                "customer": self.customer_id,
                "delivery_driver_id": self.delivery_driver_id}
