class Pizza:

    def __init__(self, pizza_id, name, cost, toppings, vegetarian):
        self.pizza_id = pizza_id
        self.name = name
        self.cost = cost
        self.toppings = toppings
        self.vegetarian = vegetarian

    def to_dict(self):
        return {"pizza_id": self.pizza_id,
                "name": self.name,
                "cost": self.cost,
                "toppings": self.toppings,
                "vegetarian": self.vegetarian}

