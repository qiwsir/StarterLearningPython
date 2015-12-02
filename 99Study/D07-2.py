
numbers = range(10)
print [ i + 2 for i in numbers]

add_fun = lambda x:x + 2
print [add_fun(i) for i in numbers]

print (lambda x,y: x + y)(2, 3)

print map(add_fun, numbers)
print reduce(lambda x,y: x + y, numbers)

print filter(lambda x: x > 2, numbers)
print [x for x in numbers if x > 2]


if __name__ == "__main__":
	print "Main function"