#!/usr/bin/env python
# coding=utf-8

class Flower:
    def __init__(self, price_table):
        self.price_table = price_table

    def buy_flower(self, count, name):
        if name in self.price_table:
            self.count = count
            self.name = name
            self.sales = self.price_table[self.name] * self.count
        else:
            self.sales = 0 

    def total(self):
        return self.sales

if __name__ == "__main__":
    price = {"petunia":50, "pansy":15, "rose":75, "violet":20, "carnation":80}
    print(price)
    f = Flower(price)
    while True:
        my = input("input the name of flower:('q'-exit)")
        if my == "q":
            print("Bye")
            break
        else:
            count = int(input("input the number that you want to buy_flower:"))
            f.buy_flower(count, my)
            print("You should pay:{0}".format(round(f.total(), 2)))

