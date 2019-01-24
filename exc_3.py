from decimal import *

class ApDecimal:

    def __init__(self):
        self.a = 2
        self.b = 5.5
        self.c = []

    def get_decimal_list(self):
        while self.a <= self.b:
            self.c.append(Decimal(self.a))
            self.a += 0.5

    def get_my_list(self):
        return self.c

apDecimalInstance = ApDecimal()

apDecimalInstance.get_decimal_list()

print(apDecimalInstance.c)