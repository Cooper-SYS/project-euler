# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime
import math
starttime = datetime.datetime.now()

#pow(x,y,z)  x的y次方再对z求余数
# print the result with a left-side zero fill to account for leading zeros if they exist.
def PE97(a, b, c, m):
    return (c * pow(a, b, m) + 1) % m

print "last 10 digits = %010d" % PE97(2, 7830457, 28433, 10**10)
            

print (edu.time()-ts0)

