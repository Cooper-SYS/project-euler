# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

import time
from math import sqrt
start= time.time()
max=0
number=0
times=0
for all in xrange(12,1000):
    num=0
    for a in xrange(1,int(all/3)):
        for b in xrange(a,all-2*a):
            times+=1
            if a*a+b*b==(all-a-b)*(all-a-b):
                print '%d %d %d' % (a,b,all-a-b)
                num+=1
    if num>max:
        max=num
        number=all
        
print number
print (edu.time()-ts0)          