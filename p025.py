#! D:/Python27/python.exe
# coding:utf-8
'''
Created on 2013年8月9日

@author: Administrator
'''
pre=1
next=1
count=0
index=2
while len(str(next))<1000:
    now=pre+next
    pre=next
    next=now
    index+=1
    print str(index)+':'+str(next)
    
print index