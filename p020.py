# coding:utf-8
'''
Created on 2013-8-8

@author: zhaoliang
'''
result=1
for x in range(1,101):
    result=result*x
print result
   
sum=0
for x in range(0,len(str(result))-1):
    sum+=int(str(result)[x:x+1])
    print int(str(result)[x:x+1])
print sum