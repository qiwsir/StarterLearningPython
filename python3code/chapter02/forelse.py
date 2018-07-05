# coding:utf-8
'''
filename: forelse.py
'''

from math import sqrt

for n in range(99, 1, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

else:
    print("Nothing.")
