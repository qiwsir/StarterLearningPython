#!/usr/bin/env python
# coding=utf-8

def change_char(character, n):
    new = []
    for c in character:
        i = ord(c) + n
        new.append(chr(i))
    return "".join(new)

if __name__ == "__main__":
    one = "abc"
    new = change_char(one, 2)
    print one
    print new

