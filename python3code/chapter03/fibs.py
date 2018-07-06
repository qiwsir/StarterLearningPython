# coding=utf-8
'''
filename: fibs.py
'''

def fibs(n):
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

lst = fibs(10)
print(lst)
