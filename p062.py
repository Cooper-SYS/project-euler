# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime
import math
starttime = datetime.datetime.now()
def p062():
    min = 1000
    max = 9999
    maxDigit = 12
    tri = []
    for x in range(min,max):
        number = x*x*x
        if len(str(number))==maxDigit:
            chars = [int(c) for c in str(number)]
            chars.sort()
            string = ''
            for c in chars:string=string+str(c)
            tri.append([str(number),string])
        if number>=(10**maxDigit):break 
    length = len(tri)
    
    for i0 in range(0,length-4):
        for i1 in range(i0+1,length-3):
            if tri[i0][1]!=tri[i1][1]:continue
            for i2 in range(i1+1,length-2):
                #if tri[i0][1]==tri[i1][1] and tri[i0][1]==tri[i2][1]:
                #    print tri[i0][0]
                if tri[i0][1]!=tri[i2][1]:continue
                for i3 in range(i2+1,length-1):
                    if tri[i0][1]!=tri[i3][1]:continue
                    for i4 in range(i3+1,length):
                        if tri[i0][1]==tri[i1][1] and tri[i0][1]==tri[i2][1] and tri[i0][1]==tri[i3][1] and tri[i0][1]==tri[i4][1]:
                            print tri[i0]
                            print tri[i1]
                            print tri[i2]
                            print tri[i3]
                            print tri[i4]
                            return tri[i0][0]

                    
                    
print p062()                    
print (edu.time()-ts0)


