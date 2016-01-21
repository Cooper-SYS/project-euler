# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

def p006_1():
    sum=0
    for x in range(1,101):
        sum+=x**2
    return sum

def p006_2():
    sum=0
    for x in range(1,101):
        sum+=x
    return sum**2

print p006_1()-p006_2()

print (edu.time()-ts0)