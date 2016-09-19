#!/usr/bin/env python
# coding=utf-8

users = ['xiaoxifeng', 'cangcang', 'tom']

while True:
    name = input("input your name:")
    if name in users:
        print("Hello, {0}".format(name))
        break
    else:
        print("Sorry. Try again, please.")

