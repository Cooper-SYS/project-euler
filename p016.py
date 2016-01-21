# coding:utf-8
# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

number=str(2**1000)
sum=0
print number
for x in range(0,len(number)):
    print int(number[x:x+1]) 
    sum+=int(number[x:x+1])  
print sum
print (edu.time()-ts0)