class Purchase:

    def __init__(self, customer_id, pizzas, drinks, desserts):
        self.purchase_id = None
        self.datetime = None
        self.delivery_driver_id = None
        self.customer_id = customer_id
        self.pizzas = pizzas
        self.drinks = drinks
        self.desserts = desserts

    def __init__(self, purchase_id, datetime, customer_id, delivery_driver_id, pizzas, drinks, desserts):
        self.purchase_id = purchase_id
        self.datetime = datetime
        self.customer_id = customer_id
        self.delivery_driver_id = delivery_driver_id
        self.pizzas = pizzas
        self.drinks = drinks
        self.desserts = desserts

    def to_dict(self):
        pizzas_list = []
        for pizza in self.pizzas:
            pizzas_list.append(pizzas.to_dict())
        
        drinks_list = []
        for drink in self.drinks:
            drinks_list.append(drink.to_dict())

        dessert_list = []
        for dessert in self.desserts:
            dessert_list.append(dessert.to_dict())

        return{"purchase_id": self.purchase_id,
                "datetime": self.datetime,
                "customer": self.customer_id,
                "pizzas": pizzas,
                "drinks": drinks,
                "desserts": desserts,
                "delivery_driver_id": self.delivery_driver_id}
