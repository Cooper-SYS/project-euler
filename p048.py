# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime
import math


starttime = datetime.datetime.now()

index=1000
num=0
for x in range(1,index+1):
    tmp=1 
    for y in range(1,x+1):
        tmp *= x
    num += tmp

print str(num)[-10:]
    
print '-----------------'
print (edu.time()-ts0)



