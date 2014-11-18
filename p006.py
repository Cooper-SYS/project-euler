# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
def a():
    sum=0
    for x in range(1,101):
        sum+=x**2
    return sum

def b():
    sum=0
    for x in range(1,101):
        sum+=x
    return sum**2

print a()-b()