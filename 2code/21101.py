#!/usr/bin/env python
# coding=utf-8

"the code is from: http://zetcode.com/lang/python/oop/"

__metaclass__ = type

class Animal:
    def __init__(self, name=""):
        self.name = name
    
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print "Meow!"

class Dog(Animal):
    def talk(self):
        print "Woof!"


a = Animal()
a.talk()

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()
