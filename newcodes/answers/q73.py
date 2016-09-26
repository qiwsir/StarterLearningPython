#!/usr/bin/env python
# coding=utf-8

import math

class Measurement:
    def __init__(self, val, perc):
        self.val = val
        self.perc = perc
        self.abs = self.val * self.perc / 100

    def __repr__(self):
        return "Measurement({0}, {1})".format(self.val, self.perc)
    def __str__(self):
        return "{0}±{1}%".format(self.val, self.perc)

    def _addition_result(self, result, other_abs):
        new_perc = 100 * (math.hypot(self.abs, other_abs) / result)
        return Measurement(result, new_perc)
    def __add__(self, other):
        result = self.val + other.val
        return self._addition_result(result, other.abs)
    def __sub__(self, other):
        result = self.val - other.val
        return self._addition_result(result, other.abs)

    def _multiplication_result(self, result, other_perc):
        new_perc = math.hypot(self.perc, other_perc)
        return Measurement(result, new_perc)
    def __mul__(self, other):
        result = self.val * other.val
        return self._multiplication_result(result, other.perc)
    def __truediv__(self, other):
        result = self.val / other.val
        return self._multiplication_result(result, other.perc)

if __name__ == "__main__":
    m1 = Measurement(110, 0.2)
    m2 = Measurement(134, 0.1)
    print("m1:{0}".format(m1))
    print("m2:{0}".format(m2))
    print("m1+m2={0}".format(m1+m2))
    print("m1-m2={0}".format(m1-m2))
    print("m1*m2={0}".format(m1*m2))
    print("m1/m2={0}".format(m1/m2))
