#coding=utf-8
#!/usr/bin/python
#python2.7.8

import datetime
import math
starttime = datetime.datetime.now()

#是否为回文数
def isPali(x):
    sx=str(x)
    num=int(len(sx)/2)
    ls=len(sx)
    for tx in range(0,num):
        a=sx[tx:tx+1]
        b=sx[ls-tx-1:ls-tx]
        if a!=b:
            return False
             
    return True
#逆转
def reverse(x):
    return int(str(x)[::-1])
   
maxNum=10000
counting=maxNum+1
n=-1
while n<maxNum:
    n+=1
    midValue=n
    it=0
    while it<=50:
        midValue+=reverse(midValue)
        it+=1
        if isPali(midValue):
            counting-=1
            print n
            print midValue
            print '------------'
            break
            

print counting
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')