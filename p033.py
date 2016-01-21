# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

fenzi=1
fenmu=1
def func(x,y):
    global fenzi
    global fenmu
    rx=x
    ry=y
    x1=int(x/10)
    x2=x%10
    y1=int(y/10)
    y2=y%10
    if x1==y1:
        x=x2
        y=y2
    elif x1==y2:
        x=x2
        y=y1
    elif x2==y1:
        x=x1
        y=y2
    elif x2==y2:
        x=x1
        y=y1
    #print '%d %d %d %d' % (rx,ry,x,y)
    if x2==0 and y2==0:return
    if rx==x and ry==y:return
    if rx*y==ry*x:
        print '%d %d %d %d' % (rx,ry,x,y)
        fenzi*=x
        fenmu*=y
    

result=1    
for x in range(10,98):
    for y in range(x+1,99):
        func(x,y)
        
print fenzi
print fenmu
print (edu.time()-ts0)