#!/usr/bin/env python
# coding=utf-8

class StatWrod(dict):
    def add(self, item, increment=1):
        self[item] = increment + self.get(item, 0)
    def counts(self, reverse=False):
        aux = [(self[k], k) for k in self]
        aux.sort()
        if reverse:
            aux.reverse()
        return [(v, k) for v,k in aux]

if __name__ == "__main__":
    sentence = "Don't stay in bed, unless you can make money in bed."
    words = sentence.split()
    c = StatWrod()
    for word in words:
        c.add(word)
    print("Ascending count:")
    print(c.counts())
    print("Descending count:")
    print(c.counts(reverse=True))
