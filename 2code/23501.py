#!/usr/bin/env python
# coding=utf-8

#read_file = open("23501.txt")
#write_file = open("23502.txt", "w")

#try:
#    r = read_file.readlines()
#    for line in r:
#        write_file.write(line)
#finally:
#    read_file.close()
#    write_file.close()

with open("23501.txt") as read_file, open("23503.txt", "w") as write_file:
    for line in read_file.readlines():
        write_file.write(line)


