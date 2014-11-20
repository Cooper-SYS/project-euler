#coding=utf-8
#!/usr/bin/python
#python2.7.8

import datetime
import math


starttime = datetime.datetime.now()

def isPrime(x):
    for tmp in range(2,int(math.sqrt(x))+1):
        if x%tmp==0:
            return False
    return True


n=2
sBase=1
primeSet=set()
squareArr=[]
squareArr.append(2*sBase*sBase)
sBase+=1
squareArr.append(2*sBase*sBase)
while True:
    #print primeSet
    if isPrime(n):
        primeSet.add(n)
    else:
        flag=False  
        if n>squareArr[len(squareArr)-1]:
            sBase+=1
            squareArr.append(2*sBase*sBase)
        if n%2==1:
            flag=True
            for pr in primeSet:
                for sq in squareArr:
                    if pr+sq==n:
                        print str(n)+' = '+str(pr)+' + '+str(sq)
                        flag=False  
                        break
                if not flag:   
                    break
        if flag:  
            print n
            break
    n+=1
    
print '-----------------'
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).microseconds)+' microseconds')



