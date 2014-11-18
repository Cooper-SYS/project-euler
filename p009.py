# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
import sys
for x in range(1,998):
    for y in range(1,998):
        z=1000-x-y
        if z<0:
            break
        if x**2+y**2==z**2:
            print '%d %d %d' % (x,y,z)
            sys.exit(0)