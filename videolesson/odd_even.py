#coding:utf-8
'''
    lesson 19-04
    filename: odd_even.py
'''
lst = [1,2,3,4,5,6,7,8,9,10]
odd = []
even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("odd: ", odd)
print("even: ", even)