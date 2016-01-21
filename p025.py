# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

pre=1
next=1
count=0
index=2
while len(str(next))<1000:
    now=pre+next
    pre=next
    next=now
    index+=1
    print str(index)+':'+str(next)
    
print index
print (edu.time()-ts0)