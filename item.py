import csv


class Item:
    all = []

    def __init__(self, name, price=0, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name # this __[name] is works like private keword in java
    
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value
        else:
            raise Exception("No name provided")
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def discout(self, discount):
        return self.calculate_total_price() * (1 - discount)

    @classmethod
    def instansiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity'))
            )

    @staticmethod
    def is_int(num):
        # will count out int that has .0 
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            return num.is_integer()
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
