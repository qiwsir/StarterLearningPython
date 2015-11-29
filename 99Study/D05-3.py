print "===================================================="
print "---> if-elif"
a = {"name": "cys"}
if not(a):
	print 'a is None'
elif a['name'] == 'cys':
	print 'name is cys'
else:
	print 'not find'
print "not none" if a else "none"

print "===================================================="
print "---> for"
h = "Hello World"
for idx in range(len(h)):
	print h[idx]
	
for k,v in {"a":1, "b":2}.iteritems():
	print k,v

print "===================================================="
print "---> range"
print range(1, 5, 2)
print range(0, -9, -1)
nums = []
for num in range(3, 100, 3):
	if num % 3 == 0:
		nums.append(str(num))
print " | ".join(nums)

print "===================================================="
print "---> zip"
s = {"name": "sfds"}
t = {"age": 12}
print zip(s, t)
print zip(*[(1, 11),(2, 22),(3, 33)])

print "===================================================="
print "---> enumerate"
week = ['Mon', 'Thu', 'Wed']
for i, day in enumerate(week):
	print i, day
print list(enumerate(week))
squares = [x**2 for x in range(1, 10)]
print squares
















	




















