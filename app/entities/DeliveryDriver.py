
class DeliveryDriver:

    def __init__(self, delivery_driver_id, name, operating_area, on_task):
        self.delivery_driver_id = delivery_driver_id
        self.name = name
        self.operating_area = operating_area
        self.on_task = on_task

    def to_dict(self):
        return {"delivery_driver_id": self.delivery_driver_id,
                "name": self.name,
                "operating area": self.operating_area,
                "on task": self.on_task}
