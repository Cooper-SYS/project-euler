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
counting=0
oldPri=0
priArr=[]
maxBase=1000000
numb=0
while n<maxBase:
    if isPrime(n):
        priArr.append(n)
        numb+=n
        if numb>maxBase:
            break
    n+=1


    

priLen=len(priArr)
maxLength=priLen
length=priLen-1 
start=0
num=953
flag=False
while not flag:
    for start in range(0,priLen-length):
        num=0
        for x in range(start,start+length):
            num+=priArr[x]
        #print str(length)+' : '+str(start)
        if isPrime(num):
            print 'start: '+str(start)+' width: '+ str(length)+' : '+str(num)
            flag=True
            break
    length=length-1
    
    
print '-----------------'
print 'primes array count '+ str(priLen)

endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).microseconds)+' microseconds')



