from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken=0):
        super.__init__(
            name=name,
            price=price,
            quantity=quantity,
        )

        assert broken >= 0 , "broken quantity can't be negative"
        self.broken = broken