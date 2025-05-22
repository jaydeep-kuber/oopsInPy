class Item:
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def discout(self, discount):
        return self.calculate_total_price() * (1 - discount)
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 10000, 3)
item2 = Item("Laptop", 50000, 2)
item3 = Item("Tablet", 20000, 1)
item4 = Item("Headphones", 3000, 2)
item5 = Item("Mouse", 1000, 3)

print(Item.all)