# coding:utf-8
'''
Created on 2013-8-8

@author: zhaoliang
'''
from math import sqrt
import time
def divi(number):
    sumnum=1
    for x in range(2,int(sqrt(number))+1):
        if number%x==0:
            sumnum+=(x+number/x)
            if x==number/x:
                sumnum-=x
    return sumnum

start=time.time()
list=[]

for x in range(1,10001):
    a=divi(x)
    b=divi(a)
    if b==x and a!=b:
        list.append(x)

count=0
for x in list:
    count+=x

print list
print count
print time.time()-start