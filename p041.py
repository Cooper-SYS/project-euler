# coding:utf-8
'''
Created on 2013-8-14

@author: zhaoliang
'''
from math import sqrt
import time

def isPrime(num):
    for x in xrange(2,int(sqrt(num))+1):
        if num%x==0:
            return False
    return True
start=time.time()

max=0

def isRepeat(n):
    for x in range(0,len(str(n))-1):
       for y in range(x+1,len(str(n))):
           if str(n)[x]==str(n)[y]:
               return False
    return True
   

# bit=2
# number=87654321
# while True:
#     length=len(str(number))
#     s=str(number)[length-bit:length]

def getNext(i):
    i=i-9
    while str(len(str(i))) in str(i):
        i=i-9
    for x in str(i):
        if int(x)>
    return i

i=87654321
while i>123:
    i
    print i
    if not isPrime(i):
        continue
    if not isRepeat(i):
        continue
    if i>max:
        max=i
    else:
        break

for dex in range(9,3):
    min=''
    max=''
    for x in range(1,dex):
        min+=str(x)
        max+=str(dex+1-x)
    
    
print max    
print time.time()-start