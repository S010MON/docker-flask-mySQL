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