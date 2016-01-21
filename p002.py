# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

x=1
y=2
sum=2
max=4000000

def p002():
    global x,y,sum,max
    if x+y<max:
        tmp=x+y
        if tmp%2==0:
            sum+=tmp
        x=y
        y=tmp
        p002()

p002()
print sum
print edu.time()-ts0