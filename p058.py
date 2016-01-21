# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from __future__ import division
import datetime

import math
'''
推导过程
根据变长变化过程，新增的对角数字
根据题目，只考虑变长为奇数的情况，因为当边长为偶数时，两条斜对角不会交叉于某个数字
0-->1   初始化  1
1-->2   2的平方-1=3
2-->3   2的平方+1=5    3的平方=9    3的平方-2=7
3-->4   4的平方-3=13
4-->5   4的平方+1=17    5的平方=25    5的平方-4=21
5-->6   6的平方-5=31
6-->7   6的平方+1=37    7的平方=49    7的平方-6=43
7-->8   57
'''

starttime = datetime.datetime.now()

def isPrime(x):
    for tmp in range(2,int(math.sqrt(x))+1):
        if x%tmp==0:
            return False
    return True
    
primeCount=0  
allCount=1
base=set()
base.add(1)
n=2 
per=100
while per>=10:
    if n%2==0:
        num=n**2-(n-1)
        base.add(num)
        allCount+=1
        if isPrime(num):
            primeCount+=1
            
    else:
        num1=(n-1)**2+1
        num2=n**2-(n-1)
        num3=n**2
        base.add(num1)
        base.add(num2)
        base.add(num3)
        allCount+=3 #n的平方不可能是质数
        if isPrime(num1):
            primeCount+=1
            
        if isPrime(num2):
            primeCount+=1
        
    n+=1 
    per=primeCount*100/allCount
    #print per
    
    
print n-1   

print '-----------------'
print (edu.time()-ts0)