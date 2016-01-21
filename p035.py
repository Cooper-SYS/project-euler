# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from math import sqrt
import time
def isPrime(num):
    for x in xrange(3,int(sqrt(num))+1):
        if num%x==0:
            return False
    return True

def isRecycle(num):
    s=str(num)
    for y in range(len(s)):
        snum=s[y:]+s[0:y]
        if int(snum) not in list:
            return False
    return True

start=time.time()   
list=set([2,3,5,7])
count=0
for x in xrange(11,1000001,2):
    if isPrime(x):
        list.add(x)

print time.time()-start    

for x in list:
    if isRecycle(x):
        count+=1
    
print count
print (edu.time()-ts0)