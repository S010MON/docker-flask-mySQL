class Address:

    def __init__(self, address_id, street, town, postcode):
        self.address_id = address_id
        self.street = street
        self.town = town
        self.postcode = postcode
        
    def __init__(self, street, town, postcode):
        self.address_id = None
        self.street = street
        self.town = town
        self.postcode = postcode

    def to_dict(self):
        return {"address_id": self.address,
                "street": self.street,
                "town": self.town,
                "postcode": self.postcode}
      