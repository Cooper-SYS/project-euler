# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from math import sqrt
import time
start=time.time()
now=2
num=1
while True:
    num=num+now
    now+=1
    t=0
    for x in range(1,int(sqrt(num))+1):
        if num%x==0:
            t+=2
    if sqrt(num)==int(sqrt(num)):
        t=t-1
    if t>500:
        break
    
print num
print (edu.time()-ts0)
