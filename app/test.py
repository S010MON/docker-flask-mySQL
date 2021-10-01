
from entities.Customer import Customer

if __name__ == '__main__':
    c = Customer("A", None, "B")
    print(c.to_dict())
