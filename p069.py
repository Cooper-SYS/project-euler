# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from __future__ import division
import datetime
import math


def isPrime(x):
    for tmp in range(2,int(math.sqrt(x))+1):
        if x%tmp==0:
            return False
    return True
    
def eachPrime(x,y):
    if x-y==1 or y==1:
        return True
    if x%y==0:
        return False
    else:
        return eachPrime(y,x%y)
    
starttime = datetime.datetime.now()

def easyWay(max):
    n=2
    maxPer=3
    maxN=6
    while n<=max:
        count=0
        for x in xrange(1,n):
            if eachPrime(n,x):
                count+=1
                if n/count<maxPer:
                    break
        if n/count>maxPer:
            maxPer=n/count
            maxN=n
        n += 1
    return maxN

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
#solution from http://blog.dreamshire.com/project-euler-69-solution/
def hardWay(L):
    maxn = 1
    for idx in range(0,len(primes)):
        p=primes[idx]
        if maxn*p > L:
            return maxn
        maxn *= p
    return "Buy me some more prime numbers!"
'''
为了使得比值最大，需要符合n尽量大，与n互质的数尽量少
为了使与n互质的数尽量少，最好满足n正好是质数的乘积
比如，如果n与2互质，那么它就不可能与所有2的倍数互质，如果n与3互质，就不可能与3的倍数互质
依次类推，所有质数的乘积，当乘到n>max时程序结束
'''
def tryWay(max):
    n=2
    maxNum=1
    priLst=set()
    priLst.add(1)
    while True:
        if isPrime(n):
            
            if maxNum * n > max:
                print priLst
                print maxNum/len(priLst)
                return maxNum
            maxNum *= n 
            priLst.add(n)
        n += 1
    
print '--------------------------------' 
print easyWay(10**2)
print '--------------------------------' 
print '--------------------------------' 
print hardWay(10**6)
print '--------------------------------' 
print '--------------------------------' 
print tryWay(10**6)
print '--------------------------------' 
print (edu.time()-ts0)