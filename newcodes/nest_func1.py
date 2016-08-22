#!/usr/bin/env python
# coding=utf-8

def foo():
    def bar():
        print("bar() is running")
    bar()
    print("foo() is running")

foo()
