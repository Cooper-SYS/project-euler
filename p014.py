# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

import time
start=time.time()
number=0
count=0
for x in range(1000000,13,-1):
    y=x
    t=1
    while y!=1:
        if y%2==0:
            y=y/2
        else:
            y=3*y+1
        t+=1
    if t>count:
        number=x
        count=t
    print str(x)+':'+str(t)
        
print str(number)+':'+str(count)
print time.time()-start
print (edu.time()-ts0)