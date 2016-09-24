#!/usr/bin/env python
# coding=utf-8

class PayCalculator:
    def __init__(self, pay_rate):
        self.pay_rate = pay_rate

    def compute_pay(self, hours):
        total_pay = self.pay_rate * hours
        return round(total_pay, 2)

if __name__ == "__main__":
    worker = PayCalculator(25.7)
    total = worker.compute_pay(8)
    print(total)
