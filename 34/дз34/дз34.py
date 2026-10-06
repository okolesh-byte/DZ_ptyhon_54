class Positive:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError(f"{self.name} должно быть положительным")
        instance.__dict__[self.name] = value

class Order:
    name = Positive("name")
    price = Positive("price")
    quantity = Positive("quantity")

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

order = Order("apple", 5, 10)
print(order.total())