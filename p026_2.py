#! D:/Python27/python.exe
# coding:utf-8
'''
Created on 2013年8月9日

@author: Administrator
'''
import time
start=time.time()
def function(n):
    while n%2==0:
        n=n/2
    while n%5==0:
        n=n/5
    return n
max=0
for x in xrange(1,1000):
    num=function(x)
    temp=9
    len=1
    if num==1:
        continue
    while temp%num!=0:
        len=len+1
        temp=temp*10+9
    if len>max:
        max=x
print max
print time.time()-start

