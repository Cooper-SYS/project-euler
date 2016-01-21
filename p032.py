# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

'''
Created on 2013-8-13
稍加分析可只该数肯定是个 4 位数
@author: zhaoliang
'''
import time
def check(s):
    for x in range(0,len(s)):
        for y in range(x+1,len(s)):
            if s[x:x+1]==s[y:y+1]:
                return True  #contain repeated number
    if s.find('0')!=-1:
        return True        #not contain a 0
    return False #not contain repeated number
start=time.time()
o=[]
for x in range(1,10000):
    if (not check(str(x))) and (x%10>1):
        o.append(x)
count=0   
 
result=[]
for x in o:
    for y in o:
        if x*y>9876:break
        if len(str(x))+len(str(y))+len(str(x*y))!=9:continue
        if check(str(x)+str(y)+str(x*y)):continue
        if x*y not in result:
            print '%d x %d = %d' %(x,y,x*y)
            result.append(x*y)

for x in result:
    count+=x
    
print '************%d****************' % count
print (edu.time()-ts0)
