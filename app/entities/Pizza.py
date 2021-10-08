class Pizza:

    def __init__(self, pizza_id, name, toppings, vegetarian):
        self.pizza_id = pizza_id
        self.name = name
        self.cost = 0.0
        self.toppings = toppings
        self.vegetarian = vegetarian

    def to_dict(self):
        return {"pizza_id": self.pizza_id,
                "name": self.name,
                "cost": round(self.cost, 2),
                "toppings": self.toppings,
                "vegetarian": self.vegetarian}

