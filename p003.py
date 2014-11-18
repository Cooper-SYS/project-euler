# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
from math import sqrt
import time
def fact():
    max=600851475143
    ret=[]
    x=2
    print int(sqrt(max))
    while x<int(sqrt(max)):
        if max%x==0 :
            ret.append(x)
        x+=1    
    return ret

def fact2(ret):
    print ret
    ret2=[]
    for x in ret:
        if len(ret2)==0:
            ret2.append(x)
        else:
            flag=True
            for y in ret2:
                if x%y==0:
                    flag=False
                    break
            if flag:
                ret2.append(x)
                
    return ret2
                
time1=time.time()  
print fact2(fact())
print (time.time()-time1)