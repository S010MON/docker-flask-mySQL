class Drink:

    def __init__(self, drink_id, name, cost):
        self.drink_id = drink_id
        self.name = name
        self.cost = cost

    def to_dict(self):
        return {"drink_id": self.drink_id,
                "name": self.name,
                "cost": round(self.cost,3)}
        
