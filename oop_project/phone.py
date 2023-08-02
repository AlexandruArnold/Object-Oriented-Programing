from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=1):
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >=0, f"Broken phone {broken_phones} nu este mai mare sau egal cu 0!"

        self.broken_phones = broken_phones