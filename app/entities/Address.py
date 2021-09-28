
class Address:

    def __init__(self, address_id, house_no, street, town, postcode):
        self.address_id = address_id
        self.house_no = house_no
        self.street = street
        self.town = town
        self.postcode = postcode

    def to_dict(self):
        return {"address_id": self.address,
                "house_no": self.house_no,
                "street": self.street,
                "town": self.town,
                "postcode": self.postcode}
