class DeliveryDriver:


    def __init__(self, driver_id, operating_area, on_task, name):
        self.driver_id = driver_id
        self.name = name
        self.operating_area = operating_area
        self.on_task = on_task

    def to_dict(self):
        return {"delivery_driver_id": self.delivery_driver_id,
                "name": self.name,
                "operating area": self.operating_area,
                "on task": self.on_task}
