# coding:utf-8
'''
Created on 2013-8-14
这个是我自己的方式
@author: zhaoliang
'''
import time
from math import sqrt
start= time.time()
max=0
number=0
times=0

lista=[]
for x in xrange(0,1000):
    lista.append(x*x)
listb=[0]*1000    
for x in xrange(11,len(lista)/2):
    for y in xrange(x,len(lista)):
        times+=1
        if x+y+sqrt(lista[x]+lista[y])>999:
            break
        if lista[x]+lista[y] in lista:
            listb[x+y+int(sqrt(lista[x]+lista[y]))]+=1

for x in xrange(0,1000):
    if listb[x]>max:
        max=listb[x]
        number=x
        
print number
print times
print time.time()-start  