#coding:utf-8
'''
filename: temperature.py
'''

class Temperature:
    coefficient = {"c": (1.0, 0.0, -273.15), "f": (1.8, -273.15, 32.0)}
    def __init__(self, **kargs):
        assert set(kargs.keys()).intersection("kfcKFC"), "invalid arguments {0}".format(kargs)
        name, value = kargs.popitem()
        name = name.lower()
        setattr(self, name, float(value)) 

    def __getattr__(self, name):
        try:
            eq = self.coefficient[name.lower()]
        except KeyError:
            raise AttributeError(name)
        return (self.k + eq[1]) * eq[0] + eq[2]

    def __setattr__(self, name, value):
        name = name.lower()
        if name in self.coefficient:
            eq = self.coefficient[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        elif name == 'k':
            object.__setattr__(self, name, value) 
        else:
            raise AttributeError(name)
    
    def __str__(self):
        return "{0}K".format(self.k)

    def __repr__(self):
        return "Temperature(K={0}".format(self.k)

t = Temperature(c=64)
print("c=64, f=", t.f)
t.f = 23
print("f=23, c=", t.c) 
