#!/usr/bin/env python
# coding=utf-8

#people_list = [ x for x in range(1, 101) ]
#while len(people_list) != 1:
#    people_list = people_list[1::2]
#print(people_list[0])

s = range(100)
while len(s) > 1:
    s = [ x for i,x in enumerate(s) if i%2==1 ]
print(s.pop()+1)
