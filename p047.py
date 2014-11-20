#coding=utf-8
#!/usr/bin/python
#python2.7.8

import datetime
import copy
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
    print n
    n+=1
    if isPrime(n):
        priSet.append(n)
    else:
        tmpN=n 
        tmpPri=set()
        maxSqrt=math.sqrt(n)
        
        for x in priSet:
            if x>maxSqrt:
                break
            if tmpN%x==0:
                tmpPri.add(x)
                while tmpN%x==0:
                    tmpN=int(tmpN/x)
            
        
        if tmpN==1 and len(tmpPri)==needCount:
            #print n
            needPri.append(n)
            #needPriX.append(copy.copy(tmpPri))
            if len(needPri)>=needCount:
                ls=len(needPri)
                if n==134043:
                    print needPri[ls-4]
                    break
                if needPri[ls-1]-needPri[ls-2]==1 and needPri[ls-2]-needPri[ls-3]==1 and needPri[ls-3]-needPri[ls-4]==1:
                    flag=True
                    print needPri[ls-4]

endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).microseconds)+' microseconds')