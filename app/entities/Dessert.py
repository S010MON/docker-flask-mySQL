class Dessert:

    def __init__(self, dessert_id, name, cost):
        self.dessert_id = dessert_id
        self.name = name
        self.cost = cost

    def to_dict(self):
        return {"dessert_id": self.dessert_id,
                "name": self.name,
                "cost": self.cost,
