#!/usr/bin/env python
print "===================================================="
print "---> while-else"
count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"
	
print "===================================================="
print "---> read file"
import os
help(os.open)
print os.stat('abc.txt')
f = open('abc.txt', 'r+')
for line in f:
	print line,
f.close()
