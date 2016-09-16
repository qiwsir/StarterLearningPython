#!/usr/bin/env python
# coding=utf-8

import random

lst = [random.randint(0,9) for i in range(100)]
print(lst)

only_int = set(lst)

num = [ lst.count(i) for i in only_int ]

dct = dict(zip(only_int, num))
print(dct)
