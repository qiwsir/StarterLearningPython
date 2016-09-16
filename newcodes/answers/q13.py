#!/usr/bin/env python
# coding=utf-8

name_lst = []
while True:
    name = input("Please input an English name(input 'q' then exit)")
    if name == "q":
        break
    else:
        name_lst.append(name)

name_lst.sort()
print(name_lst)
