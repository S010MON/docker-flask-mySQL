class Dessert:

    def __init__(self, dessert_id, name, cost_euro, cost_cents):
        self.dessert_id = dessert_id
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents

    def to_dict(self):
        return {"dessert_id": self.dessert_id,
                "name": self.name,
                "cost_euro": self.cost_euro,
                "cost_cents": self.cost_cents}
