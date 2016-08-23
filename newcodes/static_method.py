#!/usr/bin/env python
# coding=utf-8

import random


class Foo:
    def __init__(self, name):
        self.name = name

    def get_name(self, age):
        if self.select(age):
            return self.name
        else:
            return "the name is secret."
    
    @staticmethod
    def select(n):
        a = random.randint(1, 100)
        return a - n > 0


if __name__ == "__main__":
    f = Foo("luolaoshi")
    name = f.get_name(22)
    print(name)
