# coding:utf-8
'''
filename: account.py
'''
class Account(object):
    def __init__(self, number):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        try:
            assert amount > 0
            self.balance += amount
        except:
            print("The money should be bigger than zero.")

    def withdraw(self, amount):
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("balance is not enough.")

if __name__ == "__main__":
    a = Account(1000)
    a.deposit(-10)
