import json

class Customer:
    
    def __init__(self):
        self.customer_id = 1
        self.name = "Leon"
        self.address = Address("Tongerseweg", "Maastricht", "6213GA")
        self.phone = "07913978643"

    def __init__(self, customer_id, name, address, phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        
    def __init__(self, name, address, phone):
        self.customer_id = None
        self.name = name
        self.address = address
        self.phone = phone

    def to_dict(self):
        return {"customer_id": self.customer_id,
                "name": self.name, 
                "address": [self.address.to_dict()], 
                "phone": self.phone}

