# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

result=1
for x in range(1,101):
    result=result*x
print result
   
sum=0
for x in range(0,len(str(result))-1):
    sum+=int(str(result)[x:x+1])
    print int(str(result)[x:x+1])
print sum
print (edu.time()-ts0)