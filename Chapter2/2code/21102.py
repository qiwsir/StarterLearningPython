#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    def __python(self):
        print "I love Python."

    def code(self):
        print "Which language do you like?"
        self.__python()
    
    @property
    def name(self):
        return self.__name
    
if __name__ == "__main__":
    p = ProtectMe()
    #print p.me
    print p.name
    #p.code()
    #p._ProtectMe.__python()

