class Pizza:

    def __init__(self, pizza_id, name, cost_euro, cost_cents, toppings):
        self.pizza_id = pizza_id
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents
        self.toppings = toppings

    def to_JSON(self):
        return {"name": str(self.name),
                "toppings": str(self.toppings),
                "price": str(self.cost_euro + '.' + self.cost_cents)}
