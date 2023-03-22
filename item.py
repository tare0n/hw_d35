import csv


class Item:
    pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, 'r', newline = '') as data:
            input_data = csv.reader(data, delimiter=' ', quotechar='|')
            for row in input_data:
                args = row[0].split(',')
                try:
                    int(args[1])
                except ValueError:
                    pass
                else:
                    Item.all.append(Item(*args))

    def __str__(self):
        return f"Item({self.__name}, {self.price}, {self.quantity})"

