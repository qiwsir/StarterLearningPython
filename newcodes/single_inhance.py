#!/usr/bin/env python
# coding=utf-8

class Person: 
    def __init__(self, name):
        self.name = name
                        
    def height(self, m):
        h = dict((["height", m],))
        return h

    def breast(self, n):
        b = dict((["breast", n],))
        return b

class Girl(Person):
    def __init__(self):
        self.name = "Aoi sola"

    def get_name(self):
        return self.name

if __name__ == "__main__":
    cang = Girl("canglaoshi")
    print(cang.get_name())        
    print(cang.height(160))
    print(cang.breast(90))

