# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from math import sqrt
import time
def isbestPrime(num):
    for x in xrange(3,int(sqrt(num))+1):
        if num%x==0:
            return False
    a=int(str(num)[0:1])
    b=int(str(num)[len(str(num))-1:len(str(num))])
    if a in [2,3,5,7] and b in [2,3,5,7]:
        return True
    return False
    
def isPrime(num):
    for x in xrange(2,int(sqrt(num))+1):
        if num%x==0:
            return False
    return True
start=time.time() 
times=0
number=23
count=0
while times<11:
    if isbestPrime(number):
        flag=True
        s=str(number)
        
        for x in range(1,len(s)-1):
            if not isPrime(int(s[x:len(s)])):
                flag=False
                break
        if flag:
            for y in range(len(s)-1,1,-1):
                if not isPrime(int(s[0:y])):
                    flag=False
                    break
        if flag:
            times+=1
            count+=number
    number+=2
    
print count    
print (edu.time()-ts0)
