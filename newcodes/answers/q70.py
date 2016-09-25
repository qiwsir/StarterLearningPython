#!/usr/bin/env python
# coding=utf-8

import re

class make_xlat:
    def __init__(self, *args, **kwargs):
        self.adict = dict(*args, **kwargs)
        self.rx = self.make_rx()

    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))

    def one_xlat(self, match):
        return self.adict[match.group(0)]

    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

if __name__ == "__main__":
    text = "PHP is the best language"
    adict = {"PHP": "Canglaoshi", "language":"teacher",}
    t = make_xlat(adict)
    print(text)
    print("--->")
    print(t(text))
