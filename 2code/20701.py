#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type

class Person:
    def __init__(self, name):
        self.name = name
        print self
        print type(self)

    def getName(self):
        return self.name

    def color(self, color):
        print "%s is %s" % (self.name, color)

girl = Person('canglaoshi')
name = girl.getName()
print "the person's name is: ", name
girl.color("white")

print "------"
print girl.name
