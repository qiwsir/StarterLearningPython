# 111.md
# a = []
# print type(a)
# print bool(a) # False
# b = [1,2,"3","abc"]
# print b
# print b[:2] 	 # From 0 to 2
# print b[:] 		 # From start to end
# print b[2:]		 # From 2 to end
# print b[3][:1]   # 'abc' From 0 to 2 is 'a'
# print b[-2:-1]   # From last 1 to last 2 is '3'
# print b[::-1]    # Revert b
# print list(reversed(b)) # Revert b
# b[len(b):] = ["new"] # Equal to b.append("new")
# print b

# 112.md
# c = [1,2,3]
# d = [4,5,6]
# c.extend(d)
# print c
# str = "Python"
# print hasattr(str, '__iter__')   # False
# print hasattr(c, '__iter__')	 # True
new = [1,2,3]
lst = ['python']
print id(lst)
lst.extend(new)
print id(lst) 
print id(new), id(lst), id(new) == id(lst)
new.insert(999, "new")
print new
new.pop()
print new
sortedLst = ['shanghai', 'beijing', 'wuhan']
sortedLst.sort(key=len)
print sortedLst

