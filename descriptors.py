class NonNegative:
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Cannot be negative")
        instance.__dict__[self.name] = value 
 
    def __set_name__(self, owner, name):
        self.name = name

class Order:

    price = NonNegative()
    freight = NonNegative()

    def __init__(self, name, price, freight):
        self._name = name
        self.price = price
        self.freight = freight


my_order = Order("console", -500, 5)
print(my_order.price)