#! D:/Python27/python.exe
# coding:utf-8
'''
Created on 2013年8月7日

@author: Administrator
'''
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
print time.time()-start
