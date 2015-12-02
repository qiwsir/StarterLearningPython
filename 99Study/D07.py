#!/usr/bin/env python
#coding:utf-8

def add_function(a, b):
	return a + b

	
def fibs(n):
	'''
	This is a Fibonacci recursion
	'''
	result = [0, 1]
	if n in result:
		return n
	else:
		return add_function(fibs(n - 1), fibs(n - 2))
	
	
def add_num(base, *args):
	'''
	This is a add number function
	'''
	print args, type(args)
	for arg in args:
		base += arg
	return base
	
	
def add_num2(base, **args):
	'''
	This is a add number function2
	'''
	print args, type(args)
	for item in list(args.values()):
		base += int(item)
	return base
	
	
def add_num3(x, y, z):
	'''
	This is a add number function3
	'''
	return x + y + z
	
	
if __name__ == "__main__":
	print add_function(10, 1)
	print fibs(10)
	print fibs.__doc__
	print add_num.__doc__ + str(add_num(1, 2, 3, 4, 5))
	print add_num2.__doc__ + str(add_num2(0, a=1, b=2, c=3))
	print add_num3.__doc__ + str(add_num3(*(2, 3, 4)))

	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
