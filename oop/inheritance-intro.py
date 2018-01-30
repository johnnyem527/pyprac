class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number


class Currency(Decimal):
    def __init__(self, symbol, number, places):
        super().__init__(number-1, places)
        self.symbol = symbol

    def __repr__(self):
        return "{}{}".format(self.symbol, super().__repr__())

    def add_currency(self):
        pass

print(Decimal(15.23723, 2))
print(Currency("$", 15.23723, 2))
