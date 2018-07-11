#coding:utf-8
'''
filename: singleton.py
'''
class Singleton:
    _instance = None    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)    
        return cls._instance  

class MyClass(Singleton):  
    a = 1

x = MyClass()
y = MyClass()

print(x)
print(y)
print("x is y: ", x is y) 
