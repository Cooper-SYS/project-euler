# coding:utf-8
import sys
from Euler import Euler
edu = Euler()

ts0 = edu.time()

def p009():
    for x in range(1,998):
        for y in range(1,998):
            z=1000-x-y
            if z<0:
                break
            if x**2+y**2==z**2:
                return '%d %d %d' % (x,y,z)
            
print p009()

            
print edu.time()-ts0