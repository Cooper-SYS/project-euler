# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime

starttime = datetime.datetime.now()
'''
x+y=plus            in pg
x-y=minus           in pg
plus-minus=2*y      in pg
plus+minus=2*x      in pg

The result is |x-y|=minus
'''
flag = False
pgSet=set()
x=0
while not flag:
    x += 1
    plus=x*(3*x-1)/2
    pgSet.add(plus)
    for minus in pgSet:
        if (plus-minus)/2 in pgSet and (plus+minus)/2 in pgSet:
            print minus
            flag=True
            break
print len(pgSet)
print '-----------------' 


print (edu.time()-ts0)



