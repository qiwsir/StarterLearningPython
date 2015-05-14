#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type

class Person:
    def speak(self):
        print "I love you."

    def setHeight(self, n):
        self.length = n

    def breast(self, n):
        print "My breast is: ",n

class Girl(Person):
    def setHeight(self):
        print "The height is:1.70m ."

if __name__ == "__main__":
    cang = Girl()
    cang.setHeight()
    cang.speak()
    cang.breast(90)
