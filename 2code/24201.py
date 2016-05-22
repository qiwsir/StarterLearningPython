
def foo():
    a = 3
    def bar():
        return a
    return bar

f = foo()
print f()
