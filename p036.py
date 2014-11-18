# coding:utf-8
'''
Created on 2013-8-14

@author: zhaoliang
'''
import time

def tobin(num):
    r=''
    while num!=1:
        r=str(num%2)+r
        num=int(num/2)
    if num==1:
        r='1'+r
    return r
start=time.time()
count=0
for x in range(1,1000001):
    y=int(str(x)[::-1])
    if x!=y:
        continue
    if tobin(x)==tobin(y)[::-1]:
        count+=x
        
print count
print time.time()-start