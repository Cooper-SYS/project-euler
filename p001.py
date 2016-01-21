# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

def p001(max):
    num=0
    for x in range(3,max,3):
        num+=x
    for x in range(5,max,5):
        num+=x
    for x in range(15,max,15):
        num-=x
        
    return num

print p001(1000)
print edu.time()-ts0



