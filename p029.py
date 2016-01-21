# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

list=[]
for x in range(2,101):
    for y in range(2,101):
        if not x**y in list:
            list.append(x**y)
            print '%d**%d=%d' % (x,y,x**y)
            
print len(list)
print (edu.time()-ts0)