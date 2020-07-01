# stock.py

from .typedproperty import String, Integer, Float


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares:d}, {self.price:.2f})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares
