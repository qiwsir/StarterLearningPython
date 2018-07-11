#coding:utf-8
'''
filename: convert2g.py
'''

class ToGram(float):
    def __new__(cls, jin=0.0):
        gram = jin / 2 * 1000
        return float.__new__(cls, gram)

jin = 2.3
value = ToGram(jin)
print("{0}jin = {1:.2f}g".format(jin, value)) 
