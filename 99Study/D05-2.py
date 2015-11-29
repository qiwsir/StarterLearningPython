print "===================================================="
print "---> set"
s = set(["qiweri", "google", "facebook"])
s.add("Microsoft")
print s
print "---> frozenset"
f_set = frozenset('qwertyuio')
f_sub_set = frozenset('qw')
print f_set
print f_sub_set.issubset(f_set)
print f_set | set('sdf')
print f_set & set('er')
print f_set - set('er')
if f_set:
	print "f_set is True"
print not(not(f_set))
print f_set and set('er')

print "===================================================="
print "---> operator"
a = 5
b = '5'
print a > b

print "===================================================="
print "---> operator2"
a = 2
b = 5
print a, b
a, b = b, a
print a ,b






