#!/usr/bin/env python
# coding=utf-8

class Goods:
    def __init__(self, price,whole_sale, discount):
        self.price = price
        self.whole_sale = whole_sale
        self.discount = discount

    def register_sale(self, count):
        self.count = count
        if self.count > self.whole_sale:
            self.price = self.price * self.discount

    def display_sale(self):
        print("The count of goods is:{0}".format(self.count))
        sales = self.price * self.count
        print("The total sales is:{0}".format(round(sales, 2)))

if __name__ == "__main__":
    price = 106.78
    whole_sale = 60
    discount = 0.7
    goods = Goods(price, whole_sale, discount)
    goods.register_sale(100)
    goods.display_sale()

