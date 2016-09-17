#!/usr/bin/env python
# coding=utf-8

lst = ["canglaoshi", "sola", 23, 12, 3.14, [1,2,3]]
print(lst)
new_lst = []
for i in lst:
    if isinstance(i, str):
        new_lst.append(i)

print(new_lst)
