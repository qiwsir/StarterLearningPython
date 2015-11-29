t = ('Cui', 'Yansong', [123, 'abc'], ('python', 'abc'))
print t

# Tuple type index
print t[2][0]
print t[3][0]

# Tuple type with 1 element
print type((3))
print type((3, ))

# Tuple <-> List
tst = list(t)
tpt = tuple(tst)
print tst, tpt

print "===================================================="
# Dict1
mydict = {"name": "021", "site": "324"}
print "{}, {}".format(mydict['name'], hex(int(mydict['site'])))
mylist = list(mydict)
print mylist, mydict
ad = dict(name = '1', age = '22')
print ad, len(ad)
del ad['name']
print len(ad)

print "===================================================="
# Dict2
a = {'a':1, 'b':2}
b = a        #''' Shadow Copy '''
c = a.copy() #''' Deep Copy for one level   '''
print "b = a are the same object reference ? ---> " + str(id(a) == id(b))
print "c = a.copy() are the same object reference ? ---> " + str(id(a) == id(c))

o = {"Who": "CYS"}
dict1 = {"abc": o}
dict2 = dict1.copy()
dict2['abc']['Who'] = "Nobody"
print dict1, dict2

import copy
print "---> Deep Copy"
dict3 = copy.deepcopy(dict1)
dict2['abc']['Who'] = "MySelf"
print dict3, dict2

print "---> None for dict"
dd = {"1": 0, "2": 2, "3": 4}
dd2 = {"2": 5}
print dd.get('abc1') 
print dd.update(dd2)
print dd

print "---> timeit"
import timeit
def dictUpdate():
	dd.update(dd2)
def dictReplase():
	dd["2"] = 5
print timeit.timeit("dictUpdate", setup = 'from D05 import dictUpdate',number = 1000000)
print timeit.timeit("dictReplase", setup = 'from D05 import dictReplase',number = 1000000)

























