#! /usr/bin/env python
# coding:utf-8

class Person:
    def eye(self):
        print("two eyes")

    def breast(self, n):
        print("The breast is: ",n)

class Girl:
    age = 28
    def color(self):
        print("The girl is white")

class HotGirl(Person, Girl):
    pass

if __name__ == "__main__":
    kong = HotGirl()
    kong.eye()
    kong.breast(90)
    kong.color()
    print(kong.age)
