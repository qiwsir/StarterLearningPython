#!/usr/bin/env python
# coding=utf-8

import urllib

def go(a,b,c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print "%.2f%%" % per

url = "http://youxi.66wz.com/uploads/1046/1321/11410192.90d133701b06f0cc2826c3e5ac34c620.jpg"
local = "/home/qw/Pictures/g.jpg"
urllib.urlretrieve(url, local, go)
