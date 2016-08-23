#!/usr/bin/env python
# coding=utf-8

class Foo:
    lang = "Java"
    def __init__(self):
        self.lang = "python" 

    @classmethod
    def get_class_attr(cls):
        return cls.lang

if __name__ == "__main__":
    print("Foo.lang:", Foo.lang)
    r = Foo.get_class_attr()
    print("get class attribute:", r)

    f = Foo()
    print("instance attribute:", f.lang)
    print("instance get_class_attr:", f.get_class_attr())
