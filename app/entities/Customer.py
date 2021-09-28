class Customer:

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
                "address": self.address.to_dict, 
                "phone": self.phone}
