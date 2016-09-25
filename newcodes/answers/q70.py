#!/usr/bin/env python
# coding=utf-8

class Keeper:
    def __init__(self, keep):
        self.keep = keep
    def __getitem__(self, s):
        if s not in self.keep:
            return None
        return s
    def __call__(self, s):
        return s.translate(self)

if __name__ == "__main__":
    mf = Keeper
    cang = mf('canglaoshi')
    print(cang("what is your name? my name is laoshicang"))
