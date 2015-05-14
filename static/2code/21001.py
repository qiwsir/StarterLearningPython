#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type

class StaticMethod:
    @staticmethod
    def foo():
        print "This is static method foo()."


class ClassMethod:
    @classmethod
    def bar(cls):
        print "This is class method bar()."
        print "bar() is part of class:", cls.__name__

if __name__ == "__main__":
    static_foo = StaticMethod()
    static_foo.foo()
    StaticMethod.foo()
    print "********"
    class_bar = ClassMethod()
    class_bar.bar()
    ClassMethod.bar()
