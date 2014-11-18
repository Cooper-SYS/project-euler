# coding:utf-8
'''
Created on 2013-8-8

@author: zhaoliang
'''
number=str(2**1000)
sum=0
print number
for x in range(0,len(number)):
    print int(number[x:x+1]) 
    sum+=int(number[x:x+1])  
print sum