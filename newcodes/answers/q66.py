#!/usr/bin/env python
# coding=utf-8

class RoundFloat(object):    #Python 3: class RoundFloat:
    def __init__(self, val):
        assert isinstance(val, float), "value must be a float."
        self.value = round(val, 2)

    def __str__(self):
        return "{:.2f}".format(self.value)

    __repr__ = __str__

if __name__ == "__main__":
    while True:
        n = input("Input a float:('q'-exit)")
        if n == 'q':
            print('See you next time.')
            break
        else:
            n = float(n)
            r = RoundFloat(n)
            print(r)
