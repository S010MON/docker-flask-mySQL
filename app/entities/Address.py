import json

class Address:

    def __init__(self, street, town, postcode, address_id=None):
        self.street = street
        self.town = town
        self.postcode = postcode
        self.address_id = address_id


    def to_dict(self):
        return {"address_id": self.address_id,
                "street": self.street,
                "town": self.town,
                "postcode": self.postcode}
    
