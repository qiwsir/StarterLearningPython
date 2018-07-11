#coding:utf-8
'''
filename: simlist.py
'''

class SimLst:
    def __init__(self, total):
        self.__num = [None] * total
    def __setitem__(self, n, data):
        self.__num[n] = data
    def __getitem__(self, n):
        return self.__num[n]
    def __len__(self):
        return len(self.__num)

slst = SimLst(3)
print(len(slst)) 
