
class Drink:

    def __init__(self, drink_id, name, cost_euro, cost_cents):
        self.drink_id = drink_id
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents

    def to_JSON(self):
        return {"name": str(self.name),
                "price": str(self.cost_euro + "." + self.cost_cents)}
        
