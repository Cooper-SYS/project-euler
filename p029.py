# coding:utf-8
'''
Created on 2013-8-13

@author: zhaoliang
'''
list=[]
for x in range(2,101):
    for y in range(2,101):
        if not x**y in list:
            list.append(x**y)
            print '%d**%d=%d' % (x,y,x**y)
            
print len(list)