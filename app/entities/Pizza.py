class Pizza:

    def __init__(self, pizza_id, name, cost_euro, cost_cents, toppings, vegetarian):
        self.pizza_id = pizza_id
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents
        self.toppings = toppings
        self.vegetarian = vegetarian

    def to_dict(self):
        return {"pizza_id": self.pizza_id,
                "name": self.name,
                "cost_euro": self.cost_euro,
                "cost_cents": self.cost_cents,
                "toppings": self.toppings,
                "vegetarian": self.vegetarian}

