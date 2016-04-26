#!/usr/bin/env python
# coding=utf-8

import copy

class MyCopy(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

foo = MyCopy(7)

a = ["foo", foo]
b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)

a.append("abc")
foo.value = 17

print("original: {0}\n slice: {1}\n list(): {2}\n copy(): {3}\n deepcopy(): {4}\n".format(a,b,c,d,e))
