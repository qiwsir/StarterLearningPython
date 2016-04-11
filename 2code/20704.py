
def foo(fun):
    def wrap():
        print "start"
        fun()
        print "end"
        print fun.__name__
    return wrap

@foo
def bar():
    print "I am in bar()"


bar()


#start
#I am in bar()
#end
#bar
#I am in bar()
#f = foo(bar)
#f()

