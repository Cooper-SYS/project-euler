#coding=utf-8
#!/usr/bin/python
#python2.7.8

#任意相邻的三个素数，前两个相加的和都大于第三个
#只有一个例外，那就是2+3=5

import datetime
import math
starttime = datetime.datetime.now()

def isPrime(x):
    for tmp in range(2,int(math.sqrt(x))+1):
        if x%tmp==0:
            return False
    return True

maxBase=1000000000
n=2
pri=[]
while n<maxBase:
    if isPrime(n):
        pri.append(n)
        if len(pri)>=3 and pri[len(pri)-3]+pri[len(pri)-2]<=n:
            print 'P(n-1)+P(n-2)<=P(n)   n = ' + str(n)
    n+=1