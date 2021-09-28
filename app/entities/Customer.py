class Customer:

    def __init__(self, customer_id, name, address, phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone

    def to_JSON(self):
        return {"customer_id": str(self.customer_id),
                "name": self.name, 
                "address": self.address.to_JSON(), 
                "phone" str(self.phone)}
