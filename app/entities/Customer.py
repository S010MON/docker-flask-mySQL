import json

class Customer:
    
    def __init__(self, name, address, phone, customer_id=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.customer_id = customer_id


    def to_dict(self):
        if self.address is None:
            address = []
        else:
            address = [self.address.to_dict()]
        return {"customer_id": self.customer_id,
                "name": self.name, 
                "address": address,
                "phone_number": self.phone}

