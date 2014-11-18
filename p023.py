'''
Created on 2013-8-8

@author: zhaoliang
'''
from math import sqrt
import time
def divi(number):
    sumnum=1
    for x in range(2,int(sqrt(number))+1):
        if number%x==0:
            sumnum+=(x+number/x)
            if x==number/x:
                sumnum-=x
    return sumnum

start=time.time()
arr=[]
for x in range(12,28124,1):
    if divi(x)>x:
        arr.append(x)


arr2=[]        
for x in range(1,28124):
    arr2.append(x)

ter=len(arr)-1    
for x in range(0,len(arr)):
    for m in range(ter,-1,-1):
        if arr[x]+arr[m]<28124:
            ter=m
            break
    for y in range(x,ter+1):
        if arr[x]+arr[y]<28124:
            arr2[arr[x]+arr[y]-1]=0
        else:
            break
        
print sum(x for x in arr2)
print time.time()-start