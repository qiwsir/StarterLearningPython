#!/usr/bin/env python
# coding=utf-8

from bisect import bisect_left, insort_left

class Ratings(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self._rating = [(v, k) for k, v in dict.items(self)]
        self._rating.sort()
        print(self._rating)
    def copy(self):
        return Ratings(self)

    def __setitem__(self, k, v):
        if k in self:
            del self._rating[self.rating(k)]
        dict.__setitem__(self, k, v)
        insort_left(self._rating, (v, k))

    def __delitem__(self, k):
        del self._rating[self.rating(k)]
        dict.__delitem__(self, k)
    
    __len__ = dict.__len__
    __contains__ = dict.__contains__

    def __iter__(self):
        for v,k in self._rating:
            yield k

    iterkeys = __iter__

    def keys(self):
        return list(self)

    def rating(self, key):
        item = self[key], key
        i = bisect_left(self._rating, item)
        print(i)
        if item == self._rating[i]:
            return i
        raise LookupError("item not found in rating")

    def get_value_by_rating(self, rating):
        return self._rating[rating][0]

    def get_key_by_rating(self, rating):
        return self._rating[rating][1]

if __name__ == "__main__":
    d = {"zhangsan":78, "lisi":98, "wangwu":76, "zhaoliu":82}
    print(d)
    r = Ratings(d)
    print(r.keys())
    print(r.get_value_by_rating(0))
    print(r.rating("zhangsan"))
