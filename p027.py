# coding:utf-8
'''
Created on 2013-8-12

@author: zhaoliang
'''
from math import sqrt
import time
ka=1
kb=1
max=1

start=time.time()
def sushu(number):
    number=abs(number)
    for x in range(2,int(sqrt(number))+1):
        if number%x==0:
            return False
    return True

for a in range(-1000,1001):
    for b in range(-1000,1001):
        num=0
        while True:
            number=num*num+num*a+b
            if not sushu(number):
                break
            num+=1
        #print 'n*n+n*%d+%d     n(%d,%d)' % (a,b,0,num)
        #time.sleep(1)
        if num>max:
            max=num
            #print '********%d**********' % max
            ka=a
            kb=b
            
print 'n*n+n*%d+%d     n(%d,%d)' % (ka,kb,0,max)   
print ka*kb    
print time.time()-start