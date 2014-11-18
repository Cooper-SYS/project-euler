# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
x=1
y=2
sum=2
max=4000000
def test():
    global x,y,sum,max
    if x+y<max:
        tmp=x+y
        if tmp%2==0:
            sum+=tmp
        x=y
        y=tmp
        test()

test()
print sum