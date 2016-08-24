#!/usr/bin/env python
# coding=utf-8

class RoundFloat:
    def __init__(self, val):
        assert isinstance(val, float), "value must be a float."
        self.value = round(val, 2)

    def __str__(self):
        return "{:.2f}".format(self.value)

    __repr__ = __str__

if __name__ == "__main__":
    r = RoundFloat(2.185)
    print(r)
    print(type(r))
