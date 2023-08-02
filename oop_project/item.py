import csv

class Item:
    pay_rate = 0.8 # class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} este mai mic sau egal cu 0"
        assert quantity >=0, f"Quantity {quantity} este mai mic decat 0"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        return self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator - Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Numele e prea lung!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}, {self.__price}, {self.quantity}"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False