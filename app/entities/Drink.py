
class Drink:

    def __init__(self, drink_id, name, cost_euro, cost_cents):
        self.drink_id = drink_id
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents

    def to_dict(self):
        return {"drink_id": self.drink_id,
                "name": self.name,
                "cost_euro": self.cost_euro,
                "cost_cents": self.cost_cents}
        
