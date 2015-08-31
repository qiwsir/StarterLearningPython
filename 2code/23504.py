#!/usr/bin/env python
# coding=utf-8

from contextlib import contextmanager

@contextmanager
def demo():
    print "before yield."
    yield "contextmanager demo."
    print "after yield."

with demo() as dd:
    print "the word is: %s" % dd

