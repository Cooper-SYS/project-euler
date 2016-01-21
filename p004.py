# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()
def p004():
    ret=0
    for x in range(100,1000):
        for y in range(100,1000):
            sum=x*y
            #print '%dX%d=%d' % (x,y,sum)
            if str(sum)[::-1]==str(sum):
                print '%dX%d=%d' % (x,y,sum)
                if sum>ret:
                    ret=sum
                
    return ret

print p004()
print (edu.time()-ts0)