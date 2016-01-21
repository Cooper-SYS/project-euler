# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime
import math
starttime = datetime.datetime.now()

max=1 

for a in range(1,100):
    for b in range(1,100):
        pow=a**b
        dig=0
        for x in str(pow):
            dig+=int(x)
        if dig>max:
            max=dig
print max

print '-----------------'

print (edu.time()-ts0)