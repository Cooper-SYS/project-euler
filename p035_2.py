# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from math import sqrt
import time
list=set()
def getPrimes(max):
    global list
    flag=[True]*max
    for x in xrange(2,int(sqrt(max))):
        p=x
        while x*p<max:
            if flag[x*p]:
                flag[x*p]=False
            p+=1
    for x in xrange(2,max):
        if flag[x]:list.add(x)
    return list

def isRecycle(num):
    global list
    s=str(num)
    for y in range(len(s)):
        snum=s[y:]+s[0:y]
        if int(snum) not in list:
            return False
    return True

start=time.time()
list=getPrimes(1000001)

print time.time()-start    
count=0
for x in list:
    if isRecycle(x):
        count+=1
print count
print (edu.time()-ts0)
