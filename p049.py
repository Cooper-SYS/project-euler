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

   
def haveSameDigit(x,y):
    for d1 in str(x):
        if d1 not in str(y):
            return False
    for d2 in str(y):
        if d2 not in str(x):
            return False        
    return True

pri=[]
for n in range(1000,10000):
    if isPrime(n):
        pri.append(n)

ls=len(pri)

for aIdx in range(0,ls-2):
    for bIdx in range(aIdx+1,ls-1):
        if not haveSameDigit(pri[aIdx],pri[bIdx]):
            continue
        for cIdx in range(bIdx+1,ls):
            if not haveSameDigit(pri[bIdx],pri[cIdx]):
                continue
            if pri[cIdx]-pri[bIdx]==pri[bIdx]-pri[aIdx]:
                print str(aIdx)+':'+str(bIdx)+':'+str(cIdx)
                print str(pri[aIdx])+':'+str(pri[bIdx])+':'+str(pri[cIdx])+'>>>>'+str(pri[bIdx]-pri[aIdx])
                print '--------------------------------------'
                break


endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')