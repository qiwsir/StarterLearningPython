#coding:utf-8
'''
filename: simdict.py
'''

class SimDit:
    def __init__(self, k, v):
        self.dct = dict([(k, v)])

    def __setitem__(self, k, v):
        self.dct[k] = v
    
    def __getitem__(self, k):
        return self.dct[k]

    def __len__(self):
        return len(self.dct)

    def __delitem__(self, k):
        del self.dct[k]

d = SimDit('name', 'Laoqi')
d['lang'] = 'python'
d['city'] = 'Soochow'
print(d['city'])
print(len(d))
del d['city']
print(d.dct) 
