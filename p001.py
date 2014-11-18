# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
def test(max):
    num=0
    for x in range(3,max,3):
        num+=x
    for x in range(5,max,5):
        num+=x
    for x in range(15,max,15):
        num-=x
        
    return num

print test(1000)