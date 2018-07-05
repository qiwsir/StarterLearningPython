#coding:utf-8
'''
filename: aliquot.py
'''

aliquot = []

for n in range(1,100):
    if n % 3 == 0:
        aliquot.append(n)

print(aliquot)