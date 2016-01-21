# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime
import math
starttime = datetime.datetime.now()

def isPrime(x):
    for tmp in range(2,int(math.sqrt(x))+1):
        if x%tmp==0:
            return False
    return True
   
flag=False    
needCount=4
needPri=[]
n=1
priSet=[]
while not flag:
    #print n
    n+=1
    if isPrime(n):
        priSet.append(n)
    else:
        tmpN=n
        tmpPri=set()
        for x in priSet:
            if tmpN%x==0:
                tmpPri.add(x)
                while tmpN%x==0:
                    tmpN=int(tmpN/x)
                if tmpN in priSet:
                    tmpPri.add(tmpN)
                    tmpN=1
                    break
           
        
        if tmpN==1 and len(tmpPri)==needCount:
            needPri.append(n)
            if len(needPri)>=needCount:
                ls=len(needPri)
                lstValue=needPri[ls-1]
                newFlag=True
                for idx in range(2,needCount+1):  # -1 -2 -3 -4
                    midValue=needPri[ls-idx]
                    if lstValue-midValue!=idx-1:
                        newFlag=False
                        break
                if newFlag:
                    flag=True
                    print '----------------------'
                    print lstValue-needCount+1

print (edu.time()-ts0)