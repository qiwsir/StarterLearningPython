#coding:utf-8
'''
filename: foo1.py
'''
def foo():
    def bar():
        print("bar() is running")
    print("foo() is running")

foo()        #调用函数
