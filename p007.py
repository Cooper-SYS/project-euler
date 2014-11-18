# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
from math import sqrt
import time
start=time.time()
sushu=[2,3,5,7,11,13,17]
max=19
print sushu
while len(sushu)<10001:
    flag=True
    for x in range(2,int(sqrt(max))+1):
        if max%x==0:
            flag=False
            break
    if flag:
        sushu.append(max)    
        #print sushu[len(sushu)-1]
    max+=1

print sushu[len(sushu)-1]
print time.time()-start
        