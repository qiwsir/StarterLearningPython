#coding:utf-8
'''
filename: foo2.py
'''
def foo():
    def bar():
        print("bar() is running")
    bar()                    #显示调用内嵌函数
    print("foo() is running")

foo()
